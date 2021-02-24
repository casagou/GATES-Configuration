import sys
import os
import time
from math import *
from nxtps import *

# Global variable definition

#* CORRELATION TEST.tps
#******************************************************************************
#*  AUTHOR: <your name goes here>
#*
#*  DESCRIPTION:
#*  <describe the script here>
#*
#*  DATE: 6/19/2006 4:14:50 PM
#*
#*  MODIFICATIONS:
#*    DATE         WHO  NCR    DESCRIPTION
#*    ----------   ---  -----  --------------------------------------------------
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

do_fullset(20,"CorrelGIA" , "CorrelGIA")


instruction("Slowly accel to N1K=3583 and stabilize 10 min.")

wait("N1K=3583", 30, 10, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "Engine is not N1K=3583")

delay(300)

delay(300)

do_fullset(20, "WarmUp3583" , "WarmUp3583")


instruction("Slowly accel to N1K=3872 and stabilize 5 min.")

wait("N1K=3872", 30, 10, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "Engine is not N1K=3872")

delay(300)

instruction("Record fullset")

do_fullset(20, "Correl3872A" , "Correl3872A")

delay(1)

do_fullset(20, "Correl3872B" , "Correl3872B")



instruction("Slowly decel to N1K=3841 and stabilize 5 min.")

wait("N1K=3841", 30, 10, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "Engine is not N1K=3841")

delay(300)

instruction("Record fullset")

do_fullset(20, "Correl3841A" , "Correl3841A")

delay(1)

do_fullset(20, "Correl3841B" , "Correl3841B")


instruction("Slowly decel to N1K=3783 and stabilize 5 min.")

wait("N1K=3783", 30, 10, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "Engine is not N1K=3783")

delay(300)

instruction("Record fullset")

do_fullset(20 , "Correl3783A" , "Correl3783A")

delay(1)

do_fullset(20, "Correl3783B" , "Correl3783B")


instruction("Slowly decel to N1K=3683 and stabilize 5 min.")

wait("N1K=3683", 30, 10, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "Engine is not N1K=3683")

delay(300)

instruction("Record fullset")

do_fullset(20, "Correl3683A" , "Correl3683A")

delay(1)

do_fullset(20, "Correl3683B" , "Correl3683B")


instruction("Slowly decel to N1K=3583 and stabilize 5 min.")

wait("N1K=3583", 30, 10, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "Engine is not N1K=3583")

delay(300)

instruction("Record fullset")

do_fullset(20, "Correl3583A" , "Correl3583A")

delay(1)

do_fullset(20, "Correl3583B" , "Correl3583B")


instruction("Slowly decel to N1K=3496 and stabilize 5 min.")

wait("N1K=3496", 30, 10, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "Engine is not N1K=3496")

delay(300)

instruction("Record fullset")

do_fullset(20, "Correl3496A" , "Correl3496A")

delay(1)

do_fullset(20, "Correl3496B" , "Correl3496B")


instruction("Slowly decel to N1K=3411 and stabilize 5 min.")

wait("N1K=3411", 30, 10, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "Engine is not N1K=3411")

delay(300)

instruction("Record fullset")

do_fullset(20, "Correl3411A" , "Correl3411A")

delay(1)

do_fullset(20, "Correl3411B" , "Correl3411B")


instruction("Slowly decel to N1K=3325 and stabilize 5 min.")

wait("N1K=3325", 30, 10, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "Engine is not N1K=3325")

delay(300)

instruction("Record fullset")

do_fullset(20, "Correl3325A" , "Correl3325A")

delay(1)

do_fullset(20, "Correl3325B" , "Correl3325B")



instruction("Slowly decelerate to Ground Idle  and stabilize 5 min.")

wait("GIFlag=1", 120, 0.1, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "Engine not at GI after 30s")

delay(300)

do_fullset(10,"CorrelGIB" , "CorrelGIB")


instruction(" Shut Down engine ")

call_tps("Shutdown")


delay(300)



instruction("Record Fullset for post zero point after 10 minutes.")

do_fullset(20,"CorrelPostA" , "CorrelPostA")












