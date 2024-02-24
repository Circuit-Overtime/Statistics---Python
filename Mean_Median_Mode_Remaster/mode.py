import csv
from collections import Counter

with open("SOCR-HeightWeight.csv", newline="") as f:
    read = csv.reader(f)
    data = list(read)

data.pop(0)
fin_data = []

for val in range(len(data)):
    numbers = data[val][2]
    fin_data.append(float(numbers))

data_length = len(fin_data)
# fin_data.sort()
data = Counter(fin_data)
range   = {
    "50-60" : 0,
    "60-70": 0,
    "70-80" :0,
    
}

for height, occurance in data.items():
    if(50 < float(height) < 60):
        range ["50-60"]  += occurance
    elif(60 < float(height) < 70):
        range ["60-70"] += occurance
    else:
        range["70-80"] += occurance

mode_range , mode_occurance = 0,0
for x,occurance in range.items():
    if occurance > mode_occurance:
        mode_range,mode_occurance = [int(x.split("-")[0]), int(x.split("-")[1])], occurance

mode = float(mode_range[0] + mode_range[1])/2
print(f"The Mode is: {mode}")