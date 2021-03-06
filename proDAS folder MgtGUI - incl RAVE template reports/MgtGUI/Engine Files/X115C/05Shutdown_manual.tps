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
instruction "Set Fuel Supply switch to CUTOFF position"
start_log "Stop", "Stop"
set_channel FuelEnable, 0
wait "FuelOn = 0", 3, 0.1, , , , , , MSG, "Fuel is not turned off"


wait "EndStartL = 1", 120, 0.1, , , , , , MSG, "End Start indication not received in 120 s"
If cv_tToIdle >= 120 Then
result "Time from Fuel ON to Idle exceeded 120 s", REPORT & "AutoStart", RED
End If

'*  engine at idle

If cv_ModePosn <> 2 Then
set_channel Normal, 1
wait "ModePosn = 2", 3, 0.1,,,,,, MSG, "Mode Selector Switch not responding.  Use PLC"
If skipgv = TRUE Then
result "Operator skipped Mode Selector to NORMAL", REPORT & "AutoStart"
Else
result "Mode Selector Switch selected to NORMAL", REPORT & "AutoStart"
End If
Else
result "Mode Selector Switch was already in NORMAL position", REPORT & "AutoStart"
End If

'do_fullset 1, "Ground Idle following Start", "AutoStart"
do_fullset 10, "Fullset_shutdown", "shutdown"

instruction "After GI stabilization Auto-Shutdown Commences"
note "Engine Auto Shut-down"


instruction "Close Test Cell Start Air supply valve"
note "Close SAP"

instruction "Secure Engine and Test Bed"
note "Engine Shutdown"
stop_log "Stop"