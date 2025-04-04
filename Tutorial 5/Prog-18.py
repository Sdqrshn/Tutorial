import pandas as pd
import matplotlib.pyplot as plt
data = {   'date': ['2024-04-01', '2024-04-02', '2024-04-03', '2024-04-04', '2024-04-05', '2024-04-06', '2024-04-07', '2024-04-08', '2024-04-09', '2024-04-10'],
    'temperature': [30, 27, 32, 28, 29, 25, 31, 26, 33, 29],
    'humidity': [80, 85, 78, 82, 76, 90, 75, 88, 70, 79],
    'windSpeed': [12, 10, 15, 9, 11, 8, 14, 13, 10, 12],
    'precipitationType': ['Rain', 'None', 'Rain', 'Rain', 'None', 'Snow', 'None', 'Snow', 'Rain', 'None'],
    'place': ['Kochi', 'Delhi', 'Mumbai', 'Chennai', 'Kolkata', 'Shimla', 'Bangalore', 'Manali', 'Goa', 'Pune'],
    'weather': ['Rainy', 'Cloudy', 'Rainy', 'Rainy', 'Sunny', 'Snowy', 'Sunny', 'Snowy', 'Rainy', 'Cloudy']}
df = pd.DataFrame(data)
df.to_csv("weather.csv", index=False)
df = pd.read_csv("weather.csv")
print("1) First 10 rows of weather data:")
print(df.head(10))
print("\n2) Maximum Temperature:")
print(df['temperature'].max())
print("\n3) Minimum Temperature:")
print(df['temperature'].min())
print("\n4) Places with Temperature less than 28°C:")
print(df[df['temperature'] < 28]['place'])
print("\n5) Places with Weather = Cloudy:")
print(df[df['weather'] == 'Cloudy']['place'])
print("\n6) Frequency of Each Weather Type:")
print(df['weather'].value_counts().sort_index())
df.plot(x='date', y='temperature', kind='bar', title='Temperature of Each Day', legend=False)
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.tight_layout()
plt.show()
