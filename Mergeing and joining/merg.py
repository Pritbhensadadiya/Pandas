import pandas as pd

df_customer = pd.DataFrame({
    'customerID':[1,2,3],
    'name':["prit","suresh","jayesh"]}
)

df_order = pd.DataFrame({
    'customerID':[1,2,3],
    'orderID':[250,450,350]
})

df_merged = pd.merge(df_customer,df_order,on="customerID",how='inner')
print("INNER JOIN")
print(df_merged)

