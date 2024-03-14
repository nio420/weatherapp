import requests

api_key ='c74ba3502389b45512c3da13168ca086'

user_input = input("Enter city: ")


weather_data = requests.get( f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}")

   
if weather_data.json()['cod'] =='404':
   print("No city Found")
else:
  weather = weather_data.json()['weather'][0]['main']
  temp = round(weather_data.json()['main']['temp'])

  print(f"the weather in {user_input} is: {weather}")
  print(f"the tempareture in {user_input} is: {temp}ºF")



