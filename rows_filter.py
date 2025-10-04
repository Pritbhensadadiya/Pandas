import pandas as pd


data = {
    "Name":['prit','dev','babli','shyam','meer'],
    "Age": [19,20,19,22,24],
    "salary":[100000,23000,21000,32000,5900],
    "performance":[99,98,97,96,95]
}

df = pd.DataFrame(data)

high_salary = df[df['salary']>50000]
print(high_salary)

print("\n")
filtered = df[(df['Age']>15) & (df['salary']>25000)]
print(filtered)
print("\n")

filtered_or = df[(df['Age']>15) | (df['salary']>10000)]
print(filtered_or)