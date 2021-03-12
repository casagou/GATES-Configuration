import sys
import os
import time
from math import *
from nxtps import *

# Global variable definition

#*  14StartOilCons.py
#******************************************************************************
#*  AUTHOR: JSi
#*
#*  DESCRIPTION:
#*  Start Oil Consumption Check
#*
#*  DATE: 1/27/2016 10:09:21 AM
#*
#*  MODIFICATIONS:
#*    DATE         WHO  NCR    DESCRIPTION
#*
#*
#*
#*
#*
#*
#******************************************************************************

# Channel Registration

channel("Eng_On,OilConsSta,TOil_OCStr,TOil_OCStr1,GIFlag,tAtGI,OilQtySStr")





call_tps("Shutdown")


instruction("Within 15 minutes from shutdown, Mark oil level")

note("Fill the oil tank until the oil starts to flow from overflow port.")


set_channel("OilConsSta", 0)

delay(2)

set_channel("OilConsSta", 1)


do_fullset(5, "Start OC ", "StartOC")

delay(2)

set_channel("TOil_OCStr1", getCV("TOil_OCStr"))

delay(2)

result("Oil temperature was {} DegC.".format(str(round(getFV("TOil_OCStr"), 4)) ), REPORT + "StartOilCons")

result("Oil Quantity was {} ltrs.".format(str(round(getFV("OilQtySStr"), 4)) ), REPORT + "StartOilCons")

result("Oil Consumption Started.", REPORT + "StartOilCons")




