import pandas as pd


data = {
    "Name":['prit','dev',None,'shyam','meer'],
    "Age": [19,20,None,22,24],
    "salary":[100000,23000,None,32000,5900],
    "performance":[99,98,None,96,95]
}

df = pd.DataFrame(data)
print(df)
print("\n")

df.dropna(inplace=True)
print(df)

df.fillna(0,inplace=True)
print(df)