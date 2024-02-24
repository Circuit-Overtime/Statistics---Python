import pandas as pd
import csv
import statistics

data_read = pd.read_csv("F:\Python works\Python Program 2\WhiteHatJt\C101 python\C109_WHT\StudentsPerformance.csv")
height = data_read["reading score"].to_list()
# weight = data_read["Weight(Pounds)"].to_list()

#finding mean for height and weight
height_mean = statistics.mean(height)
# weight_mean = statistics.mean(weight)

#median for height and weight 
height_median = statistics.median(height)
# weight_median = statistics.median(weight)

#mode for height and weight

height_mode  = statistics.mode(height)
# weight_mode = statistics.mode(weight)

#printing the mean , median and mode all together
print("Mean, median and mode of the reading score is {},{},{}".format(height_mean, height_median, height_mode))
# print("Mean, median and mode of the weight is {},{},{}".format(weight_mean, weight_median, weight_mode))

#the standard deviation for the height and weight
height_standard_deviation = statistics.stdev(height)
# weight_standard_deviation = statistics.stdev(weight)

#1 2 and 3 Standard deviation for height
height_first_standard_deviation_start, height_first_standard_deviation_end = height_mean-height_standard_deviation, height_mean + height_standard_deviation
print("The first reading score standard deviation start is: ", height_first_standard_deviation_start)
print("The first reading score standard deviation end is:" , height_first_standard_deviation_end)


height_second_standard_deviation_start, height_second_standard_deviation_end = height_mean- (2*height_standard_deviation), height_mean + (2*height_standard_deviation)
print("The second reading score standard deviation start is: ", height_second_standard_deviation_start)
print("The second reading score standard deviation end is:" , height_second_standard_deviation_end)


height_third_standard_deviation_start, height_third_standard_deviation_end = height_mean- (3*height_standard_deviation), height_mean + (3*height_standard_deviation)
print("The third reading score standard deviation start is: ", height_third_standard_deviation_start)
print("The third reading score standard deviation end is:" , height_third_standard_deviation_end)

#1 2 and 3 Standard Deviation for weight

# weight_first_standard_deviation_start, weight_first_standard_deviation_end = weight_mean-weight_standard_deviation, weight_mean + weight_standard_deviation
# print("The first weight standard deviation start is: ", weight_first_standard_deviation_start)
# print("The first weight standard deviation end is:" , weight_first_standard_deviation_end)


# weight_second_standard_deviation_start, weight_second_standard_deviation_end = weight_mean- (2*weight_standard_deviation), weight_mean + (2*weight_standard_deviation)
# print("The second weight standard deviation start is: ", weight_second_standard_deviation_start)
# print("The second weight standard deviation end is:" , weight_second_standard_deviation_end)


# weight_third_standard_deviation_start, weight_third_standard_deviation_end = weight_mean- (3*weight_standard_deviation), weight_mean + (3*weight_standard_deviation)
# print("The third weight standard deviation start is: ", weight_third_standard_deviation_start)
# print("The third weight standard deviation end is:" , weight_third_standard_deviation_end)

#Calculating Percentage in 1 2 and 3 for height
height_percentage_within_first_std = [result for result in height if result > height_first_standard_deviation_start and result < height_first_standard_deviation_end]
height_percentage_within_second_std = [result for result in height if result > height_second_standard_deviation_start and result < height_second_standard_deviation_end]
height_percentage_within_third_std = [result for result in height if result > height_third_standard_deviation_start and result < height_third_standard_deviation_end]

#Calculating Percentage in 1 2 and 3 for weight
# weight_percentage_within_first_std = [result for result in weight if result > weight_first_standard_deviation_start and result < weight_first_standard_deviation_end]
# weight_percentage_within_second_std = [result for result in weight if result > weight_second_standard_deviation_start and result < weight_second_standard_deviation_end]
# weight_percentage_within_third_std = [result for result in weight if result > weight_third_standard_deviation_start and result < weight_third_standard_deviation_end]

#Printing everything
print("{}% of the data of reading score lies in the 1st standard deviation" .format(len(height_percentage_within_first_std)*100.0/len(height)))
print("{}% of the data of reading score lies in the 2nd standard deviation" .format(len(height_percentage_within_second_std)*100.0/len(height)))
print("{}% of the data of reading score lies in the 3rd standard deviation" .format(len(height_percentage_within_third_std)*100.0/len(height)))

# print("{}% of the data of weight lies in the 1st standard deviation" .format(len(weight_percentage_within_first_std)*100.0/len(weight)))
# print("{}% of the data of weight lies in the 2nd standard deviation" .format(len(weight_percentage_within_second_std)*100.0/len(weight)))
# print("{}% of the data of weight lies in the 3rd standard deviation" .format(len(weight_percentage_within_third_std)*100.0/len(weight)))