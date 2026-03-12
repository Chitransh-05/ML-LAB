# Read a CSV file and display first five & last five records

import pandas as pd

df = pd.read_csv("diabetes_data_upload.csv")  # replace with your file name

print("First 5 Records:")
print(df.head())

print("\nLast 5 Records:")
print(df.tail())
