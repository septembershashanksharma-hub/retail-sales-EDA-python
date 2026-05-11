# ================================
# RETAIL SALES EDA
# By Shashank Sharma
# ================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Plot styling
sns.set_theme(style="whitegrid")
plt.rcParams["figure.figsize"] = (10, 5)

# ================================
# 1. LOAD DATA
# ================================
df = pd.read_csv("superstore.csv", encoding="latin-1")

print("Shape:", df.shape)
print("\nColumn Names:\n", df.columns.tolist())
print("\nFirst 5 rows:")
print(df.head())

# ================================
# 2. UNDERSTAND YOUR DATA
# ================================
print("\nData Types:\n", df.dtypes)

print("\nMissing Values:\n", df.isnull().sum())

print("\nBasic Statistics:")
print(df.describe())

# ================================
# 3. FIX DATA TYPES
# ================================
df["Order Date"] = pd.to_datetime(df["Order Date"])
df["Ship Date"] = pd.to_datetime(df["Ship Date"])

df["Year"] = df["Order Date"].dt.year
df["Month"] = df["Order Date"].dt.month

print("\nFixed Date Columns")
print(df["Order Date"].head())

# ================================
# 4. SALES BY CATEGORY
# ================================
category_sales = (
    df.groupby("Category")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

category_sales.plot(
    kind="bar",
    color=["#2196F3", "#FF5722", "#4CAF50"]
)

plt.title("Total Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales (USD)")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

print("\nSales by Category:")
print(category_sales)

# ================================
# 5. PROFIT BY REGION
# ================================
region_profit = (
    df.groupby("Region")["Profit"]
    .sum()
    .sort_values()
)

region_profit.plot(
    kind="barh",
    color=["#f44336", "#FF9800", "#2196F3", "#4CAF50"]
)

plt.title("Total Profit by Region")
plt.xlabel("Profit (USD)")
plt.tight_layout()
plt.show()

# ================================
# 6. MONTHLY SALES TREND
# ================================
monthly = (
    df.groupby(["Year", "Month"])["Sales"]
    .sum()
    .reset_index()
)

monthly["Period"] = (
    monthly["Year"].astype(str)
    + "-"
    + monthly["Month"].astype(str).str.zfill(2)
)

plt.plot(
    monthly["Period"],
    monthly["Sales"],
    marker="o",
    color="#2196F3"
)

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()

# ================================
# 7. TOP SUB-CATEGORIES BY PROFIT
# ================================
sub_profit = (
    df.groupby("Sub-Category")["Profit"]
    .sum()
    .sort_values()
)

sub_profit.plot(
    kind="barh",
    color=[
        "#f44336" if x < 0 else "#4CAF50"
        for x in sub_profit
    ]
)

plt.title("Profit by Sub-Category (Red = Loss)")
plt.xlabel("Profit (USD)")
plt.tight_layout()
plt.show()

# ================================
# 8. CORRELATION: DISCOUNT vs PROFIT
# ================================
sns.scatterplot(
    data=df,
    x="Discount",
    y="Profit",
    alpha=0.4,
    color="#FF5722"
)

plt.title("Does Higher Discount = Lower Profit?")
plt.tight_layout()
plt.show()
