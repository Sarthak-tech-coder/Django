import requests
country = input()
link ="http://api.weatherapi.com/v1/current.json?key=af86a460bbe94c6384e62423200109&q="+country
json = requests.get(link)
data= json.json()
location = data['location']['name']
tempraturec = data['current']['temp_c']
tempraturef = data['current']['temp_f']
text= data['current']['condition']['text']
icon= data['current']['condition']['icon']