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
'*  V1.05 03/03/2015 SG  Updated to Throttle Mark III
'*  V1.04 15/09/2005 JC  Converted to phase 3 format
'*  V1.03 11/09/2004 DP  Changed Log name to Vibration
'*  V1.02 10/07/2004 DP  Added set_channel for ENABLE_ALARMS
'*  V1.01 06/02/2001 RH  Initial
'*
'******************************************************************************

' Channel Registration
Channel "N1R, N1R_TO, GIFlag, tAtGI, VibReset, Accel, Vib1N1Pk, N1atV1MxA, Vib2N1Pk, N1atV2MxA, Vib1N2Pk, N2atV1MxA, Vib2N2Pk, N2atV2MxA, Vib1N1PkD, N1atV1MxD, Vib2N1PkD, N1atV2MxD, Vib1N2PkD, N2atV1MxD, Vib2N2PkD, N2atV2MxD, GetAccTrg, TLA, Theta, XN1, KCondN1, KHN1, GI, START, N1TOTrgt, ENABLE_ALARMS,C4,ENGMOD,PLA,N1,FuelEnable,N2,EGT"
Dim returnCode

set_channel ENABLE_ALARMS, 1
set_channel C4, 1
set_channel ENGMOD, 1
set_channel START, 1

instruction "Put throttle into auto mode"
'* V1.05 rtp_start

returncode = at_startautomode
result "returncode for at_startautomode "& returncode &"", REPORT & "Vib_Aecel"

caution "THE FAN MUST BE BALANCED FOR THIS TEST"

note "NOTE: Prior to performing Vibration Survey, warm up the"
note "engine at MC for 5 min or 80% N1 for 7 min"

'* V1.05 rtp_relax, set FuelEnable to 1 otherwise won't meet GI
set_channel FuelEnable, 1

instruction "Make sure the Fuel is ON on the throttle page"
note "Make sure the Idle/CutOff are turned off on the throttle page"

instruction "Stabilize at Idle for 5 minutes"

'*  V1.02 set_channel GI = 1
'if cv_PLA > 5 then
' V1.04 rtp_movest N1, 960, 10, 45, 10, 0
'* V1.05 rtp_movest PLA, 0, 5, 7.0, 1.0, 1.0
returncode = at_Move (TLA, 0, 5, 7.0, 1.0, 1.0)
result "returncode for at_Move "& returncode &"", REPORT & "Vib_Aecel"


'* V1.05 rtp_relax, set FuelEnable to 1 otherwise won't meet GI
'set_channel FuelEnable, 1

'end if

wait "GIFlag = 1", 30, 0.1, , , , , , MSG, " Did not reach GI in 30 s "
delay 300
'delay 15
result "Engine at GI"
result "N1 speed at GI is "& fv_N1 &"", REPORT & "Vib_Aecel"
result "N2 speed at GI is "& cv_N2 &"", REPORT & "Vib_Aecel"
result "EGT at GI is "& cv_EGT &"", REPORT & "Vib_Aecel"
result "PLA at GI is "& cv_PLA &"", REPORT & "Vib_Aecel"

'*  reset Vibration Parameters at Acceleration
set_channel VibReset, 1
delay 2
set_channel VibReset, 0
set_channel Accel, 1

'*  V1.03 start_log VibAccel
start_log "Vibration", "Vibration_Accel", "Acceleration"
'*  start_log Vibration, VibAccel, "Vibration Acceleration"
'*  start_log Vibration, Vibration, "Vibration Acceleration"
result "Vibration Acceleration Log started", REPORT & "Vibration"

'* V1.05 rtp_resume

returncode = at_SetClosedLoopMode
result "returncode for at_SetClosedLoopMode "& returncode &"", REPORT & "Vib_Aecel"

instruction "Slowly and constantly accelerate to Take Off in 2 min, "
note "hold it there for 30 s and set the throttle stop."

'* V1.05 rtp_movest N1, cv_N1TOTrgt, 60, 90, 5, 1
'at_move "N1", cv_N1TOTrgt, 60, 90, 5, 1
'result "returncode for at_Move "& returncode &"", REPORT & "Vib_Decel"
returncode = at_Move (TLA, 56.8, 60, 90.0, 1.0, 1.0)


'* V1.05 rtp_relax

returncode = at_SetOpenLoopMode
result "returncode for at_SetOpenLoopMode "& returncode &"", REPORT & "Vib_Aecel"

wait "N1R = " & cv_N1R_TO, 120, 10, , , , , , MSG, "Engine not at TO in 120 s"
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
'do_fullset 1, "Vib Survey Accel", "Vib_Survey_Acc"
do_fullset 30, "Fullset_Vib_Survey_Acc", "Vib_Survey_Acc"
delay 5
set_channel GetAccTrg, 1
set_channel Accel, 0

'*  V1.03 start_log VibAccel
start_log "Vibration", "Vibration_Decel", "deceleration"

result "Vibration Deceleration Log started", REPORT & "Vibration"

'* V1.05 rtp_resume
at_SetClosedLoopMode

instruction "Slowly and constantly decelerate to Ground Idle"
note "in 2 minutes and stabilize for 5 minutes."

'*  V1.02 set_channel GI = 1
' V1.04 rtp_movest N1, 960, 10, 60, 10, 0
'* V1.05 rtp_movest PLA, 0, 10, 60, 1.0, 1.0

returncode = at_Move ("TLA", 0, 10, 60, 1.0, 1.0)
result "returncode for at_Move "& returncode &"", REPORT & "Vib_Decel"

wait "GIFlag = 1", 120, 0.1, , , , , , MSG, " Did not reach GI in 120 s" 
delay 300
'*  V1.03 stop_log VibAccel
result "Engine at GI"
result "N1 speed at GI is "& cv_N1 &"", REPORT & "Vib_Decel"
result "N2 speed at GI is "& cv_N2 &"", REPORT & "Vib_Decel"
result "EGT at GI is "& cv_EGT &"", REPORT & "Vib_Decel"
result "PLA at GI is "& cv_PLA &"", REPORT & "Vib_Decel"

'* V1.05 rtp_relax
'at_SetOpenLoopMode

stop_log "Vibration"

'do_fullset 1, "Vib Survey Deceleration ", "Vib_Survey_Dec"
do_fullset 30, "Fullset_Vib_Survey_Dec ", "Vib_Survey_Dec"
delay 5
result "Vibration check - Peaks", REPORT & "Vib_Decel"
result "Max #1 Brg Vibn = " & fv_Vib1N1Pk & " mils. N1 at #1 Brg Vibn = " & fv_N1atV1MxA & " rpm.", REPORT & "Vib_Accel"
result "Max Turb Fr. Fwd Flange Vibn = " & fv_Vib2N1Pk & " mils. N1 at FFCCV Flange Vibn = " & fv_N1atV2MxA & " rpm.", REPORT & "Vib_Accel"
result "Max #1 Brg Vibn = " & fv_Vib1N2Pk & " ips. N2 at #1 Brg Vibn = " & fv_N2atV1MxA & " rpm.", REPORT & "Vib_Accel"
result "Max Turb Fr. Fwd Flange Vibn = " & fv_Vib2N2Pk & " ips. N2 at FFCCV Flange Vibn = " & fv_N2atV2MxA & " rpm.", REPORT & "Vib_Accel"
'*  delay 300
delay 15
'instruction "Put throttle in manual mode"
'* V1.05 rtp_stop
at_stopautomode
