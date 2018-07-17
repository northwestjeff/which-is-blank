import csv



def create_country_db():
    filename = 'country_area_population_2002_2008.csv'
    reader = csv.DictReader(open(filename))
    for i in reader:
        print(i['Rank'])
        # pass
    return reader

create_country_db()
