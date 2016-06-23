import RPi.GPIO as GPIO
import time

distance = 0
ultrasound_trig = 7
ultrasound_echo = 13

def init():
#	global distance
	global ultrasound_trig
	ultrasound_trig = 7
	global ultrasound_echo
	ultrasound_echo = 13
#	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(ultrasound_trig,GPIO.OUT,initial = GPIO.LOW)
	GPIO.setup(ultrasound_echo,GPIO.IN)

def checkdist():
	global distance
	global ultrasound_trig
	global ultrasound_echo
	GPIO.output(ultrasound_trig,GPIO.HIGH)
	time.sleep(0.000015)
	GPIO.output(ultrasound_trig,GPIO.LOW)
	while not GPIO.input(ultrasound_echo):
		pass 
	t1 = time.time()
	#print "t1: %0.2f" % t1
	while GPIO.input(ultrasound_echo):
		pass
	t2 = time.time()
	#print "t2: %0.2f" % t2
	distance =  (t2-t1) * 340 / 2
	time.sleep(0.000015)
	#print "Distance: %0.2f m" % distance
	#time.sleep(1)
#	return (t2-t1) * 340 / 2


if __name__=="__main__":
    try:
		init()
	#	global distance
		while True:
			print "Distance: %0.2f m" % distance
			print "Distance22: %0.2f m" % checkdist()
			time.sleep(3)
    except KeyboardInterrupt:
        GPIO.cleanup()
