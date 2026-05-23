# Customer Segmentation Analysis Dashboard

An interactive customer segmentation and analytics dashboard built using Python, SQL, Streamlit, and Machine Learning.

## Live Demo

https://customer-segmentation-analysis-project.streamlit.app/

---

# Project Overview

This project analyzes customer demographic and spending behavior data to identify meaningful customer segments using exploratory data analysis and K-Means clustering.

The dashboard provides interactive visualizations and filtering capabilities to help understand customer purchasing patterns, income distribution, and behavioral segmentation.

---

# Features

- Customer demographic analysis
- Spending behavior analysis
- Income vs spending visualization
- Interactive dashboard filters
- K-Means clustering for customer segmentation
- Cluster distribution analysis
- Business insights generation
- SQL-based analytical queries
- Interactive Streamlit dashboard

---

# Technologies Used

| Technology | Purpose |
|---|---|
| Python | Data analysis and dashboard development |
| Pandas | Data preprocessing and manipulation |
| NumPy | Numerical computations |
| Matplotlib | Data visualization |
| Seaborn | Statistical visualization |
| Scikit-learn | K-Means clustering |
| MySQL | SQL analysis and querying |
| Streamlit | Interactive dashboard deployment |
| Git & GitHub | Version control and project hosting |

---

# Machine Learning Implementation

The project uses **K-Means Clustering** to segment customers based on:

- Annual Income
- Spending Score

## Identified Customer Segments

- Premium Customers
- Budget Customers
- Impulsive Customers
- Careful Customers
- Standard Customers

---

# Dashboard Features

## Interactive Filters

- Gender Filter
- Age Range Filter
- Annual Income Filter
- Spending Score Filter

## KPI Metrics

- Total Customers
- Average Income
- Average Spending Score

## Visualizations

- Age Distribution
- Gender Distribution
- Income vs Spending Analysis
- Customer Segment Visualization
- Cluster Distribution Pie Chart

---

# SQL Analysis

The project includes SQL queries for:

- Customer distribution analysis
- Spending behavior analysis
- Income analysis
- Segment identification
- Customer category analysis

---

# Project Structure

```text
customer-segmentation-analysis/
│
├── data/
│   └── Mall_Customers.csv
│
├── dashboard/
│   └── app.py
│
├── notebooks/
│   └── customer_analysis.ipynb
│
├── sql/
│   └── customer_queries.sql
│
├── visuals/
│   ├── customer_segments.png
│   ├── income_vs_spending.png
│   └── age_distribution.png
│
├── README.md
├── requirements.txt
├── runtime.txt
└── load_data.py
```

---

# Installation and Setup

## Clone Repository

```bash
git clone https://github.com/Ashutosh-K0/customer-segmentation-analysis
```

## Navigate to Project Directory

```bash
cd customer-segmentation-analysis
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Run Streamlit Dashboard

```bash
streamlit run dashboard/app.py
```

---

# Key Business Insights

- Premium customers exhibit high income and high spending behavior.
- Careful customers have high income but lower spending tendencies.
- Impulsive customers spend aggressively despite lower income levels.
- Budget customers demonstrate lower purchasing engagement.
- Standard customers represent the average consumer population.

---

# Future Improvements

- Add real-time database integration
- Implement advanced clustering algorithms
- Add predictive customer analytics
- Improve dashboard responsiveness
- Add downloadable analytics reports
- Deploy using Docker and cloud infrastructure

---

# Author

Ashutosh Kumar

---

# Deployment

Streamlit Cloud Deployment:

https://customer-segmentation-analysis-project.streamlit.app/
