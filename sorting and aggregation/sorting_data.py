import pandas as pd


data = {
    "Name":['prit','dev',None,'shyam','meer'],
    "Age": [19,20,23,22,24],
    "salary":[100000,23000,34000,32000,5900],
}

df = pd.DataFrame(data)
print(df)
print("\n")

df.sort_values(by="Age" , ascending=False,inplace=True)
print(df) 
print("\n")
df.sort_values(by=["Age","salary"] , ascending=[True,False],inplace=True)
print(df)
