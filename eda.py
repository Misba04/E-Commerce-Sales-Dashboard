import pandas as pd

df = pd.read_csv(
    r"C:\E-Commerce Sales Dashboard\Dataset\Cleaned_Amazon_Sales_Report.csv"
)

print("Total Sales:", df["Amount"].sum())
print("Total Orders:", df["Order ID"].nunique())
print("Average Order Value:", df["Amount"].mean())

print("\nTop 10 States by Sales")
print(df.groupby("ship-state")["Amount"].sum().sort_values(ascending=False).head(10))

print("\nTop 10 Categories by Sales")
print(df.groupby("Category")["Amount"].sum().sort_values(ascending=False).head(10))

print("\nOrder Status Count")
print(df["Status"].value_counts())

print("\nSales by Fulfilment")
print(df.groupby("Fulfilment")["Amount"].sum().sort_values(ascending=False))

print("\nAvailable Columns:")
print(df.columns.tolist())

print("\nAverage Quantity per Order")
print(df["Qty"].mean())

print("\nTop 10 Products by Sales")
print(df.groupby("SKU")["Amount"].sum().sort_values(ascending=False).head(10))

print("\nTop 10 Cities by Sales")
print(df.groupby("ship-city")["Amount"].sum().sort_values(ascending=False).head(10))