import requests

def get_city_temp(city):
    r = requests.get('http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=d3822a0f2749b910d5703088314faf7B'.format(city))
    info = r.json()
    raw_temp = info['main']
    temp = raw_temp['temp']
    return float(temp)


def convert_float(dic):
    temp = {}
    for k,v in dic.items():
        temp.update({float(k):v})
    return temp
