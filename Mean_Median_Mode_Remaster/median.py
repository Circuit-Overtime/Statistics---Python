import csv
with open("SOCR-HeightWeight.csv", newline="") as f:
    read = csv.reader(f)
    data = list(read)

data.pop(0)
fin_data = []
for val in range(len(data)):
    numbers = data[val][2]
    fin_data.append(float(numbers))

data_length = len(fin_data)
fin_data.sort()

if data_length % 2 == 0:
    median_one = float(fin_data[data_length//2])
    median_two = float(fin_data[data_length//2 - 1])
    median = (median_one + median_two) / 2

else:
    median = float(fin_data[data_length//2])

print("The Median is:   " + str(round(median)))
