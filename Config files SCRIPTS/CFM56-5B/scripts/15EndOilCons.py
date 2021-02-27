import sys
import os
import time
from math import *
from nxtps import *

# Global variable definition

#* 15EndOilCons.py
#******************************************************************************
#*  AUTHOR: Nicholas Jeffers
#*
#*  DESCRIPTION:REFERANCE: ENGINE MANUAL 72-00-00, TESTING 003
#*  Oil Consumption Check
#*
#*  DATE: 12/09/2020
#*
#*  MODIFICATIONS:
#*    DATE         WHO  NCR    DESCRIPTION
#*
#******************************************************************************

# ***** LOCAL VARIABLE DECLARATIONS *****
Shutdown = None
EndOil = None

channel("OilCSStr,Eng_On,GIFlag,AIFlag,TOil_2DegC,OilConRate,BadOilCons,OilConsum,tOilConsum,TOil_EngOf,TOil_OCStr,TOil_OCStr1,tAtGI,N1RDWN,N2RDWN,NADownL,NBDownL,NARDWN,NBRDWN,TransReset,A27211,NAStop,NBStop,FuelEnable,GndPower")


if getCV("OilCSStr") == 0 or getCV("Eng_On") == 0:
	result("An Oil Consumption check has not been started.")
quit()
pass
    

	


EndOil = prompt_num("End Oil Consumption check?")

if not EndOil:
    result("Oil Consumption check not finished.")
    
    quit()
    
    pass
    
set_channel("OilCSEnd",1)




delay(2)

instruction("Record fullset")

do_fullset(5, "OilConsumption - Final", "OilConsumption2")

delay(5)

result("Oil Consumption = {} L per h. {} OilConsumption ".format(getCV("OilConRate") , REPORT))

result("Max limit is 0.57 L per h {} OilConsumption ".format(REPORT))


if getCV("BadOilCons") == 1:
	
	result("Oil Consumption is above limit. {} OilConsumption ".format(REPORT), "RED")

	
	lvaddtest = prompt_boo("Do you want to run the Additional Oil Consumption Test?")

	
	if lvaddtest:
		set_channel("OilConsSta", 0)

		auto_start("18AdditionalOilCons")

		pass
	pass

result("Oil added in litres = {} litres {} OilConsumption ".format(getCV("OilConsum") , REPORT))

result("Oil Consumption test duration = {} secs {} OilConsumption ".format(getCV("tOilConsum") , REPORT))

