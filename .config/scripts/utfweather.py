#!/bin/python

from urllib.parse import urlparse
from configparser import ConfigParser
from collections import defaultdict
import zipcode
import argparse
import os
import requests
import json
import subprocess
import logging
import re
import time

logging.getLogger().setLevel(logging.WARNING)

def get_icon(icon, isDaytime):
   if isDaytime:
       parsed = urlparse(icon).path
       icon = re.search('[^/]+$', parsed)
       icon = icon.group(0)
       icon = re.sub(r',.*', '', icon)
       icons = {
                "skc": "",
                "few": "",
                "sct": "",
                "bkn": "",
                "ovc": "",
                "wind_skc": "",
                "wind_few": "",
                "wind_sct": "",
                "wind_bkn": "",
                "wind_ovc": "",
                "snow": "",
                "rain_snow": "",
                "rain_sleet": "",
                "snow_sleet": "",
                "fzra": "",
                "rain_fzra": "",
                "snow_fzra": "",
                "sleet": "",
                "rain": "",
                "rain_showers": "",
                "rain_shows_hi": "",
                "tsra": "",
                "tsra_sct": "",
                "tsra_hi": "",
                "tornado": "",
                "hurricane": "",
                "tropical_storm": "",
                "dust": "",
                "smoke": "",
                "haze": "",
                "hot": "",
                "cold": "",
                "blizzard": "",
                "fog": "",
                }
       result = str(icons.get(icon, "?"))
       return result
   else:
       parsed = urlparse(icon).path
       icon = re.search('[^/]+$', parsed)
       icon = icon.group(0)
       icon = re.sub(r',.*', '', icon)
       icons = {
                "skc": "",
                "few": "",
                "sct": "",
                "bkn": "",
                "ovc": "",
                "wind_skc": "",
                "wind_few": "",
                "wind_sct": "",
                "wind_bkn": "",
                "wind_ovc": "",
                "snow": "",
                "rain_snow": "",
                "rain_sleet": "",
                "snow_sleet": "",
                "fzra": "",
                "rain_fzra": "",
                "snow_fzra": "",
                "sleet": "",
                "rain": "",
                "rain_showers": "",
                "rain_shows_hi": "",
                "tsra": "",
                "tsra_sct": "",
                "tsra_hi": "",
                "tornado": "",
                "hurricane": "",
                "tropical_storm": "",
                "dust": "",
                "smoke": "",
                "haze": "",
                "hot": "",
                "cold": "",
                "blizzard": "",
                "fog": "",
                }
       result = str(icons.get(icon, "?"))
       return result

def wind_direction(winddir):
    icons = {
            'N': "⭣",
            'NE': "⭩",
            'E': "⭠",
            'SE':"⭦",
            'S' : "⭡",
            'SW': "⭧",
            'W' :"⭢",
            'NW':"⭨"
            }
    winddir = icons.get(winddir)
    return winddir

def sendmessage(message):
    subprocess.Popen(['notify-send', "-t", "100000", message])

