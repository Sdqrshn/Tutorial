import pandas as pd
data = {'Car': ['BMW', 'Benz', 'Tesla'], 'Make': [2000, 2015, 2025], 'Price': [19000,45000,100]}
df = pd.DataFrame(data)
df.to_excel("output.xlsx", index=False)
print("Data written to output.xlsx successfully!")
