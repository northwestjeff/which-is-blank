import csv



def create_country_db():
    filename = 'country_area_population_2002_2008.csv'
    reader = csv.DictReader(open(filename))
    dict = {}
    pk = 1
    for i in reader:
        dict[pk] = {"Ran}
        new_list.append(i['Rank'])
        # pass
    return new_list

create_country_db()
