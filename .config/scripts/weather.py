#!/bin/python

import urllib.request, json

city = "85021"
api_key = "8ae78c366c786712d4ba87b48016361b"
units = "imperial"
unit_key = "F"

weather = eval(str(urllib.request.urlopen("http://api.openweathermap.org/data/2.5/weather?zip={}&APPID={}&units={}".format(city, api_key, units)).read())[2:-1])

info = weather["weather"][0]["description"].capitalize()
temp = int(float(weather["main"]["temp"]))

print("%s, %i °%s" % (info, temp, unit_key))
