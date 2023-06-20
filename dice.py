import random
import plotly.figure_factory as FF
import plotly.graph_objects as go
import statistics


dice_result = []
for i in range(0,1000):
    dice1=random.randint(1,6)
    dice2=random.randint(1,6)
    dice_result.append(dice1+dice2)

#Calculating the mean and the standard deviation
mean=sum(dice_result)/len(dice_result)
std_deviation = statistics.stdev(dice_result)
median = statistics.median(dice_result)
mode = statistics.mode(dice_result)

print("Mean of this data is ",mean)
print("standard deviation of this data is ",std_deviation)
print("Median of this data is ",median)
print("Mode of this data is ",mode)

first_stdev_start, first_stdev_end= mean-std_deviation, mean+std_deviation
second_stdev_start, second_stdev_end= mean-(2*std_deviation), mean+(2*std_deviation)
thrid_stdev_start, thrid_stdev_end= mean-(3*std_deviation), mean+(3*std_deviation)

fig=FF.create_distplot([dice_result],["Result"] ,show_hist=False )
fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.17], mode="lines", name="MEAN"))
fig.add_trace(go.Scatter(x=[first_stdev_start, first_stdev_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1 start"))
fig.add_trace(go.Scatter(x=[first_stdev_end, first_stdev_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1 end"))
fig.add_trace(go.Scatter(x=[second_stdev_start, second_stdev_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2 start"))
fig.add_trace(go.Scatter(x=[second_stdev_end, second_stdev_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2 end"))
fig.show()



list_of_data_within_1_std_deviation = [result for result in dice_result if result > first_stdev_start and result < first_stdev_end]
list_of_data_within_2_std_deviation = [result for result in dice_result if result > second_stdev_start and result < second_stdev_end]
list_of_data_within_3_std_deviation = [result for result in dice_result if result > thrid_stdev_start and result < second_stdev_end]

print("{}% of data lies within 1 standard deviation".format(len(list_of_data_within_1_std_deviation)*100.0/len(dice_result)))
print("{}% of data lies within 2 standard deviations".format(len(list_of_data_within_2_std_deviation)*100.0/len(dice_result)))
print("{}% of data lies within 3 standard deviations".format(len(list_of_data_within_3_std_deviation)*100.0/len(dice_result)))


#days=7
#print("number of days in a week ={}".format(days))