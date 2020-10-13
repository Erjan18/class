import requests
import pprint

class RapidWeatherForecast:

    def get(self, city):
        url = "https://community-open-weather-map.p.rapidapi.com/weather"
        query_param = {"units": "%22metric%22 or %22imperial%22", "mode": "xml%2C html", "q": city}
        headers = {
            'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com",
            'x-rapidapi-key': "106752d063msh4307e8d1df6a4c2p11db14jsn31f7916d6a54"
        }
        print("SENDING HTTP REQUEST")
        data = requests.request('GET',url,headers=headers,params=query_param)
        data = data.json()
        # main,wind,clouds
        data_main,data_wind,data_clouds = data['main'],data['wind'],data['clouds']
        data_main['temp']=data_main['temp']-273
        data_main['feels_like']=data_main['feels_like']-273
        data_main['temp'] = round(data_main['temp'])
        data_main['feels_like'] = round(data_main['feels_like'])
        data_final_main = {}
        data_final_main['Температура']= data_main['temp']

        return {'data':f'В городе:{city} {data_final_main}градусов'}




class CityInfo:

    def __init__(self,city,weather_forecast=None):
        self.city = city
        self._weather_forecast = weather_forecast or RapidWeatherForecast()

    def weather_forecast(self):
        return self._weather_forecast.get(self.city)

    def __str__(self):
        return self.city

city = CityInfo('Бишкек')
city_info = city.weather_forecast()
pprint.pprint(city_info)