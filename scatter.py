import csv
import plotly_express as px
import pandas as pd 
df=pd.read_csv("data.csv")
fig=px.scatter(df, x="Height(Inches)", y="Weight(Pounds)")
fig.show()