def get5day(geolocation):
    forecast = requests.get(geolocation)
    forecast = json.loads(forecast.text)
    d = defaultdict(dict)
    for day in range(0,14):
        d["name"][day] = forecast["properties"]["periods"][day]["name"]
        d["isDaytime"][day] = forecast["properties"]["periods"][day]["isDaytime"]
        d["desc"][day] = forecast["properties"]["periods"][day]["detailedForecast"]
        d["shrtdesc"][day] = forecast["properties"]["periods"][day]["shortForecast"]
        d["temp"][day] = forecast["properties"]["periods"][day]["temperature"]
        if d["isDaytime"][day]:
            isDaytime = True
            d["icon"][day] = get_icon(forecast["properties"]["periods"][day]["icon"], isDaytime)
        else:
            isDaytime = False
            d["icon"][day] = get_icon(forecast["properties"]["periods"][day]["icon"], isDaytime)

    if d["isDaytime"][2]:
        message = ("%s - %s°F\t%s\n%s\n\n%s\t%s°F\t%s\t%s\n\t%s°F\t%s\t%s\n%s\t%s°F\t%s\t%s\n\t%s°F\t%s\t%s\n%s\t%s°F\t%s\t%s\n\t%s°F\t%s\t%s\n%s\t%s°F\t%s\t%s\n\t%s°F\t%s\t%s\n%s\t%s°F\t%s\t%s\n\t%s°F\t%s\t%s" % (d["name"][1], d["temp"][1], d["icon"][1], d["desc"][1], d["name"][2][:3], d["temp"][2], d["icon"][2], d["shrtdesc"][2], d["temp"][3], d["icon"][3], d["shrtdesc"][3], d["name"][4][:3], d["temp"][4], d["icon"][4], d["shrtdesc"][4], d["temp"][5], d["icon"][5], d["shrtdesc"][5], d["name"][6][:3], d["temp"][6], d["icon"][6], d["shrtdesc"][6], d["temp"][7], d["icon"][7], d["shrtdesc"][7], d["name"][8][:3], d["temp"][8], d["icon"][8], d["shrtdesc"][8], d["temp"][9], d["icon"][9], d["shrtdesc"][9], d["name"][10][:3], d["temp"][10], d["icon"][10], d["shrtdesc"][10], d["temp"][11], d["icon"][11], d["shrtdesc"][11]))
    else:
        message = ("%s - %s°F\t%s\n%s\n\n%s\t%s°F\t%s\t%s\n\t%s°F\t%s\t%s\n%s\t%s°F\t%s\t%s\n\t%s°F\t%s\t%s\n%s\t%s°F\t%s\t%s\n\t%s°F\t%s\t%s\n%s\t%s°F\t%s\t%s\n\t%s°F\t%s\t%s\n%s\t%s°F\t%s\t%s\n\t%s°F\t%s\t%s" % (d["name"][0], d["temp"][0], d["icon"][0], d["desc"][0], d["name"][1][:3], d["temp"][1], d["icon"][1], d["shrtdesc"][1], d["temp"][2], d["icon"][2], d["shrtdesc"][2], d["name"][3][:3], d["temp"][3], d["icon"][3], d["shrtdesc"][3], d["temp"][4], d["icon"][4], d["shrtdesc"][4], d["name"][5][:3], d["temp"][5], d["icon"][5], d["shrtdesc"][5], d["temp"][6], d["icon"][6], d["shrtdesc"][6], d["name"][7][:3], d["temp"][7], d["icon"][7], d["shrtdesc"][7], d["temp"][8], d["icon"][8], d["shrtdesc"][8], d["name"][9][:3], d["temp"][9], d["icon"][9], d["shrtdesc"][9], d["temp"][10], d["icon"][10], d["shrtdesc"][10]))
    return message

def get_weather(config):
    if config['forecast_type'] == "short":
        forecast = (location() + "/hourly")
        forecast = requests.get(forecast)
        forecast = json.loads(forecast.text)

        # set variables
        isDaytime = forecast["properties"]["periods"][0]["isDaytime"]
        icon = get_icon(forecast["properties"]["periods"][0]["icon"], isDaytime)
        temp = forecast["properties"]["periods"][0]["temperature"]
        info = forecast["properties"]["periods"][0]["shortForecast"]
        result = ("%s°F %s %s" % (temp, icon, info))
    elif config['forecast_type'] == "long":
        forecast = (location())
        forecast = requests.get(forecast)
        forecast = json.loads(forecast.text)

        # set variables
        isDaytime = forecast["properties"]["periods"][0]["isDaytime"]
        icon = get_icon(forecast["properties"]["periods"][0]["icon"], isDaytime)
        temp = forecast["properties"]["periods"][0]["temperature"]
        info = forecast["properties"]["periods"][0]["shortForecast"]
        title = forecast["properties"]["periods"][0]["name"]
        windspd = forecast["properties"]["periods"][0]["windSpeed"]
        windicon = wind_direction(forecast["properties"]["periods"][0]["windDirection"])
        winddir = forecast["properties"]["periods"][0]["windDirection"]
        result = ("%s: %s°F %s %s      %s %s" % (title, temp, icon, info, windspd, windicon))
    with open(cache_path, 'w') as cache_file:
        logging.debug("Writing cache.")
        cache_file.write(result)
    return result

