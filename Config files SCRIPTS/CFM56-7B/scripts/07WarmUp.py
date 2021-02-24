import sys
import os
import time
from math import *
from nxtps import *

# Global variable definition

#* 07WarmUp.py
#******************************************************************************
#*  AUTHOR: Nicholas Jeffers
#*
#*  DESCRIPTION:REFERANCE CFM56-7B ENGINE MANUAL 72-00-00 TESTING 003
#*
#*  DATE: 12/16/2020
#*
#*  MODIFICATIONS:
#*    DATE         WHO  NCR    DESCRIPTION
#*    
#*
#******************************************************************************

# Channel Registration
channel("GIFlag,tAtGI,N1PCT")



instruction("Start and Stabilize engine at Idle for 5 minutes")

wait("GIFlag = 1", 30, 0.1, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, " Did not reach GI in 30 s ")

wait("tAtGI > 300", 300, 2, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, " Time at GI has not reached 300 s ")



instruction("Slowly accelerate to 80% N1,and keep engine 5 minutes")

wait("N1PCT = 80", 40, 1, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, " Did not reach 80% N1 in 40s ")

delay(300)



