import Adafruit_PCA9685
import time

class drive(object):

	forwardLeft = 14
	backwardLeft = 15
	forwardRight = 12
	backwardRight = 13
	rinv = 1
	linv = 1
	def __init__(self,pwmFreq=1000): #init sets pwmFreq to 1000ms by default 
		self.freq = pwmFreq
		print("PCA init to pwmFreq of: " + str(self.freq))
		self.pwm = Adafruit_PCA9685.PCA9685()
		self.pwm.set_pwm_freq(pwmFreq)
	def setMotors(self,dutyR,dutyL): #duty cycle of each motor -100-100
		if(dutyR < -100 or dutyR > 100): #validation
			return -1
		if(dutyL < -100 or dutyL > 100): #validation
			return -1

		self.pwm.set_pwm(self.forwardRight,0,0)#erase previous
		self.pwm.set_pwm(self.backwardRight,0,0)#settings on
		self.pwm.set_pwm(self.backwardLeft,0,0)#all motors
		self.pwm.set_pwm(self.forwardLeft,0,0)

		dutyR = self.rinv*self.__map(dutyR,-100,100,-4095,4095) #scale duty cycle from -100-100 to min and max values of pwm board
		dutyL = self.linv*self.__map(dutyL,-100,100,-4095,4095)
		print("r/l: " + str(dutyR) + " / " + str(dutyL))
		if (dutyR >= 0): #positive values go forward
			self.pwm.set_pwm(self.forwardRight,0,dutyR)
		else: #negative values go backward
			self.pwm.set_pwm(self.backwardRight,0,-dutyR)
		if(dutyL >= 0):
			self.pwm.set_pwm(self.forwardLeft,0,dutyL)
		else:
			self.pwm.set_pwm(self.backwardLeft,0,-dutyL)
	def __map(self,x, in_min, in_max, out_min, out_max): #proportionaly maps ranges of values
		return (x - in_min) * (out_max - out_min) // (in_max - in_min) + out_min
	def brake(self):
		self.pwm.set_pwm(12,0,4095)
		self.pwm.set_pwm(13,0,4095)
		self.pwm.set_pwm(14,0,4095)
		self.pwm.set_pwm(15,0,4095)		
