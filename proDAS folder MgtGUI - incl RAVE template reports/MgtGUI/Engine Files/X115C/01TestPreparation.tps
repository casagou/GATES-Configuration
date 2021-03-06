Option Explicit

'* <script.tps>
'******************************************************************************
'*  AUTHOR: <your name goes here>
'*
'*  DESCRIPTION:
'*  Test Preparation
'*
'*  DATE: 9/15/2005 8:18:15 AM
'*
'*  MODIFICATIONS:
'*    DATE         WHO  NCR    DESCRIPTION
'*    ----------   ---  -----  --------------------------------------------------
'*  V1.05 03/03/2015  SG  updated for Throttle MarkIII
'*  V1.01 07/09/2001  RH  Initial
'*  V1.02 09/07/2004  DP  Modified for Demo.  Added set_channels for ENGMOD and C4
'*                        since the TIP is not working right now.
'*  V1.03  15/09/05   JC  Converted to phase 3 language
'*  V1.04  19/10/05   DP  Testing errors
'*  --------------------------------------------------------------'*
'******************************************************************************

' ***** LOCAL VARIABLE DECLARATIONS *****
Dim lvIDGdisc, lvIDGinst, lvNo1IGN, lvNo2IGN, lvOilLevel
Dim lvPreFuel, lvPreHr, lvPreMin, lvStartleak, returncode
'*  V1.05 Dim tempvar1gv

' Channel Registration
channel "Eng_On, PreRTMin, PreRTHr, PreFuel, IDGDisc, IDGDiscST, FuelOnS, Normal, ModePosn, StMode, StModeST, IgnStart, FuelOffFB, ENGMOD, C4,ENABLE_ALARMS, TLA"

set_channel ENABLE_ALARMS, 1
set_channel ENGMOD, 1
set_channel C4, 1
'*  V1.05 tempvar1gv = 0
If cv_Eng_On = 1 Then
quit
End If

'prompt_num "Enter previous run time: Hours", lvPreHr, 0, 100, 1
'set_channel PreRTHr, lvPreHr
'prompt_num "Enter previous run time: Minutes", lvPreMin, 0, 60,10
'set_channel PreRTMin, lvPreMin
'prompt_num "Enter the amount of fuel used for previous run in litres", lvPreFuel, 0, 100000, 55
'set_channel PreFuel, lvPreFuel

prompt_boo "Is the IDG installed?", lvIDGinst

If lvIDGinst = TRUE Then
result "Enter the IDG Installed logic"
instruction "Check IDG disconnect or press SKIP", SKIP
If skipgv = FALSE Then
set_channel IDGDisc, 1
wait "IDGDiscST = 1", 3, 0.1, , , , , , MSG, "IDG disconnect failed. Use PLC."
prompt_boo "Was IDG disconnect satisfactory?", lvIDGdisc
If lvIDGdisc = TRUE Then
result "IDG disconnect operation OK", REPORT & "IDGdisc"
Else
result "IDG disconnect operation NOT OK", REPORT & "IDGdisc"
End If
set_channel IDGDisc, 0
wait "IDGDiscST = 0", 3, 0.1, , , , , , MSG, "IDG disconnect failed. Use PLC."
End If
' * V1.03  Added the Else for testing
Else
result "Enter the IDG Not Installed logic"
End If

instruction "Do Ignition Check"

instruction "5.J.(1)(a) Set fuel select switch to CUTOFF position"
' * DPP wait "FuelOnS = 0", 10, 0.1, , , , , , MSG, "Fuel select switch not in Cutoff position after 10 s."
wait "FuelOnS = 0", 10, 0.1, , , , , , MSG, "Fuel select switch not in Cutoff position after 10 s."
If skipgv = 1 Then
result "Operator skipped fuel select switch Cutoff check."
End If

instruction "5.J.(1)(b) Set Throttle to GI"

