import pandas as pd

data = {
    'index': [1, 2, 3, 4, 5],
    'company': ['Toyota', 'BMW', 'Mercedes', 'Audi', 'Ford'],
    'body-style': ['sedan', 'SUV', 'sedan', 'coupe', 'hatchback'],
    'wheel-base': [95.0, 102.5, 98.7, 99.3, 96.2],
    'length': [150.3, 170.5, 165.0, 155.2, 148.7],
    'engine-type': ['gas', 'diesel', 'gas', 'gas', 'diesel'],
    'num-of-cylinders': [4, 6, 4, 8, 4],
    'horsepower': [130, 250, 190, 220, 140],
    'average-mileage': [30, 20, 25, 22, 28],
    'price': [20000, 50000, 40000, 45000, 18000]
}

df = pd.DataFrame(data)
df.to_csv("auto.csv", index=False)

df = pd.read_csv("auto.csv")
df.dropna(inplace=True)

print("\n1) Cleaned and Updated CSV File:")
print(df.to_string(index=False))

most_expensive_company = df.loc[df['price'].idxmax(), 'company']
print(f"\n2) Most Expensive Car Company: {most_expensive_company}")

toyota_cars = df[df['company'].str.lower() == 'toyota']
print("\n3) All Toyota Car Details:")
print(toyota_cars.to_string(index=False))

car_counts = df['company'].value_counts()
print("\n4) Total Cars of Each Company:")
print(car_counts.to_string())

highest_priced_cars = df.loc[df.groupby('company')['price'].idxmax()]
print("\n5) Highest Priced Car of Each Company:")
print(highest_priced_cars.to_string(index=False))

avg_mileage = df.groupby('company')['average-mileage'].mean()
print("\n6) Average Mileage of Each Company:")
print(avg_mileage.to_string())

sorted_cars = df.sort_values(by='price', ascending=False)
print("\n7) Cars Sorted by Price:")
print(sorted_cars.to_string(index=False))
