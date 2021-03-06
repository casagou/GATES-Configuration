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
'*  V1.04 04/12/2009  DP  Deleted test blocks - they were generating errors
'*  V1.05 21/10/2017  DP  changed most of the instructions to notes in order to speed up execution
'******************************************************************************
' ***** LOCAL VARIABLE DECLARATIONS *****
' Channel Registration
channel "Tq_PT_, Sol_Fuel_, n_GG, n_PT, tStable"


'*  V1.02 show_view facility, Performance.0

'*   *  *
set_channel Sol_Fuel_, 42.5
set_channel Tq_PT_, 6220

instruction "Stabilize at Idle for 5 minutes"

wait "n_GG < 8600", 30, 0.1, , , , SKIP, " n_GG is above 8600 rpm"
wait "tStable > 30", 30, 0.1, , , , SKIP, " tStable is less than 300s"
'*  delay 300
delay 15

instruction  "Accelerate to n_GG = 10500"
note  "Stabilize the engine for 10 min."
set_channel Sol_Fuel_, 50.8
set_channel Tq_PT_, 6390
wait "n_GG > 10500", 30, 0.1, , , , SKIP, " n_GG is above 8600 rpm"
delay 30
do_fullset 5, "Perf Point: warmup", "WarmUp"

' -------------------------------------------

instruction  "Accelerate GG speed to 11500 and set PT to 6000"
note  "Stabilize the engine for 10 min."
set_channel Sol_Fuel_, 57.3
set_channel Tq_PT_, 7230
wait "n_GG > 11500", 30, 0.1, , , , SKIP, " n_GG is below 11500 rpm"
wait "n_PT > 6000", 30, 0.1, , , , SKIP, " n_PT is below 6000 rpm"
delay 30
do_fullset 5, "Perf Point: Speed1_Point1", "GG_Sp1_Pt1"

instruction  "Increase PT speed to 8400"
note  "Stabilize the engine for 2 min."
set_channel Tq_PT_, 5670
wait "n_GG > 11500", 30, 0.1, , , , SKIP, " n_GG is below 11500 rpm"
wait "n_PT > 8400", 30, 0.1, , , , SKIP, " n_PT is below 8400 rpm"
delay 5
do_fullset 5, "Perf Point: Speed1_Point2", "GG_Sp1_Pt2"

instruction  "Increase PT speed to 10800"
note  "Stabilize the engine for 2 min."
set_channel Tq_PT_, 4110
wait "n_GG > 11500", 30, 0.1, , , , SKIP, " n_GG is below 11500 rpm"
wait "n_PT > 10800", 30, 0.1, , , , SKIP, " n_PT is below 10800 rpm"
delay 5
do_fullset 5, "Perf Point: Speed1_Point3", "GG_Sp1_Pt3"

' * V1.05 instruction  "Increase PT speed to 11200"
note  "Increase PT speed to 11200"
note  "Stabilize the engine for 2 min."
set_channel Tq_PT_, 3850
wait "n_GG > 11500", 30, 0.1, , , , SKIP, " n_GG is below 11500 rpm"
wait "n_PT > 11200", 30, 0.1, , , , SKIP, " n_PT is below 11200 rpm"
delay 5
do_fullset 5, "Perf Point: Speed1_Point4", "GG_Sp1_Pt4"

' * V1.05 instruction  "Increase PT speed to 11500"
note  "Increase PT speed to 11500"
note  "Stabilize the engine for 2 min."
set_channel Tq_PT_, 3655
wait "n_GG > 11500", 30, 0.1, , , , SKIP, " n_GG is below 11500 rpm"
wait "n_PT > 11500", 30, 0.1, , , , SKIP, " n_PT is below 11500 rpm"
delay 5
do_fullset 5, "Perf Point: Speed1_Point5", "GG_Sp1_Pt5"

' * V1.05 instruction  "Decrease PT speed to 6000"
note  "Decrease PT speed to 6000"
set_channel Tq_PT_, 7230
wait "n_PT < 6100", 30, 0.1, , , , SKIP, " n_PT is below 6000 rpm"
delay 5

' ---------------------------------------------

' * V1.05 instruction  "Accelerate GG speed to 12000 and set PT to 7200"
note  "Accelerate GG speed to 12000 and set PT to 7200"
note  "Stabilize the engine for 10 min."
set_channel Sol_Fuel_, 62.2
set_channel Tq_PT_, 7580
wait "n_GG > 12000", 30, 0.1, , , , SKIP, " n_GG is below 12000 rpm"
wait "n_PT > 7200", 30, 0.1, , , , SKIP, " n_PT is below 7200 rpm"
delay 30
do_fullset 5, "Perf Point: Speed2_Point1", "GG_Sp2_Pt1"

