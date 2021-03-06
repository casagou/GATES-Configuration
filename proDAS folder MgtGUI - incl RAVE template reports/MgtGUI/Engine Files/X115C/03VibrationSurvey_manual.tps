Option Explicit

'* <script.tps>
'******************************************************************************
'*  AUTHOR: <your name goes here>
'*
'*  DESCRIPTION:
'*  Vibration Survey
'*
'*  DATE: 9/15/2005 8:34:00 AM
'*
'*  MODIFICATIONS:
'*    DATE         WHO  NCR    DESCRIPTION
'*    ----------   ---  -----  --------------------------------------------------
'*  V1.01 06/02/2001 RH  Initial
'*  V1.02 10/07/2004 DP  Added set_channel for ENABLE_ALARMS
'*  V1.03 11/09/2004 DP  Changed Log name to Vibration
'*  V1.04 15/09/2005 JC  Converted to phase 3 format
'*
'******************************************************************************

' Channel Registration
channel "N1, N2, PLA, EGT, N1R, N1R_TO, GIFlag, tAtGI, VibReset, Accel, Vib1N1Pk, N1atV1MxA, Vib2N1Pk, N1atV2MxA, Vib1N2Pk, N2atV1MxA, Vib2N2Pk, N2atV2MxA, Vib1N1PkD, N1atV1MxD, Vib2N1PkD, N1atV2MxD, Vib1N2PkD, N2atV1MxD, Vib2N2PkD, N2atV2MxD, GetAccTrg, TLA, Theta, XN1, KCondN1, KHN1, GI, START, N1TOTrgt, FuelEnable, ENABLE_ALARMS,C4,ENGMOD"

set_channel ENABLE_ALARMS, 1
set_channel C4, 1
set_channel ENGMOD, 1
set_channel START, 1
'*  Vtemp start_autothrottle

caution "THE FAN MUST BE BALANCED FOR THIS TEST"

note "NOTE: Prior to performing Vibration Survey, warm up the"
note "engine at MC for 5 min or 80% N1 for 7 min"

instruction "Stabilize at Idle for 5 minutes"

'*  V1.02 set_channel GI = 1
'*  Vtemp if cv_TLA > 5
'*  Vtemp movest N1, 960, 10, 45, 10, 0
'*  Vtemp relax
'*  Vtemp endif


set_channel FuelEnable, 1
wait "GIFlag = 1", 40, 0.1, , , , , , MSG, " Did not reach GI in 30 s "
delay 300
result "Engine at GI"
result "N1 speed at GI is "& cv_N1 &"", REPORT & "Vib_Aecel"
result "N2 speed at GI is "& cv_N2 &"", REPORT & "Vib_Aecel"
result "EGT at GI is "& cv_EGT &"", REPORT & "Vib_Aecel"
result "PLA at GI is "& cv_PLA &"", REPORT & "Vib_Aecel"

'delay 15

'*  reset Vibration Parameters at Acceleration
set_channel VibReset, 1
delay 2
set_channel VibReset, 0
set_channel Accel, 1

'*  V1.03 start_log VibAccel
start_log "Vibration", "Vibration_Accel"
'*  start_log Vibration, VibAccel, "Vibration Acceleration"
'*  start_log Vibration, Vibration, "Vibration Acceleration"
result "Vibration Acceleration Log started", REPORT & "Vibration"

'*  Vtemp resume

instruction "Slowly and constantly accelerate to Take Off in 2 min by select the PLA UP button from the control page, "
note "hold it there for 30 s and set the throttle stop."

'*  Vtemp movest N1, cv_N1TOTrgt, 10, 45, 10, 0
'*  Vtemp relax

wait "N1R = " & cv_N1R_TO, 160, 10, , , , , , MSG, "Engine not at TO in 120 s"
If skipgv = 1 Then
result "Operator skipped Take Off check", REPORT & "Vib_Accel"
End If
delay 30

result "Engine at TO"
result "N1 speed at TO is "& cv_N1 &"", REPORT & "Vib_Aecel"
result "N2 speed at TO is "& cv_N2 &"", REPORT & "Vib_Aecel"
result "EGT at TO is "& cv_EGT &"", REPORT & "Vib_Aecel"
result "PLA at TO is "& cv_PLA &"", REPORT & "Vib_Aecel"

'*  V1.03 stop_log VibAccel
stop_log "Vibration"
'do_fullset 30, "Vib Survey Accel", "Vib_Survey_Acc"
do_fullset 30, "Fullset_Vib_Survey_Acc", "Vib_Survey_Acc"
delay 5
set_channel GetAccTrg, 1
set_channel Accel, 0
'*  start_log Vibration, Vibration, "Vibration Acceleration"
'*  V1.03 start_log VibAccel
start_log "Vibration", "Vibration_Decel"

result "Vibration Deceleration Log started", REPORT & "Vibration"

'*  Vtemp resume

instruction "Slowly and constantly decelerate to Ground Idle by select the PLA DOWN button from the control page"
note "in 2 minutes and stabilize for 5 minutes."

'*  V1.02 set_channel GI = 1
'*  Vtemp movest N1, 960, 10, 60, 10, 0
'*  Vtemp relax

wait "GIFlag = 1", 160, 0.1, , , , , , MSG, " Did not reach GI in 120 s" 
delay 300
result "Engine at GI"
result "N1 speed at GI is "& cv_N1 &"", REPORT & "Vib_Aecel"
result "N2 speed at GI is "& cv_N2 &"", REPORT & "Vib_Aecel"
result "EGT at GI is "& cv_EGT &"", REPORT & "Vib_Aecel"
result "PLA at GI is "& cv_PLA &"", REPORT & "Vib_Aecel"

'*  V1.03 stop_log VibAccel
stop_log "Vibration"

'do_fullset 30, "Vib Survey Deceleration ", "Vib_Survey_Dec"
do_fullset 30, "Fullset_Vib_Survey_Dec", "Vib_Survey_Dec"
delay 5
result "Vibration check - Peaks", REPORT & "Vib_Decel"
result "Max #1 Brg Vibn = " & fv_Vib1N1Pk & " mils. N1 at #1 Brg Vibn = " & fv_N1atV1MxA & " rpm.", REPORT & "Vib_Accel"
result "Max Turb Fr. Fwd Flange Vibn = " & fv_Vib2N1Pk & " mils. N1 at FFCCV Flange Vibn = " & fv_N1atV2MxA & " rpm.", REPORT & "Vib_Accel"
result "Max #1 Brg Vibn = " & fv_Vib1N2Pk & " ips. N2 at #1 Brg Vibn = " & fv_N2atV1MxA & " rpm.", REPORT & "Vib_Accel"
result "Max Turb Fr. Fwd Flange Vibn = " & fv_Vib2N2Pk & " ips. N2 at FFCCV Flange Vibn = " & fv_N2atV2MxA & " rpm.", REPORT & "Vib_Accel"
'*  delay 300
delay 15
'*  Vtemp stop_autothrottle