def location():
    # Get geo location based on IP
    if config['use_geoloc'] == "0":
        zipcodes = config['zipcode']
        city = zipcode.isequal(zipcodes)
        logging.debug("USING CONFIGURED ZIP CODE: %s" % zipcodes)
        geojson = requests.get("https://api.weather.gov/points/%s,%s" % (city.lat, city.lng))
        geojson = json.loads(geojson.text)
        geolocation = geojson["properties"]["forecast"]
        city = geojson["properties"]["relativeLocation"]["properties"]["city"]
        state = geojson["properties"]["relativeLocation"]["properties"]["state"]

        return geolocation

    else:
        logging.debug("ATTEMPTING TO GEO LOCATE BASED ON IP...")
        geo_loc = requests.get('https://ipinfo.io/json')
        geo_loc = json.loads(geo_loc.text)
        geo_loc = geo_loc["loc"]

        # Get weather.gov Forecast Office URL
        logging.debug("WEATHER.GOV ENTRY URL: https://api.weather.gov/points/%s" % geo_loc)
        geojson = requests.get("https://api.weather.gov/points/%s" % geo_loc)
        geojson = json.loads(geojson.text)
        city = geojson["properties"]["relativeLocation"]["properties"]["city"]
        state = geojson["properties"]["relativeLocation"]["properties"]["state"]
        geolocation = geojson["properties"]["forecast"]
        logging.debug("WEATHER.GOV GRID POINTS URL: %s" % geolocation)

    return geolocation

parser = argparse.ArgumentParser()
parser.add_argument("-t", "--toggle-forecast", help="toggle between 5 day and current", action="store_true")
parser.add_argument("-v", "--verbose", help="enable verbose logging", action="store_true")
parser.add_argument("-n", "--notify-send", help="send", action="store_true")

args = parser.parse_args()

if args.verbose:
    logging.getLogger().setLevel(logging.DEBUG)

home_dir = os.getenv("HOME")
config_path = ("%s/.config/utfweather/utfweather.conf" % home_dir)
cache_path = ("%s/.cache/utfweather/utfweather.cache" % home_dir)


if not os.path.exists(cache_path):
    os.makedirs(os.path.dirname(cache_path))

# load config file
cp = ConfigParser()
cp.read(config_path)

logging.debug("Loaded the following settings:")
logging.debug(dict(cp.items('general')))

config = {
        'use_geoloc': cp.get('general', 'use_geoloc'),
        'zipcode': cp.get('general', 'zipcode'),
        'forecast_type': cp.get('general', 'forecast_type'),
        'cache_ageout': cp.get('general', 'cache_ageout')
        }

if args.notify_send:
    geolocation = location()
    message = get5day(geolocation)
    sendmessage(message)
    exit

if args.toggle_forecast:
    if config['forecast_type'] == "short":
        config['forecast_type'] = "long"
        cp.set('general', 'forecast_type', "long")
    elif config['forecast_type'] == "long":
        config['forecast_type'] = "short"
        cp.set('general', 'forecast_type', "short")

    logging.debug("Writing the following settings:")
    logging.debug(dict(cp.items('general')))

    with open(config_path, 'w') as config_file:
        cp.write(config_file)

    get_weather(config)

else:
    # check if cache exists and is current
    if os.path.exists(cache_path):
        mod_time = int(os.stat(cache_path).st_mtime)
        current_time = int(time.time())
        cache_age = current_time - mod_time

        logging.debug("Mod Time: " + str(mod_time))
        logging.debug("Current Time: " + str(current_time))
        logging.debug("Cache Age: " + str(cache_age))

        if cache_age > int(config["cache_ageout"]):
            logging.debug("Cache old.. Getting current weather..")
            result = get_weather(config)

        else:
            with open(cache_path, 'r') as cache_file:
                logging.debug("Reading cache.")
                result = cache_file.read()
    else:
        result = get_weather(config)

    print(result)
