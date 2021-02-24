import sys
import os
import time
from math import *
from nxtps import *

# Global variable definition

#* CorrelationFC.tps
#******************************************************************************
#*  AUTHOR: Jacques Simard
#*
#*  DESCRIPTION:
#*  CF6 GE Corellation Procedure - Functional Checkout
#*
#*  MODIFICATIONS:
#*    REV    DATE         WHO  NCR    DESCRIPTION
#*
#*    1.00   28/07/19      JSi   ---    Initial write
#*
#******************************************************************************

lvwork = None
lvmast = None

Channel "N1K,GIFlag,FNO_lbsTare,FNCal_Tare,FNOBS_raw,FNCAL_raw"

instruction("Record Fullset for pre zero point")

do_fullset(10,"CorrelPreA" , "CorrelPreA")


delay(300)

delay(300)


instruction("Tare Working thrust cell ")

result("Working Cell reads= {} lbs".format(str(round(getFV("FNOBS_raw"), 4)) ), REPORT + "Tare")

lvwork = prompt_num("Enter initial value displayed on working thrust cell.", -100.1, 100.1, 0)

set_channel("FNO_lbsTare", lvwork)


instruction("Tare Master thrust cell ")

result("Master Cell reads= {} lbs".format(str(round(getFV("FNCAL_raw"), 4)) ), REPORT + "Tare")

lvmast = prompt_num("Enter initial value displayed on master thrust cell.", -100.1, 100.1, 0)

set_channel("FNCal_Tare", lvmast)



instruction("Record fullset at zero tare point. ")

do_fullset(10, "PreCorrelTare" , "PreCorrelTare")



instruction("Start engine and run 5 min. at Ground Idle")

call_tps("Start")

instruction("Record fullset")

start_log("CorrelGI","CorrelGI")

do_fullset(20,"CorrelGIA" , "CorrelGIA")

stop_log("CorrelGI")


instruction("Slowly accel to N1K=3583 and stabilize 10 min.")

wait("N1K=3583", 30, 10, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "Engine is not N1K=3583")

instruction("Record fullset")

delay(300)

delay(300)

start_log("Correl3583","Correl3583")

do_fullset(20, "WarmUp3583" , "WarmUp3583")

stop_log("Correl3583")



instruction("Slowly accel to N1K=3872 and stabilize 5 min.", SKIP)

note("Or SKIP if step is not required")

wait("N1K=3872", 30, 10, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "Engine is not N1K=3872")

delay(300)

instruction("Record fullset")

start_log("Correl3872","Correl3872")

do_fullset(20,"Correl3872A" , "Correl3872A")

delay(1)

do_fullset(20, "Correl3872B" , "Correl3872B")

stop_log("Correl3872")



instruction("Slowly decel to N1K=3783 and stabilize 5 min.")

wait("N1K=3783", 30, 10, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "Engine is not N1K=3783")

delay(300)

instruction("Record fullset")

start_log("Correl3783","Correl3783")

do_fullset(20 , "Correl3783A" , "Correl3783A")

delay(1)

do_fullset(20, "Correl3783B" , "Correl3783B")

stop_log("Correl3783")



instruction("Slowly decel to N1K=3583 and stabilize 5 min.")

wait("N1K=3583", 30, 10, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "Engine is not N1K=3583")

delay(300)

instruction("Record fullset")

start_log("Correl3583","Correl3583")

do_fullset(20, "Correl3583A" , "Correl3583A")

delay(1)

do_fullset(20, "Correl3583B" , "Correl3583B")

stop_log("Correl3583")


instruction("Slowly decelerate to Ground Idle  and stabilize 5 min.")

wait("GIFlag=1", 120, 0.1, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "Engine not at GI after 30s")

delay(300)

do_fullset(20, "CorrelGIB" , "CorrelGIB")


instruction(" Shut Down engine ")

call_tps("Shutdown")


delay(300)



instruction("Record Fullset for post zero point after 10 minutes.")

do_fullset(10, "CorrelPostA" , "CorrelPostA")

