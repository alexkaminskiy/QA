import requests

request = requests.get('https://api.darksky.net/forecast/355089cedeeff2988b9f812707ca2a29/46.47747,30.73262')
weather_temperature = request.json()['currently']['temperature']
weather_windSpeed = request.json()['currently']['windSpeed']
weather_humidity = request.json()['currently']['humidity']

a='The temperature in Odessa today is: {} F\n' \
  'Wind:{} m/s\n' \
  'Humidity:{}'.format(weather_temperature,weather_windSpeed,weather_humidity)

f = open('weather.txt','w')
f.write(a)
f.close()
