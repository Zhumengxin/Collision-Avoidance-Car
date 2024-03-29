# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import time 
# '''
# 使用2块L298N驱动控制4个直流电机
# 前轮驱动：18-ENDA, 22-ENDB, 11-左前前, 12-左前后, 16-右前前, 29-右前后
# 后轮驱动：38-ENDA, 40-ENDB, 31-左后前, 33-左后后, 35-右后前, 37-右后后
# '''
# 初始化设置引脚输出
def init():
#        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(18, GPIO.OUT)
        GPIO.setup(11, GPIO.OUT)
        GPIO.setup(12, GPIO.OUT)
        GPIO.setup(22, GPIO.OUT)
        GPIO.setup(16, GPIO.OUT)
        GPIO.setup(29, GPIO.OUT) 
        GPIO.setup(38, GPIO.OUT)
        GPIO.setup(31, GPIO.OUT)
        GPIO.setup(33, GPIO.OUT)
        GPIO.setup(40, GPIO.OUT)
        GPIO.setup(35, GPIO.OUT)
        GPIO.setup(37, GPIO.OUT)
# 所有引脚置低电平，用于复位、停止运行的功能
def reset():
        GPIO.output(18, GPIO.LOW)
        GPIO.output(11, GPIO.LOW)
        GPIO.output(12, GPIO.LOW)
        GPIO.output(22, GPIO.LOW)
        GPIO.output(16, GPIO.LOW)
        GPIO.output(29, GPIO.LOW)
        GPIO.output(38, GPIO.LOW)
        GPIO.output(31, GPIO.LOW)
        GPIO.output(33, GPIO.LOW)
        GPIO.output(40, GPIO.LOW)
        GPIO.output(35, GPIO.LOW)
        GPIO.output(37, GPIO.LOW)
# 左前轮向前转
def front_left_back():
        GPIO.output(18, GPIO.HIGH)
        GPIO.output(11, GPIO.HIGH)
        GPIO.output(12, GPIO.LOW)

def front_right_forward():
        GPIO.output(22, GPIO.HIGH)
        GPIO.output(16, GPIO.HIGH)
        GPIO.output(29, GPIO.LOW)

def rear_left_forward():
        GPIO.output(38, GPIO.HIGH)
        GPIO.output(31, GPIO.HIGH)
        GPIO.output(33, GPIO.LOW)

def rear_right_forward():
        GPIO.output(40, GPIO.HIGH)
        GPIO.output(35, GPIO.HIGH)
        GPIO.output(37, GPIO.LOW) 
def front_left_forward():
        GPIO.output(18, GPIO.HIGH)
        GPIO.output(11, GPIO.LOW)
        GPIO.output(12, GPIO.HIGH)
def front_right_back():
        GPIO.output(22, GPIO.HIGH)
        GPIO.output(16, GPIO.LOW)
        GPIO.output(29, GPIO.HIGH)
def rear_left_back():
        GPIO.output(38, GPIO.HIGH)
        GPIO.output(31, GPIO.LOW)
        GPIO.output(33, GPIO.HIGH)
def rear_right_back():
        GPIO.output(40, GPIO.HIGH)
        GPIO.output(35, GPIO.LOW)
        GPIO.output(37, GPIO.HIGH)
def forward():
        reset()
        front_left_forward()
        front_right_forward()
        rear_left_forward()
        rear_right_forward()
def yuandi():
		reset()
		rear_right_back()
		rear_left_forward()
		front_right_back()
		front_left_forward()

def back():
        reset()
        front_left_back()
        front_right_back()
        rear_left_back()
        rear_right_back()

def front_left_turn():
        reset()
        front_right_forward()
        rear_right_forward()

def front_right_turn():
        reset()
        front_left_forward()
        rear_left_forward()

def rear_left_turn():
        reset()
        rear_left_back()
        front_left_back()

def rear_right_turn():
        reset()
        rear_right_back()
        front_right_back()

def stop():
        reset()

if __name__ == "__main__":
        init()
        try:
            while True:
				reset()
				forward()
			#	reset()
			#	front_left_forward()
				time.sleep(5)
        except:
            GPIO.cleanup()
        # while(1):
        #         reset()
        #         #front_left_forward()
        #         #front_right_forward()
        #         #rear_left_forward()
        #         #rear_right_forward()
        #         forward()
        #         time.sleep(30)
        #         back()
        #         time.sleep(30)
        #         # front_left_turn()
        #         # time.sleep(1)
        #         # front_right_turn()
        #         # time.sleep(1)
        #         # rear_left_turn()
        #         # time.sleep(1)
        #         # rear_right_turn()
        #         stop()
        #         GPIO.cleanup() 
