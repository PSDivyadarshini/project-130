import pandas as pd
import csv

df=pd.read_csv("final.csv")
print(df.shape)

del df["luminosity"]
del df["temp_star_date"]

print(df.shape)