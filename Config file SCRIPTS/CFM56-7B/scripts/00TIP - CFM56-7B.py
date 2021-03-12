import sys
import os
import time
from math import *
from nxtps import *

# Global variable definition

#* Test Information.py
#******************************************************************************
#*  AUTHOR:
#*
#*  DESCRIPTION:
#*  Identifier : CFM56-7B Manual 72-00-00 Testing 000
#*
#*
#*  DATE: 12/18/2020 10:12:45 AM
#*
#*  MODIFICATIONS:
#*    DATE         WHO  NCR    DESCRIPTION
#*
#*
#******************************************************************************

# ***** LOCAL VARIABLE DECLARATIONS *****
lvSN = None
lvLHV = None
lvTSN = None
lvCSN = None
lvWRK1 = None
lvWRK2 = None
lvWRK3 = None
lvWRK4 = None
TEST = None
lvESM = None
EEC_PN = None
EEC_SV = None
lvMulti = None
lvB27 = None
lvB26B2 = None
lvB26 = None
lvB24B1 = None
lvB24 = None
lvB22B2 = None
lvB22B1 = None
lvB22 = None
lvB20 = None
lvFmodel = None

# Channel Registration
channel("EngineSN,Workscope,MultiDevTest,ESM_No,LHV,TSN,CSN,B27,B26B2,B26,B24B1,B24,B22B2,B22B1,B22,B20")



lvSN = prompt_num("Enter Engine Serial Number", -1, 999999, 0)

set_channel("EngineSN", lvSN)

lvLHV = prompt_num("Enter Latent Heat value", -1, 20000, 0)

set_channel("LHV", lvLHV)

lvTSN = prompt_num("Enter Time since new", -1, 999999, 0)

set_channel("TSN", lvTSN)

lvCSN = prompt_num("Enter Cycle since new", -1, 999999, 0)

set_channel("CSN", lvCSN)

lvESM = prompt_num("Enter ESM revision Number", -1, 1000, 0)

set_channel("ESM_No", lvESM)

EEC_PN = prompt_str("Enter EEC Part Number", "2042M67P04")

EEC_SV = prompt_str("Enter EEC Software Version", "7.B.W2F3")

TEST = prompt_str("Reason for Test", "Test after repair")



instruction("Enter Engine Repair Workscope adder")

lvWRK3 = prompt_boo("Engine with NO flowpath restoration?")

if lvWRK3:
	set_channel("Workscope", 3)

else:
	lvWRK1 = prompt_boo("Engine with FULL OVERHAUL?")

	if lvWRK1:
		set_channel("Workscope", 1)

	else:
		lvWRK2 = prompt_boo("Engine with PARTIAL workscope?")

		if lvWRK2:
			set_channel("Workscope", 2)

			pass
		pass
	pass


lvMulti = prompt_boo("Will you test multiple ratings?")

if lvMulti:
	set_channel("MultiDevTest", 1)

	lvB27 = prompt_boo("Will you test B27 rating?")

	if lvB27:
		set_channel("B27", 1)
        
        lvFmodel = prompt_boo("Is the Engine a /F Rating?")
        
        if lvFmodel:
            set_channel("F_model",1)
            
            else:
                set_channel("F_model",0)
                pass
        
		pass
	lvB26B2 = prompt_boo("Will you test B26B2 rating?")

	if lvB26B2:
		set_channel("B26B2", 1)
        
        lvFmodel = prompt_boo("Is the Engine a /F Rating?")
        
        if lvFmodel:
            set_channel("F_model",1)
            
            else:
                set_channel("F_model",0)
                pass
		pass
	lvB26 = prompt_boo("Will you test B26 rating?")

	if lvB26:
		set_channel("B26", 1)
        
        lvFmodel = prompt_boo("Is the Engine a /F Rating?")
        
        if lvFmodel:
            set_channel("F_model",1)
            
            else:
                set_channel("F_model",0)
                pass
		pass
	lvB24B1 = prompt_boo("Will you test B24B1 rating?")

	if lvB24B1:
		set_channel("B24B1", 1)

		pass
	lvB24 = prompt_boo("Will you test B4 rating?")

	if lvB24:
		set_channel("B24", 1)

		pass
	lvB22B2 = prompt_boo("Will you test B22B2 rating?")

	if lvB22B2:
		set_channel("B22B2", 1)

		pass
	lvB22B1 = prompt_boo("Will you test B22B1 rating?")

	if lvB22B1:
		set_channel("B22B1", 1)

		pass
	lvB22 = prompt_boo("Will you test B22 rating?")

	if lvB22:
		set_channel("B22", 1)

		pass
	lvB20 = prompt_boo("Will you test B20 rating?")

	if lvB20:
		set_channel("B20", 1)

		pass
else:
	
	lvB27 = prompt_boo("Will you test B27 rating?")

	if lvB27:
		set_channel("B27", 1)

		quit()

		pass
	lvB26B2 = prompt_boo("Will you test B26B2 rating?")

	if lvB26B2:
		set_channel("B26B2", 1)

		quit()

		pass
	lvB26 = prompt_boo("Will you test B26 rating?")

	if lvB26:
		set_channel("B26", 1)

		quit()

		pass
	lvB24B1 = prompt_boo("Will you test B24B1 rating?")

	if lvB24B1:
		set_channel("B24B1", 1)

		quit()

		pass
	lvB24 = prompt_boo("Will you test B4 rating?")

	if lvB24:
		set_channel("B24", 1)

		quit()

		pass
	lvB22B2 = prompt_boo("Will you test B22B2 rating?")

	if lvB22B2:
		set_channel("B22B2", 1)

		quit()

		pass
	lvB22B1 = prompt_boo("Will you test B22B1 rating?")

	if lvB22B1:
		set_channel("B22B1", 1)

		quit()

		pass
	lvB22 = prompt_boo("Will you test B22 rating?")

	if lvB22:
		set_channel("B22", 1)

		quit()

		pass
	lvB20 = prompt_boo("Will you test B20 rating?")

	if lvB20:
		set_channel("B20", 1)

		pass
	pass









