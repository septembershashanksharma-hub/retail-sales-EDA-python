# Retail Sales Exploratory Data Analysis (EDA)

## Overview
This project performs Exploratory Data Analysis (EDA) on a retail sales dataset using Python. The goal is to analyze sales performance, profitability, customer trends, and business insights through data visualization and statistical analysis.

The project covers:
- Data loading and cleaning
- Sales analysis
- Profit analysis
- Monthly trend analysis
- Correlation analysis
- Business insights generation

---

# Tech Stack

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Jupyter Notebook

---

# Dataset

Dataset Used:
- Superstore Sales Dataset

The dataset contains:
- Order information
- Sales
- Profit
- Discount
- Product categories
- Regions
- Shipping details

---

# Project Structure

```bash
Retail-Sales-EDA/
│
├── superstore.csv
├── retail_sales_eda.ipynb
├── README.md
└── images/
```

---

# Objectives

The main objectives of this project are:

- Understand retail sales performance
- Identify profitable and loss-making categories
- Analyze regional profitability
- Discover monthly sales trends
- Understand the relationship between discount and profit
- Generate business-focused insights from data

---

# Features & Analysis Performed

## 1. Data Loading & Inspection
- Loaded dataset using Pandas
- Checked shape and columns
- Displayed sample records

## 2. Data Understanding
- Checked data types
- Identified missing values
- Generated statistical summaries

## 3. Data Cleaning & Feature Engineering
- Converted date columns to datetime format
- Extracted:
  - Year
  - Month

## 4. Sales by Category
Visualization showing:
- Technology
- Furniture
- Office Supplies

Purpose:
- Identify highest revenue-generating categories

---

## 5. Profit by Region
Horizontal bar chart showing:
- Regional profit performance

Purpose:
- Identify strongest and weakest business regions

---

## 6. Monthly Sales Trend
Time-series analysis of:
- Monthly sales growth
- Seasonal trends

Purpose:
- Detect business growth patterns over time

---

## 7. Profit by Sub-Category
Visualization showing:
- Most profitable sub-categories
- Loss-making sub-categories

Purpose:
- Identify products hurting profitability

---

## 8. Discount vs Profit Correlation
Scatterplot analysis between:
- Discount
- Profit

Purpose:
- Understand how discounts impact profitability

---

# Key Business Insights

- Some product sub-categories generate losses despite strong sales.
- Higher discounts often reduce profitability.
- Sales trends show seasonal fluctuations across months.
- Certain regions contribute significantly more profit than others.
- Technology category contributes highest overall sales.

---

# Visualizations Included

- Bar Charts
- Horizontal Bar Charts
- Line Charts
- Scatter Plots

All visualizations were created using:
- Matplotlib
- Seaborn

---

# How to Run the Project

## Step 1 — Install Required Libraries

```bash
pip install pandas numpy matplotlib seaborn
```

---

## Step 2 — Open Jupyter Notebook

```bash
jupyter notebook
```

---

## Step 3 — Run the Notebook

Open:
```bash
retail_sales_eda.ipynb
```

Run all cells sequentially.

---

# Future Improvements

Possible future enhancements:
- Interactive dashboard using Power BI or Streamlit
- Forecasting future sales using Machine Learning
- Customer segmentation analysis
- KPI dashboard creation
- Automated reporting pipeline

---

# Author

## Shashank Sharma
Data Analytics | SQL | Python | AI Enthusiast

Portfolio:
https://shashanksharma-io.lovable.app/

---

# License

This project is for educational and portfolio purposes.Python
Pandas
NumPy
Matplotlib
Seaborn
Jupyter Notebook
Dataset

**Dataset Used:**

Superstore Sales Dataset

The dataset contains:

Order information
Sales
Profit
Discount
Product categories
Regions
Shipping details
Project Structure
Retail-Sales-EDA/
│
├── superstore.csv
├── retail_sales_eda.ipynb
├── README.md
└── images/
**Objectives**

The main objectives of this project are:

Understand retail sales performance
Identify profitable and loss-making categories
Analyze regional profitability
Discover monthly sales trends
Understand the relationship between discount and profit
Generate business-focused insights from data
Features & Analysis Performed
1. Data Loading & Inspection
Loaded dataset using Pandas
Checked shape and columns
Displayed sample records
2. Data Understanding
Checked data types
Identified missing values
Generated statistical summaries
3. Data Cleaning & Feature Engineering
Converted date columns to datetime format
Extracted:
Year
Month
4. Sales by Category

Visualization showing:

Technology
Furniture
Office Supplies

Purpose:

Identify highest revenue-generating categories
5. Profit by Region

Horizontal bar chart showing:

Regional profit performance

Purpose:

Identify strongest and weakest business regions
6. Monthly Sales Trend

Time-series analysis of:

Monthly sales growth
Seasonal trends

Purpose:

Detect business growth patterns over time
7. Profit by Sub-Category

Visualization showing:

Most profitable sub-categories
Loss-making sub-categories

Purpose:

Identify products hurting profitability
8. Discount vs Profit Correlation

Scatterplot analysis between:

Discount
Profit

Purpose:

Understand how discounts impact profitability


**Key Business Insights**
Some product sub-categories generate losses despite strong sales.
Higher discounts often reduce profitability.
Sales trends show seasonal fluctuations across months.
Certain regions contribute significantly more profit than others.
Technology category contributes highest overall sales.
Visualizations Included
Bar Charts
Horizontal Bar Charts
Line Charts
Scatter Plots

All visualizations were created using:

Matplotlib
Seaborn
