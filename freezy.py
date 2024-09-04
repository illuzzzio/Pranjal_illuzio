import requests
import json
import win32com.client as wincom
speak = wincom.Dispatch("SAPI.SpVoice")
text = ("welcome to freeze weather reports , plzz enter the name of the city whose temperature you want to know")
speak.speak(text)
city = input("enter the name of the city\n")
url = f"https://api.weatherapi.com/v1/current.json?key=b13989793f184149a91141538230103&q={city}"

r = requests.get(url)
print(r.text)
weatherdic = json.loads(r.text)
w=(weatherdic["current"]["temp_c"])
wind_speed = (weatherdic["current"]
["wind_kph"])
feel_l =(weatherdic["current"]["feelslike_c"])
humidity =(weatherdic["current"]["humidity"])
uv = (weatherdic["current"]["uv"])
speak = wincom.Dispatch("SAPI.SpVoice")
text = (f"'Alright! soThe current temperature in {city} is{w} degrees celcius")
speak.speak(text)
while True:
  speak = wincom.Dispatch("SAPI.SpVoice")
  text = ("do you want to further know the wind speed in kph in the city you entered? press w")
  speak.speak(text)
  win = input('press w : ').lower()
  if win=="w":
   speak = wincom.Dispatch("SAPI.SpVoice")
   text = (f"the wind speed in the {city} is {wind_speed} kilometer per hour")
   speak.speak(text)
   break
  else:
   speak = wincom.Dispatch("SAPI.SpVoice")
   text = ("wrong key has been pressed, please press w only , now i will repeat instructions please listen carefully")
  speak.speak(text)
while True:
 speak = wincom.Dispatch("SAPI.SpVoice")
 text = (f"do you want me to tell how it feels like in the {city}, instead of actual temperatures? just press (f) to get this info")
 speak.speak(text)
 felllike = input("press f : ").lower()
 if felllike=="f":
  speak = wincom.Dispatch("SAPI.SpVoice")
  text = (f"actual temperature in {city} is {w} degree celcius but it feels like {feel_l}")
  break
 else:
  speak = wincom.Dispatch("SAPI.SpVoice")
  text = ("you have pressed wrong key my friend, please press f only , now i will repeat the instructions, listen carefully")
  speak.speak(text)
while True:
 speak = wincom.Dispatch("SAPI.SpVoice")
 text = ("and for the humidity and uv radiations press  H : ")
 speak.speak(text)
 xuv = input("press H :").lower()
 if xuv =="h":
  speak = wincom.Dispatch("SAPI.SpVoice")
  text = (f"the humidity level is {humidity} and uv raditions level is {uv} ")
  speak.speak(text)
  break
 else:
  speak = wincom.Dispatch("SAPI.SpVoice")
  text = ( "wrong key has been pressed , please press h only , now i will repeat the instructions , please listen carefully")
  speak.speak(text)

speak = wincom.Dispatch("SAPI.SpVoice")
text = ("so thats it for todays weather report , feel free to visit freeze weather reports anytime  , quote of the day : a day without laughter is a day wasted(by: Charlie chaplin)  Thank you ")
speak.speak(text)



  


  