' * V1.05 instruction  "Increase PT speed to 9600"
note  "Increase PT speed to 9600"
note  "Stabilize the engine for 2 min."
set_channel Tq_PT_, 5890
wait "n_GG > 12000", 30, 0.1, , , , SKIP, " n_GG is below 12500 rpm"
wait "n_PT > 9600", 30, 0.1, , , , SKIP, " n_PT is below 9600 rpm"
delay 5
do_fullset 5, "Perf Point: Speed2_Point2", "GG_Sp2_Pt2"

' * V1.05 instruction  "Increase PT speed to 11200"
note  "Increase PT speed to 11200"
note  "Stabilize the engine for 2 min."
set_channel Tq_PT_, 4760
wait "n_GG > 12000", 30, 0.1, , , , SKIP, " n_GG is below 11500 rpm"
wait "n_PT > 11200", 30, 0.1, , , , SKIP, " n_PT is below 11200 rpm"
delay 5
do_fullset 5, "Perf Point: Speed2_Point3", "GG_Sp2_Pt3"

' * V1.05 instruction  "Decrease PT speed to 7200"
set_channel Tq_PT_, 7580
wait "n_PT < 7300", 30, 0.1, , , , SKIP, " n_PT is below 6000 rpm"
delay 5

' -------------------------------------------

' * V1.05 instruction  "Accelerate GG speed to 12500 and set PT to 6000"
note  "Accelerate GG speed to 12500 and set PT to 6000"
note  "Stabilize the engine for 10 min."
set_channel Sol_Fuel_, 70.6
set_channel Tq_PT_, 10960
wait "n_GG > 12500", 30, 0.1, , , , SKIP, " n_GG is below 12500 rpm"
wait "n_PT > 6000", 30, 0.1, , , , SKIP, " n_PT is below 6000 rpm"
delay 30
do_fullset 5, "Perf Point: Speed3_Point1", "GG_Sp3_Pt1"

' * V1.05 instruction  "Increase PT speed to 8400"
note  "Increase PT speed to 8400"
note  "Stabilize the engine for 2 min."
set_channel Tq_PT_, 8990
wait "n_GG > 12500", 30, 0.1, , , , SKIP, " n_GG is below 12500 rpm"
wait "n_PT > 8400", 30, 0.1, , , , SKIP, " n_PT is below 8400 rpm"
delay 5
do_fullset 5, "Perf Point: Speed3_Point2", "GG_Sp3_Pt2"

' * V1.05 instruction  "Increase PT speed to 10800"
note  "Increase PT speed to 10800"
note  "Stabilize the engine for 2 min."
set_channel Tq_PT_, 7020
wait "n_GG > 12500", 30, 0.1, , , , SKIP, " n_GG is below 12500 rpm"
wait "n_PT > 10800", 30, 0.1, , , , SKIP, " n_PT is below 10800 rpm"
delay 5
do_fullset 5, "Perf Point: Speed3_Point3", "GG_Sp3_Pt3"

' * V1.05 instruction  "Increase PT speed to 11200"
note  "Increase PT speed to 11200"
note  "Stabilize the engine for 2 min."
set_channel Tq_PT_, 6690
wait "n_GG > 11500", 30, 0.1, , , , SKIP, " n_GG is below 12500 rpm"
wait "n_PT > 11200", 30, 0.1, , , , SKIP, " n_PT is below 11200 rpm"
delay 5
do_fullset 5, "Perf Point: Speed3_Point4", "GG_Sp3_Pt4"

' * V1.05 instruction  "Increase PT speed to 11500"
note  "Increase PT speed to 11500"
note  "Stabilize the engine for 2 min."
set_channel Tq_PT_, 6440
wait "n_GG > 11500", 30, 0.1, , , , SKIP, " n_GG is below 12500 rpm"
wait "n_PT > 11500", 30, 0.1, , , , SKIP, " n_PT is below 11500 rpm"
delay 5
do_fullset 5, "Perf Point: Speed3_Point5", "GG_Sp3_Pt5"

' * V1.05 instruction  "Decrease PT speed to 6000"
set_channel Tq_PT_, 11000
wait "n_PT < 6100", 30, 0.1, , , , SKIP, " n_PT is below 6000 rpm"
delay 5

' ---------------------------------------------

