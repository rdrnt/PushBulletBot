from pushbullet import Pushbullet
import pywapi
import time
from time import sleep
from datetime import datetime
import praw

#Fill out this info
weatherCode = 'InsertWeatherCode'
name = 'PutYourNameHere'

#Pushbullet API Key
api_key = 'PutYourAPIKeyHere'

def pushGoodMorning():

	#time info
	now = datetime.now().time()
	print ('The hour is ', now.hour)
	print ('The minute rn is ', now.minute)
	#This line is used for determining AM or PM
	mornAfternoon = datetime.now().strftime('%p')


	#Connected Devices
	#print ("The current devices are", pb.devices)

	#getting reddit info
	user_agent = "Comment Reader 1.0 by /u/x9a"
	r = praw.Reddit(user_agent=user_agent)
	submissions = r.get_subreddit('news').get_hot(limit=1)
	for x in submissions:
		print str(x.title)
		topTitle = str(x.title)

	#weather info
	weather_results = pywapi.get_weather_from_weather_com(weatherCode)
	print ("\n The weather outside is: " + weather_results['current_conditions']['text'] + "& The temp is " + weather_results['current_conditions']['temperature'] + "C" + "\n")
	weather_saying = ("The weather is " + weather_results['current_conditions']['text'])
	#weather_saying = ("The weather is " + weather_results['current_conditions']['text'] + "  & The temperature outside is " + weather_results['current_conditions']['temperature'] + "C.")

	#pushbullet info
	pb = Pushbullet(api_key)

	#If you dont know 24 hour clocks, refer to this = http://www.officeclocks.com/home/Html/Images/st1143.jpg
	#Here we push the stuff at 7:30 AM.
	if now.hour == 19 and now.minute == 30 and mornAfternoon == 'AM':
		push = pb.push_note(name + ", it's currently " + str(now.hour-12) + ":" + str(now.minute) + mornAfternoon + ".",  weather_saying)
		print ("Pushed the notification, have a great day!")
	else:
		print ("The time doesnt match up, so we're gonna try again soon.")

	if now.hour == 22 and now.minute == 24 and mornAfternoon == 'PM':
		push = pb.push_note("Riley, the latest news is:",  topTitle)
		print ("Sent the top title from today, enjoy it!")
	else:
		print ("Reddit: The time doesnt match up, so we're gonna try again.")

while True:
	print("Sleeping...")
	sleep(45)
	pushGoodMorning()

