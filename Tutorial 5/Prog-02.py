import pandas as pd
data = [['Aswin', 21], ['Aravind', 23], ['Ashif', 19]]
df = pd.DataFrame(data, columns=['Name', 'Age'])
df.set_index('Name', inplace=True)
print(df)
