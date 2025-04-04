import pandas as pd
data = {  'Name': ['Aleena', 'Aravind', 'Devan', 'Chulli', 'Anshiba', 'Ashif', 'Ayana', 'Aswini'],
    'Branch': ['CSE', 'ECE', 'CSE', 'ME', 'CSE', 'EEE', 'ECE', 'ME'],
    'Year': [2, 3, 2, 1, 3, 2, 1, 3],
    'CGPA': [9.2, 8.5, 9.4, 7.9, 9.1, 8.2, 9.5, 7.8]}
df = pd.DataFrame(data)
df.to_csv("student.csv", index=False)
df = pd.read_csv("student.csv")
print("1) Average CGPA of all students:")
print(df['CGPA'].mean())
print("\n2) Students having CGPA > 9:")
print(df[df['CGPA'] > 9])
print("\n3) CSE students with CGPA > 9:")
print(df[(df['Branch'] == 'CSE') & (df['CGPA'] > 9)])
print("\n4) Student(s) with maximum CGPA:")
print(df[df['CGPA'] == df['CGPA'].max()])
print("\n5) Average CGPA of each branch:")
print(df.groupby('Branch')['CGPA'].mean())
