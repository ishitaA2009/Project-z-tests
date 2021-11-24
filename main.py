import plotly.figure_factory as ff 
import statistics
import random
import csv
import pandas as pd 
import plotly.graph_objects as go 

df = pd.read_csv("medium_data.csv")
data = df["reading_time"].to_list()
population_mean = statistics.mean(data)
print("Mean of the data is : ", population_mean)

def random_set_of_mean(counter):
    dataset = []

    for i in range(0, counter):
        random_index= random.randint(0,len(data))
        value = data[random_index]
        dataset.append(value)

    mean = statistics.mean(dataset)
    return mean

def show_fig(mean_list):
    df = mean_list
    fig = ff.create_distplot([df], ["reading_time"], show_hist=False)
    fig.show()

def setup():
    mean_list = []

    for i in range(0,100):
        set_of_means= random_set_of_mean(30)
        mean_list.append(set_of_means)

    show_fig(mean_list)

    sampling_mean = statistics.mean(mean_list)
    stdDev = statistics.stdev(mean_list)
    print("Sampling mean:- ",sampling_mean)
    print("Sampling Standard Deviation:- ",stdDev)

    firststdDevStart, firststdDevEnd = sampling_mean - stdDev, sampling_mean + stdDev
    secondstdDevStart, secondstdDevEnd = sampling_mean - (2*stdDev), sampling_mean + (2*stdDev)
    thirdstdDevStart, thirdstdDevEnd = sampling_mean - (3*stdDev), sampling_mean + (3*stdDev)

    df = pd.read_csv("medium_data.csv")
    data = df["reading_time"].to_list()
    new_sample_mean = statistics.mean(data)
    print("Mean of Sampling Distribution", new_sample_mean)

    fig = ff.create_distplot([mean_list],["Population Mean"], show_hist = False)

    fig.add_trace(go.Scatter(x=[sampling_mean, sampling_mean], y=[0,0.17],mode = "lines",name = "Mean"))
    fig.add_trace(go.Scatter(x=[new_sample_mean, new_sample_mean], y=[0,0.17],mode = "lines",name = "Mean of Sample"))
    fig.add_trace(go.Scatter(x=[firststdDevEnd,firststdDevEnd], y=[0,0.17],mode = "lines",name = "Standard Deviation 1 end"))
    fig.add_trace(go.Scatter(x=[secondstdDevEnd,secondstdDevEnd], y=[0,0.17],mode = "lines",name = "Standard Deviation 2 end"))
    fig.add_trace(go.Scatter(x=[thirdstdDevEnd,thirdstdDevEnd], y=[0,0.17],mode = "lines",name = "Standard Deviation 3 end"))
    fig.show()

    zScore = (new_sample_mean - sampling_mean)/stdDev
    print("z Score is : ", zScore)

setup()

