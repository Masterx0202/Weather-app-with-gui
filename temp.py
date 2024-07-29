import requests
import json

def char_list(s):
    char_list = list(s)
    return char_list[:2]

def temp(c):
    #paste api key here
    Api_Key = 'API key!!!'
    city = c
    base_url = "http://api.openweathermap.org/data/2.5/weather?appid="+ Api_Key+ "&q=" + city
    weather_data = requests.get(base_url).json()
    f = weather_data['main']['temp']
    root = f - 273.15
    end = filter(char_list(str(root)))
    return end

def filter(lst):
    concatenated_str = ''.join(map(str, lst))
    concatenated_int = int(concatenated_str)  
    return concatenated_int


