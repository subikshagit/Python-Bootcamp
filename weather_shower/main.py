#with open("data.csv") as file:
# file_read = file.readlines()
#  file
# print(file_read)


import csv
import pandas

data = pandas.read_csv('data.csv')
print(data['temp'].max())
print(data[data['temp']==data['temp'].max()])

with open("data.csv") as csv_file:
    data = csv.reader(csv_file)
    temperature = []
    for row in data:
        if row[1]!='temp':
            temperature.append(row[1])
    print(temperature)

