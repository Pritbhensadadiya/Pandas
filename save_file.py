import pandas as pd

data = {
    "Name":['ran','shyam','ghanshyam'],
    "Age": [10,20,30],
    "City": ['gujarat','junagadh','vanthli']

}

df = pd.DataFrame(data)

print(df)

df.to_csv("save.csv",index=False)
df.to_excel("save.xlsx",index=False)