from whichisblank.models import Country, Comparison, Selection


def add_countries_to_model(user, a, b):
    try:
        Comparison.objects.create(user=user, first_comp=a, second_comp=b)
    except:
        print("add countries to model error")
    return
