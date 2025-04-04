import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = {
    'rollno': [40, 48, 235, 50, 43],
    'name': ['Sony', 'Shotta', 'Gigi', 'Gopu', 'Shahim'],
    'place': ['TVM', 'MLP', 'EKM', 'TSR', 'MLP'],
    'mark': [78, 92, 85, 88, 76]
}

df = pd.DataFrame(data)
df.to_csv("stud.csv", index=False)

df = pd.read_csv("stud.csv")
print("a) File Contents\n", df)

df.set_index('rollno', inplace=True)
print("\nb) Roll Number as Index\n", df)

print("\nc) Name and Mark\n", df[['name', 'mark']])

print("\nd) Sorted by Name\n", df.sort_values('name')[['name', 'mark']])

print("\ne) Sorted by Mark Descending\n", df.sort_values('mark', ascending=False)[['name', 'mark']])

print("\nf) Statistics")
print("Average:", df['mark'].mean())
print("Median:", df['mark'].median())
print("Mode:", df['mark'].mode()[0])

print("\ng) Min and Max Marks")
print("Minimum:", df['mark'].min())
print("Maximum:", df['mark'].max())

print("\nh) Variance and Standard Deviation")
print("Variance:", df['mark'].var())
print("Standard Deviation:", df['mark'].std())

plt.hist(df['mark'], bins=5, edgecolor='black')
plt.xlabel('Marks')
plt.ylabel('Frequency')
plt.title('Histogram of Marks')
plt.show()

df.drop(columns=['place'], inplace=True)
print("\ni) After Removing Place Column\n", df)
