import pandas as pd
df = pd.read_csv("auto.csv")
df.dropna(inplace=True)
print(df.loc[df['price'].idxmax(), 'company'])
print(df[df['company'].str.lower() == 'toyota'])
print(df['company'].value_counts())
print(df.loc[df.groupby('company')['price'].idxmax()])
print(df.groupby('company')['average-mileage'].mean())
print(df.sort_values(by='price', ascending=False))
