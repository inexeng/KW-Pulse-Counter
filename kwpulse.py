#!/usr/bin/env python

import sys, os
import time
from time import sleep   
import pickle
import RPi.GPIO as GPIO  

GPIO.setmode(GPIO.BCM)     # set up BCM GPIO numbering  
GPIO.setup(26, GPIO.IN) # set GPIO4 as input (button)  


GPIO.setwarnings(True)

try:
    while True:
        NUM_CYCLES = 10
        start = time.time()
        for impulse_count in range(NUM_CYCLES):
            GPIO.wait_for_edge(26, GPIO.RISING, bouncetime=250)
            dur = time.time() - start      #seconds to run for loop
            f1 = NUM_CYCLES / dur   #in Hz
        f2 = round(f1, 3)
##        print "frequency = ", f2
        t1 = 1 / f1
        t2 = round(t1, 3)
        print "time = ", t2
        kw1 = 3600 / (t1 * 1000)
        kw2 = round(kw1, 3)
        print "kW = ", kw2
        pickle.dump(kw2, open( "kw.p", "wb" ))
          

finally:                   # this block will run no matter how the try block exits  
    GPIO.cleanup()         # clean up after yourself  
    file.close()
