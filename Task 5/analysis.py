import pandas as pd
import matplotlib.pyplot as plt

# Load CSV
df = pd.read_csv("sales.csv")
print(df.head())

# Total sales by product
sales_by_product = df.groupby("Product")["Sales"].sum()
print("\nSales by Product:\n", sales_by_product)

sales_by_product.plot(kind="bar", figsize=(7,4))
plt.title("Total Sales by Product")
plt.xlabel("Product")
plt.ylabel("Sales")
plt.show()

# Sales by region
sales_by_region = df.groupby("Region")["Sales"].sum()
print("\nSales by Region:\n", sales_by_region)

sales_by_region.plot(kind="pie", autopct="%1.1f%%", figsize=(6,6))
plt.title("Sales Distribution by Region")
plt.ylabel("")
plt.show()

# Sales trend
sales_by_date = df.groupby("Date")["Sales"].sum()
print("\nSales by Date:\n", sales_by_date)

sales_by_date.plot(kind="line", marker="o", figsize=(7,4))
plt.title("Sales Trend Over Time")
plt.xlabel("Date")
plt.ylabel("Sales")
plt.grid()
plt.show()
