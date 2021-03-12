import sys
import os
import time
from math import *
from nxtps import *

# Global variable definition

#* Test Information.tps
#******************************************************************************
#*  AUTHOR:
#*
#*  DESCRIPTION:
#*  Identifier : CF6-80C2 Manual 72-00-00 Testing 000
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
lvESM = None
TEST = None
EEC_PN = None
EEC_SV = None
lvMulti = None
lvB1 = None
lvB2 = None
lvB4 = None
lvB5 = None
lvB6 = None
lvB7 = None
lvB8 = None
lvB6FA = None

# Channel Registration
channel("EngineSN,MultiDevTest,LHV,TSN,CSN,ESM_No,B1F,B2F,B4F,B5F,B6F,B6FA,B7F,B8F")



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

EEC_PN = prompt_str("Enter EEC Part Number", "1820M33P09")

EEC_SV = prompt_str("Enter EEC Software Version", "8.2 M")

TEST = prompt_str("Reason for Test", "Test after repair")


lvMulti = prompt_boo("Will you test multiple ratings?")

if lvMulti:
	set_channel("MultiDevTest", 1)

	lvB1 = prompt_boo("Will you test B1F rating?")

	if lvB1:
		set_channel("B1F", 1)

		pass
	lvB2 = prompt_boo("Will you test B2F rating?")

	if lvB2:
		set_channel("B2F", 1)

		pass
	lvB4 = prompt_boo("Will you test B4F rating?")

	if lvB4:
		set_channel("B4F", 1)

		pass
	lvB5 = prompt_boo("Will you test B5F rating?")

	if lvB5:
		set_channel("B5F", 1)

		pass
	lvB6 = prompt_boo("Will you test B6F rating?")

	if lvB6:
		set_channel("B6F", 1)

		pass
	lvB6FA = prompt_boo("Will you test B6FA rating?")

	if lvB6FA:
		set_channel("B6FA", 1)

		pass
	lvB7 = prompt_boo("Will you test B7F rating?")

	if lvB7:
		set_channel("B7F", 1)

		pass
	lvB8 = prompt_boo("Will you test B8F rating?")

	if lvB8:
		set_channel("B8F", 1)

		pass
else:
	
	lvB1 = prompt_boo("Will you test B1F rating?")

	if lvB1:
		set_channel("B1F", 1)

		quit()

		pass
	lvB2 = prompt_boo("Will you test B2F rating?")

	if lvB2:
		set_channel("B2F", 1)

		quit()

		pass
	lvB4 = prompt_boo("Will you test B4F rating?")

	if lvB4:
		set_channel("B4F", 1)

		quit()

		pass
	lvB5 = prompt_boo("Will you test B5F rating?")

	if lvB5:
		set_channel("B5F", 1)

		quit()

		pass
	lvB6 = prompt_boo("Will you test B6F rating?")

	if lvB6:
		set_channel("B6F", 1)

		quit()

		pass
	lvB6FA = prompt_boo("Will you test B6FA rating?")

	if lvB6FA:
		set_channel("B6FA", 1)

		quit()

		pass
	lvB7 = prompt_boo("Will you test B7F rating?")

	if lvB7:
		set_channel("B7F", 1)

		quit()

		pass
	lvB8 = prompt_boo("Will you test B8F rating?")

	if lvB8:
		set_channel("B8F", 1)

		pass
	pass









