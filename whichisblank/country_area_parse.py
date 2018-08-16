import csv



def create_country_db():
    filename = 'country_area_population_2002_2008.csv'
    reader = csv.DictReader(open(filename))
    dict = {}
    pk = 1
    for i in reader:
        dict[pk] = {"rank": i['rank'],
                    "country": i["country"],
                    "land_area_km": i['land_area_km'],
                    'population': i["population_2008"],
                    "capital_city": i["capital_city"]}
        # dict['Country'] =
        pk += 1
        # new_list.append(i['Rank'])
        # pass
    return dict

create_country_db()
