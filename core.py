import pandas as pd
import plotly.express as px
import math
df=pd.read_csv("data.csv")

data=df ["Population"]. tolist()
print(data)
def mean():
  total=0
  for i in range(0,len(data)):
    total=total+data[i]
  mean=total/len(data)
  print(mean)
  return mean
  
sqlist=[]
for i in data:
  a=int(i)-mean()
  a=a**2
  sqlist.append(a)
print(sqlist)      