instruction "5.J.(1)(c) Set Mode Selector to NORMAL"
If cv_ModePosn <> 2 Then
set_channel Normal, 1
wait "ModePosn = 2", 3, 0.1,,,,,, MSG,  "Mode Selector Switch not responding.  Use PLC"
If skipgv = 1 Then
result "Operator skipped Mode Selector to NORMAL"
Else
result "Mode Selector Switch selected to NORMAL"
End If
Else
result "Mode Selector Switch was already in NORMAL position"
End If

instruction "5.J.(1)(e) Make sure there is no starter inlet air pressure"
note "The engine will not be motored during this test."

instruction "5.J.(2)(a) Turn off the 115VAC ignition power to ECU B channel, "
note "or disconnect the J2 harness from the ECU."

instruction "5.J.(2)(b) Set the Manual Start switch to ON"
set_channel StMode, 1
delay 1
wait "StModeST = 1", 3, 0.1,,,,,, MSG, "Start Mode switch not responding. Use PLC"
If skipgv = 1 Then
result "Operator skipped Start Mode MANUAL instruction.", REPORT & "PreTest"
Else
result "Start Mode set to MANUAL", REPORT & "PreTest"
End If

instruction "5.J.(2)(c) Set the Mode Selector switch to IGNITION"
set_channel IgnStart, 1
set_channel Normal, 0
wait "ModePosn = 3", 3, 0.1,,,,,, MSG, "Mode Selector Switch not responding.  Use PLC"
If skipgv = 1 Then
result "Operator skipped Mode Selector Switch IGNITION instruction", REPORT & "PreTest"
Else
result "Mode Selector Switch selected to IGNITION", REPORT & "PreTest"
End If

'instruction "Set Fuel to ON"
'wait "FuelOffFB = 0", 3, 0.1, , , , , , MSG, "Fuel not ON"
'If skipgv = 1 Then
'result "Operator skipped Fuel ON instruction", REPORT & "ManStart"
'End If

instruction "Make sure the Fuel is OFF"
wait "FuelOffFB = 1", 3, 0.1, , , , , , MSG, "Fuel not OFF"
If skipgv = 1 Then
result "Operator skipped Fuel OFF instruction", REPORT & "ManStart"
End If

instruction "5.J.(2)(d) Make sure the No. 1 ignition system (left hand side)"
note "is firing.  Listen for an audible check in the cell."

prompt_boo "Was No. 1 Ignitor operation satisfactory?", lvNo1IGN
If lvNo1IGN = TRUE Then
result "No. 1 Ignitor operation OK", REPORT & "NO1IGNIT"
Else
result "No. 1 Ignitor operation NOT OK", REPORT & "NO1IGNIT"
End If

'instruction "Set Fuel to OFF"
'wait "FuelOffFB = 1", 3, 0.1, , , , , , MSG, "Fuel not OFF"
'If skipgv = 1 Then
'result "Operator skipped Fuel OFF instruction", REPORT & "ManStart"
'End If

instruction "5.J.(2)(e) Set the Manual Start switch to OFF"
set_channel StMode, 0
delay 1
wait "StModeST = 0", 3, 0.1,,,,,, MSG, "Start Mode switch not responding. Use PLC"
If skipgv = 1 Then
result "Operator skipped Start Mode MANUAL OFF instruction.", REPORT & "PreTest"
Else
result "Start Mode set to MANUAL", REPORT & "PreTest"
End If

instruction "5.J.(2)(f) Set the Mode Selector to NORMAL"
set_channel Normal, 1
wait "ModePosn = 2", 3, 0.1,,,,,, MSG, "Mode Selector Switch not responding.  Use PLC"
If skipgv = 1 Then
result "Operator skipped Mode Selector to NORMAL"
Else
result "Mode Selector Switch selected to NORMAL"
End If

instruction "5.J.(2)(g)1 Turn on the 115VAC ignition power to ECU B channel, "
note "or connect the J2 harness to the ECU."

instruction "5.J.(2)(g)2 Turn off the 115VAC ignition power to ECU A channel, "
note "or disconnect the J1 harness from the ECU."

