import sys
import os
import time
from math import *
from nxtps import *

# Global variable definition
#******************************************************************************
#* 05IdleLeakCheck.py
#******************************************************************************
#*  AUTHOR: J.Si
#*
#*  DESCRIPTION:
#*  CF6-80 ENGINE MANUAL GEK92451 - Rev ,Dated: 06/01/2012
#*  EM 72-00-00 ENGINE TESTING
#*  CF6-80 Idle Leak Check
#*  TESTING 003-004 TASK 72-00-00-760-004-C
#*
#*  MODIFICATIONS:
#*    REV    DATE         WHO  NCR    DESCRIPTION
#*
#*
#*    1.0   01/04/20      JSi   ---    Initial write
#*
#******************************************************************************

lvtemp2 = None
lvtemp1 = None
TestYes = None
In_ExhOK = None
OilReTop = None
MCDOK = None

channel("Eng_On,N1_OBS,N2_OBS,N2GIL,N2GIH,TT2,VSVSEL,VBVSEL,T495SELAOB,OILQTY,FANBRGN1,FANBRGN2,FANBRGN1_ALT,FANBRGN2_ALT,VIBCRFN1,VIBCRFN2,POIL,PoilC,POILCLOLO,POILCHIHI,FN,WF")


note("First starts may be done with cowls open")

caution("DO NOT RUN ABOVE MIN IDLE WITH COWLS OPEN")


#show_view("rtd2host","View 0","Idle.v")



if getCV("Eng_On") == 0:

    #call_tps("04AutoStart.py")

    pass

# ***** TESTING 004 PARA 3.C (1) (2) (3) *****


if (getCV("N2_OBS") < getCV("N2GIL")) or (getCV("N2_OBS") > getCV("N2GIH")):
	result("N2 is not within idle limits - adjust",REPORT+"IdleLeakCheck",RED)
	result("N2= {} rpm".format(str(getCV("N2"))),REPORT+"IdleLeakCheck",RED)

else:
	result("N2= {} rpm".format(str(getCV("N2"))),REPORT + "IdleLeakCheck")

	pass

result("T2 = {} DegC".format(str(getFV("TT2"))),REPORT + "IdleLeakCheck")

result("Oil Level = {} Qt".format(str(getFV("OILQTY"))),REPORT + "IdleLeakCheck")

result("N2 = {} rpm".format(str(getFV("N2_OBS"))),REPORT + "IdleLeakCheck")

result("N1 = {} rpm".format(str(getFV("N1_OBS"))),REPORT + "IdleLeakCheck")

result("EGT = {} degC".format(str(getFV("T495SELAOB"))),REPORT + "IdleLeakCheck")

result("Fan Vibs N1 = {} mils".format(str(getFV("FANBRGN1"))),REPORT + "IdleLeakCheck")

result("Fan Vibs N2 = {} mils".format(str(getFV("FANBRGN2"))),REPORT + "IdleLeakCheck")

result("Alt Vibs N1 = {} mils".format(str(getFV("FANBRGN1_ALT"))),REPORT + "IdleLeakCheck")

result("Alt Vibs N2 = {} mils".format(str(getFV("FANBRGN2_ALT"))),REPORT + "IdleLeakCheck")

result("TMF Vibs N1 = {} mils".format(str(getFV("VIBCRFN1"))),REPORT + "IdleLeakCheck")

result("TMF Vibs N2 = {} mils".format(str(getFV("VIBCRFN2"))),REPORT + "IdleLeakCheck")

result("Oil pressure is {} psig.".format(str(getFV("POIL"))),REPORT + "IdleLeakCheck")

if getCV("PoilC") < getCV("POILCLOLO") or getCV("PoilC") > getCV("POILCHIHI"):
	result("Oil pressure is not within idle limits",REPORT + "IdleLeakCheck",RED)

	result("Oil pressure corrected = {} psig".format(str(getCV("PoilC"))),REPORT + "IdleLeakCheck",RED)

else:
	result("Oil pressure corrected = {} psig".format(str(getCV("PoilC"))),REPORT + "IdleLeakCheck")

	pass
result("VSV = {} deg".format(str(getFV("VSVSEL"))),REPORT + "IdleLeakCheck")

result("VBV = {} in".format(str(getFV("VBVSEL"))),REPORT + "IdleLeakCheck")

result("Thrust = {} lbs".format(str(getFV("FN"))),REPORT + "IdleLeakCheck")

result("WF = {} lbs".format(str(getFV("WF"))),REPORT + "IdleLeakCheck")



# ***** TESTING 004 PARA 3.B *****


instruction("Enter test cell,check for leaks and good drainage")

lvtemp2 = prompt_boo("Are there fuel leaks?")

if lvtemp2:
	result("There are fuel leaks",REPORT +"IdleLeakCheck")

	result("Stop engine floor leaks and repeat leak check",REPORT +"IdleLeakCheck")

else:
	result("Fuel leak check OK",REPORT +"IdleLeakCheck")

	pass

lvtemp1 = prompt_boo("Are there oil leaks?")

if lvtemp1:
	result("There are oil leaks",REPORT +"IdleLeakCheck")

	result("Stop engine floor leaks and repeat leak check",REPORT +"IdleLeakCheck")

else:
	result("Oil leak check OK",REPORT +"IdleLeakCheck")

	pass


TestYes = prompt_boo("Is Test Initial leakcheck completed?")

if TestYes:
	result("Test Initial leakcheck completed and authorized.",REPORT + "Test3")

else:
    call_tps("17Shutdown.py")
        
    pass


instruction("Check inlet and exhaust")

In_ExhOK = prompt_boo("Was inlet and exhaust check satisfactory?")

if In_ExhOK:
	result("Inlet and exhaust checked OK.",REPORT + "IdleLeakCheck")

else:
	result("A problem was found in the inlet or exhaust.",REPORT + "IdleLeakCheck")

	pass

OilReTop = prompt_boo("Were oil levels checked and serviced as required?")

if OilReTop:
	result("Oil levels are checked and serviced",REPORT + "IdleLeakCheck")

else:
	result("Oil levels are not checked and serviced",REPORT + "IdleLeakCheck")

	pass

MCDOK = prompt_boo("Were filters and MCDs verified and found satisfactory?")

if MCDOK:
	result("Filters and MCDs verified and found satisfactory",REPORT + "IdleLeakCheck")

else:
	result("Filters and MCDs verified and found not satisfactory",REPORT + "IdleLeakCheck")

	pass
instruction("Close and Secure Cowlings")

