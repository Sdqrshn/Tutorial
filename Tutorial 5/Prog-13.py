import pandas as pd  
data = {  
    "name": ["Aleena", "Aravind", "Devan", "Chulli", "Anshiba", "Ashif", "Ayana", "Aswini"],  
    "gender": ["F", "M", "M", "M", "F", "M", "F", "F"],  
    "start_date": ["2015-06-23", "2016-07-12", "2017-08-19", "2018-09-25", "2019-10-30", "2020-11-15", "2021-12-01", "2022-01-20"],  
    "salary": [50000, 60000, 75000, 54000, 72000, 51000, 68000, 57000],  
    "team": ["HR", "Finance", "IT", "Marketing", "IT", "HR", "Finance", "Marketing"]  
}  
df = pd.DataFrame(data)  
df.to_csv("employee.csv", index=False)  
df = pd.read_csv("employee.csv")  
print("1) First 7 Records:\n", df.head(7), "\n")  
print("2) Employee Names in Alphabetical Order:\n", df.sort_values(by="name")["name"].tolist(), "\n")  
print("3) Employee with Highest Salary:\n", df.loc[df["salary"].idxmax(), "name"], "\n")  
print("4) Male Employees:\n", df[df["gender"] == "M"]["name"].tolist(), "\n")  
print("5) Teams Employees Belong To:\n", df["team"].unique().tolist())  
