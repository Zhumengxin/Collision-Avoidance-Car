# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import ultrasound as sound
import L298 as wheel 
import thread
import sys,tty,termios
import time
control_flag = 0

def print_info():
	info = "input what you want to see: \n1: Speed\n2:god"
	while True:
		print info
		tty.setraw(sys.stdin.fileno())
		ch = sys.stdin.read(1)
		termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
		if ch == '0':
			control_flag = 0
		elif ch == '1':
			control_flag = 1
		elif ch == '2':
			print "Distance: %0.2f" % sound.distance
		elif ch == 'q':
			break
		else:
			print "error message!"

def control():
	while control_flag !=0:
		a = 1	 

if __name__=="__main__":
	global control_flag
	try:
		print "begin"
	#PIO.cleanup()
		GPIO.setmode(GPIO.BOARD)
	#	wheel.reset()
		sound.init()
		wheel.init()
		wheel.reset()
		# while True:
#		wheel.forward()
		fd = sys.stdin.fileno()
		old_settings = termios.tcgetattr(fd)
		a = raw_input("Which mode do you want to choose:\n1.atuo\n2.manual\n")
		while str(a) == "1":
			sound.checkdist()
			#print "noe"
			print sound.distance
 			if sound.distance < 0.15:
				wheel.back()
			elif sound.distance < 0.3:
				wheel.front_right_turn()
				#wheel.yuandi()
			elif sound.distance >0.3:
				wheel.forward()
			time.sleep(0.5)		
		while str(a) == "2":
#			sound.checkdist()
#			if sound.distance < 0.15:
#				wheel.stop() 
#			elif sound.distance < 0.3:
#				wheel.front_right_turn()
#			sleep(0.5)
			tty.setraw(sys.stdin.fileno())
			ch = sys.stdin.read(1)
			termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
			if ch == 'w':
				if control_flag == 1:
					pass
				else:
					control_flag = 1
					wheel.forward()
					print "forward"
			elif ch == 'a':
				if control_flag == 2:
					pass
				else:
					control_flag = 2
					wheel.front_left_turn()
					print "turn left"
			elif ch == 's':
				if control_flag == 3:
					pass
				else:
					control_flag = 3
					wheel.back()
					print "back"
			elif ch == 'd':
				if control_flag == 4:
					pass
				else:
					control_flag = 4
					wheel.front_right_turn()
					print "turn right"
			elif ch == 'q':
				print "quit"
				GPIO.cleanup()
				break
			elif ch == ' ':
				control_flag = 0
				wheel.stop()
				print "stop"
			else:
				control_flag = 0
				print "error message!"
				wheel.stop()
		# 	if flag == 0 :
		# 		pass
		# 	else if flag == 1 :
		# 		print cur_speed
		# 	else:
		# 		pass
		# 	flag = 0
		# 	if distance < 0.1:
		# 		back()
		# 	else if distance < 0.3 :
		# 		print "turn god"
		# 		turn_zero_three()
				
		# 		print "the speed is "+cur_speed;
		# 	else if distance > 0.3
		# 		forward()

		# 	else if 0.3 * cur_speed > distance:
		# 		front_left_turn()
	except Exception,e:
		print "aaa"
		print e
		GPIO.cleanup()
	except:
		print "final"
		GPIO.cleanup()
