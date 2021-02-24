import sys
import os
import time
from math import *
from nxtps import *

# Global variable definition

#* 05AbortStart.tps
#******************************************************************************
#*  AUTHOR: Nicholas Jeffers
#*
#*  DESCRIPTION:
#*  Abort Start
#*
#*  DATE: 12/04/2020 
#*
#*  MODIFICATIONS:
#*    DATE         WHO  NCR    DESCRIPTION
#*
#*
#******************************************************************************

# Channel Registration
channel("EngSelectorNRML,EngSelectorIGN,EngSelectorCRNK,D03115,FCS_AirRdy")


note("NOTE: This TP is to be used only as a part of Start TP")


instruction("Ensure MASTER LEVER is set to OFF")

wait("D03115 = 0", 5, 0.1, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "MASTER LEVER is not OFF")


if skipgv:
    result("Operator skipped Fuel OFF check {} AbortStart ".format(REPORT))
    pass

instruction("Set MODE SELECTOR to NORMAL")

set_channel("EngSelectorNRML", 1)
set_channel("EngSelectorIGN", 0)
set_channel("EngSelectorCRNK", 0)


instruction("Close Facility air supply valve")

wait("FCS_AirRdy = 0", 5, 0.1, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "Facility Air not OFF")


instruction("Manually turn Off fuel pumps")



