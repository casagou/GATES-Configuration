Option Explicit

'* <script.tps>
'******************************************************************************
'*  AUTHOR: Don Pereira
'*
'*  DESCRIPTION:
'*  Performance
'*
'*  DATE: 9/15/2005 8:39:40 AM
'*
'*  MODIFICATIONS:
'*    DATE         WHO  NCR    DESCRIPTION
'*    ----------   ---  -----  --------------------------------------------------
'*  V1.01 06/02/2003  RH  Initial
'*  V1.02 10/07/2004  DP  Added set_channel for ENABLE_ALARMS'*
'*  V1.03 15/09/2005  JC  Converted to phase 3 format
'******************************************************************************
' ***** LOCAL VARIABLE DECLARATIONS *****
Dim lvabort

' Channel Registration
channel "N1, N2, EGT, PLA, Eng_On, OilCSEnd, tAtGI, AIFlag, GIFlag, N1R, HoldFNK3, N1R_MC, N1R_TO, N1KRated_MC, WFK3_MC, SFC_MC, SFCRef_MC, SFCMrg_MC, N2HD_MC, EGTHDLim_MC, EGTHDMrg_MC, EGTLim_MC, EGTMrg_MC, EGTK3_MC, EGTHD_MC, FNK3_MC, FNMrg_MC, N1RMC, N2K3_MC, N1KRated_TO, WFK3_TO, SFC_TO, SFCRef_TO, SFCMrg_TO, N2HD_TO, N2HDLim_TO, N2HDMrg_TO, EGTHDLim_TO, EGTHDMrg_TO, EGTLim_TO, EGTMrg_TO, EGTK3_TO, EGTHD_TO, FNK3_TO, FNMrg_TO, N1RTO, N2K3_TO, WFK3, SFCK3, SFCMrg, N2HD, N2HDMrg, EGTHDMrg, N2Lim, N2Mrg, EGTMrg, EGTK3, EGTHD, FNK3, FNMrgPC, N1R, N2K3, N2K3_MC, N2Mrg_TO, TO_Pnt, EGTHDM, TCQT3, TCQT3HI, TCQT3LO, WFK3_kgHr, TLA, Theta, XN1, KCondN1, KHN1, FI, GI, N1MCTrgt, N1TOTrgt, START, ENABLE_ALARMS, C4, ENGMOD"



'*  V1.02 show_view facility, Performance.0

'*   *  *
set_channel ENABLE_ALARMS, 1
set_channel C4, 1
set_channel ENGMOD, 1
set_channel START, 1
'*   *  *

set_channel TO_Pnt, 0

set_channel HoldFNK3, 0

'*  Vtemp start_autothrottle

instruction "Stabilize at Idle for 5 minutes"
'*   *  *
'*  V1.02 set_channel FI = 0
'*  V1.02 set_channel GI = 1
'*  Vtemp if cv_TLA > 5
'*  Vtemp movest N1, 960, 10, 45, 10, 0
'*  Vtemp relax
'*  Vtemp endif
'*   *  *
wait "GIFlag = 1", 30, 0.1, , , , SKIP, " Did not reach GI in 30 s"
delay 300
'delay 15

result "Engine at GI"
result "N1 speed at GI is "& cv_N1 &"", REPORT & "Performance_GI"
result "N2 speed at GI is "& cv_N2 &"", REPORT & "Performance_GI"
result "EGT at GI is "& cv_EGT &"", REPORT & "Performance_GI"
result "PLA at GI is "& cv_PLA &"", REPORT & "Performance_GI"

'*  Vtemp resume

instruction  "2.D.(9) Carefully and slowly accelerate to MAX CONT by select the PLA UP button from the control page."
note  "Stabilize the engine for 10 min."

'*  Vtemp movest N1, cv_N1MCTrgt, 10, 45, 10, 0
'*  Vtemp relax
'msgbox cv_N1R_MC

