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


def home(request):
    # authors = Author.objects.all()
    data = create_country_db()
    data_list = []
    example = type(data)
    # for i in data:
    #     data_list.append(i)
    #     if Country.objects.filter(Country=i["Country"]):
    #         example = "yes"
    #     else:
    #         example = "no"
    #         Country.objects.create(
    #             country_name=i['Country'],
    #             capital_city=i['Capital city'],
    #             size_rank=i['Rank'],
    #             population_2008=i['2008 Population'],
    #             land_area_sq_km=i['Land_area_sq_km']
    #         )
    countries = Country.objects.all()

    return render(request, 'whichisblank/home.html', {"countries": countries,
                                                      "data": data,
                                                      "example":example,
                                                      "data_list":data_list})