instruction "5.J.(2)(h) Set the Manual Start switch to ON"
set_channel StMode, 1
delay 1
wait "StModeST = 1", 3, 0.1,,,,,, MSG, "Start Mode switch not responding. Use PLC"
If skipgv = 1 Then
result "Operator skipped Start Mode MANUAL instruction.", REPORT & "PreTest"
Else
result "Start Mode set to MANUAL", REPORT & "PreTest"
End If

instruction "5.J.(2)(i) Set the Mode Selector switch to IGNITION"
set_channel IgnStart, 1
set_channel Normal, 0
wait "ModePosn = 3", 3, 0.1,,,,,, MSG, "Mode Selector Switch not responding.  Use PLC"
If skipgv = 1 Then
result "Operator skipped Mode Selector Switch IGNITION instruction", REPORT & "PreTest"
Else
result "Mode Selector Switch selected to IGNITION", REPORT & "PreTest"
End If

'instruction "Set Fuel to ON"
'wait "FuelOffFB = 0", 3, 0.1, , , , , , MSG, "Fuel not ON"
'If skipgv = 1 Then
'result "Operator skipped Fuel ON instruction", REPORT & "ManStart"
'End If

instruction "Make sure the Fuel is OFF"
wait "FuelOffFB = 1", 3, 0.1, , , , , , MSG, "Fuel not OFF"
If skipgv = 1 Then
result "Operator skipped Fuel OFF instruction", REPORT & "ManStart"
End If

instruction "5.J.(2)(j) Make sure the No. 2 ignition system (right hand side)"
note "is firing.  Listen for an audible check in the cell."

prompt_boo "Was No. 2 Ignitor operation satisfactory?", lvNo2IGN
If lvNo2IGN = 1 Then
result "No. 2 Ignitor operation OK", REPORT & "NO2IGNIT"
Else
result "No. 2 Ignitor operation NOT OK", REPORT & "NO2IGNIT"
End If

'instruction "Set Fuel to OFF"
'wait "FuelOffFB = 1", 3, 0.1, , , , , , MSG, "Fuel not OFF"
'If skipgv = 1 Then
'result "Operator skipped Fuel OFF instruction", REPORT & "ManStart"
'End If

instruction "5.J.(2)(k) Set the Manual Start switch to OFF"
set_channel StMode, 0
delay 1
wait "StModeST = 0", 3, 0.1,,,,,, MSG, "Start Mode switch not responding. Use PLC"
If skipgv = 1 Then
result "Operator skipped Start Mode MANUAL OFF instruction.", REPORT & "PreTest"
Else
result "Start Mode set to MANUAL", REPORT & "PreTest"
End If

instruction "5.J.(2)(l) Set the Mode Selector to NORMAL"
set_channel Normal, 1
wait "ModePosn = 2", 3, 0.1,,,,,, MSG, "Mode Selector Switch not responding.  Use PLC"
If skipgv = 1 Then
result "Operator skipped Mode Selector to NORMAL"
Else
result "Mode Selector Switch selected to NORMAL"
End If

instruction "5.J.(2)(m) Turn on the 115VAC ignition power to ECU A channel, "
note "or connect the J1 harness to the ECU."

instruction "Do an Air System leakcheck"
note "Turn Test Cell start air ON"
note "Check for any air leaks"
note "Turn Test Cell start air OFF"
prompt_boo "Was air leak check satisfactory?", lvStartleak
If lvStartleak = TRUE Then
result "Start air leak check OK", REPORT & "Startleak"
Else
result "Start air leak check NOT OK", REPORT & "Startleak"
End If

instruction "Do an oil quantity check"
prompt_boo "Is oil level satisfactory?", lvOilLevel
If lvOilLevel = TRUE Then
result "Oil level OK", REPORT & "OilLevel"
Else
result "Oil level NOT OK.  Refill oil tank", REPORT & "OilLevel"
End If

