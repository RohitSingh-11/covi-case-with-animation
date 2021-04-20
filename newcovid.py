import covid_daily as cd
import pandas as pd

data = cd.data(country='india', chart='coronavirus-cases-linear')
df = pd.DataFrame(data)
df.to_csv("test.csv")
data2 = pd.read_csv("test.csv")
case = []
day = []
days = 1
for i in data2.iloc[:,-1]:
    case.append(i)
    day.append(days)
    days = days + 1