wait "N1R = " & cv_N1R_MC, 150, 10, , , , SKIP, "Engine not at MC in 150 s."
delay 600
'delay 15
'*  if (cv_TCQT3 < cv_TCQT3LO) Or (cv_TCQT3 > cv_TCQT3HI)
'*  prompt "TCQT3 is not within limits, do you wish to abort?", lvabort, boolean
'*  if lvabort = 1
'*  quit
'*  endif
'*  endif
'*  lvabort = 0
'do_fullset 5, "Perf Point: MC warmup", "MC_WarmUp"
do_fullset 30, "Fullset_MC_WarmUp", "MC_WarmUp"
'*  delay 300
'*  delay 140
'delay 15
result "Engine at MC"
result "N1 speed at MC is "& cv_N1 &"", REPORT & "Performance_MC"
result "N2 speed at MC is "& cv_N2 &"", REPORT & "Performance_MC"
result "EGT at MC is "& cv_EGT &"", REPORT & "Performance_MC"
result "PLA at MC is "& cv_PLA &"", REPORT & "Performance_MC"
'*  Vtemp resume

instruction  "2.D.(11) Accelerate slowly to Take-Off by select the PLA UP button from the control page."
note  "Stabilize the engine for 5 min."

'*  Vtemp movest N1, cv_N1TOTrgt, 10, 45, 10, 0
'*  Vtemp relax

wait "N1R = " & cv_N1R_TO, 30, 10, , , , SKIP, "Engine not at TO in 30 s."
delay 300
'delay 15
'*  if (cv_TCQT3 < cv_TCQT3LO) Or (cv_TCQT3 > cv_TCQT3HI)
'*  prompt "TCQT3 is not within limits, do you wish to abort?", lvabort, boolean
'*  if lvabort = 1
'*  quit
'*  endif
'*  endif
'*  lvabort = 0
'*  delay 120
delay 15
set_channel HoldFNK3, 1
delay 5
'do_fullset 10, "Perf Point: Take-Off", "Take_Off"
do_fullset 30, "Fullset_Take_Off", "Take_Off"
result "Engine at TO"
result "N1 speed at TO is "& cv_N1 &"", REPORT & "Performance_TO"
result "N2 speed at TO is "& cv_N2 &"", REPORT & "Performance_TO"
result "EGT at TO is "& cv_EGT &"", REPORT & "Performance_TO"
result "PLA at TO is "& cv_PLA &"", REPORT & "Performance_TO"
delay 5

set_channel WFK3_TO, fv_WFK3
set_channel SFC_TO, fv_SFCK3
set_channel SFCMrg_TO, fv_SFCMrg
set_channel N2HD_TO, fv_N2HD
set_channel N2HDMrg_TO, fv_N2HDMrg
set_channel EGTHDMrg_TO, fv_EGTHDMrg
set_channel N2Mrg_TO, fv_N2Mrg
set_channel EGTMrg_TO, fv_EGTMrg
set_channel EGTK3_TO, fv_EGTK3
set_channel EGTHD_TO, fv_EGTHDM
set_channel FNK3_TO, fv_FNK3
set_channel FNMrg_TO, fv_FNMrgPC
set_channel N1RTO, fv_N1R
set_channel N2K3_TO, fv_N2K3

set_channel TO_Pnt, 1
set_channel HoldFNK3, 0

'*  Vtemp resume

instruction  ".D.(12) Decelerate to MAX CONT. Stabilize the engine for 5 min by select the PLA DOWN button from the control page."
'note  "Perform QEC check during stabilization."

'*  Vtemp movest N1, cv_N1MCTrgt, 10, 45, 10, 0
'*  Vtemp relax

