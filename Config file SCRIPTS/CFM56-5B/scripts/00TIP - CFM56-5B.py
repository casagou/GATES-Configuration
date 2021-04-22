import sys
import os
import time
from math import *
from nxtps import *

from nxdas_tps_lib.update_oracle_db import * 
active_test_name = os.popen("/usr/local/bin/nxget /nxdas/configuration/master/active-test-name").read() 

# Global variable definition

#* Test Information.py
#******************************************************************************
#*  AUTHOR:
#*
#*  DESCRIPTION:
#*  Identifier : CFM56-5B Manual 72-00-00 Testing 000
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
lvB3 = None
lvB2 = None
lvB1 = None
lvB4 = None
lvB7 = None
lvB5 = None
lvB6 = None
lvB8 = None
lvB9 = None

#example to write database
#update_customer_specific(active_test_name, "ecu_pn", "abc", "b1", "2", "b2", "m", "b3", "n", "b4", "123", "b5", "abc") 
#update_customer_specific(active_test_name, "WORKSCOPE", getCV("Workscope")) 
#update_customer_specific(active_test_name, "WORKSCOPE", "Life s great")


# Channel Registration
channel("EngineSN,Workscope,LHV,TSN,CSN,ESM_No,MultiDevTest,B3,B2,B1,B4,B7,B5,B6,B8,B9")
#channel("EngineSN,Workscope,LHV,MultiDevTest,B3,B2,B1,B4,B7,B5,B6,B8,B9")



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

EEC_PN = prompt_str("Enter EEC Part Number", "2123M56P03")

EEC_SV = prompt_str("Enter EEC Software Version", "5BS2")

TEST = prompt_str("Reason for Test", "Test after repair")



instruction("Enter Engine Repair Workscope adder")

lvWRK1 = prompt_boo("Engine with NO flowpath restoration?")

if lvWRK1:
	set_channel("Workscope", 1)

else:
	lvWRK2 = prompt_boo("Engine with PARTIAL workscope?")

	if lvWRK2:
		set_channel("Workscope", 2)

	else:
		lvWRK3 = prompt_boo("Engine with PERFORMANCE workscope?")

		if lvWRK3:
			set_channel("Workscope", 3)

		else:
			lvWRK4 = prompt_boo("Engine with FULL OVERHAUL?")

			if lvWRK4:
				set_channel("Workscope", 4)

				pass
			pass
		pass
	pass




lvMulti = prompt_boo("Will you test multiple ratings?")

if lvMulti:
	set_channel("MultiDevTest", 1)

	
	lvB3 = prompt_boo("Will you test B3 rating?")

	if lvB3:
		set_channel("B3", 1)

		pass
	lvB2 = prompt_boo("Will you test B2 rating?")

	if lvB2:
		set_channel("B2", 1)

		pass
	lvB1 = prompt_boo("Will you test B1 rating?")

	if lvB1:
		set_channel("B1", 1)

		pass
	lvB4 = prompt_boo("Will you test B4 rating?")

	if lvB4:
		set_channel("B4", 1)

		pass
	lvB7 = prompt_boo("Will you test B7 rating?")

	if lvB7:
		set_channel("B7", 1)

		pass
	lvB5 = prompt_boo("Will you test B5 rating?")

	if lvB5:
		set_channel("B5", 1)

		pass
	lvB6 = prompt_boo("Will you test B6 rating?")

	if lvB6:
		set_channel("B6", 1)

		pass
	lvB8 = prompt_boo("Will you test B8 rating?")

	if lvB8:
		set_channel("B8", 1)

		pass
	lvB9 = prompt_boo("Will you test B9 rating?")

	if lvB9:
		set_channel("B9", 1)

		pass
else:
	
	lvB3 = prompt_boo("Will you test B3 rating?")

	if lvB3:
		set_channel("B3", 1)

		quit()

		pass
	lvB2 = prompt_boo("Will you test B2 rating?")

	if lvB2:
		set_channel("B2", 1)

		quit()

		pass
	lvB1 = prompt_boo("Will you test B1 rating?")

	if lvB1:
		set_channel("B1", 1)

		quit()

		pass
	lvB4 = prompt_boo("Will you test B4 rating?")

	if lvB4:
		set_channel("B4", 1)

		quit()

		pass
	lvB7 = prompt_boo("Will you test B7 rating?")

	if lvB7:
		set_channel("B7", 1)

		quit()

		pass
	lvB5 = prompt_boo("Will you test B5 rating?")

	if lvB5:
		set_channel("B5", 1)

		quit()

		pass
	lvB6 = prompt_boo("Will you test B6 rating?")

	if lvB6:
		set_channel("B6", 1)

		quit()

		pass
	lvB8 = prompt_boo("Will you test B8 rating?")

	if lvB8:
		set_channel("B8", 1)

		quit()

		pass
	lvB9 = prompt_boo("Will you test B9 rating?")

	if lvB9:
		set_channel("B9", 1)

		pass
	pass









