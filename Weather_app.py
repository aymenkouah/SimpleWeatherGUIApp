#Made by: Kouah Mohammed Aymen
#Computer science student at "National Computer science Engineering School, Algiers (ESI)"
#E-mail: jm_kouah@esi.dz
#Github: https://github.com/aymenkouah

#written in the "Python" programming language
#Requires installaling "tkinter" (TK) and "requests"

#modules and packages
from tkinter import *
import json
import requests
import math

#Main tab/window
root = Tk()
root.title('Weather app')
root.geometry("400x200")

global api_id  '''the api' id'''
api_id = 'bff320cb9189c239ac9a6339dc5ef5b2'


#functions
def weather(zipcode, country):
	global weather_window
	weather_window = Toplevel()
	getweather(zipcode, country)


def getweather(zipcode, country):
	global weather_window, api_id
	try:
		api_request = requests.get("https://api.openweathermap.org/data/2.5/weather?q=%s,%s&appid=%s" %(zipcode, country, api_id))
		api = json.loads(api_request.content)
		if api['cod'] != 200:
			weather_cast_text = "Not Found"
			weather_color = "white"

		else:
			temperature = math.floor(api['main']['temp'] - 273) 
			city = api['name'] + ', ' + api['sys']['country']
			weather_state = api['weather'][0]['main']
			description = api['weather'][0]['description']
			weather_color = weather_color_get(temperature)
			weather_cast_text = "Temperature: %s, Weather: %s, Description: %s " %(str(temperature), weather_state, description )
			weather_window.title('%s' %city)

		Label(weather_window, text=weather_cast_text, font=('Helvetica', 20), bg=weather_color).grid(sticky="we")
	except:
		Label(weather_window, text="Not Found", font=('Helvetica', 20)).grid(sticky="we")
def weather_color_get(temp):
	if temp<5:
		return 'blue'
	elif 4<temp<10:
		return 'cyan'
	elif 9<temp<25:
		return 'green'
	elif 24<temp<35:
		return 'yellow'
	else:
		return 'red'
	pass


#main window contents
country_code_lbl = Label(root, text="country Code")
country_code_entry = Entry(root)
country_code_entry.insert(0, "us")
country_code_lbl.pack()
country_code_entry.pack()




city_name_lbl = Label(root, text="city name")
city_name_entry = Entry(root)
city_name_lbl.pack()
city_name_entry.pack()

search_button = Button(root, text="Search", bg="yellow", command=lambda: weather(city_name_entry.get(), country_code_entry.get() ))
search_button.pack(pady=(10, 0) )


root.mainloop()
