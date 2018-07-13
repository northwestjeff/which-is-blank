import csv
import sys
import json


data = []

with open('country_area_population_2002_2008.csv') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        data.append(row)


fieldnames = data[0]

print(fieldnames)

