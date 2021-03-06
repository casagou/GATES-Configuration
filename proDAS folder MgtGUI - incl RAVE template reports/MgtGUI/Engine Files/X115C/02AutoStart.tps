Option Explicit

'* <script.tps>
'******************************************************************************
'*  AUTHOR: 
'*
'*  DESCRIPTION:
'*  Auto Start
'*
'*  DATE: 9/15/2005 8:26:58 AM
'*
'*  MODIFICATIONS:
'*    DATE         WHO  NCR    DESCRIPTION
'*    ----------   ---  -----  --------------------------------------------------
'*  V1.01 07/02/2003 RH  Initial
'*  V1.02 10/03/2004 DP  Modified for proDAS w/ RTE on Win2K for Hamburg Trade Show 2004
'*  V1.03 02/04/2004 DP  Modified for demo
'*  V1.04 10/07/2004 DP  Added set_channel for ENABLE_ALARMS
'*  V1.05 15/09/2005 JC  Converted to phase 3 format 
'*
'******************************************************************************

' Channel Registration
channel "A27520, B27520, FuelEnable, A27518, B27518, A27519, A27519, Eng_On, FuelOnS, tToLite, WFK_kgHr, EndStartL, tToIdle, FuelOn, EndLite, N2S, StartReset, IgnStart, Normal, ModePosn, POIL, Ignitor1FB, Ignitor2FB, MasterChA, MasterChB, MasterChAST, MasterChBST, StartMode, StartMode_E, START, GI, FI, WF,ENABLE_ALARMS,IgnitionST"


'*  note 100% N2 = 14460 rpm; 100% N1 = 4784 rpm.
'*   *  *
set_channel ENABLE_ALARMS, 1
set_channel START, 0

set_channel StartReset, 1
'delay 2
set_channel StartReset, 0

'*  V1.02 set_channel FI = 0
'*  V1.02 set_channel GI = 1
'*   *  *

'*  V1.02 show_view facility, Start.0

instruction "Turn on Channel A and B Master switches"
set_channel MasterChA, 1
wait "MasterChAST = 1", 3, 0.1,,,,,,MSG, "Channel A Master switch not responding.  Use PLC"
set_channel MasterChB, 1
wait "MasterChBST = 1", 3, 0.1,,,,,, MSG, "Channel B Master switch not responding.  Use PLC"

instruction "Open Test Cell Start Air supply valve"
note "NOTE: Open SAV on FCS"
instruction "Ensure intake is open"
note "NOTE: Set the starter air supply pressure to 25 psig on FCS"

warning "Max EGT on Start is 854 DegC"
caution "Obey the oil pressure limits. If the engine operates at low"
caution "oil pressures, bearing damage can occur."

caution "Do not operate the engine above the GI with the cowl OPEN."

note "NOTE: The GI leak check will be done with the cowlings OPEN"

caution "Carefully monitor the start cycle when you use lower starter"
caution "inlet air-pressure than recommended.  Low air-pressure at the"
caution "starter inlet can cause lower speed, higher peak EGT and unusual time to idle."

instruction "Adhere to all Cautions"
PromptOK "Cautions Noted"

note "NOTE1: If the engine fails to light-off (in 10 - 15 s), ECU auto-"
note "      matically de-energizes the ignition system, stops fuel flow"
note "      and dry-motor the engine for 30 s. The ECU will make"
note "      another attempt, and if it fails again, it will de-energize"
note "      ignition system, stop fuel flow, dry-motor the engine for"
note "      30 s and give START ABORT message."

note "NOTE2: If ECU cannot automatically start the engine, select"
note "       fuel Off, set Mode Selector to NORMAL and troubleshoot."

instruction "Adhere to all Operator Notes above"
PromptOK "Confirm Notes"

instruction "Set fuel select switch to CUTOFF position"

wait "FuelOnS = 0", 10, 0.1, , , , , , MSG, "Fuel select switch not in Cutoff position after 10 s."
If skipgv = TRUE Then
result "Operator skipped fuel select switch Cutoff check. Procedure aborted.", REPORT & "Start"
quit
End If

instruction "Set Throttle to GI (0 Deg)"
'*   *  *
'*  V1.02 if cv_TLA > 5
'*  V1.02 movest N1, 0, 10, 45, 2, 0
'*  V1.02 endif
'*   *  *

instruction "Set Mode Selector to Normal on ECS"
note "Mode Selector switch to normal on ECS"
If cv_ModePosn <> 2 Then
set_channel Normal, 1
wait "ModePosn = 2", 3, 0.1,,,,,, MSG, "Mode Selector Switch not responding.  Use PLC"
If skipgv = TRUE Then
result "Operator skipped Mode Selector to NORMAL", REPORT & "Start"
Else
result "Mode Selector Switch selected to NORMAL", REPORT & "Start"
End If
Else
result "Mode Selector Switch was already in NORMAL position", REPORT & "Start"
End If

