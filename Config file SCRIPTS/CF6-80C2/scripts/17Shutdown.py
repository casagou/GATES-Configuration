import sys
import os
import time
from math import *
from nxtps import *

# Global variable definition

#*  17Shutdown.py
#******************************************************************************
#*  AUTHOR: J.Si
#*
#*  DESCRIPTION:
#*  CF6-50 ENGINE MANUAL GEK50481 - Rev 87, 07/15/2017
#*  EM 72-00-00 ENGINE TESTING
#*  CF6-50 Shutdown procedure
#*  TESTING 002 72-00-00-760-002
#*
#*  MODIFICATIONS:
#*    REV   DATE        WHO  NCR    DESCRIPTION
#*
#*
#*    1.0   04/01/09    JSi   ----   New write
#*
#******************************************************************************


booRotnbr = None
Moto = None
bootemp1 = None
bootemp2 = None

channel("Eng_On,GIFlag,tAtGI,NAStop,NBStop,T495SELAOB,TransReset,FUEL_ON,NARDWN,NBRDWN,N1RDWN,N2RDWN,FCS_AirRdy,SAV_ON,StrtVlvEnST")



instruction("Run the engine 5 minutes at Ground Idle")

wait("GIFlag=1",10,0.1,WAIT_PARAM3_DFT,WAIT_PARAM4_DFT,WAIT_PARAM5_DFT,WAIT_PARAM6_DFT,WAIT_PARAM7_DFT,SKIP,"Engine not at GI")

wait("tAtGI>300",30,1,WAIT_PARAM3_DFT,WAIT_PARAM4_DFT,WAIT_PARAM5_DFT,WAIT_PARAM6_DFT,WAIT_PARAM7_DFT,MSG,"Skip button enable in 30 secs")


set_channel("NAStop",0)

set_channel("NBStop",0)

set_channel("TransReset",1)

delay(2)

set_channel("TransReset",0)


instruction("Set FUEL CONDITION LEVER to CUTOFF position")

caution("MAKE SURE THE EGT CONSTANTLY DECREASES TO PREVENT DAMAGE TO THE ENGINE")

wait("FUEL_ON=0",10,0.1,WAIT_PARAM3_DFT,WAIT_PARAM4_DFT,WAIT_PARAM5_DFT,WAIT_PARAM6_DFT,WAIT_PARAM7_DFT, MSG,"Fuel switch not off")

result("Engine Shut down",REPORT+"Shutdown")


prompt_ok("Press OK button when the first rotor has fully stopped")

set_channel("NAStop",1)

prompt_ok("Press OK button when the second rotor has fully stopped")

set_channel("NBStop",1)


booRotnbr = prompt_boo("Did N2 Rotor stop first?")

if booRotnbr:
	set_channel("N1RDWN",getCV("NBRDWN"))

	set_channel("N2RDWN",getCV("NARDWN"))

else:
	set_channel("N1RDWN",getCV("NARDWN"))

	set_channel("N2RDWN",getCV("NBRDWN"))

	pass


delay(2)

result("Rundown times were: N1= {} secs  N2= {} secs.".format(str(round(getCV("N1RDWN"),4)),str(round(getCV("N2RDWN"),4)) ),REPORT + "Shutdown")


do_fullset(1,"Fullset following Stop","Shutdown")


Moto = prompt_boo("Do you want to do a dry motoring?")

if Moto:
	instruction("After N2 has stopped, dry motor for 2min or until EGT is below 100 C")

	if getCV("FCS_AirRdy") == 0:
		instruction("Set Facility air supply to ON")
		
		wait("FCS_AirRdy = 1",10,0.1,WAIT_PARAM3_DFT,WAIT_PARAM4_DFT,WAIT_PARAM5_DFT,WAIT_PARAM6_DFT,WAIT_PARAM7_DFT, MSG,"Start Air not responding. Use PLC")

		if SkipGV:
			result("Operator skipped Facility Air ON instruction",REPORT + "Shutdown")

		else:
			result("Facility Air turned ON",REPORT + "Shutdown")

			pass
	else:
		result("Facility Air was already ON",REPORT + "Shutdown")

		pass
	
	delay(5)

	instruction("Energize Engine Start valve.")
    
	set_channel("SAV_ON",1)

	wait("StrtVlvEnST=1",3,0.1,WAIT_PARAM3_DFT,WAIT_PARAM4_DFT,WAIT_PARAM5_DFT,WAIT_PARAM6_DFT,WAIT_PARAM7_DFT,MSG,"Start Air Valve did not open in 3s")

	if SkipGV:
		result("Operator skipped Starter ON instruction",REPORT + "Shutdown")

	else:
		result("Start valve is open",REPORT + "Shutdown")

		pass
	
    if delay(120)=true() or getCV("T495SELAOB")<100:

	instruction("Set Engine Start Valve OFF.")

	set_channel("SAV_ON",0)

	wait("StrtVlvEnST = 0",10,0.1,WAIT_PARAM3_DFT,WAIT_PARAM4_DFT,WAIT_PARAM5_DFT,WAIT_PARAM6_DFT,WAIT_PARAM7_DFT,MSG,"Start Air not responding. Use PLC")

    else:
        caution("Engine has not been motored for 2 Minutes or until EGT is below 100 degC")
        
        pass
       
	if SkipGV:
		result("Operator skipped Start Air OFF instruction",REPORT + "Shutdown")

	else:
		result("Start Air turned OFF",REPORT + "Shutdown")

		pass
	delay(20)

	
	instruction("Check for unusual noises during rundown")

	pass