wait "N1R = " & cv_N1R_MC, 30, 10, , , , SKIP, "Engine not at MC in 30 s."
delay 300
result "Engine at MC"
result "N1 speed at MC is "& cv_N1 &"", REPORT & "Performance_MC"
result "N2 speed at MC is "& cv_N2 &"", REPORT & "Performance_MC"
result "EGT at MC is "& cv_EGT &"", REPORT & "Performance_MC"
result "PLA at MC is "& cv_PLA &"", REPORT & "Performance_MC"
'delay 30
'*  if (cv_TCQT3 < cv_TCQT3LO) Or (cv_TCQT3 > cv_TCQT3HI)
'*  prompt "TCQT3 is not within limits, do you wish to abort?", lvabort, boolean
'*  if lvabort = 1
'*  quit
'*  endif
'*  endif
'*  lvabort = 0
'*  delay 130
delay 15
set_channel HoldFNK3, 1
delay 5
'do_fullset 10, "Perf Point: MAX CONT", "MAX_CONT"
do_fullset 30, "Fullset_MAX_CONT", "MAX_CONT"
delay 5

set_channel WFK3_MC, fv_WFK3
set_channel SFC_MC, fv_SFCK3
set_channel SFCMrg_MC, fv_SFCMrg
set_channel N2HD_MC, fv_N2HD
'set_channel N2HDMrg_MC, fv_N2HDMrg
set_channel EGTHDMrg_MC, fv_EGTHDMrg
set_channel EGTMrg_MC, fv_EGTMrg
set_channel EGTK3_MC, fv_EGTK3
set_channel EGTHD_MC, fv_EGTHDM
set_channel FNK3_MC, fv_FNK3
set_channel FNMrg_MC, fv_FNMrgPC
set_channel N1RMC, fv_N1R
set_channel N2K3_MC, fv_N2K3

instruction  "2.D.(13) Decelerate slowly to FI in 2 minutes by select the PLA DOWN button from the control page."
instruction  "Switch the Flight Idle Control to ON from the control page"
note  "Stabilize the engine for 5 min."
'*   *  *
'*  Vtemp resume
'*  V1.02 set_channel GI = 0
'*  V1.02 set_channel FI = 1
'*  Vtemp movest N1, 1100, 10, 45, 10, 0
'*  Vtemp relax
'*   *  *
wait "AIFlag = 1", 120, 0.1,,,,SKIP, "Failed to reach FI in 120 s"
delay 300
result "Engine at FI"
result "N1 speed at FI is "& cv_N1 &"", REPORT & "Performance_FI"
result "N2 speed at FI is "& cv_N2 &"", REPORT & "Performance_FI"
result "EGT at FI is "& cv_EGT &"", REPORT & "Performance_FI"
result "PLA at FI is "& cv_PLA &"", REPORT & "Performance_FI"
'delay 15
'do_fullset 5, "Perf Point: AI", "Perf_AI"
do_fullset 30, "Fullset_Perf_AI", "Perf_AI"

'*  Vtemp resume

instruction  "2.D.(14) Select Ground Idle by Switch the Flight Idle Control to OFF from the control page."
note  "Stabilize the engine for 5 min."
'*   *  *
'*  V1.02 set_channel FI = 0
'*  V1.02 set_channel GI = 1
'*  Vtemp movest N1, 960, 10, 45, 10, 0
'*  Vtemp relax
'*   *  *
wait "GIFlag = 1", 30, 0.1 ,,,, SKIP, "Failed to reach MIN. IDLE in 30 s"
delay 300

result "Engine at GI"
result "N1 speed at GI is "& cv_N1 &"", REPORT & "Performance_GI"
result "N2 speed at GI is "& cv_N2 &"", REPORT & "Performance_GI"
result "EGT at GI is "& cv_EGT &"", REPORT & "Performance_GI"
result "PLA at GI is "& cv_PLA &"", REPORT & "Performance_GI"
'do_fullset 5, "Perf Point: GI", "Perf_GI"
do_fullset 30, "Fullset_Perf_GI", "Perf_GI"
'*  Vtemp stop_autothrottle
