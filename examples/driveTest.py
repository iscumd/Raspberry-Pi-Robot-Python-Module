#This file needs to be in the same directory as the pibot.py file for it to import properly
from pibot import drive
import time

bot = drive()
bot.rinv = -1
while True:
	bot.setMotors(100,100)
	time.sleep(1)
	bot.setMotors(-100,100)
	time.sleep(2)
	bot.setMotors(100,-100)
	time.sleep(2)
	bot.setMotors(100,100)
	time.sleep(5)
	bot.brake()
	time.sleep(2)
