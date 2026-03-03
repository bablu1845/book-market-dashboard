import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# =====================================
# PAGE CONFIG
# =====================================

st.set_page_config(
    page_title="Book Market Intelligence",
    layout="wide",
    page_icon="📊"
)

# =====================================
# LOAD DATA FROM CSV (CLOUD SAFE)
# =====================================

df = pd.read_csv("books_data.csv")

# -------------------------
# CLEAN DATA (IMPORTANT)
# -------------------------

# Clean Price column (remove £, Â, etc.)
df["Price"] = df["Price"].str.replace(r"[^\d.]", "", regex=True)
df["Price"] = df["Price"].astype(float)

# Convert Rating text to numeric
rating_map = {
    "One": 1,
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5
}

df["Rating"] = df["Rating"].map(rating_map)

# Compute overall metrics (used for delta comparison)
overall_avg_price = df["Price"].mean()
overall_avg_rating = df["Rating"].mean()

# =====================================
# SIDEBAR FILTERS
# =====================================

st.sidebar.title("🔎 Filters")

# Category Filter
selected_category = st.sidebar.multiselect(
    "Select Category",
    options=sorted(df["Category"].unique()),
    default=sorted(df["Category"].unique())
)

# Rating Filter
selected_rating = st.sidebar.multiselect(
    "Select Rating",
    options=sorted(df["Rating"].unique()),
    default=sorted(df["Rating"].unique())
)

# Price Range Slider
price_range = st.sidebar.slider(
    "Select Price Range",
    min_value=float(df["Price"].min()),
    max_value=float(df["Price"].max()),
    value=(float(df["Price"].min()), float(df["Price"].max()))
)

# Price Segment Function
def price_segment(price):
    if price < 20:
        return "Low"
    elif price <= 40:
        return "Medium"
    else:
        return "High"

df["Segment"] = df["Price"].apply(price_segment)

selected_segment = st.sidebar.multiselect(
    "Select Price Segment",
    options=["Low", "Medium", "High"],
    default=["Low", "Medium", "High"]
)

# Apply All Filters
filtered_df = df[
    (df["Category"].isin(selected_category)) &
    (df["Rating"].isin(selected_rating)) &
    (df["Price"] >= price_range[0]) &
    (df["Price"] <= price_range[1]) &
    (df["Segment"].isin(selected_segment))
].copy()

# =====================================
# HEADER
# =====================================

st.markdown(
    """
    <h1 style='text-align: center;'>📊 Book Market Intelligence Dashboard</h1>
    <p style='text-align: center; font-size:18px;'>
    Interactive Pricing & Category Analytics
    </p>
    """,
    unsafe_allow_html=True
)

st.markdown("---")

# =====================================
# KPI SECTION
# =====================================

st.subheader("📌 Key Performance Indicators")

col1, col2, col3, col4 = st.columns(4)

avg_price = filtered_df["Price"].mean()
avg_rating = filtered_df["Rating"].mean()

price_delta = avg_price - overall_avg_price
rating_delta = avg_rating - overall_avg_rating

col1.metric("Total Books", len(filtered_df))

col2.metric(
    "Average Price",
    f"{avg_price:.2f}",
    f"{price_delta:.2f}",
    delta_color="normal"
)

col3.metric(
    "Average Rating",
    f"{avg_rating:.2f}",
    f"{rating_delta:.2f}",
    delta_color="normal"
)

p90 = filtered_df["Price"].quantile(0.90)
col4.metric("90th Percentile Price", f"{p90:.2f}")

st.markdown("---")

# =====================================
# VISUAL SECTION
# =====================================

colA, colB = st.columns(2)

with colA:
    st.subheader("📈 Price Distribution")
    fig1, ax1 = plt.subplots()
    sns.histplot(filtered_df["Price"], bins=20, ax=ax1)
    ax1.set_xlabel("Price")
    ax1.set_ylabel("Frequency")
    st.pyplot(fig1)

with colB:
    st.subheader("⭐ Rating Distribution")
    fig2, ax2 = plt.subplots()
    sns.countplot(x="Rating", data=filtered_df, ax=ax2)
    st.pyplot(fig2)

st.markdown("---")

# =====================================
# CATEGORY ANALYSIS
# =====================================

colC, colD = st.columns(2)

with colC:
    st.subheader("💰 Top 10 Categories by Avg Price")
    avg_price_cat = (
        filtered_df.groupby("Category")["Price"]
        .mean()
        .sort_values(ascending=False)
        .head(10)
    )

    fig3, ax3 = plt.subplots(figsize=(8, 5))
    avg_price_cat.plot(kind="bar", ax=ax3)
    plt.xticks(rotation=45)
    st.pyplot(fig3)

with colD:
    st.subheader("📊 Price Segmentation")
    segment_counts = filtered_df["Segment"].value_counts()

    fig4, ax4 = plt.subplots()
    segment_counts.plot(kind="bar", ax=ax4)
    st.pyplot(fig4)

st.markdown("---")

# =====================================
# CORRELATION HEATMAP
# =====================================

st.subheader("🔍 Correlation Heatmap")

fig5, ax5 = plt.subplots()
sns.heatmap(
    filtered_df[["Price", "Rating"]].corr(),
    annot=True,
    cmap="coolwarm",
    ax=ax5
)
st.pyplot(fig5)

st.markdown("---")

# =====================================
# DOWNLOAD SECTION
# =====================================

st.subheader("⬇ Download Filtered Dataset")

csv = filtered_df.to_csv(index=False).encode("utf-8")

st.download_button(
    label="Download CSV",
    data=csv,
    file_name="filtered_books.csv",
    mime="text/csv"
)

st.markdown(
    """
    <hr>
    <p style='text-align:center;font-size:14px;'>
    Built with Python • Streamlit • Data Analytics Pipeline
    </p>
    """,
    unsafe_allow_html=True
)