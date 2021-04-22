import sys
import os
import time
from math import *
from nxtps import *

# Global variable definition

#*  16EndOilCons.py
#******************************************************************************
#*  AUTHOR: JSi
#*
#*  DESCRIPTION:REFERENCE: ENGINE MANUAL 72-00-00,TESTING 007
#*  Oil Consumption Check
#*
#*  DATE: 1/27/2016 10:01:10 AM
#*
#*  MODIFICATIONS:
#*    DATE         WHO  NCR    DESCRIPTION
#*
#*
#*
#*
#*
#*
#*
#******************************************************************************

# ***** LOCAL VARIABLE DECLARATIONS *****
OilLtr = None

# Channel Registration

channel("TOil_OCStr1,OilQtySStr,OilConsum,OilConRate,TOil_EngOf,TOIL,OilConsSta")


#* SEQUENCE # 1
if getCV("Eng_On") == 1:
    call_tps("18Shutdown.py")
    
    pass

#set_channel("TOil_EngOf",getCV("TOIL"))

result("Oil Temperature at Oil Consumption start is = {} DegC".format(str(round(getFV("TOil_OCStr1"),4)) ),REPORT + "OilCons")

result("Oil Quantity at Oil Consumption start was {} ltrs.".format(str(round(getFV("OilQtySStr"),4)) ),REPORT + "OilCons")



instruction("Within 15 minutes after shutdown check oil level")

note("NOTE: Add oil into oil tank, if required, to bring the oil level to the intitial marked level at the start of the oil consumption run.")

note("      The quantity of oil required to return oil to")

note("      marked level at start of oil consumption represents the total consumption.")


OilLtr = prompt_num("Enter the amount of added oil in litres",-0.1,10.1,0)

set_channel("OilConsum",OilLtr)

delay(5)

do_fullset(0,"Oil Consumption End","OilConsumption")

delay(2)

result("Oil Consumption = {} liters per hour.".format(str(round(getFV("OilConRate"),4)) ),REPORT + "OilConsumption")

if getFV("OilConRate") >0.4:
	result("Oil Consumption is above limit.",REPORT + "OilConsumption",RED)

	pass

#* SEQUENCE # 2

note("NOTE: If there is more oil in the oil tank than before (such")

note("      as oil that comes out the scupper drain),the oil must")

note("      be checked for fuel by a laboratory")


set_channel("OilConsSta",0)


