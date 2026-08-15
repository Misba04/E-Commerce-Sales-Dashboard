import pandas as pd

df = pd.read_csv(
    r"C:\E-Commerce Sales Dashboard\Dataset\Amazon_Sales_Report.csv",
    low_memory=False
)

print(df.head())
print(df.info())
print(df.describe())
print(df.isnull().sum())

df.drop_duplicates(inplace=True)

df.drop(columns=["Unnamed: 22"], inplace=True, errors="ignore")

df["Date"] = pd.to_datetime(
    df["Date"],
    format="%m-%d-%y",
    errors="coerce"
)

df.to_csv(
    r"C:\E-Commerce Sales Dashboard\Dataset\Cleaned_Amazon_Sales_Report.csv",
    index=False
)

print("Data cleaned successfully!")

import sqlite3

conn = sqlite3.connect(
    r"C:\E-Commerce Sales Dashboard\ecommerce.db"
)

df.to_sql(
    "sales",
    conn,
    if_exists="replace",
    index=False
)

conn.close()

print("Data saved to SQLite successfully!")

df.to_csv(
    r"C:\E-Commerce Sales Dashboard\Dataset\Cleaned_Amazon_Sales_Report.csv",
    index=False
)

print("Data cleaned successfully!")

import sqlite3

conn = sqlite3.connect(
    r"C:\E-Commerce Sales Dashboard\ecommerce.db"
)

df.to_sql(
    "sales",
    conn,
    if_exists="replace",
    index=False
)

conn.close()

print("Data saved to SQLite successfully!")