import os
import csv

script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

csv_file = "weather_data.csv"
csv_file_2 = "2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240312.csv"

# with open("weather_data.csv", "r") as file:
#     data = file.readlines()
#     print(data)


"""column reading with csv module."""
# with open(csv_file, "r") as file:
#     data = csv.reader(file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(row[1])
    #print(temperatures)

import pandas

"""import csv with pandas to create table and extract column(series) 'temp' """
# data = pandas.read_csv(csv_file)
# print(data)
# print("\n ****************** \n")
#print(data["temp"])

"""turn data into dictionary"""
# data_dict = data.to_dict()
# print(data_dict)


"""convert 'temp' column into list and get average"""
# data_list = data["temp"].to_list()
#average_temp = sum(data_list) / len(data_list)
#print(average_temp)


"""Use built in pandas method to get average and max value"""
#print(data["temp"].mean())
#print(data["temp"].max())

"""use 'column' as method to get same data"""
#print(data.temp)


"""Get data in row and do filtering"""
#print(data[data.condition == "Sunny"])
#print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]

"""get filtered row's associated data ex: mondays 'temp'"""

# celsius = monday.temp
# fahrenheit = celsius * 9/5 + 32
#print(fahrenheit)


"""Turn row into list"""
#print(data.values.tolist())

"""create a dataframe from scratch"""
# data_dict = { 
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
# new_df = pandas.DataFrame(data_dict)  
# print(new_df)
# new_df.to_csv("new_data.csv")

"""Import Squirrel data, get all fur color count counts"""
df = pandas.read_csv(csv_file_2)


# MIKEs method... Easier
color_count = df["Primary Fur Color"].value_counts()
new_df = pandas.DataFrame(color_count)
new_df.to_csv("squirrel_color_count_1.csv")
    
# 100 days of code method
grey_squirrels_count = len(df[df["Primary Fur Color"] == "Gray"])
black_squirrels_count = len(df[df["Primary Fur Color"] == "Black"])
red_squirrels_count = len(df[df["Primary Fur Color"] == "Cinnamon"])

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
}

new_df = pandas.DataFrame(data_dict)
new_df.to_csv("squirrel_color_count_2.csv")


