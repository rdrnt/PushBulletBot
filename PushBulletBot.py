from pushbullet import Pushbullet
import pywapi
import time
from time import sleep
from datetime import datetime
import praw

#Fill out this info
weatherCode = 'YourWeatherCode'
name = 'YourName'

#Pushbullet API Key
api_key = 'yourApiKeyHere'

def pushGoodMorning():
	#PushBullet API
	pb = Pushbullet(api_key)

	#getting time
	now = datetime.now().time()
	#AM or PM
	mornAfternoon = datetime.now().strftime('%p')

	#Here we push the notifcation(s)
	if now.hour == 6 and now.minute == 30:
		#Getting the weather
		weather_results = pywapi.get_weather_from_weather_com(weatherCode)
		weather_saying = ("The weather is " + weather_results['current_conditions']['text'])
		#pushing
		push = pb.push_note(name + ", it's currently " + str(now.hour-12) + ":" + str(now.minute) + mornAfternoon + ".",  weather_saying)
	else:
		#Put something else here

	if now.hour == 7 and now.minute == 30:
		#getting reddit post title
		user_agent = "Bot that grabs top title in /r/ news"
		r = praw.Reddit(user_agent=user_agent)
		submission = r.get_subreddit('news').get_hot(limit=1)
		for x in submission:
			topTitle = str(x.title)
		#Pushing
		push = pb.push_note("Riley, the latest news is:",  topTitle)
	else:
		#Put something else here

while True:
	sleep(45)
	pushGoodMorning()

