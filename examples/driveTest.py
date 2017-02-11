from robot import robot
import time

pibot = robot()
pibot.rinv = -1
while True:
	pibot.setMotors(100,100)
	'''time.sleep(1)
	pibot.setMotors(-100,100)
	time.sleep(2)
	pibot.setMotors(100,-100)
	time.sleep(2)
	pibot.setMotors(100,100)'''
	time.sleep(5)
	pibot.brake()
	time.sleep(2)
