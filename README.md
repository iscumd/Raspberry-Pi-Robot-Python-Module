# Raspberry-Pi-Robot-Python-Module
  Module containing class to drive motors as skid steer/differential drive

  This module interfaces with the PCA9685 i2c pwm driver with 16 controllable channels. 
  Connected to channel 12,13,14, and 15 of the pwm driver is the TI DRV 8871 motor driver chip capable of controlling two motors

  Motor 1 is connected to channels 12 and 13 on the pwm driver
  Motor 2 is connected to channels 14 and 15 on the pwm driver

# Before use make sure to Install:
  Adafruit PCA9685 python module 
  https://github.com/adafruit/Adafruit_Python_PCA9685
    sudo pip install adafruit-pca9685
  or
    sudo apt-get install git build-essential python-dev
    cd ~
    git clone https://github.com/adafruit/Adafruit_Python_PCA9685.git
    cd Adafruit_Python_PCA9685
    sudo python setup.py install
# Use example:
    import pibot
    import time
  
    bot = pibot.drive() #defaults to 1000ms pwm frequency 
    #bot = pibot.drive(500) #would set pwmfrequency to 500ms
  
    bot.rinv = -1 #inverts the right side motor
    #bot.linv = -1 #would invert the left side
  
    bot.setMotors(100,100) #full speed forward!
    time.sleep(1)
    bot.brake() #brakes the motors, does NOT coast
    time.sleep(1)
    bot.setMotors(-100,-100) #full speed backward!
    time.sleep(1)
    bot.setMotors(50,-50) #spins clockwise at half speed
    time.sleep(1)
    bot.setMotors(0,0) #coasts to a stop...
  
