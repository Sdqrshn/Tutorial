import pandas as pd
data = {'Car': ['BMW', 'Benz', 'Tesla'], 'Make': [2000, 2015, 2025], 'Price': [19000, 45000, 100]}
df = pd.DataFrame(data)
df.to_excel("cars.xlsx", index=False)
df2 = pd.read_excel("cars.xlsx")
print(df2)
