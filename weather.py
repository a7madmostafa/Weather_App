import requests

def get_weather(city_name):
    API_key = '84bece80722d0f3248e42cf34198d2e5'
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}&units=metric'
    res = requests.get(url)
    data = res.json()
    temp = data['main']['temp']
    humidity = data['main']['humidity']
    country = data['sys']['country']
    print(f'In {city_name}, {country}, the temperature is {temp} degree Celsius and humidity is {humidity}%')

if __name__ == '__main__':
    city = input('Enter city name: ')
    get_weather(city)