set_channel StartReset, 1
delay 2
set_channel StartReset, 0

'*  define a Start log with:
'*  EGT, WFM, WFM1, N2S, N1S, POIL, TLA
start_log "Start", "Start"

instruction "Set Start Mode to Auto on ECS"
note "Mode Selector switch to Auto on ECS"
set_channel StartMode, 1
wait "StartMode_E = 0", 3, 0.1, , , , , , MSG, "Place StartMode switch in Auto mode using PLC"
If skipgv = 1 Then
result "Operator skipped Start Mode AUTO instruction.", REPORT & "AutoStart"
Else
result "Start Mode set to AUTO", REPORT & "AutoStart"
End If

instruction "Set Mode Selector to Ignition on ECS"
note "Mode Selector switch to Ignition on ECS"
set_channel IgnStart, 1
set_channel Normal, 0
wait "ModePosn = 3", 3, 0.1,,,,,, MSG, "Mode Selector Switch not responding.  Use PLC"
If skipgv = TRUE Then
result "Operator skipped Mode Selector Switch IGNITION instruction", REPORT & "AutoStart"
Else
result "Mode Selector Switch selected to IGNITION", REPORT & "AutoStart"
End If

instruction "9.A.(3)(b) Set Fuel ON on ECS"
note "Set Fuel ON on ECS"
'*   *  *
set_channel START, 1
'*   *  *


set_channel IgnitionST, 1
note "NOTE1: EEC automatically turns the ignition ON at 16% N2 (2314 rpm)"
note "NOTE2: EEC automatically turns fuel ON at 22 % (3181 rpm) N2"
note "NOTE3: EEC automatically turns the starter air valve and"
note "       ignition OFF at approximately 50 % (7230 rpm) N2"

set_channel FuelEnable, 1
wait "FuelOn = 1", 3, 0.1, , , , , , MSG, "Fuel ON not selected"

instruction "Check for positive, increasing oil pressure"

wait "N2S >= 2314", 30, 1, , , , , , MSG, "Engine didn not reach 2314 rpm N2 in 30 s. Press SKIP to abort."
'If skipgv = TRUE Then
'*  autostart AbortStart
'End If
If skipgv = TRUE Then
result "Operator skipped IGNITION ON", REPORT & "AutoStart"
Else
result "EEC turned Ignitor ON at 16% N2 (2314 rpm)", REPORT & "AutoStart"
End If

wait "N2S >= 3181", 30, 1, , , , , , MSG, "Engine didn not reach 3181 rpm N2 in 30 s. Press SKIP to abort."
If skipgv = TRUE Then
'*  autostart AbortStart
End If
'*  V1.03 if WFK_kgHr > 0
If cv_WF > 0 Then
result "EEC turned fuel ON at 22 % N2(3181 rpm)", REPORT & "AutoStart"
Else
result "FAULT: Fuel not ON at 22 % N2(3181 rpm)", REPORT & "AutoStart"
End If

set_channel IgnitionST, 0

wait "EndLite = 1", 20, 0.1, , , , , , MSG, "No lite-off after 20 s. Press SKIP to abort Start"
If skipgv = TRUE Then
result "Start aborted", REPORT & "AutoStart"
'*  quit
'*  autostart AbortStart
End If

If cv_tToLite > 15 Then
result "Time to lite is " & cv_tToLite & " s and it should be 15 s max. Start aborted", REPORT & "AutoStart", RED
'*  quit
'*  autostart AbortStart
End If

'*  V1.03 result "Fuel flow during start is " cv_WFK_kgHr " kg per hour." /report "AutoStart"
result "Fuel flow during start is " & cv_WF & " kg per hour", REPORT & "AutoStart"

wait "N2S >= 7230", 30, 50, , , , , , MSG, "Engine didn not reach 7230 rpm N2 in 30 s. Press SKIP to abort."
If skipgv = TRUE Then
'*  quit
'*  autostart AbortStart
End If



If cv_Ignitor1FB = TRUE Or cv_Ignitor2FB = TRUE Then
result "IGNITORS NOT OFF", REPORT & "AbortStart"
Else
result "Both Ignitors are OFF", REPORT & "AbortStart"
End If

instruction "Start engine stabilization at GI"
PromptOK "Stablize engine after Autostart for 120 secs"
Delay 120

do_fullset 10, "Fullset_AutoStart", "AutoStart"

stop_log "Start"
instruction "Check Engine parameters OK at GI"