' * V1.05 instruction  "Accelerate GG speed to 12750 and set PT to 7200"
note  "Accelerate GG speed to 12750 and set PT to 7200"
note  "Stabilize the engine for 10 min."
set_channel Sol_Fuel_, 81.8
set_channel Tq_PT_, 11720
wait "n_GG > 12750", 30, 0.1, , , , SKIP, " n_GG is below 12750 rpm"
wait "n_PT > 7200", 30, 0.1, , , , SKIP, " n_PT is below 7200 rpm"
delay 30
do_fullset 5, "Perf Point: Speed4_Point1", "GG_Sp4_Pt1"

' * V1.05 instruction  "Increase PT speed to 9600"
note  "Increase PT speed to 9600"
note  "Stabilize the engine for 2 min."
set_channel Tq_PT_, 9660
wait "n_GG > 12750", 30, 0.1, , , , SKIP, " n_GG is below 12750 rpm"
wait "n_PT > 9600", 30, 0.1, , , , SKIP, " n_PT is below 9600 rpm"
delay 5
do_fullset 5, "Perf Point: Speed4_Point2", "GG_Sp4_Pt2"

' * V1.05 instruction  "Increase PT speed to 11200"
note  "Increase PT speed to 11200"
note  "Stabilize the engine for 2 min."
set_channel Tq_PT_, 8290
wait "n_GG > 12750", 30, 0.1, , , , SKIP, " n_GG is below 12750 rpm"
wait "n_PT > 11200", 30, 0.1, , , , SKIP, " n_PT is below 11200 rpm"
delay 5
do_fullset 5, "Perf Point: Speed4_Point3", "GG_Sp4_Pt3"

' * V1.05 instruction  "Decrease PT speed to 7200"
note  "Decrease PT speed to 7200"
set_channel Tq_PT_, 11720
wait "n_PT < 7300", 30, 0.1, , , , SKIP, " n_PT is below 6000 rpm"
delay 5

' -------------------------------------------

' * V1.05 instruction  "Accelerate GG speed to 13000 and set PT to 6000"
note  "Accelerate GG speed to 13000 and set PT to 6000"
note  "Stabilize the engine for 10 min."
set_channel Sol_Fuel_, 91.8
set_channel Tq_PT_, 13800
wait "n_GG > 13000", 30, 0.1, , , , SKIP, " n_GG is below 13000 rpm"
wait "n_PT > 6000", 30, 0.1, , , , SKIP, " n_PT is below 6000 rpm"
delay 30
do_fullset 5, "Perf Point: Speed5_Point1", "GG_Sp5_Pt1"

' * V1.05 instruction  "Increase PT speed to 8400"
note  "Increase PT speed to 8400"
note  "Stabilize the engine for 2 min."
set_channel Tq_PT_, 11570
wait "n_GG > 13000", 30, 0.1, , , , SKIP, " n_GG is below 13000 rpm"
wait "n_PT > 8400", 30, 0.1, , , , SKIP, " n_PT is below 8400 rpm"
delay 5
do_fullset 5, "Perf Point: Speed5_Point2", "GG_Sp5_Pt2"

' * V1.05 instruction  "Increase PT speed to 10800"
note  "Increase PT speed to 10800"
note  "Stabilize the engine for 2 min."
set_channel Tq_PT_, 9350
wait "n_GG > 13000", 30, 0.1, , , , SKIP, " n_GG is below 13000 rpm"
wait "n_PT > 10800", 30, 0.1, , , , SKIP, " n_PT is below 10800 rpm"
delay 5
do_fullset 5, "Perf Point: Speed5_Point3", "GG_Sp5_Pt3"

' * V1.05 instruction  "Increase PT speed to 11200"
note  "Increase PT speed to 11200"
note  "Stabilize the engine for 2 min."
set_channel Tq_PT_, 8970
wait "n_GG > 13000", 30, 0.1, , , , SKIP, " n_GG is below 13000 rpm"
wait "n_PT > 11200", 30, 0.1, , , , SKIP, " n_PT is below 11200 rpm"
delay 5
do_fullset 5, "Perf Point: Speed5_Point4", "GG_Sp5_Pt4"

' * V1.05 instruction  "Increase PT speed to 11500"
note  "Increase PT speed to 11500"
note  "Stabilize the engine for 2 min."
set_channel Tq_PT_, 8700
wait "n_GG > 13000", 30, 0.1, , , , SKIP, " n_GG is below 13000 rpm"
wait "n_PT > 11500", 30, 0.1, , , , SKIP, " n_PT is below 11500 rpm"
delay 5
do_fullset 5, "Perf Point: Speed5_Point5", "GG_Sp5_Pt5"

instruction  "Decrease PT speed to 6000"
set_channel Tq_PT_, 13800
wait "n_PT < 6100", 30, 0.1, , , , SKIP, " n_PT is below 6000 rpm"
delay 5

instruction "Continue with GG Test Max procedure"
