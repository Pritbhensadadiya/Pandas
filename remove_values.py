import pandas as pd


data = {
    "Name":['prit','dev','babli','shyam','meer'],
    "Age": [19,20,19,22,24],
    "salary":[100000,23000,21000,32000,5900],
    "performance":[99,98,97,96,95]
}

df = pd.DataFrame(data)
print(df)
print("\n")
print("AFTER")
df.drop(columns=["performance"],inplace=True)
print(df)

