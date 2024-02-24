import numpy as np
import csv 
import plotly.express as px

def plot(path):
    with open(path) as f:
        read_graph = csv.DictReader(f)
        fig = px.scatter(read_graph, x = "Roll No", y="Days Present")
        fig.show()


def open_data(path):
    roll = []
    days = []
    with open(path) as r:
        read = csv.DictReader(r)

        for i in read:
            roll.append(float(i["Roll No"]))
            days.append(float(i["Days Present"]))

    return {"x" : roll, "y": days} 

def calc(value):
    corr = np.corrcoef(value["x"], value["y"])
    print("The corelation co-efficient of the above values is: " ,corr[0,1])



def main():
    path = "F:\Python works\Python Program 2\WhiteHatJt\C106\Student Marks vs Days Present.csv"
    value = open_data(path)
    calc(value)
    plot(path)

main()

