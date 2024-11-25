import RPi.GPIO as GPIO
import time

#--------------TO DO------------------#
# setup pins for Switches
# test switches
# define functions to allow less code
# define traffic algrithm as desired
#-------------------------------------#

LIGHT_ON_TIME = 3

TRAFFIC_1_RED = 2
TRAFFIC_1_YELLOW = 3
TRAFFIC_1_GREEN = 4

TRAFFIC_2_RED = 17
TRAFFIC_2_YELLOW = 27
TRAFFIC_2_GREEN = 22

TRAFFIC_3_RED = 10
TRAFFIC_3_YELLOW = 9
TRAFFIC_3_GREEN = 11

TRAFFIC_4_RED = 0
TRAFFIC_4_YELLOW = 5
TRAFFIC_4_GREEN = 6

TRAFFIC_5_RED = 13
TRAFFIC_5_YELLOW = 19
TRAFFIC_5_GREEN = 26

TRAFFIC_6_RED = 14
TRAFFIC_6_YELLOW = 15
TRAFFIC_6_GREEN = 18

#SWITCH_1 =
#SWITCH_2 =
#SWITCH_3 =
#SWITCH_4 =
#SWITCH_5 =

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(TRAFFIC_1_RED, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(TRAFFIC_1_YELLOW, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(TRAFFIC_1_GREEN, GPIO.OUT, initial=GPIO.LOW)

GPIO.setup(TRAFFIC_2_RED, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(TRAFFIC_2_YELLOW, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(TRAFFIC_2_GREEN, GPIO.OUT, initial=GPIO.LOW)

GPIO.setup(TRAFFIC_3_RED, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(TRAFFIC_3_YELLOW, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(TRAFFIC_3_GREEN, GPIO.OUT, initial=GPIO.LOW)

GPIO.setup(TRAFFIC_4_RED, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(TRAFFIC_4_YELLOW, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(TRAFFIC_4_GREEN, GPIO.OUT, initial=GPIO.LOW)

GPIO.setup(TRAFFIC_5_RED, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(TRAFFIC_5_YELLOW, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(TRAFFIC_5_GREEN, GPIO.OUT, initial=GPIO.LOW)

GPIO.setup(TRAFFIC_6_RED, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(TRAFFIC_6_YELLOW, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(TRAFFIC_6_GREEN, GPIO.OUT, initial=GPIO.LOW)

while True:
    GPIO.output(TRAFFIC_1_GREEN, GPIO.HIGH)
    GPIO.output(TRAFFIC_1_RED, GPIO.LOW)
    time.sleep(LIGHT_ON_TIME)
    GPIO.output(TRAFFIC_1_YELLOW, GPIO.HIGH)
    GPIO.output(TRAFFIC_1_GREEN, GPIO.LOW)
    time.sleep(LIGHT_ON_TIME)
    GPIO.output(TRAFFIC_1_YELLOW, GPIO.LOW)
    GPIO.output(TRAFFIC_1_RED, GPIO.HIGH)
    time.sleep(LIGHT_ON_TIME)
    GPIO.output(TRAFFIC_1_RED, GPIO.LOW)

    GPIO.output(TRAFFIC_2_GREEN, GPIO.HIGH)
    GPIO.output(TRAFFIC_2_RED, GPIO.LOW)
    time.sleep(LIGHT_ON_TIME)
    GPIO.output(TRAFFIC_2_YELLOW, GPIO.HIGH)
    GPIO.output(TRAFFIC_2_GREEN, GPIO.LOW)
    time.sleep(LIGHT_ON_TIME)
    GPIO.output(TRAFFIC_2_YELLOW, GPIO.LOW)
    GPIO.output(TRAFFIC_2_RED, GPIO.HIGH)
    time.sleep(LIGHT_ON_TIME)
    GPIO.output(TRAFFIC_2_RED, GPIO.LOW)

    GPIO.output(TRAFFIC_3_GREEN, GPIO.HIGH)
    GPIO.output(TRAFFIC_3_RED, GPIO.LOW)
    time.sleep(LIGHT_ON_TIME)
    GPIO.output(TRAFFIC_3_YELLOW, GPIO.HIGH)
    GPIO.output(TRAFFIC_3_GREEN, GPIO.LOW)
    time.sleep(LIGHT_ON_TIME)
    GPIO.output(TRAFFIC_3_YELLOW, GPIO.LOW)
    GPIO.output(TRAFFIC_3_RED, GPIO.HIGH)
    time.sleep(LIGHT_ON_TIME)
    GPIO.output(TRAFFIC_3_RED, GPIO.LOW)

    GPIO.output(TRAFFIC_4_GREEN, GPIO.HIGH)
    GPIO.output(TRAFFIC_4_RED, GPIO.LOW)
    time.sleep(LIGHT_ON_TIME)
    GPIO.output(TRAFFIC_4_YELLOW, GPIO.HIGH)
    GPIO.output(TRAFFIC_4_GREEN, GPIO.LOW)
    time.sleep(LIGHT_ON_TIME)
    GPIO.output(TRAFFIC_4_YELLOW, GPIO.LOW)
    GPIO.output(TRAFFIC_4_RED, GPIO.HIGH)
    time.sleep(LIGHT_ON_TIME)
    GPIO.output(TRAFFIC_4_RED, GPIO.LOW)

    GPIO.output(TRAFFIC_5_GREEN, GPIO.HIGH)
    GPIO.output(TRAFFIC_5_RED, GPIO.LOW)
    time.sleep(LIGHT_ON_TIME)
    GPIO.output(TRAFFIC_5_YELLOW, GPIO.HIGH)
    GPIO.output(TRAFFIC_5_GREEN, GPIO.LOW)
    time.sleep(LIGHT_ON_TIME)
    GPIO.output(TRAFFIC_5_YELLOW, GPIO.LOW)
    GPIO.output(TRAFFIC_5_RED, GPIO.HIGH)
    time.sleep(LIGHT_ON_TIME)
    GPIO.output(TRAFFIC_5_RED, GPIO.LOW)

    GPIO.output(TRAFFIC_6_GREEN, GPIO.HIGH)
    GPIO.output(TRAFFIC_6_RED, GPIO.LOW)
    time.sleep(LIGHT_ON_TIME)
    GPIO.output(TRAFFIC_6_YELLOW, GPIO.HIGH)
    GPIO.output(TRAFFIC_6_GREEN, GPIO.LOW)
    time.sleep(LIGHT_ON_TIME)
    GPIO.output(TRAFFIC_6_YELLOW, GPIO.LOW)
    GPIO.output(TRAFFIC_6_RED, GPIO.HIGH)
    time.sleep(LIGHT_ON_TIME)
    GPIO.output(TRAFFIC_6_RED, GPIO.LOW)