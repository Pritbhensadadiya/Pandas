import pandas as pd

df_customer = pd.DataFrame({
    'customerID':[1,2,3],
    'name':["prit","suresh","jayesh"]}
)

df_order = pd.DataFrame({
    'customerID':[1,2,3],
    'orderID':[250,450,350]
})

df_concate = pd.concat([df_customer,df_order],ignore_index=True)
print(df_concate)