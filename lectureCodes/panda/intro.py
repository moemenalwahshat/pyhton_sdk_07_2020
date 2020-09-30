import pandas as pd 
url ="https://raw.githubusercontent.com/cs109/2014_data/master/countries.csv" 
data = pd.read_csv(url)
print(data["Country"][1])
print(data.head(10))
print(data.tail(10))
data_des = data.describe(include="all")


path = "C:\\Users\\share\\Desktop\\data.xlsx" 
data2 = pd.read_excel(path)
data_des2 = data2.describe(include="all")
print(data2.head(10))