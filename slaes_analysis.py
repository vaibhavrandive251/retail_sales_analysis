import pandas as pd
import matplotlib.pyplot as plt

# 1. Load Dataset
df = pd.read_csv("train.csv")

print("Dataset Shape:", df.shape)
print("\nColumn Names:")
print(df.columns)

# 2. Data Cleaning
print("\nMissing Values:")
print(df.isnull().sum())

df = df.dropna()

# 3. Convert Date Column
df['Order Date'] = pd.to_datetime(df['Order Date'], dayfirst=True)


# 4. Feature Engineering
df['Month'] = df['Order Date'].dt.month
df['Year'] = df['Order Date'].dt.year

# 5. Total Sales
total_sales = df['Sales'].sum()
print("\nTotal Sales:", total_sales)

# 6. Monthly Sales Analysis
monthly_sales = df.groupby('Month')['Sales'].sum()

plt.figure()
plt.plot(monthly_sales)
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()

# 7. Top 5 Products
top_products = df.groupby('Product Name')['Sales'].sum().sort_values(ascending=False).head(5)

print("\nTop 5 Revenue Generating Products:")
print(top_products)
