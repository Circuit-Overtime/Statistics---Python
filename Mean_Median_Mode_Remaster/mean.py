
import csv
with open("SOCR-HeightWeight.csv", newline="") as f:
    f_read = csv.reader(f)
    data = list(f_read)

data.pop(0)
new_data = []
for row in range(len(data)):
    num = data[row][2]
    new_data.append(float(num))

length = len(new_data)
get_sum = 0
for x in new_data:
    get_sum += x

mean = get_sum/length
print("The Mean of the Above observations are  " + str(round(mean)))
