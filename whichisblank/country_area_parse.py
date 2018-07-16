import csv
import sys
import json

from whichisblank.


data = []

with open('country_area_population_2002_2008.csv') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        data.append(row)


fieldnames = data[0]

print(fieldnames)

country_data = {}
country_data['pk'] = ''

for i in fieldnames:
    country_data[i] = ""
print(country_data)


pk = 1
print("====")
for i in data[1:]:
    for x in i:
        pass



