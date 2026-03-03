# Book Market Intelligence Dashboard

An end-to-end data analytics project that analyzes pricing strategies, rating distributions, and category-level trends across 1,000+ e-commerce book records using Python, SQL, and Streamlit.

---

## Live Application

Deployed Dashboard:  
https://book-market-dashboard-ape84y2du4b9csr93qdxqf.streamlit.app/

---

## Project Objective

The objective of this project was to build a complete analytics pipeline to evaluate whether pricing strategies align with customer satisfaction metrics.

This project focuses on:

- Identifying pricing patterns across categories
- Evaluating rating distribution
- Segmenting products into pricing tiers
- Measuring correlation between price and customer rating

---

## Architecture Overview

The solution follows a structured analytics workflow:

1. Data Extraction – Web scraped 1,000+ book records.
2. Data Cleaning – Resolved encoding issues and converted categorical ratings into numerical values.
3. SQL Analysis – Performed aggregation, segmentation, and distribution analysis.
4. Dashboard Development – Built interactive Streamlit application with dynamic filters.
5. Cloud Deployment – Deployed publicly using Streamlit Community Cloud.

---

## Tech Stack

- Python (Pandas, NumPy)
- SQL (SQLite)
- Streamlit
- Matplotlib
- Seaborn
- Git & GitHub

---

## Key Dashboard Features

- Dynamic filtering by:
  - Category
  - Rating
  - Price range
  - Price segment (Low / Medium / High)

- KPI Tracking:
  - Total Books
  - Average Price
  - Average Rating
  - 90th Percentile Price

- Visual Analytics:
  - Price distribution histogram
  - Rating distribution chart
  - Category-wise average pricing
  - Correlation heatmap (Price vs Rating)

- Downloadable filtered dataset

---

## Key Business Insights

- Pricing strategies show weak correlation with customer ratings.
- Premium categories do not consistently exhibit higher satisfaction levels.
- Approximately 80% of products fall within medium-to-high price tiers.
- Price segmentation provides clearer strategic positioning than raw averages.

---

## Skills Demonstrated

- Data Cleaning & Transformation
- Exploratory Data Analysis (EDA)
- SQL Aggregation & Segmentation
- KPI Design & Business Interpretation
- Interactive Dashboard Development
- Cloud Deployment
- Version Control

---

## Running the Project Locally



git clone : https://github.com/bablu1845/book-market-dashboard

Install dependencies:

pip install -r requirements.txt

Run the dashboard:

streamlit run dashboard.py

---

## Repository Structure

book-market-dashboard/
│
├── dashboard.py
├── books_data.csv
├── requirements.txt
└── README.md

---

## Author

Belide Adithya  
B.Tech – Data Science  
Aspiring Data Analyst