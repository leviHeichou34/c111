import csv 
import pandas as pd
import random 
import statistics
import plotly.graph_objects as go
import plotly.figure_factory as ff

df = pd.read_csv("studentMarks.csv")
data = df["Math_score"].tolist()

mean = statistics.mean(data)
stddev = statistics.stdev(data)
print("mean of population: ", mean)
print("stdev of population: ", stddev)

def random_set_of_mean(counter):
    dataset = []
    for i in range(0, counter):
        random_index = random.randint(0, len(data)-1) 
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean 

mean_list = []
for i in range(0,1000):
    set_of_means = random_set_of_mean(100)
    mean_list.append(set_of_means)

std_dev = statistics.stdev(mean_list)
fig = ff.create_distplot([mean_list], ["math Scores"], show_hist = False)
fig.show()

first_stdev_start, first_stdev_end = mean - std_dev, mean + std_dev 
second_stdev_start, second_stdev_end = mean - (2*std_dev), mean + (2*std_dev) 
third_stdev_start, third_stdev_end = mean - (3*std_dev) , mean + (3*std_dev) 
print("std 1", first_stdev_start, first_stdev_end)
print("std 2", second_stdev_start, second_stdev_end)
print("std 3", third_stdev_start, third_stdev_end)

df = pd.read_csv("data1.csv")
data = df["Math_score"].tolist()

mean_of_sample1 = statistics.mean(data)
stddev = statistics.stdev(data)
print("mean of population: ", mean)
print("stdev of population: ", stddev)

fig = ff.create_distplot([mean_list], ["math Scores"], show_hist = False)
fig.add_trace(go.Scatter(x =[mean, mean], y=[0, 0.17], mode = "lines", name = "MEAN"))
fig.add_trace(go.Scatter(x =[mean_of_sample1, mean_of_sample1], y=[0, 0.17], mode = "lines", name = "MEAN OF SAMPLE"))
fig.add_trace(go.Scatter(x =[first_stdev_end, first_stdev_end], y=[0, 0.17], mode = "lines", name = "MEAN OF SAMPLE"))
fig.show()



