import pandas as pd
import numpy as np

df=pd.read_csv("project.csv")
#df.to_csv("output.csv",index=False)
#print(df)
'''#print(df.head())
print(df.describe())
print(df.shape)
'''

df_filled=df.copy()
df_filled['Quantity']=df_filled['Quantity'].fillna(0)
print(df_filled['Quantity'])
df_filled['Quantity']=df_filled['Quantity'].replace(0,np.average(df_filled['Quantity']))
#df_filled['Category']=df_filled['Category'].fillna(0)
print("\n data frame after filling missing value\n",df_filled['Quantity'])

df_filled['TotalAmount']=df_filled['TotalAmount'].fillna(0)
df_filled['TotalAmount']=df_filled['TotalAmount'].replace(0,np.average(df_filled['TotalAmount']))
print("\n data frame after filling missing value\n",df_filled['TotalAmount'])


df_filled.to_csv("Retail59.csv",index=False)
print(df_filled)




