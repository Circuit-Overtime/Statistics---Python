import math
import pyttsx3
import csv 

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine = pyttsx3.init()

with open('F:\Python works\Python Program 2\WhiteHatJt\Graph_Python_Project\Standard Deviation\data.csv', newline= '') as f:
    reader = csv.reader(f)
    data_file = list(reader)
data = data_file[0]
# total = 0

def mean(data):
    length = len(data)
    total = 0
    for x in data:
        total  += int(x)

    mean = total/length
    return mean

obv = []
for y in data:
    sd = int(y) - mean(data)
    sd  = sd**2
    obv.append(sd)
sum_obv = 0
for i in obv:
    sum_obv = sum_obv + i

standard_dev = (str(round(math.sqrt(sum_obv/(len(data) - 1)))))
print("The Standard Deviation of the Above Observations are:  " + standard_dev)
pyttsx3.speak(f"The Standard Deviation of the Above Observations is {standard_dev}")



