import random
import csv
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from country_area_parse import create_country_db
# from services import add_countries_to_model
from services import add_countries_to_model


from whichisblank.models import Country, Comparison, Selection

def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'whichisblank/signup.html', {'form': form})

# def login(request):
#     if request.method == "POST":
#



def home(request):
    data = create_country_db()
    example = ""
    for i in data.values():
        if Country.objects.filter(country_name=i['country']):
            pass
        else:
            try:
                Country.objects.create(
                            country_name=i['country'],
                            capital_city=i['capital_city'],
                            size_rank=i['rank'],
                            population_2008=i['population'],
                            land_area_sq_km=i['land_area_km'])
            except:
                print("except error")
    countries = Country.objects.all()

    return render(request, 'whichisblank/home.html', {"countries": countries,
                                                      "example": example,
                                                      "data": data})

def random_assignment():
    countries = Country.objects.all()
    a = random.choice(countries)
    return a

def no_dup_second(a):
    b = random_assignment()
    if a == b:
        b = random_assignment()
    return b



def play(request):
    country_a = random_assignment()
    country_b = no_dup_second(country_a)
    if request.user.is_authenticated:
        user = request.user
        add_countries_to_model(user, country_a, country_b)
        #Todo add these instances to the db with an objects.create using the countries above
    return render(request, 'whichisblank/play.html', {"country_a":country_a,
                                                      "country_b":country_b})

def comp_history(request):
    comp_instances = Comparison.objects.all() #TODO There are no objects because there is no .create in play()
    return render(request, 'whichisblank/comp-history.html', {"comp_instances": comp_instances,
                                                      })