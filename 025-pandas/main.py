# import csv
#
# Python has inbuilt csv library
# with open("./data/weather_data.csv") as weather:
#     # data = list(map(lambda w: w.rstrip("\n"), weather.readlines()))
#     data = csv.reader(weather)
#     temperatures = []
#     for row in data:
#         print(row)
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#
#     print(temperatures)

import pandas

data = pandas.read_csv("./data/weather_data.csv")
print(type(data))
print(data["temp"])
print(type(data["temp"]))

data_dict = data.to_dict()
print(data_dict)
data_json = data.to_json()
print(data_json)

temps = data["temp"].to_list()
print(temps)
print(f"Average temperature - method 1: {sum(temps) / len(temps)}")
print(f"Average temperature - method 2: {data["temp"].mean()}")
print(f"Max temperature: {data["temp"].max()}")
print(f"Max temperature: {data.temp.max()}")
print(f"Max temperature: {data.iloc[:,1].max()}")

# Get row data for single row by using a filter condition
print(data[data["day"] == "Monday"])
print(data[data.day == "Monday"])
print(data.iloc[0,:])
print(data.loc[0,:])

# Get row for day that had highest temp
print(data[data.temp == data.temp.max()])

# Get Monday's temperature and convert to Fahrenheit
print(f"Monday's temperature: {data[data.day == "Monday"].temp[0] * 9/5 + 32} F")

# Create a dataframe from scratch
data_dict = {
    "students": ["Bob", "Charlie", "Vic"],
    "scores": [76, 47, 88]
}

df = pandas.DataFrame(data_dict)
df.to_csv("./data/student_scores.csv")

squirrel_data = pandas.read_csv("./data/2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240208.csv")
print(squirrel_data.head(10))

print(squirrel_data['Primary Fur Color'].value_counts())
s_dict = squirrel_data['Primary Fur Color'].value_counts().to_dict()
print(s_dict)
squirrel_dict = {
    "Fur Color": s_dict.keys(),
    "Count": s_dict.values()
}
print(squirrel_dict)
squirrel_count_df = pandas.DataFrame(squirrel_dict)
print(squirrel_count_df)
squirrel_count_df.to_csv("./data/squirrel_count.csv")