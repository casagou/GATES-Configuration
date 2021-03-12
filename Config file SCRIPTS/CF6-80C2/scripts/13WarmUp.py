import sys
import os
import time
from math import *
from nxtps import *

# Global variable definition

#*  13WarmUp.py
#******************************************************************************
#*  AUTHOR: J.Si
#*
#*  DESCRIPTION:
#*  CF6-50 ENGINE MANUAL GEK50481 - Rev 87,07/15/2017
#*  EM 72-00-00 ENGINE TESTING
#*  TESTING 003 PG 1303
#*
#*
#*  MODIFICATIONS:
#*    DATE       NO     WHO  NCR    DESCRIPTION
#*    1.0   01/04/09      JSi   ---    Initial write
#*
#*****************************************************************************
channel("N185,GIFlag,N1_OBS")


instruction("Stabilize at Ground Idle for 5 mins")

wait("GIFlag=1",30,0.1,WAIT_PARAM3_DFT,WAIT_PARAM4_DFT,WAIT_PARAM5_DFT,WAIT_PARAM6_DFT,WAIT_PARAM7_DFT,MSG,"Not at GI in 30s")

result("Engine at GI")

delay(300)


instruction("Slowly accelerate (1 min) to 86 % N1 and hold for 5 minutes")

wait("N1_OBS="+str(round(getCV("N185"),4)) ,90,20,WAIT_PARAM3_DFT,WAIT_PARAM4_DFT,WAIT_PARAM5_DFT,WAIT_PARAM6_DFT,WAIT_PARAM7_DFT,MSG,"Not at MC in 90s")

result("Engine at 85% N1")

delay(300)


instruction("Slowly decelerate (1min) to GI and hold for 5min")

wait("GIFlag=1",90,0.1,WAIT_PARAM3_DFT,WAIT_PARAM4_DFT,WAIT_PARAM5_DFT,WAIT_PARAM6_DFT,WAIT_PARAM7_DFT,MSG,"Not at GI in 90sec")

result("Engine at GI")

delay(300)


