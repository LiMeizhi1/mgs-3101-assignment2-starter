
import pandas as pd

df = pd.read_csv("data/Sales-Export_2019-2020.csv")
df.columns = df.columns.str.strip()
df["order_value_EUR"] = pd.to_numeric(df["order_value_EUR"].str.replace(",", ""))
print(df.head())
print(df.shape)
print(df.columns.tolist())
print(df.isnull().sum())
print("\nCategories:")
print(df["category"].value_counts())
print("\nData types:")
print(df.dtypes)
print(df["order_value_EUR"].head(10))
print(df["cost"].head(10))
print("\nOrder Value Statistics:")
print(df["order_value_EUR"].describe())
print("\nCost Statistics:")
print(df["cost"].describe())

sales_by_category = df.groupby("category")["order_value_EUR"].sum()
print("\nSales by Category:")
print(sales_by_category.sort_values(ascending=False))
print("\nHighest Order:")
print(df[df["order_value_EUR"] == df["order_value_EUR"].max()])
print("\nLowest Order:")
print(df[df["order_value_EUR"] == df["order_value_EUR"].min()])
average_order = df["order_value_EUR"].mean()
if average_order >= 100000:
    print("Average order value meets the target.")
else:
    print("Average order value is below the target.")
