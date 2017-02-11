import time
import Adafruit_PCA9685

pwm = Adafruit_PCA9685.PCA9685()

pwm.set_pwm_freq(1000)

while True:
        print("spining with 14/15")
        pwm.set_pwm(14, 0, 4095)
#       pwm.set_pwm(11,4095,4095)
        time.sleep(1)
	pwm.set_pwm(14,0,0)
	time.sleep(1)
	pwm.set_pwm(15,0,4095)
	time.sleep(1)
	pwm.set_pwm(15,0,0)
	time.sleep(1)
