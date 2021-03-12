import sys
import os
import time
from math import *
from nxtps import *

# Global variable definition

#* 18AdditionalOilCons.py
#******************************************************************************
#*  AUTHOR: Nicholas Jeffers
#*
#*  DESCRIPTION:CFM56-7B ESM 72-00-00 TESTING 003
#*  Oil Consumption Penalty Run Test Procedure
#*
#*  DATE: 12/09/2020
#*
#*  MODIFICATIONS:
#*   REV      DATE         WHO  NCR    DESCRIPTION
#*
#*
#******************************************************************************

channel("Eng_On,AIFlag,GIFlag,N1K,OilCSEnd,OilCSStr,N1MC,N1TO,FI")


if getCV("OilCSStr") == 1: ##or getCV("OilConsSta") == 1:
	result("Oil Consumption Check already running. Test Procedure aborted. {} ShutdownOilCons ".format(REPORT))

	quit()

	pass
if getCV("Eng_On") == 1:


    call_tps("04ManualStart")


    instruction("Ensure engine is at MIN IDLE.")

    note("Stabilize the engine for 5 min.")

    wait("GIFlag = 1", 30, 0.1, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "Did not reach MIN IDLE in 30 seconds.")

    delay(300)


    instruction("Perform 2 minute acceleration to MC.")

    note("Stabilize the engine for 5 min.")

    #TLA movement
    
#JOA: synthax incorrect
    wait("N1K = str(getCV("N1MC")) ", 120, 10, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "Engine not at MC in 120 seconds.")

    delay(300)


    instruction("Decelerate engine to MIN IDLE.")

    note("Stabilize the engine for 5 min.")

    #TLA movement

    wait("GIFlag = 1", 30, 0.1, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, SKIP, "Failed to reach MIN. IDLE in 30 s.")

    delay(300)

    set_channel("OilCSStr", 0)
    set_channel("OilCSEnd", 0)
    set_channel("OilCSStr", 1)

    delay(3)


    instruction("Accelerate engine to 4000 RPM N1K.")

    note("Stabilize the engine for 35 min.")

    wait("N1K = 4000", 30, 10, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "Engine not at 4000 RPM N1K in 30 seconds.")

    delay(300)

    delay(300)

    delay(300)

    delay(300)

    delay(300)

    delay(300)

    delay(300)


    instruction("Accelerate engine to TAKE OFF N1K.")

    note("Stabilize the engine for 5 min.")

    #TLA movement
#JOA: synthax incorrect
    wait("N1K = str(getCV("N1TO")) ", 30, 10, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "Engine not at TO in 30 seconds.")

    delay(300)


    instruction("Decelerate engine to APPROACH IDLE.")

    note("Stabilize the engine for 5 min.")

    set_channel("FI",0)
    
    wait("AIFlag = 1", 30, 0.1, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, SKIP, "Failed to reach AI in 30 s.")

    delay(300)


    instruction("Select MIN IDLE.")

    note("Stabilize the engine for 5 min at MIN IDLE.")

    set_channel("FI",1)

    wait("GIFlag = 1", 30, 0.1, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, SKIP, "Failed to reach MIN. IDLE in 30 s.")

    delay(300)

    autostart("15EndOilCons.py")
    
else:
    
    instruction("Ensure engine is at MIN IDLE.")

    note("Stabilize the engine for 5 min.")

    wait("GIFlag = 1", 10, 0.1, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "Engine is not at MIN IDLE.")

    delay(300)

    set_channel("OilCSStr", 0)
    set_channel("OilCSEnd", 0)
    set_channel("OilCSStr", 1)

    delay(3)


    instruction("Accelerate engine to 4000 RPM N1K.")

    note("Stabilize the engine for 35 min.")

    wait("N1K = 4000", 30, 10, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "Engine not at 4000 RPM N1K in 30 seconds.")

    delay(300)

    delay(300)

    delay(300)

    delay(300)


    instruction("Accelerate engine to TAKE OFF N1K.")

    note("Stabilize the engine for 5 min.")

    #TLA movement

#JOA: synthax incorrect
    wait("N1K = str(getCV("N1TO")) ", 30, 10, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "Engine not at TO in 30 seconds.")

    delay(300)


    instruction("Decelerate engine to APPROACH IDLE.")

    note("Stabilize the engine for 5 min.")

    set_channel("FI",0)

    wait("AIFlag = 1", 30, 0.1, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, SKIP, "Failed to reach AI in 30 s.")

    delay(300)


    instruction("Select MIN IDLE.")

    note("Stabilize the engine for 5 min at MIN IDLE.")
    
    set_channel("FI",1)

    wait("GIFlag = 1", 30, 0.1, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, SKIP, "Failed to reach MIN. IDLE in 30 s.")

    delay(300)

    autostart("15EndOilCons.py")
    
    pass
pass
