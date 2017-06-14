#!/usr/bin/python
from time import gmtime, strftime 
import spidev
import time
import os
import numpy as np

#Define Variables
delay = 0.5
ldr_channel = 0

#Create SPI
spi = spidev.SpiDev()
spi.open(0, 0)
 
def readadc(adcnum):
    # read SPI data from the MCP3008, 8 channels in total
    if adcnum > 7 or adcnum < 0:
        return -1
    r = spi.xfer2([1, 8 + adcnum << 4, 0])
    data = ((r[1] & 3) << 8) + r[2]
    return data


def moving_average(a, n=3) :
    ret = np.cumsum(a, dtype=float)
    ret[n:] = ret[n:] - ret[:-n]
    return ret[n - 1:] / n    

i=0
averageList=[]

while True:
    ldr_value = readadc(ldr_channel)
    averageList.append(ldr_value)
    
    print "%d %d" %(i,ldr_value) 
    time.sleep(delay)
    i=i+1	
    
