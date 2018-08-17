import csv
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from country_area_parse import create_country_db

from whichisblank.models import User, Author, Country

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
            print("country name found")
            pass
        else:
            try:
                print("country name not found")
                print(i['country'])
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


