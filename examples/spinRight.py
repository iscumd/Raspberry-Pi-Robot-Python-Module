import time
import Adafruit_PCA9685

pwm = Adafruit_PCA9685.PCA9685()

pwm.set_pwm_freq(1000)

while True:
        print("spining with 12/13")
        pwm.set_pwm(12, 0, 4095)
#       pwm.set_pwm(11,4095,4095)
        time.sleep(1)
	pwm.set_pwm(12,0,0)
	time.sleep(1)
	pwm.set_pwm(13,0,4095)
	time.sleep(1)
	pwm.set_pwm(13,0,0)
	time.sleep(1)
