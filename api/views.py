from django.shortcuts import render, redirect
import requests
from . import models
import requests
import json


def home(request):
    cities = models.Country.objects.all()
    weatherData = []
    for country in cities:
        link = "http://api.weatherapi.com/v1/current.json?key=af86a460bbe94c6384e62423200109&q=" + \
            str(country.place)
        data = requests.get(link).json()
        weather = {
            'location': str(data['location']['name']),
            'tempraturec': str(data['current']['temp_c']),
            'tempraturef': str(data['current']['temp_f']),
            'text': str(data['current']['condition']['text']),
            'icon': str(data['current']['condition']['icon'])
        }
        weatherData.append(weather)
    return render(request, "main.html", {"weather": weatherData})


def logic(request):
    country = str(request.POST["country2"])
    helloooo = "http://api.weatherapi.com/v1/current.json?key=af86a460bbe94c6384e62423200109&q=" + country
    hi = requests.get(helloooo).json()
    location = str(hi['location']['name'])
    if models.Country.objects.filter(place=country):
        pass
    else:
        bs = models.Country(place=location)
        bs.save()
    cities = models.Country.objects.all()
    weatherData = []
    for country in cities:
        link = "http://api.weatherapi.com/v1/current.json?key=af86a460bbe94c6384e62423200109&q=" + str(country.place)
        data = requests.get(link).json()
        weather = {
            'location': str(data['location']['name']),
            'tempraturec': str(data['current']['temp_c']),
            'tempraturef': str(data['current']['temp_f']),
            'text': str(data['current']['condition']['text']),
            'icon': str(data['current']['condition']['icon'])
        }
        
        weatherData.append(weather)
    return render(request, "extends.html", {"weather": weatherData})


def delete_city(request, name_place):
    models.Country.objects.get(place=name_place).delete()
    return redirect('home')


def nasa(request):
    nasaKey = "g16onw6OFs5dXytx5gNiFBzrqr4XIRB5baxzo5rj"
    link = f"https://api.nasa.gov/planetary/apod?api_key={nasaKey}"
    page_content = requests.get(link)
    decoded_page = page_content.content.decode()
    json2 = json.loads(decoded_page)
    title = json2['title']
    url = json2['url']
    conten = json2['explanation']
    return render(request,'nasapi.html',{"Link" : url, "title": title, "content1":conten})