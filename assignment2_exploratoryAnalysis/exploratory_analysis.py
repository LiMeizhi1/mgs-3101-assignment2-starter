
import pandas as pd

df = pd.read_csv("data/Sales-Export_2019-2020.csv")

print(df.head())
print(df.shape)
print(df.columns)
print(df.isnull().sum())
print("\nCategories:")
print(df["category"].value_counts())

print("\nData types:")
print(df.dtypes)
