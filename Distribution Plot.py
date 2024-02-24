import plotly.express as px
import plotly.figure_factory as ff
import csv
import pandas as pd
df = pd.read_csv("F:\\Python works\\Python Program 2\\WhiteHatJt\\C101 python\\C109_WHT\\108data.csv")
fig = ff.create_distplot([df["Avg Rating"].tolist()], ["Average Rating"], show_hist = False)
fig.show()