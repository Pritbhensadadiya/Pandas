import pandas as pd

df = pd.read_csv("sales_data_sample.csv",encoding="latin1")

print("Display the info of dataset :")

print(df.info())
