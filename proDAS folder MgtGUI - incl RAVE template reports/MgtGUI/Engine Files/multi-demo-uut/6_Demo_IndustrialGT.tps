Option Explicit

'* <script.tps>
'******************************************************************************
'*  AUTHOR: <Joachim Agou>
'*
'*  DESCRIPTION:
'*  <Demonstrate thermomodynamic test of an industrial Gas Turbine. Require RTD page.>
'*
'*  DATE: 12/24/2019
'*
'*  MODIFICATIONS:
'*    DATE         WHO  VERSION   DESCRIPTION
'*    ----------   ---  --------  ---------------------------------------------
'*    20191225     JOA  1.0       Initial version
'*    20200602     MSK  1.1       Added test steps for nxDAS demo
'******************************************************************************

'******************************************************************************
'************************* LOCAL VARIABLE DECLARATIONS ************************
'******************************************************************************

dim booFullset, booWarmUp, booStartTest, lvMechIntChk

channel "Sim_IndustrialGT_N_GG, Sim_IndustrialGT_N_PT, Sim_IndustrialGT_N_Generator, Sim_IndustrialGT_T_M, Sim_IndustrialGT_ZI_0404030, Sim_IndustrialGT_P_Baro, Sim_IndustrialGT_ME_0405690, Sim_IndustrialGT_PDT_2210, Sim_IndustrialGT_PDT_400X, Sim_IndustrialGT_TE_0404000_A, Sim_IndustrialGT_TE_0404000_B, Sim_IndustrialGT_PD_Inlet_A, Sim_IndustrialGT_PD_Inlet_B, Sim_IndustrialGT_PT_0404000, Sim_IndustrialGT_TE_0404900, Sim_IndustrialGT_PT_0404900, Sim_IndustrialGT_TE_040461X, Sim_IndustrialGT_PT_040460X, Sim_IndustrialGT_TE_0404650, Sim_IndustrialGT_PT_0404650, Sim_IndustrialGT_TT_040_2001, Sim_IndustrialGT_PT_040_2001, Sim_IndustrialGT_FT_040_2001, Sim_IndustrialGT_T_O_in, Sim_IndustrialGT_T_O_GG_fr_out, Sim_IndustrialGT_T_O_GG_re_out, Sim_IndustrialGT_T_O_PT_out, Sim_IndustrialGT_P_O_GG_fr, Sim_IndustrialGT_P_O_GG_re, Sim_IndustrialGT_P_O_PT, Sim_IndustrialGT_F_O_GG_fr, Sim_IndustrialGT_F_O_GG_re, Sim_IndustrialGT_F_O_PT, Sim_IndustrialGT_TE_0401110_A, Sim_IndustrialGT_TE_0401110_B, Sim_IndustrialGT_TE_0401120_A, Sim_IndustrialGT_TE_0401120_B, Sim_IndustrialGT_TE_0401130_A, Sim_IndustrialGT_TE_0401130_B, Sim_IndustrialGT_TE_0401140_A, Sim_IndustrialGT_TE_0401140_B, Sim_IndustrialGT_TE_0401310_A, Sim_IndustrialGT_TE_0401310_B, Sim_IndustrialGT_TE_0401320_A, Sim_IndustrialGT_TE_0401320_B, Sim_IndustrialGT_TE_0401330_A, Sim_IndustrialGT_TE_0401330_B, Sim_IndustrialGT_TE_0401340_A, Sim_IndustrialGT_TE_0401340_B, Sim_IndustrialGT_T_O_LG_in, Sim_IndustrialGT_T_O_LG_out, Sim_IndustrialGT_F_O_LG, Demo_IndustrialGT_GG_PT_Selector, Demo_IndustrialGT_GG_Target_ISO, Demo_IndustrialGT_PT_Target_ISO, Demo_IndustrialGT_GG_Target, Demo_IndustrialGT_PT_Target, Demo_IndustrialGT_N_GG_ISO, Demo_IndustrialGT_N_PT_ISO, Demo_IndustrialGT_Pow_ISO, Demo_IndustrialGT_Eta_ISO, Demo_IndustrialGT_T4_ISO, Demo_IndustrialGT_GG_PT_Status, Demo_IndustrialGT_Response "

'******************************************************************************
'******************************** PREREQUISITES *******************************
'******************************************************************************
note "Sample Test Run - Industrial Gas Turbine"
note " "
instruction "Confirm that the prerequisite test preparation steps have been carried out."
prompt_boo "The mechanical integrity and measurement instrumentation checks been completed successfuly.", lvMechIntChk
If lvMechIntChk = TRUE Then
result "Mechanical integrity and measurement preparation checks OK.", REPORT & "MechIntChk", GREEN
Else
result "Mechanical integrity and measurement preparation checks INCOMPLETE.", REPORT & "MechIntChk", RED
End If

instruction "Start a transient data recording."
start_log "Demo_Report", "Accel", "Demo industrial gas turbine sample test run."
result "Demo_Report transient recording started.", REPORT & "Log", BLACK

result "Setting simulated channel values.", REPORT, BLACK
set_channel Demo_IndustrialGT_Response, 0.1
set_channel Sim_IndustrialGT_N_GG, 11000
set_channel Sim_IndustrialGT_N_PT, 5500
set_channel Sim_IndustrialGT_N_Generator, 3816
set_channel Sim_IndustrialGT_T_M, 8000
set_channel Sim_IndustrialGT_ZI_0404030, 14
set_channel Sim_IndustrialGT_P_Baro, 1.0155
set_channel Sim_IndustrialGT_ME_0405690, 64
set_channel Sim_IndustrialGT_PDT_2210, -1.3
set_channel Sim_IndustrialGT_PDT_400X, 0.0272
set_channel Sim_IndustrialGT_TE_0404000_A, 21.6
set_channel Sim_IndustrialGT_TE_0404000_B, 21.4
set_channel Sim_IndustrialGT_PD_Inlet_A, -0.0047
set_channel Sim_IndustrialGT_PD_Inlet_B, -0.0052
set_channel Sim_IndustrialGT_PT_0404000, 0.00645
set_channel Sim_IndustrialGT_TE_0404900, 320.9
set_channel Sim_IndustrialGT_PT_0404900, 7.91
set_channel Sim_IndustrialGT_TE_040461X, 539.666666666667
set_channel Sim_IndustrialGT_PT_040460X, 1.1304
set_channel Sim_IndustrialGT_TE_0404650, 421.38125
set_channel Sim_IndustrialGT_PT_0404650, -0.00265
set_channel Sim_IndustrialGT_TT_040_2001, 20
set_channel Sim_IndustrialGT_PT_040_2001, 23
set_channel Sim_IndustrialGT_FT_040_2001, 1000
set_channel Sim_IndustrialGT_T_O_in, 41.6
set_channel Sim_IndustrialGT_T_O_GG_fr_out, 50.7
set_channel Sim_IndustrialGT_T_O_GG_re_out, 63
set_channel Sim_IndustrialGT_T_O_PT_out, 54.4
set_channel Sim_IndustrialGT_P_O_GG_fr, 2.3329
set_channel Sim_IndustrialGT_P_O_GG_re, 2.1272
set_channel Sim_IndustrialGT_P_O_PT, 2.0498
set_channel Sim_IndustrialGT_F_O_GG_fr, 233.5
set_channel Sim_IndustrialGT_F_O_GG_re, 49.9
set_channel Sim_IndustrialGT_F_O_PT, 181.7
set_channel Sim_IndustrialGT_TE_0401110_A, 79.2
set_channel Sim_IndustrialGT_TE_0401110_B, 81.9
set_channel Sim_IndustrialGT_TE_0401120_A, 63.6
set_channel Sim_IndustrialGT_TE_0401120_B, 63.2
set_channel Sim_IndustrialGT_TE_0401130_A, 61.8
set_channel Sim_IndustrialGT_TE_0401130_B, 61.3
set_channel Sim_IndustrialGT_TE_0401140_A, 56.3
set_channel Sim_IndustrialGT_TE_0401140_B, 57.3
set_channel Sim_IndustrialGT_TE_0401310_A, 50.7
set_channel Sim_IndustrialGT_TE_0401310_B, 52.1
set_channel Sim_IndustrialGT_TE_0401320_A, 58.7
set_channel Sim_IndustrialGT_TE_0401320_B, 56.9
set_channel Sim_IndustrialGT_TE_0401330_A, 49.3
set_channel Sim_IndustrialGT_TE_0401330_B, 48.8
set_channel Sim_IndustrialGT_TE_0401340_A, 51.7
set_channel Sim_IndustrialGT_TE_0401340_B, 50.9
set_channel Sim_IndustrialGT_T_O_LG_in, 41.9
set_channel Sim_IndustrialGT_T_O_LG_out, 46.9
set_channel Sim_IndustrialGT_F_O_LG, 287.4

instruction "Ensure that the Speed_Monitoring view page is available in a Real-Time Display window."
result "Speed monitoring operator display has been loaded.", REPORT & "RTD page", BLACK


instruction "Warm up the GG for 45 minutes."
set_channel Demo_IndustrialGT_GG_PT_Status, 24
result "Warm up sequence started.", REPORT & "Warm Up", BLACK
delay 5
result "Warm up COMPLETE.", REPORT & "Warm Up", GREEN
beep 1
set_channel Demo_IndustrialGT_GG_PT_Status, 25

'******************************************************************************
'************************************ GG1 *************************************
'******************************************************************************

instruction "Accelerate the test article and power turbine to the first test point."
'instruction "Accelerate the test article to" &cv_Demo_IndustrialGT_GG_Target_ISO &" rpm and the power turbine to" &cv_Demo_IndustrialGT_PT_Target_ISO &" rpm."
'note " ISO corrected GG speed target = " &cv_Demo_IndustrialGT_GG_Target &" rpm"
'note " ISO corrected PT speed target = " &cv_Demo_IndustrialGT_PT_Target &" rpm"
delay 1

'************************************ PT1 *************************************

set_channel Demo_IndustrialGT_GG_PT_Selector, 1
set_channel Demo_IndustrialGT_GG_PT_Status, 1
set_channel Demo_IndustrialGT_GG_Target_ISO, 11500
set_channel Demo_IndustrialGT_PT_Target_ISO, 6000

result "Moving to GG speed target = " &cv_Demo_IndustrialGT_GG_Target_ISO &" rpm", REPORT & "Set Point", BLACK
result "Moving to PT speed target = " &cv_Demo_IndustrialGT_PT_Target_ISO &" rpm", REPORT & "Set Point", BLACK

delay 2

set_channel Sim_IndustrialGT_N_GG, cv_Demo_IndustrialGT_GG_Target
set_channel Sim_IndustrialGT_N_PT, cv_Demo_IndustrialGT_PT_Target

set_channel Sim_IndustrialGT_N_GG, 11625
set_channel Sim_IndustrialGT_N_PT, 6065
set_channel Sim_IndustrialGT_N_Generator, 3816
set_channel Sim_IndustrialGT_T_M, 6165.1
set_channel Sim_IndustrialGT_ZI_0404030, 14.2
set_channel Sim_IndustrialGT_P_Baro, 1.0155
set_channel Sim_IndustrialGT_ME_0405690, 64.3
set_channel Sim_IndustrialGT_PDT_2210, -1.38
set_channel Sim_IndustrialGT_PDT_400X, 0.0272
set_channel Sim_IndustrialGT_TE_0404000_A, 21.6
set_channel Sim_IndustrialGT_TE_0404000_B, 21.4
set_channel Sim_IndustrialGT_PD_Inlet_A, -0.0047
set_channel Sim_IndustrialGT_PD_Inlet_B, -0.0052
set_channel Sim_IndustrialGT_PT_0404000, 0.00645
set_channel Sim_IndustrialGT_TE_0404900, 320.9
set_channel Sim_IndustrialGT_PT_0404900, 7.91
set_channel Sim_IndustrialGT_TE_040461X, 539.666666666667
set_channel Sim_IndustrialGT_PT_040460X, 1.1304
set_channel Sim_IndustrialGT_TE_0404650, 421.38125
set_channel Sim_IndustrialGT_PT_0404650, -0.00265
set_channel Sim_IndustrialGT_TT_040_2001, 20.7
set_channel Sim_IndustrialGT_PT_040_2001, 24.5578
set_channel Sim_IndustrialGT_FT_040_2001, 1192.1
set_channel Sim_IndustrialGT_T_O_in, 41.6
set_channel Sim_IndustrialGT_T_O_GG_fr_out, 50.7
set_channel Sim_IndustrialGT_T_O_GG_re_out, 63
set_channel Sim_IndustrialGT_T_O_PT_out, 54.4
set_channel Sim_IndustrialGT_P_O_GG_fr, 2.3329
set_channel Sim_IndustrialGT_P_O_GG_re, 2.1272
set_channel Sim_IndustrialGT_P_O_PT, 2.0498
set_channel Sim_IndustrialGT_F_O_GG_fr, 233.5
set_channel Sim_IndustrialGT_F_O_GG_re, 49.9
set_channel Sim_IndustrialGT_F_O_PT, 181.7
set_channel Sim_IndustrialGT_TE_0401110_A, 79.2
set_channel Sim_IndustrialGT_TE_0401110_B, 81.9
set_channel Sim_IndustrialGT_TE_0401120_A, 63.6
set_channel Sim_IndustrialGT_TE_0401120_B, 63.2
set_channel Sim_IndustrialGT_TE_0401130_A, 61.8
set_channel Sim_IndustrialGT_TE_0401130_B, 61.3
set_channel Sim_IndustrialGT_TE_0401140_A, 56.3
set_channel Sim_IndustrialGT_TE_0401140_B, 57.3
set_channel Sim_IndustrialGT_TE_0401310_A, 50.7
set_channel Sim_IndustrialGT_TE_0401310_B, 52.1
set_channel Sim_IndustrialGT_TE_0401320_A, 58.7
set_channel Sim_IndustrialGT_TE_0401320_B, 56.9
set_channel Sim_IndustrialGT_TE_0401330_A, 49.3
set_channel Sim_IndustrialGT_TE_0401330_B, 48.8
set_channel Sim_IndustrialGT_TE_0401340_A, 51.7
set_channel Sim_IndustrialGT_TE_0401340_B, 50.9
set_channel Sim_IndustrialGT_T_O_LG_in, 41.9
set_channel Sim_IndustrialGT_T_O_LG_out, 46.9
set_channel Sim_IndustrialGT_F_O_LG, 287.4

wait "Demo_IndustrialGT_N_GG_ISO = " &cv_Demo_IndustrialGT_GG_Target_ISO, 20, 20
wait "Demo_IndustrialGT_N_PT_ISO = " &cv_Demo_IndustrialGT_PT_Target_ISO, 20, 20
beep 1

result "First target point reached:"
result "GG speed is " &cv_Sim_IndustrialGT_N_GG &" rpm", REPORT & "Set Point", BLUE
result "PT speed is " &cv_Sim_IndustrialGT_N_PT &" rpm", REPORT & "Set Point", BLUE

instruction "Stabilize for 10 minutes at first target point."
set_channel Demo_IndustrialGT_GG_PT_Status, 21
delay 1
result "First target point stabilization completed.", REPORT & "Stabilization", GREEN
delay 1
instruction "Initiate target point performance recording."
set_channel Demo_IndustrialGT_GG_PT_Status, 22
delay 1
do_fullset 1, "Thermodynamic measurement: N_GG1 N_PT1", "GG1_PT1"
result "A steady-state measurement has been recorded:", REPORT & "Fullset", BLACK
result "     * GG speed ISO =" &fv_Demo_IndustrialGT_N_GG_ISO &" rpm", REPORT & "Fullset", BLUE
'result "         ** GG target offset =" &FormatNumber(fv_Demo_IndustrialGT_N_GG_ISO-fv_Demo_IndustrialGT_GG_Target_ISO,0) & " rpm", REPORT & "Fullset", RED
result "     * PT speed ISO =" &fv_Demo_IndustrialGT_N_PT_ISO &" rpm", REPORT & "Fullset", BLUE
'result "         ** PT target offset =" &FormatNumber(fv_Demo_IndustrialGT_N_PT_ISO-fv_Demo_IndustrialGT_PT_Target_ISO,0) & " rpm", REPORT & "Fullset", RED
result "     * Power ISO =" &fv_Demo_IndustrialGT_Pow_ISO &" kW", REPORT & "Fullset", BLUE
result "     * Efficiency ISO =" &fv_Demo_IndustrialGT_Eta_ISO &" %", REPORT & "Fullset", BLUE
result "     * T4 ISO =" &fv_Demo_IndustrialGT_T4_ISO &" degC", REPORT & "Fullset", BLUE
set_channel Demo_IndustrialGT_GG_PT_Status, 23
delay 1
'result "Thermodynamic measurement GG1_PT1 completed", REPORT & "Fullset", GREEN
result "Thermodynamic measurement at first target point completed.", REPORT & "Fullset", GREEN
result " ", REPORT
result " ", REPORT


'************************************ PT2 *************************************

instruction "Set the power turbine to the second PT test point."
delay 1

set_channel Demo_IndustrialGT_GG_PT_Selector, 2
set_channel Demo_IndustrialGT_GG_PT_Status, 2
set_channel Demo_IndustrialGT_GG_Target_ISO, 11500
set_channel Demo_IndustrialGT_PT_Target_ISO, 8400
do_fullset 0
result "Moving to PT speed target = " &cv_Demo_IndustrialGT_PT_Target_ISO &" rpm", REPORT & "Set Point", BLACK
delay 2

set_channel Sim_IndustrialGT_N_GG, cv_Demo_IndustrialGT_GG_Target
set_channel Sim_IndustrialGT_N_PT, cv_Demo_IndustrialGT_PT_Target

set_channel Sim_IndustrialGT_N_GG, 11626
set_channel Sim_IndustrialGT_N_PT, 8506
set_channel Sim_IndustrialGT_N_Generator, 5353
set_channel Sim_IndustrialGT_T_M, 4583.9
set_channel Sim_IndustrialGT_ZI_0404030, 14.2
set_channel Sim_IndustrialGT_P_Baro, 1.0155
set_channel Sim_IndustrialGT_ME_0405690, 62.7
set_channel Sim_IndustrialGT_PDT_2210, -1.38
set_channel Sim_IndustrialGT_PDT_400X, 0.0274
set_channel Sim_IndustrialGT_TE_0404000_A, 21.7
set_channel Sim_IndustrialGT_TE_0404000_B, 21.5
set_channel Sim_IndustrialGT_PD_Inlet_A, -0.0047
set_channel Sim_IndustrialGT_PD_Inlet_B, -0.0052
set_channel Sim_IndustrialGT_PT_0404000, 0.00645
set_channel Sim_IndustrialGT_TE_0404900, 321.85
set_channel Sim_IndustrialGT_PT_0404900, 7.93115
set_channel Sim_IndustrialGT_TE_040461X, 544.85
set_channel Sim_IndustrialGT_PT_040460X, 1.1457
set_channel Sim_IndustrialGT_TE_0404650, 418.35
set_channel Sim_IndustrialGT_PT_0404650, -0.00315
set_channel Sim_IndustrialGT_TT_040_2001, 20.8
set_channel Sim_IndustrialGT_PT_040_2001, 24.544
set_channel Sim_IndustrialGT_FT_040_2001, 1202.8
set_channel Sim_IndustrialGT_T_O_in, 42.1
set_channel Sim_IndustrialGT_T_O_GG_fr_out, 51.2
set_channel Sim_IndustrialGT_T_O_GG_re_out, 63.8
set_channel Sim_IndustrialGT_T_O_PT_out, 58.4
set_channel Sim_IndustrialGT_P_O_GG_fr, 2.3083
set_channel Sim_IndustrialGT_P_O_GG_re, 2.1066
set_channel Sim_IndustrialGT_P_O_PT, 2.0301
set_channel Sim_IndustrialGT_F_O_GG_fr, 232.6
set_channel Sim_IndustrialGT_F_O_GG_re, 49.7
set_channel Sim_IndustrialGT_F_O_PT, 180.7
set_channel Sim_IndustrialGT_TE_0401110_A, 79.6
set_channel Sim_IndustrialGT_TE_0401110_B, 82.3
set_channel Sim_IndustrialGT_TE_0401120_A, 64.1
set_channel Sim_IndustrialGT_TE_0401120_B, 63.7
set_channel Sim_IndustrialGT_TE_0401130_A, 62.4
set_channel Sim_IndustrialGT_TE_0401130_B, 61.8
set_channel Sim_IndustrialGT_TE_0401140_A, 56.9
set_channel Sim_IndustrialGT_TE_0401140_B, 57.9
set_channel Sim_IndustrialGT_TE_0401310_A, 54.3
set_channel Sim_IndustrialGT_TE_0401310_B, 56
set_channel Sim_IndustrialGT_TE_0401320_A, 64.9
set_channel Sim_IndustrialGT_TE_0401320_B, 62.7
set_channel Sim_IndustrialGT_TE_0401330_A, 54.2
set_channel Sim_IndustrialGT_TE_0401330_B, 53.5
set_channel Sim_IndustrialGT_TE_0401340_A, 54.7
set_channel Sim_IndustrialGT_TE_0401340_B, 53.8
set_channel Sim_IndustrialGT_T_O_LG_in, 42.4
set_channel Sim_IndustrialGT_T_O_LG_out, 50.1
set_channel Sim_IndustrialGT_F_O_LG, 294.4

wait "Demo_IndustrialGT_N_GG_ISO = " &cv_Demo_IndustrialGT_GG_Target_ISO, 20, 20
wait "Demo_IndustrialGT_N_PT_ISO = " &cv_Demo_IndustrialGT_PT_Target_ISO, 20, 20

result "Second PT target point reached:"
result "GG speed is " &cv_Sim_IndustrialGT_N_GG &" rpm", REPORT & "Set Point", BLUE
result "PT speed is " &cv_Sim_IndustrialGT_N_PT &" rpm", REPORT & "Set Point", BLUE

instruction "Stabilize for 10 minutes."
set_channel Demo_IndustrialGT_GG_PT_Status, 21
delay 1
result "Target point stabilization completed.", REPORT & "Stabilization", GREEN
delay 1
instruction "Initiate target point performance recording."
set_channel Demo_IndustrialGT_GG_PT_Status, 22
delay 1
do_fullset 1, "Thermodynamic measurement: N_GG1 N_PT2", "GG1_PT2"
result "A steady-state measurement has been recorded:", REPORT & "Fullset", BLACK
result "     * GG speed ISO =" &fv_Demo_IndustrialGT_N_GG_ISO &" rpm", REPORT & "Fullset", BLUE
'result "         ** GG target offset =" &FormatNumber(fv_Demo_IndustrialGT_N_GG_ISO-fv_Demo_IndustrialGT_GG_Target_ISO,0) & " rpm", REPORT & "Fullset", RED
result "     * PT speed ISO =" &fv_Demo_IndustrialGT_N_PT_ISO &" rpm", REPORT & "Fullset", BLUE
'result "         ** PT target offset =" &FormatNumber(fv_Demo_IndustrialGT_N_PT_ISO-fv_Demo_IndustrialGT_PT_Target_ISO,0) & " rpm", REPORT & "Fullset", RED
result "     * Power ISO =" &fv_Demo_IndustrialGT_Pow_ISO &" kW", REPORT & "Fullset", BLUE
result "     * Efficiency ISO =" &fv_Demo_IndustrialGT_Eta_ISO &" %", REPORT & "Fullset", BLUE
result "     * T4 ISO =" &fv_Demo_IndustrialGT_T4_ISO &" degC", REPORT & "Fullset", BLUE
set_channel Demo_IndustrialGT_GG_PT_Status, 23
delay 1
result "Thermodynamic measurement at second PT point completed.", REPORT & "Fullset", GREEN
result " ", REPORT
result " ", REPORT
beep 1

'************************************ PT3 *************************************

note "Going to GG1_PT3"

set_channel Demo_IndustrialGT_GG_PT_Selector, 3
set_channel Demo_IndustrialGT_GG_PT_Status, 3

set_channel Demo_IndustrialGT_GG_Target_ISO, 11500
set_channel Demo_IndustrialGT_PT_Target_ISO, 10800
do_fullset 0
result "Going to GG speed ISO target = " &cv_Demo_IndustrialGT_GG_Target_ISO &" rpm and PT speed ISO target = " &cv_Demo_IndustrialGT_PT_Target_ISO &" rpm", REPORT & "Set Point", BLACK
delay 2

result "     * Estimated GG speed target = " &cv_Demo_IndustrialGT_GG_Target &" rpm", REPORT & "Set Point", BLUE
result "     * Estimated PT speed target = " &cv_Demo_IndustrialGT_PT_Target &" rpm", REPORT & "Set Point", BLUE
set_channel Sim_IndustrialGT_N_GG, cv_Demo_IndustrialGT_GG_Target
set_channel Sim_IndustrialGT_N_PT, cv_Demo_IndustrialGT_PT_Target

set_channel Sim_IndustrialGT_N_GG, 11625
set_channel Sim_IndustrialGT_N_PT, 10933
set_channel Sim_IndustrialGT_N_Generator, 6883
set_channel Sim_IndustrialGT_T_M, 3099.7
set_channel Sim_IndustrialGT_ZI_0404030, 14.2
set_channel Sim_IndustrialGT_P_Baro, 1.0155
set_channel Sim_IndustrialGT_ME_0405690, 61.5
set_channel Sim_IndustrialGT_PDT_2210, -1.38
set_channel Sim_IndustrialGT_PDT_400X, 0.0273

set_channel Sim_IndustrialGT_TE_0404000_A, 22
set_channel Sim_IndustrialGT_TE_0404000_B, 21.7
set_channel Sim_IndustrialGT_PD_Inlet_A, -0.0047
set_channel Sim_IndustrialGT_PD_Inlet_B, -0.0052
set_channel Sim_IndustrialGT_PT_0404000, 0.00645
set_channel Sim_IndustrialGT_TE_0404900, 321.05
set_channel Sim_IndustrialGT_PT_0404900, 7.8689
set_channel Sim_IndustrialGT_TE_040461X, 533.366666666667
set_channel Sim_IndustrialGT_PT_040460X, 1.10925
set_channel Sim_IndustrialGT_TE_0404650, 416.1375
set_channel Sim_IndustrialGT_PT_0404650, -0.00295
set_channel Sim_IndustrialGT_TT_040_2001, 21.1
set_channel Sim_IndustrialGT_PT_040_2001, 24.5554
set_channel Sim_IndustrialGT_FT_040_2001, 1178.7
set_channel Sim_IndustrialGT_T_O_in, 43.4
set_channel Sim_IndustrialGT_T_O_GG_fr_out, 52.1
set_channel Sim_IndustrialGT_T_O_GG_re_out, 64.8
set_channel Sim_IndustrialGT_T_O_PT_out, 64
set_channel Sim_IndustrialGT_P_O_GG_fr, 2.2695
set_channel Sim_IndustrialGT_P_O_GG_re, 2.0804
set_channel Sim_IndustrialGT_P_O_PT, 2.0007
set_channel Sim_IndustrialGT_F_O_GG_fr, 231.6
set_channel Sim_IndustrialGT_F_O_GG_re, 49.4
set_channel Sim_IndustrialGT_F_O_PT, 179.9

set_channel Sim_IndustrialGT_TE_0401110_A, 80.2
set_channel Sim_IndustrialGT_TE_0401110_B, 82.9
set_channel Sim_IndustrialGT_TE_0401120_A, 65
set_channel Sim_IndustrialGT_TE_0401120_B, 64.6
set_channel Sim_IndustrialGT_TE_0401130_A, 63.4
set_channel Sim_IndustrialGT_TE_0401130_B, 62.8
set_channel Sim_IndustrialGT_TE_0401140_A, 57.9
set_channel Sim_IndustrialGT_TE_0401140_B, 58.9
set_channel Sim_IndustrialGT_TE_0401310_A, 59.6
set_channel Sim_IndustrialGT_TE_0401310_B, 61.6
set_channel Sim_IndustrialGT_TE_0401320_A, 73
set_channel Sim_IndustrialGT_TE_0401320_B, 70.6
set_channel Sim_IndustrialGT_TE_0401330_A, 62.1
set_channel Sim_IndustrialGT_TE_0401330_B, 60.4
set_channel Sim_IndustrialGT_TE_0401340_A, 58.4
set_channel Sim_IndustrialGT_TE_0401340_B, 57.7

set_channel Sim_IndustrialGT_T_O_LG_in, 43.8
set_channel Sim_IndustrialGT_T_O_LG_out, 55.5
set_channel Sim_IndustrialGT_F_O_LG, 300.3

wait "Demo_IndustrialGT_N_GG_ISO = " &cv_Demo_IndustrialGT_GG_Target_ISO, 20, 20
wait "Demo_IndustrialGT_N_PT_ISO = " &cv_Demo_IndustrialGT_PT_Target_ISO, 20, 20

'delay 16
beep 1

set_channel Demo_IndustrialGT_GG_PT_Status, 21
result "Stabilizing - minimum 5 minutes", REPORT & "Stabilization", BLACK
delay 3
result "Stabilization completed", REPORT & "Stabilization", GREEN
delay 1

set_channel Demo_IndustrialGT_GG_PT_Status, 22
delay 1
do_fullset 1, "Thermodynamic measurement: N_GG1 N_PT3", "GG1_PT3"
result "A steady-state measurement has been taken automatically", REPORT & "Fullset", BLACK
result "     * GG speed ISO =" &fv_Demo_IndustrialGT_N_GG_ISO &" rpm", REPORT & "Fullset", BLUE
'result "         ** GG target offset =" &FormatNumber(fv_Demo_IndustrialGT_N_GG_ISO-fv_Demo_IndustrialGT_GG_Target_ISO,0) & " rpm", REPORT & "Fullset", RED
result "     * PT speed ISO =" &fv_Demo_IndustrialGT_N_PT_ISO &" rpm", REPORT & "Fullset", BLUE
'result "         ** PT target offset =" &FormatNumber(fv_Demo_IndustrialGT_N_PT_ISO-fv_Demo_IndustrialGT_PT_Target_ISO,0) & " rpm", REPORT & "Fullset", RED
result "     * Power ISO =" &fv_Demo_IndustrialGT_Pow_ISO &" kW", REPORT & "Fullset", BLUE
result "     * Efficiency ISO =" &fv_Demo_IndustrialGT_Eta_ISO &" %", REPORT & "Fullset", BLUE
result "     * T4 ISO =" &fv_Demo_IndustrialGT_T4_ISO &" degC", REPORT & "Fullset", BLUE
set_channel Demo_IndustrialGT_GG_PT_Status, 23
delay 1
result "Thermodynamic measurement GG1_PT3 completed", REPORT & "Fullset", GREEN
result " ", REPORT
result " ", REPORT

set_channel Demo_IndustrialGT_Response, 0.06

'************************************ PT4 *************************************

note "Going to GG1_PT4"

set_channel Demo_IndustrialGT_GG_PT_Selector, 4
set_channel Demo_IndustrialGT_GG_PT_Status, 4

set_channel Demo_IndustrialGT_GG_Target_ISO, 11500
set_channel Demo_IndustrialGT_PT_Target_ISO, 12000
do_fullset 0
result "Going to GG speed ISO target = " &cv_Demo_IndustrialGT_GG_Target_ISO &" rpm and PT speed ISO target = " &cv_Demo_IndustrialGT_PT_Target_ISO &" rpm", REPORT & "Set Point", BLACK
delay 2


result "     * Estimated GG speed target = " &cv_Demo_IndustrialGT_GG_Target &" rpm", REPORT & "Set Point", BLUE
result "     * Estimated PT speed target = " &cv_Demo_IndustrialGT_PT_Target &" rpm", REPORT & "Set Point", BLUE
set_channel Sim_IndustrialGT_N_GG, cv_Demo_IndustrialGT_GG_Target
set_channel Sim_IndustrialGT_N_PT, cv_Demo_IndustrialGT_PT_Target


set_channel Sim_IndustrialGT_N_GG, 11626
set_channel Sim_IndustrialGT_N_PT, 12153
set_channel Sim_IndustrialGT_N_Generator, 7653
set_channel Sim_IndustrialGT_T_M, 2370.5
set_channel Sim_IndustrialGT_ZI_0404030, 14.2
set_channel Sim_IndustrialGT_P_Baro, 1.0155
set_channel Sim_IndustrialGT_ME_0405690, 61.5
set_channel Sim_IndustrialGT_PDT_2210, -1.39
set_channel Sim_IndustrialGT_PDT_400X, 0.0273

set_channel Sim_IndustrialGT_TE_0404000_A, 22
set_channel Sim_IndustrialGT_TE_0404000_B, 21.7
set_channel Sim_IndustrialGT_PD_Inlet_A, -0.0046
set_channel Sim_IndustrialGT_PD_Inlet_B, -0.0051
set_channel Sim_IndustrialGT_PT_0404000, 0.00635
set_channel Sim_IndustrialGT_TE_0404900, 320.5
set_channel Sim_IndustrialGT_PT_0404900, 7.83225
set_channel Sim_IndustrialGT_TE_040461X, 522.491666666667
set_channel Sim_IndustrialGT_PT_040460X, 1.0751
set_channel Sim_IndustrialGT_TE_0404650, 417.4
set_channel Sim_IndustrialGT_PT_0404650, -0.0029
set_channel Sim_IndustrialGT_TT_040_2001, 21.2
set_channel Sim_IndustrialGT_PT_040_2001, 24.5762
set_channel Sim_IndustrialGT_FT_040_2001, 1152.5
set_channel Sim_IndustrialGT_T_O_in, 44.5
set_channel Sim_IndustrialGT_T_O_GG_fr_out, 53.1
set_channel Sim_IndustrialGT_T_O_GG_re_out, 65.8
set_channel Sim_IndustrialGT_T_O_PT_out, 67.2
set_channel Sim_IndustrialGT_P_O_GG_fr, 2.2535
set_channel Sim_IndustrialGT_P_O_GG_re, 2.0718
set_channel Sim_IndustrialGT_P_O_PT, 1.9904
set_channel Sim_IndustrialGT_F_O_GG_fr, 231.6
set_channel Sim_IndustrialGT_F_O_GG_re, 49.4
set_channel Sim_IndustrialGT_F_O_PT, 180.1

set_channel Sim_IndustrialGT_TE_0401110_A, 80.6
set_channel Sim_IndustrialGT_TE_0401110_B, 83.3
set_channel Sim_IndustrialGT_TE_0401120_A, 65.8
set_channel Sim_IndustrialGT_TE_0401120_B, 65.4
set_channel Sim_IndustrialGT_TE_0401130_A, 64.4
set_channel Sim_IndustrialGT_TE_0401130_B, 63.7
set_channel Sim_IndustrialGT_TE_0401140_A, 58.8
set_channel Sim_IndustrialGT_TE_0401140_B, 60
set_channel Sim_IndustrialGT_TE_0401310_A, 62.9
set_channel Sim_IndustrialGT_TE_0401310_B, 65
set_channel Sim_IndustrialGT_TE_0401320_A, 77
set_channel Sim_IndustrialGT_TE_0401320_B, 74
set_channel Sim_IndustrialGT_TE_0401330_A, 66.5
set_channel Sim_IndustrialGT_TE_0401330_B, 64.3
set_channel Sim_IndustrialGT_TE_0401340_A, 61.2
set_channel Sim_IndustrialGT_TE_0401340_B, 61.5

set_channel Sim_IndustrialGT_T_O_LG_in, 44.9
set_channel Sim_IndustrialGT_T_O_LG_out, 58.5
set_channel Sim_IndustrialGT_F_O_LG, 303.7

wait "Demo_IndustrialGT_N_GG_ISO = " &cv_Demo_IndustrialGT_GG_Target_ISO, 20, 20
wait "Demo_IndustrialGT_N_PT_ISO = " &cv_Demo_IndustrialGT_PT_Target_ISO, 20, 20


'delay 14
beep 1

set_channel Demo_IndustrialGT_GG_PT_Status, 21
result "Stabilizing - Minimum 5 minutes ...", REPORT & "Stabilization", BLACK
'delay 3
result "Stabilization completed", REPORT & "Stabilization", GREEN
'delay 1

set_channel Demo_IndustrialGT_GG_PT_Status, 22
'delay 1
do_fullset 1, "Thermodynamic measurement: N_GG1 N_PT4", "GG1_PT4"
result "A steady-state measurement has been taken automatically", REPORT & "Fullset", BLACK
result "     * GG speed ISO =" &fv_Demo_IndustrialGT_N_GG_ISO &" rpm", REPORT & "Fullset", BLUE
'result "         ** GG target offset =" &FormatNumber(fv_Demo_IndustrialGT_N_GG_ISO-fv_Demo_IndustrialGT_GG_Target_ISO,0) & " rpm", REPORT & "Fullset", RED
result "     * PT speed ISO =" &fv_Demo_IndustrialGT_N_PT_ISO &" rpm", REPORT & "Fullset", BLUE
'result "         ** PT target offset =" &FormatNumber(fv_Demo_IndustrialGT_N_PT_ISO-fv_Demo_IndustrialGT_PT_Target_ISO,0) & " rpm", REPORT & "Fullset", RED
result "     * Power ISO =" &fv_Demo_IndustrialGT_Pow_ISO &" kW", REPORT & "Fullset", BLUE
result "     * Efficiency ISO =" &fv_Demo_IndustrialGT_Eta_ISO &" %", REPORT & "Fullset", BLUE
result "     * T4 ISO =" &fv_Demo_IndustrialGT_T4_ISO &" degC", REPORT & "Fullset", BLUE
set_channel Demo_IndustrialGT_GG_PT_Status, 23
delay 1
result "Thermodynamic measurement GG1_PT4 completed", REPORT & "Fullset", GREEN
result " ", REPORT
result " ", REPORT
result " *** All GG1 measurements have been completed ***", REPORT & "Fullset", GREEN
result " ", REPORT
result " ", REPORT



'******************************************************************************
'************************************ GG2 *************************************
'******************************************************************************

instruction "GG2"



'************************************ PT1 *************************************

note "Going to GG2_PT1"

note "Setting new targets and displaying status on the RTD page."
	set_channel Demo_IndustrialGT_GG_PT_Selector, 5
	set_channel Demo_IndustrialGT_GG_PT_Status, 5
	set_channel Demo_IndustrialGT_GG_Target_ISO, 12000
	set_channel Demo_IndustrialGT_PT_Target_ISO, 7200
	do_fullset 0

result "Going to GG speed ISO target = " &cv_Demo_IndustrialGT_GG_Target_ISO &" rpm and PT speed ISO target = " &cv_Demo_IndustrialGT_PT_Target_ISO &" rpm", REPORT & "Set Point", BLACK
delay 2


result "     * Estimated GG speed target = " &cv_Demo_IndustrialGT_GG_Target &" rpm", REPORT & "Set Point", BLUE
result "     * Estimated PT speed target = " &cv_Demo_IndustrialGT_PT_Target &" rpm", REPORT & "Set Point", BLUE
set_channel Sim_IndustrialGT_N_GG, cv_Demo_IndustrialGT_GG_Target
set_channel Sim_IndustrialGT_N_PT, cv_Demo_IndustrialGT_PT_Target


set_channel Sim_IndustrialGT_N_GG, 12150
set_channel Sim_IndustrialGT_N_PT, 7308
set_channel Sim_IndustrialGT_N_Generator, 4599
set_channel Sim_IndustrialGT_T_M, 7102.5
set_channel Sim_IndustrialGT_ZI_0404030, 9.9
set_channel Sim_IndustrialGT_P_Baro, 1.0153
set_channel Sim_IndustrialGT_ME_0405690, 60.4
set_channel Sim_IndustrialGT_PDT_2210, -1.62
set_channel Sim_IndustrialGT_PDT_400X, 0.0344

set_channel Sim_IndustrialGT_TE_0404000_A, 22.7
set_channel Sim_IndustrialGT_TE_0404000_B, 22.5
set_channel Sim_IndustrialGT_PD_Inlet_A, -0.0058
set_channel Sim_IndustrialGT_PD_Inlet_B, -0.0064
set_channel Sim_IndustrialGT_PT_0404000, 0.00795
set_channel Sim_IndustrialGT_TE_0404900, 347.65
set_channel Sim_IndustrialGT_PT_0404900, 9.28665
set_channel Sim_IndustrialGT_TE_040461X, 579.133333333333
set_channel Sim_IndustrialGT_PT_040460X, 1.3923
set_channel Sim_IndustrialGT_TE_0404650, 434.825
set_channel Sim_IndustrialGT_PT_0404650, -0.0031
set_channel Sim_IndustrialGT_TT_040_2001, 23.9
set_channel Sim_IndustrialGT_PT_040_2001, 24.475
set_channel Sim_IndustrialGT_FT_040_2001, 1440.9
set_channel Sim_IndustrialGT_T_O_in, 45.5
set_channel Sim_IndustrialGT_T_O_GG_fr_out, 55.2
set_channel Sim_IndustrialGT_T_O_GG_re_out, 69.6
set_channel Sim_IndustrialGT_T_O_PT_out, 60.8
set_channel Sim_IndustrialGT_P_O_GG_fr, 2.2759
set_channel Sim_IndustrialGT_P_O_GG_re, 2.1091
set_channel Sim_IndustrialGT_P_O_PT, 2.0144
set_channel Sim_IndustrialGT_F_O_GG_fr, 233.3
set_channel Sim_IndustrialGT_F_O_GG_re, 49.5
set_channel Sim_IndustrialGT_F_O_PT, 181.3

set_channel Sim_IndustrialGT_TE_0401110_A, 82
set_channel Sim_IndustrialGT_TE_0401110_B, 84.8
set_channel Sim_IndustrialGT_TE_0401120_A, 67.5
set_channel Sim_IndustrialGT_TE_0401120_B, 67.2
set_channel Sim_IndustrialGT_TE_0401130_A, 66.6
set_channel Sim_IndustrialGT_TE_0401130_B, 65.9
set_channel Sim_IndustrialGT_TE_0401140_A, 60.6
set_channel Sim_IndustrialGT_TE_0401140_B, 62.1
set_channel Sim_IndustrialGT_TE_0401310_A, 55.8
set_channel Sim_IndustrialGT_TE_0401310_B, 57.1
set_channel Sim_IndustrialGT_TE_0401320_A, 64.6
set_channel Sim_IndustrialGT_TE_0401320_B, 62.7
set_channel Sim_IndustrialGT_TE_0401330_A, 55.3
set_channel Sim_IndustrialGT_TE_0401330_B, 54.5
set_channel Sim_IndustrialGT_TE_0401340_A, 57.1
set_channel Sim_IndustrialGT_TE_0401340_B, 56.4

set_channel Sim_IndustrialGT_T_O_LG_in, 45.7
set_channel Sim_IndustrialGT_T_O_LG_out, 52.7
set_channel Sim_IndustrialGT_F_O_LG, 293.2

wait "Demo_IndustrialGT_N_GG_ISO = " &cv_Demo_IndustrialGT_GG_Target_ISO, 20, 20
wait "Demo_IndustrialGT_N_PT_ISO = " &cv_Demo_IndustrialGT_PT_Target_ISO, 20, 20


'delay 14
beep 1

set_channel Demo_IndustrialGT_GG_PT_Status, 21
result "Stabilizing - Minimum 10 minutes", REPORT & "Stabilization", BLACK
delay 1
result "Stabilization completed", REPORT & "Stabilization", GREEN

set_channel Demo_IndustrialGT_GG_PT_Status, 22
do_fullset 1, "Thermodynamic measurement: N_GG2 N_PT1", "GG2_PT1"
result "A steady-state measurement has been taken automatically", REPORT & "Fullset", BLACK
result "     * GG speed ISO =" &fv_Demo_IndustrialGT_N_GG_ISO &" rpm", REPORT & "Fullset", BLUE
'result "         ** GG target offset =" &FormatNumber(fv_Demo_IndustrialGT_N_GG_ISO-fv_Demo_IndustrialGT_GG_Target_ISO,0) & " rpm", REPORT & "Fullset", RED
result "     * GPT speed ISO =" &fv_Demo_IndustrialGT_N_PT_ISO &" rpm", REPORT & "Fullset", BLUE
'result "         ** PT target offset =" &FormatNumber(fv_Demo_IndustrialGT_N_PT_ISO-fv_Demo_IndustrialGT_PT_Target_ISO,0) & " rpm", REPORT & "Fullset", RED
result "     * Power ISO =" &fv_Demo_IndustrialGT_Pow_ISO &" kW", REPORT & "Fullset", BLUE
result "     * Efficiency ISO =" &fv_Demo_IndustrialGT_Eta_ISO &" %", REPORT & "Fullset", BLUE
result "     * T4 ISO =" &fv_Demo_IndustrialGT_T4_ISO &" degC", REPORT & "Fullset", BLUE
set_channel Demo_IndustrialGT_GG_PT_Status, 23
'delay 1
result "Thermodynamic measurement GG2_PT1 completed", REPORT & "Fullset", GREEN
result " ", REPORT
result " ", REPORT



set_channel Demo_IndustrialGT_Response, 0.09



'************************************ PT2 *************************************

note "Going to GG2_PT2"

note "Setting new targets and displaying status on the RTD page."
	set_channel Demo_IndustrialGT_GG_PT_Selector, 6
	set_channel Demo_IndustrialGT_GG_PT_Status, 6
	set_channel Demo_IndustrialGT_GG_Target_ISO, 12000
	set_channel Demo_IndustrialGT_PT_Target_ISO, 9600
	do_fullset 0

note "Estimating GG and PT speeds to reach the ISO target speeds."
	result "Going to GG speed ISO target = " &cv_Demo_IndustrialGT_GG_Target_ISO &" rpm", REPORT & "Set Point", BLACK
	result "     * Estimated GG speed target = " &cv_Demo_IndustrialGT_GG_Target &" rpm", REPORT & "Set Point", BLUE
	result "Going to PT speed ISO target = " &cv_Demo_IndustrialGT_PT_Target_ISO &" rpm", REPORT & "Set Point", BLACK
	result "     * Estimated PT speed target = " &cv_Demo_IndustrialGT_PT_Target &" rpm", REPORT & "Set Point", BLUE
	delay 5

note "Injecting simulated values."
	set_channel Sim_IndustrialGT_N_GG, cv_Demo_IndustrialGT_GG_Target
	set_channel Sim_IndustrialGT_N_PT, cv_Demo_IndustrialGT_PT_Target

	set_channel Sim_IndustrialGT_N_GG, 12150
	set_channel Sim_IndustrialGT_N_PT, 9752
	set_channel Sim_IndustrialGT_N_Generator, 6139
	set_channel Sim_IndustrialGT_T_M, 5405.4
	set_channel Sim_IndustrialGT_ZI_0404030, 10
	set_channel Sim_IndustrialGT_P_Baro, 1.0153
	set_channel Sim_IndustrialGT_ME_0405690, 55.8
	set_channel Sim_IndustrialGT_PDT_2210, -1.63
	set_channel Sim_IndustrialGT_PDT_400X, 0.0344

	set_channel Sim_IndustrialGT_TE_0404000_A, 23
	set_channel Sim_IndustrialGT_TE_0404000_B, 22.7
	set_channel Sim_IndustrialGT_PD_Inlet_A, -0.0058
	set_channel Sim_IndustrialGT_PD_Inlet_B, -0.0063
	set_channel Sim_IndustrialGT_PT_0404000, 0.00785
	set_channel Sim_IndustrialGT_TE_0404900, 348.7
	set_channel Sim_IndustrialGT_PT_0404900, 9.31455
	set_channel Sim_IndustrialGT_TE_040461X, 582.65
	set_channel Sim_IndustrialGT_PT_040460X, 1.4081
	set_channel Sim_IndustrialGT_TE_0404650, 433.76875
	set_channel Sim_IndustrialGT_PT_0404650, -0.0036
	set_channel Sim_IndustrialGT_TT_040_2001, 24.3
	set_channel Sim_IndustrialGT_PT_040_2001, 24.465
	set_channel Sim_IndustrialGT_FT_040_2001, 1452.6
	set_channel Sim_IndustrialGT_T_O_in, 45.6
	set_channel Sim_IndustrialGT_T_O_GG_fr_out, 55.3
	set_channel Sim_IndustrialGT_T_O_GG_re_out, 69.8
	set_channel Sim_IndustrialGT_T_O_PT_out, 64.9
	set_channel Sim_IndustrialGT_P_O_GG_fr, 2.2532
	set_channel Sim_IndustrialGT_P_O_GG_re, 2.0883
	set_channel Sim_IndustrialGT_P_O_PT, 1.9946
	set_channel Sim_IndustrialGT_F_O_GG_fr, 232
	set_channel Sim_IndustrialGT_F_O_GG_re, 49.2
	set_channel Sim_IndustrialGT_F_O_PT, 180.2

	set_channel Sim_IndustrialGT_TE_0401110_A, 82
	set_channel Sim_IndustrialGT_TE_0401110_B, 84.8
	set_channel Sim_IndustrialGT_TE_0401120_A, 67.6
	set_channel Sim_IndustrialGT_TE_0401120_B, 67.4
	set_channel Sim_IndustrialGT_TE_0401130_A, 66.7
	set_channel Sim_IndustrialGT_TE_0401130_B, 66
	set_channel Sim_IndustrialGT_TE_0401140_A, 60.7
	set_channel Sim_IndustrialGT_TE_0401140_B, 62.2
	set_channel Sim_IndustrialGT_TE_0401310_A, 59.3
	set_channel Sim_IndustrialGT_TE_0401310_B, 60.9
	set_channel Sim_IndustrialGT_TE_0401320_A, 70.3
	set_channel Sim_IndustrialGT_TE_0401320_B, 67.8
	set_channel Sim_IndustrialGT_TE_0401330_A, 60.9
	set_channel Sim_IndustrialGT_TE_0401330_B, 59.4
	set_channel Sim_IndustrialGT_TE_0401340_A, 59.6
	set_channel Sim_IndustrialGT_TE_0401340_B, 59

	set_channel Sim_IndustrialGT_T_O_LG_in, 45.8
	set_channel Sim_IndustrialGT_T_O_LG_out, 56
	set_channel Sim_IndustrialGT_F_O_LG, 298.6

	wait "Demo_IndustrialGT_N_GG_ISO = " &cv_Demo_IndustrialGT_GG_Target_ISO, 20, 20
	wait "Demo_IndustrialGT_N_PT_ISO = " &cv_Demo_IndustrialGT_PT_Target_ISO, 20, 20
	beep 1

'note "Stabilizing ..."
	set_channel Demo_IndustrialGT_GG_PT_Status, 21
	result "Stabilizing - Minimum 5 minutes", REPORT & "Stabilization", BLACK
	delay 5
	result "Stabilization completed", REPORT & "Stabilization", GREEN
	delay 1

'note "recording a measurement ..."
	set_channel Demo_IndustrialGT_GG_PT_Status, 22
	delay 1
	do_fullset 1, "Thermodynamic measurement: N_GG2 N_PT2", "GG2_PT2"
	result "A steady-state measurement has been taken automatically", REPORT & "Fullset", BLACK
		result "     * GG speed ISO =" &fv_Demo_IndustrialGT_N_GG_ISO &" rpm", REPORT & "Fullset", BLUE
'		result "         ** GG target offset =" &FormatNumber(fv_Demo_IndustrialGT_N_GG_ISO-fv_Demo_IndustrialGT_GG_Target_ISO,0) & " rpm", REPORT & "Fullset", RED
		result "     * PT speed ISO =" &fv_Demo_IndustrialGT_N_PT_ISO &" rpm", REPORT & "Fullset", BLUE
'		result "         ** PT target offset =" &FormatNumber(fv_Demo_IndustrialGT_N_PT_ISO-fv_Demo_IndustrialGT_PT_Target_ISO,0) & " rpm", REPORT & "Fullset", RED
		result "     * Power ISO =" &fv_Demo_IndustrialGT_Pow_ISO &" kW", REPORT & "Fullset", BLUE
		result "     * Efficiency ISO =" &fv_Demo_IndustrialGT_Eta_ISO &" %", REPORT & "Fullset", BLUE
		result "     * T4 ISO =" &fv_Demo_IndustrialGT_T4_ISO &" degC", REPORT & "Fullset", BLUE
	set_channel Demo_IndustrialGT_GG_PT_Status, 23
	delay 3

result "Thermodynamic measurement GG2_PT2 completed", REPORT & "Fullset", GREEN
result " ", REPORT
result " ", REPORT



'************************************ PT3 *************************************

note "Going to GG2_PT3"

set_channel Demo_IndustrialGT_GG_PT_Selector, 7
set_channel Demo_IndustrialGT_GG_PT_Status, 7

set_channel Demo_IndustrialGT_GG_Target_ISO, 12000
set_channel Demo_IndustrialGT_PT_Target_ISO, 12000
do_fullset 0
result "Going to GG speed ISO target = " &cv_Demo_IndustrialGT_GG_Target_ISO &" rpm and PT speed ISO target = " &cv_Demo_IndustrialGT_PT_Target_ISO &" rpm", REPORT & "Set Point", BLACK
'delay 1


result "     * Estimated GG speed target = " &cv_Demo_IndustrialGT_GG_Target &" rpm", REPORT & "Set Point", BLUE
result "     * Estimated PT speed target = " &cv_Demo_IndustrialGT_PT_Target &" rpm", REPORT & "Set Point", BLUE
set_channel Sim_IndustrialGT_N_GG, cv_Demo_IndustrialGT_GG_Target
set_channel Sim_IndustrialGT_N_PT, cv_Demo_IndustrialGT_PT_Target

set_channel Sim_IndustrialGT_N_GG, 12150
set_channel Sim_IndustrialGT_N_PT, 12181
set_channel Sim_IndustrialGT_N_Generator, 7670
set_channel Sim_IndustrialGT_T_M, 3763.5
set_channel Sim_IndustrialGT_ZI_0404030, 10
set_channel Sim_IndustrialGT_P_Baro, 1.0152
set_channel Sim_IndustrialGT_ME_0405690, 58.7
set_channel Sim_IndustrialGT_PDT_2210, -1.63
set_channel Sim_IndustrialGT_PDT_400X, 0.0345


set_channel Sim_IndustrialGT_TE_0404000_A, 23
set_channel Sim_IndustrialGT_TE_0404000_B, 22.8
set_channel Sim_IndustrialGT_PD_Inlet_A, -0.0058
set_channel Sim_IndustrialGT_PD_Inlet_B, -0.0064
set_channel Sim_IndustrialGT_PT_0404000, 0.00795
set_channel Sim_IndustrialGT_TE_0404900, 347.7
set_channel Sim_IndustrialGT_PT_0404900, 9.24985
set_channel Sim_IndustrialGT_TE_040461X, 570.333333333333
set_channel Sim_IndustrialGT_PT_040460X, 1.3594
set_channel Sim_IndustrialGT_TE_0404650, 432.83125
set_channel Sim_IndustrialGT_PT_0404650, -0.0035
set_channel Sim_IndustrialGT_TT_040_2001, 25.1
set_channel Sim_IndustrialGT_PT_040_2001, 24.4786
set_channel Sim_IndustrialGT_FT_040_2001, 1416.4
set_channel Sim_IndustrialGT_T_O_in, 46
set_channel Sim_IndustrialGT_T_O_GG_fr_out, 56.5
set_channel Sim_IndustrialGT_T_O_GG_re_out, 70
set_channel Sim_IndustrialGT_T_O_PT_out, 70
set_channel Sim_IndustrialGT_P_O_GG_fr, 2.2239
set_channel Sim_IndustrialGT_P_O_GG_re, 2.0643
set_channel Sim_IndustrialGT_P_O_PT, 1.969
set_channel Sim_IndustrialGT_F_O_GG_fr, 230.5
set_channel Sim_IndustrialGT_F_O_GG_re, 49
set_channel Sim_IndustrialGT_F_O_PT, 179.4

set_channel Sim_IndustrialGT_TE_0401110_A, 82
set_channel Sim_IndustrialGT_TE_0401110_B, 84.9
set_channel Sim_IndustrialGT_TE_0401120_A, 67.8
set_channel Sim_IndustrialGT_TE_0401120_B, 67.6
set_channel Sim_IndustrialGT_TE_0401130_A, 67.2
set_channel Sim_IndustrialGT_TE_0401130_B, 66.4
set_channel Sim_IndustrialGT_TE_0401140_A, 66.9
set_channel Sim_IndustrialGT_TE_0401140_B, 66.8
set_channel Sim_IndustrialGT_TE_0401310_A, 64.4
set_channel Sim_IndustrialGT_TE_0401310_B, 66.2
set_channel Sim_IndustrialGT_TE_0401320_A, 77.4
set_channel Sim_IndustrialGT_TE_0401320_B, 74.6
set_channel Sim_IndustrialGT_TE_0401330_A, 68.2
set_channel Sim_IndustrialGT_TE_0401330_B, 66
set_channel Sim_IndustrialGT_TE_0401340_A, 63
set_channel Sim_IndustrialGT_TE_0401340_B, 62.9


set_channel Sim_IndustrialGT_T_O_LG_in, 46.2
set_channel Sim_IndustrialGT_T_O_LG_out, 60.8
set_channel Sim_IndustrialGT_F_O_LG, 303.4


wait "Demo_IndustrialGT_N_GG_ISO = " &cv_Demo_IndustrialGT_GG_Target_ISO, 20, 20
wait "Demo_IndustrialGT_N_PT_ISO = " &cv_Demo_IndustrialGT_PT_Target_ISO, 20, 20

'delay 8
beep 1


set_channel Demo_IndustrialGT_GG_PT_Status, 21
result "Stabilizing - Minimum 5 minutes", REPORT & "Stabilization", BLACK
delay 1
result "Stabilization completed", REPORT & "Stabilization", GREEN
delay 1

set_channel Demo_IndustrialGT_GG_PT_Status, 22
'delay 1
do_fullset 1, "Thermodynamic measurement: N_GG2 N_PT3", "GG2_PT3"
result "A steady-state measurement has been taken automatically", REPORT & "Fullset", BLACK
result "     * GG speed ISO =" &fv_Demo_IndustrialGT_N_GG_ISO &" rpm", REPORT & "Fullset", BLUE
'result "         ** GG target offset =" &FormatNumber(fv_Demo_IndustrialGT_N_GG_ISO-fv_Demo_IndustrialGT_GG_Target_ISO,0) & " rpm", REPORT & "Fullset", RED
result "     * PT speed ISO =" &fv_Demo_IndustrialGT_N_PT_ISO &" rpm", REPORT & "Fullset", BLUE
'result "         ** PT target offset =" &FormatNumber(fv_Demo_IndustrialGT_N_PT_ISO-fv_Demo_IndustrialGT_PT_Target_ISO,0) & " rpm", REPORT & "Fullset", RED
result "     * Power ISO =" &fv_Demo_IndustrialGT_Pow_ISO &" kW", REPORT & "Fullset", BLUE
result "     * Efficiency ISO =" &fv_Demo_IndustrialGT_Eta_ISO &" %", REPORT & "Fullset", BLUE
result "     * T4 ISO =" &fv_Demo_IndustrialGT_T4_ISO &" degC", REPORT & "Fullset", BLUE
set_channel Demo_IndustrialGT_GG_PT_Status, 23
'delay 1
result "Thermodynamic measurement GG2_PT3 completed", REPORT & "Fullset", GREEN
result " ", REPORT
result " ", REPORT
result " *** All GG2 measurements have been completed ***", REPORT & "Fullset", GREEN
result " ", REPORT
result " ", REPORT



'******************************************************************************
'************************************ GG3 *************************************
'******************************************************************************



note "GG3"

'************************************ PT1 *************************************

note "Going to GG3_PT1"

set_channel Demo_IndustrialGT_GG_PT_Selector, 8
set_channel Demo_IndustrialGT_GG_PT_Status, 8

set_channel Demo_IndustrialGT_GG_Target_ISO, 12500
set_channel Demo_IndustrialGT_PT_Target_ISO, 6000
do_fullset 0
result "Going to GG speed ISO target = " &cv_Demo_IndustrialGT_GG_Target_ISO &" rpm and PT speed ISO target = " &cv_Demo_IndustrialGT_PT_Target_ISO &" rpm", REPORT & "Set Point", BLACK
'delay 1

result "     * Estimated GG speed target = " &cv_Demo_IndustrialGT_GG_Target &" rpm", REPORT & "Set Point", BLUE
result "     * Estimated GG speed target = " &cv_Demo_IndustrialGT_PT_Target &" rpm", REPORT & "Set Point", BLUE
set_channel Sim_IndustrialGT_N_GG, cv_Demo_IndustrialGT_GG_Target
set_channel Sim_IndustrialGT_N_PT, cv_Demo_IndustrialGT_PT_Target


set_channel Sim_IndustrialGT_N_GG, 12655
set_channel Sim_IndustrialGT_N_PT, 6099
set_channel Sim_IndustrialGT_N_Generator, 3835
set_channel Sim_IndustrialGT_T_M, 10518
set_channel Sim_IndustrialGT_ZI_0404030, 4.9
set_channel Sim_IndustrialGT_P_Baro, 1.0151
set_channel Sim_IndustrialGT_ME_0405690, 54.2
set_channel Sim_IndustrialGT_PDT_2210, -1.96
set_channel Sim_IndustrialGT_PDT_400X, 0.0433


set_channel Sim_IndustrialGT_TE_0404000_A, 23.3
set_channel Sim_IndustrialGT_TE_0404000_B, 23
set_channel Sim_IndustrialGT_PD_Inlet_A, -0.007
set_channel Sim_IndustrialGT_PD_Inlet_B, -0.008
set_channel Sim_IndustrialGT_PT_0404000, 0.00975
set_channel Sim_IndustrialGT_TE_0404900, 377.35
set_channel Sim_IndustrialGT_PT_0404900, 10.9903
set_channel Sim_IndustrialGT_TE_040461X, 629.691666666667
set_channel Sim_IndustrialGT_PT_040460X, 1.7428
set_channel Sim_IndustrialGT_TE_0404650, 476.46875
set_channel Sim_IndustrialGT_PT_0404650, -0.00325
set_channel Sim_IndustrialGT_TT_040_2001, 29
set_channel Sim_IndustrialGT_PT_040_2001, 24.3359
set_channel Sim_IndustrialGT_FT_040_2001, 1785.9
set_channel Sim_IndustrialGT_T_O_in, 45.5
set_channel Sim_IndustrialGT_T_O_GG_fr_out, 57.2
set_channel Sim_IndustrialGT_T_O_GG_re_out, 72.8
set_channel Sim_IndustrialGT_T_O_PT_out, 61.9
set_channel Sim_IndustrialGT_P_O_GG_fr, 2.2843
set_channel Sim_IndustrialGT_P_O_GG_re, 2.118
set_channel Sim_IndustrialGT_P_O_PT, 2.0202
set_channel Sim_IndustrialGT_F_O_GG_fr, 232.8
set_channel Sim_IndustrialGT_F_O_GG_re, 49.4
set_channel Sim_IndustrialGT_F_O_PT, 181.6

set_channel Sim_IndustrialGT_TE_0401110_A, 82.5
set_channel Sim_IndustrialGT_TE_0401110_B, 85.5
set_channel Sim_IndustrialGT_TE_0401120_A, 68.3
set_channel Sim_IndustrialGT_TE_0401120_B, 68.3
set_channel Sim_IndustrialGT_TE_0401130_A, 68
set_channel Sim_IndustrialGT_TE_0401130_B, 67.2
set_channel Sim_IndustrialGT_TE_0401140_A, 67.2
set_channel Sim_IndustrialGT_TE_0401140_B, 67.2
set_channel Sim_IndustrialGT_TE_0401310_A, 54.1
set_channel Sim_IndustrialGT_TE_0401310_B, 55.6
set_channel Sim_IndustrialGT_TE_0401320_A, 62
set_channel Sim_IndustrialGT_TE_0401320_B, 60.1
set_channel Sim_IndustrialGT_TE_0401330_A, 53.2
set_channel Sim_IndustrialGT_TE_0401330_B, 52.4
set_channel Sim_IndustrialGT_TE_0401340_A, 57.6
set_channel Sim_IndustrialGT_TE_0401340_B, 58.5


set_channel Sim_IndustrialGT_T_O_LG_in, 45.6
set_channel Sim_IndustrialGT_T_O_LG_out, 51.5
set_channel Sim_IndustrialGT_F_O_LG, 290.6


wait "Demo_IndustrialGT_N_GG_ISO = " &cv_Demo_IndustrialGT_GG_Target_ISO, 20, 20
wait "Demo_IndustrialGT_N_PT_ISO = " &cv_Demo_IndustrialGT_PT_Target_ISO, 20, 20


'delay 8
beep 1

set_channel Demo_IndustrialGT_GG_PT_Status, 21
result "Stabilizing - Minimum 10 minutes ...", REPORT & "Stabilization", BLACK
'delay 1
result "Halfway - 5 more minutes ...", REPORT & "Stabilization", BLACK
'delay 1
result "Stabilization completed", REPORT & "Stabilization", GREEN
'delay 1

set_channel Demo_IndustrialGT_GG_PT_Status, 22
'delay 1
do_fullset 1, "Thermodynamic measurement: N_GG3 N_PT1", "GG3_PT1"
result "A steady-state measurement has been taken automatically", REPORT & "Fullset", BLACK
result "     * GG speed ISO =" &fv_Demo_IndustrialGT_N_GG_ISO &" rpm", REPORT & "Fullset", BLUE
'result "         ** GG target offset =" &FormatNumber(fv_Demo_IndustrialGT_N_GG_ISO-fv_Demo_IndustrialGT_GG_Target_ISO,0) & " rpm", REPORT & "Fullset", RED
result "     * PT speed ISO =" &fv_Demo_IndustrialGT_N_PT_ISO &" rpm", REPORT & "Fullset", BLUE
'result "         ** PT target offset =" &FormatNumber(fv_Demo_IndustrialGT_N_PT_ISO-fv_Demo_IndustrialGT_PT_Target_ISO,0) & " rpm", REPORT & "Fullset", RED
result "     * Power ISO =" &fv_Demo_IndustrialGT_Pow_ISO &" kW", REPORT & "Fullset", BLUE
result "     * Efficiency ISO =" &fv_Demo_IndustrialGT_Eta_ISO &" %", REPORT & "Fullset", BLUE
result "     * T4 ISO =" &fv_Demo_IndustrialGT_T4_ISO &" degC", REPORT & "Fullset", BLUE
set_channel Demo_IndustrialGT_GG_PT_Status, 23
'delay 1
result "Thermodynamic measurement GG3_PT1 completed", REPORT & "Fullset", GREEN
result " ", REPORT
result " ", REPORT



'************************************ PT2 *************************************

note "Going to GG3_PT2"


set_channel Demo_IndustrialGT_GG_PT_Selector, 9
set_channel Demo_IndustrialGT_GG_PT_Status, 9

set_channel Demo_IndustrialGT_GG_Target_ISO, 12500
set_channel Demo_IndustrialGT_PT_Target_ISO, 8400
do_fullset 0
result "Going to GG speed ISO target = " &cv_Demo_IndustrialGT_GG_Target_ISO &" rpm and PT speed ISO target = " &cv_Demo_IndustrialGT_PT_Target_ISO &" rpm", REPORT & "Set Point", BLACK
'delay 1


result "     * Estimated GG speed target = " &cv_Demo_IndustrialGT_GG_Target &" rpm", REPORT & "Set Point", BLUE
result "     * Estimated GG speed target = " &cv_Demo_IndustrialGT_PT_Target &" rpm", REPORT & "Set Point", BLUE
set_channel Sim_IndustrialGT_N_GG, cv_Demo_IndustrialGT_GG_Target
set_channel Sim_IndustrialGT_N_PT, cv_Demo_IndustrialGT_PT_Target


set_channel Sim_IndustrialGT_N_GG, 12655
set_channel Sim_IndustrialGT_N_PT, 8534
set_channel Sim_IndustrialGT_N_Generator, 5371
set_channel Sim_IndustrialGT_T_M, 8350.1
set_channel Sim_IndustrialGT_ZI_0404030, 4.9
set_channel Sim_IndustrialGT_P_Baro, 1.015
set_channel Sim_IndustrialGT_ME_0405690, 55.8
set_channel Sim_IndustrialGT_PDT_2210, -1.98
set_channel Sim_IndustrialGT_PDT_400X, 0.043


set_channel Sim_IndustrialGT_TE_0404000_A, 23.5
set_channel Sim_IndustrialGT_TE_0404000_B, 23.3
set_channel Sim_IndustrialGT_PD_Inlet_A, -0.0071
set_channel Sim_IndustrialGT_PD_Inlet_B, -0.008
set_channel Sim_IndustrialGT_PT_0404000, 0.00985
set_channel Sim_IndustrialGT_TE_0404900, 377.55
set_channel Sim_IndustrialGT_PT_0404900, 10.9423
set_channel Sim_IndustrialGT_TE_040461X, 627.675
set_channel Sim_IndustrialGT_PT_040460X, 1.726
set_channel Sim_IndustrialGT_TE_0404650, 457.3125
set_channel Sim_IndustrialGT_PT_0404650, -0.0033
set_channel Sim_IndustrialGT_TT_040_2001, 29.5
set_channel Sim_IndustrialGT_PT_040_2001, 24.3418
set_channel Sim_IndustrialGT_FT_040_2001, 1768.6
set_channel Sim_IndustrialGT_T_O_in, 45.5
set_channel Sim_IndustrialGT_T_O_GG_fr_out, 57.2
set_channel Sim_IndustrialGT_T_O_GG_re_out, 72.8
set_channel Sim_IndustrialGT_T_O_PT_out, 65.2
set_channel Sim_IndustrialGT_P_O_GG_fr, 2.2625
set_channel Sim_IndustrialGT_P_O_GG_re, 2.1013
set_channel Sim_IndustrialGT_P_O_PT, 2.0032
set_channel Sim_IndustrialGT_F_O_GG_fr, 231.7
set_channel Sim_IndustrialGT_F_O_GG_re, 49.2
set_channel Sim_IndustrialGT_F_O_PT, 180.2

set_channel Sim_IndustrialGT_TE_0401110_A, 82.7
set_channel Sim_IndustrialGT_TE_0401110_B, 85.5
set_channel Sim_IndustrialGT_TE_0401120_A, 68.4
set_channel Sim_IndustrialGT_TE_0401120_B, 68.3
set_channel Sim_IndustrialGT_TE_0401130_A, 68
set_channel Sim_IndustrialGT_TE_0401130_B, 67.1
set_channel Sim_IndustrialGT_TE_0401140_A, 67.1
set_channel Sim_IndustrialGT_TE_0401140_B, 67
set_channel Sim_IndustrialGT_TE_0401310_A, 57.3
set_channel Sim_IndustrialGT_TE_0401310_B, 58.9
set_channel Sim_IndustrialGT_TE_0401320_A, 67.6
set_channel Sim_IndustrialGT_TE_0401320_B, 65.2
set_channel Sim_IndustrialGT_TE_0401330_A, 57.8
set_channel Sim_IndustrialGT_TE_0401330_B, 56.7
set_channel Sim_IndustrialGT_TE_0401340_A, 59.6
set_channel Sim_IndustrialGT_TE_0401340_B, 59.5

set_channel Sim_IndustrialGT_T_O_LG_in, 45.6
set_channel Sim_IndustrialGT_T_O_LG_out, 54.5
set_channel Sim_IndustrialGT_F_O_LG, 295.8


wait "Demo_IndustrialGT_N_GG_ISO = " &cv_Demo_IndustrialGT_GG_Target_ISO, 20, 20
wait "Demo_IndustrialGT_N_PT_ISO = " &cv_Demo_IndustrialGT_PT_Target_ISO, 20, 20


'delay 8
beep 1

set_channel Demo_IndustrialGT_GG_PT_Status, 21
result "Stabilizing - Minimum 5 minutes ...", REPORT & "Stabilization", BLACK
'delay 1
result "Stabilization completed", REPORT & "Stabilization", GREEN
'delay 1

set_channel Demo_IndustrialGT_GG_PT_Status, 22
'delay 1
do_fullset 1, "Thermodynamic measurement: N_GG3 N_PT2", "GG3_PT2"
result "A steady-state measurement has been taken automatically", REPORT & "Fullset", BLACK
result "     * GG speed ISO =" &fv_Demo_IndustrialGT_N_GG_ISO &" rpm", REPORT & "Fullset", BLUE
'result "         ** GG target offset =" &FormatNumber(fv_Demo_IndustrialGT_N_GG_ISO-fv_Demo_IndustrialGT_GG_Target_ISO,0) & " rpm", REPORT & "Fullset", RED
result "     * PT speed ISO =" &fv_Demo_IndustrialGT_N_PT_ISO &" rpm", REPORT & "Fullset", BLUE
'result "         ** PT target offset =" &FormatNumber(fv_Demo_IndustrialGT_N_PT_ISO-fv_Demo_IndustrialGT_PT_Target_ISO,0) & " rpm", REPORT & "Fullset", RED
result "     * Power ISO =" &fv_Demo_IndustrialGT_Pow_ISO &" kW", REPORT & "Fullset", BLUE
result "     * Efficiency ISO =" &fv_Demo_IndustrialGT_Eta_ISO &" %", REPORT & "Fullset", BLUE
result "     * T4 ISO =" &fv_Demo_IndustrialGT_T4_ISO &" degC", REPORT & "Fullset", BLUE
set_channel Demo_IndustrialGT_GG_PT_Status, 23
'delay 1
result "Thermodynamic measurement GG3_PT2 completed", REPORT & "Fullset", GREEN
result " ", REPORT
result " ", REPORT



'************************************ PT3 *************************************

note "Going to GG3_PT3"

set_channel Demo_IndustrialGT_GG_PT_Selector, 10
set_channel Demo_IndustrialGT_GG_PT_Status, 10

set_channel Demo_IndustrialGT_GG_Target_ISO, 12500
set_channel Demo_IndustrialGT_PT_Target_ISO, 10800
do_fullset 0
result "Going to GG speed ISO target = " &cv_Demo_IndustrialGT_GG_Target_ISO &" rpm and PT speed ISO target = " &cv_Demo_IndustrialGT_PT_Target_ISO &" rpm", REPORT & "Set Point", BLACK
'delay 1


result "     * Estimated GG speed target = " &cv_Demo_IndustrialGT_GG_Target &" rpm", REPORT & "Set Point", BLUE
result "     * Estimated GG speed target = " &cv_Demo_IndustrialGT_PT_Target &" rpm", REPORT & "Set Point", BLUE
set_channel Sim_IndustrialGT_N_GG, cv_Demo_IndustrialGT_GG_Target
set_channel Sim_IndustrialGT_N_PT, cv_Demo_IndustrialGT_PT_Target


set_channel Sim_IndustrialGT_N_GG, 12654
set_channel Sim_IndustrialGT_N_PT, 10988
set_channel Sim_IndustrialGT_N_Generator, 6917
set_channel Sim_IndustrialGT_T_M, 6438.5
set_channel Sim_IndustrialGT_ZI_0404030, 5.1
set_channel Sim_IndustrialGT_P_Baro, 1.015
set_channel Sim_IndustrialGT_ME_0405690, 52.7
set_channel Sim_IndustrialGT_PDT_2210, -1.97
set_channel Sim_IndustrialGT_PDT_400X, 0.0432


set_channel Sim_IndustrialGT_TE_0404000_A, 24.1
set_channel Sim_IndustrialGT_TE_0404000_B, 23.8
set_channel Sim_IndustrialGT_PD_Inlet_A, -0.007
set_channel Sim_IndustrialGT_PD_Inlet_B, -0.0078
set_channel Sim_IndustrialGT_PT_0404000, 0.00975
set_channel Sim_IndustrialGT_TE_0404900, 377.9
set_channel Sim_IndustrialGT_PT_0404900, 10.94155
set_channel Sim_IndustrialGT_TE_040461X, 626.983333333333
set_channel Sim_IndustrialGT_PT_040460X, 1.7233
set_channel Sim_IndustrialGT_TE_0404650, 454.23125
set_channel Sim_IndustrialGT_PT_0404650, -0.0039
set_channel Sim_IndustrialGT_TT_040_2001, 29.9
set_channel Sim_IndustrialGT_PT_040_2001, 24.3427
set_channel Sim_IndustrialGT_FT_040_2001, 1765.1
set_channel Sim_IndustrialGT_T_O_in, 45.4
set_channel Sim_IndustrialGT_T_O_GG_fr_out, 57.1
set_channel Sim_IndustrialGT_T_O_GG_re_out, 72.9
set_channel Sim_IndustrialGT_T_O_PT_out, 69.5
set_channel Sim_IndustrialGT_P_O_GG_fr, 2.2395
set_channel Sim_IndustrialGT_P_O_GG_re, 2.0843
set_channel Sim_IndustrialGT_P_O_PT, 1.9825
set_channel Sim_IndustrialGT_F_O_GG_fr, 230.4
set_channel Sim_IndustrialGT_F_O_GG_re, 48.9
set_channel Sim_IndustrialGT_F_O_PT, 179.2

set_channel Sim_IndustrialGT_TE_0401110_A, 82.7
set_channel Sim_IndustrialGT_TE_0401110_B, 85.5
set_channel Sim_IndustrialGT_TE_0401120_A, 68.4
set_channel Sim_IndustrialGT_TE_0401120_B, 68.4
set_channel Sim_IndustrialGT_TE_0401130_A, 68
set_channel Sim_IndustrialGT_TE_0401130_B, 67.1
set_channel Sim_IndustrialGT_TE_0401140_A, 66.9
set_channel Sim_IndustrialGT_TE_0401140_B, 67
set_channel Sim_IndustrialGT_TE_0401310_A, 61.4
set_channel Sim_IndustrialGT_TE_0401310_B, 63.3
set_channel Sim_IndustrialGT_TE_0401320_A, 73.6
set_channel Sim_IndustrialGT_TE_0401320_B, 70.9
set_channel Sim_IndustrialGT_TE_0401330_A, 64.3
set_channel Sim_IndustrialGT_TE_0401330_B, 62.5
set_channel Sim_IndustrialGT_TE_0401340_A, 61.8
set_channel Sim_IndustrialGT_TE_0401340_B, 61.5


set_channel Sim_IndustrialGT_T_O_LG_in, 45.6
set_channel Sim_IndustrialGT_T_O_LG_out, 58.6
set_channel Sim_IndustrialGT_F_O_LG, 300.7


wait "Demo_IndustrialGT_N_GG_ISO = " &cv_Demo_IndustrialGT_GG_Target_ISO, 20, 20
wait "Demo_IndustrialGT_N_PT_ISO = " &cv_Demo_IndustrialGT_PT_Target_ISO, 20, 20


'delay 8
beep 1


set_channel Demo_IndustrialGT_GG_PT_Status, 21
result "Stabilizing - Minimum 5 minutes ...", REPORT & "Stabilization", BLACK
'delay 1
result "Stabilization completed", REPORT & "Stabilization", GREEN
'delay 1


set_channel Demo_IndustrialGT_GG_PT_Status, 22
'delay 1
do_fullset 1, "Thermodynamic measurement: N_GG3 N_PT3", "GG3_PT3"
result "A steady-state measurement has been taken automatically", REPORT & "Fullset", BLACK
result "     * GG speed ISO =" &fv_Demo_IndustrialGT_N_GG_ISO &" rpm", REPORT & "Fullset", BLUE
'result "         ** GG target offset =" &FormatNumber(fv_Demo_IndustrialGT_N_GG_ISO-fv_Demo_IndustrialGT_GG_Target_ISO,0) & " rpm", REPORT & "Fullset", RED
result "     * PT speed ISO =" &fv_Demo_IndustrialGT_N_PT_ISO &" rpm", REPORT & "Fullset", BLUE
'result "         ** PT target offset =" &FormatNumber(fv_Demo_IndustrialGT_N_PT_ISO-fv_Demo_IndustrialGT_PT_Target_ISO,0) & " rpm", REPORT & "Fullset", RED
result "     * Power ISO =" &fv_Demo_IndustrialGT_Pow_ISO &" kW", REPORT & "Fullset", BLUE
result "     * Efficiency ISO =" &fv_Demo_IndustrialGT_Eta_ISO &" %", REPORT & "Fullset", BLUE
result "     * T4 ISO =" &fv_Demo_IndustrialGT_T4_ISO &" degC", REPORT & "Fullset", BLUE
set_channel Demo_IndustrialGT_GG_PT_Status, 23
'delay 1
result "Thermodynamic measurement GG3_PT3 completed", REPORT & "Fullset", GREEN
result " ", REPORT
result " ", REPORT



'************************************ PT4 *************************************

note "Going to GG3_PT4"

set_channel Demo_IndustrialGT_GG_PT_Selector, 11
set_channel Demo_IndustrialGT_GG_PT_Status, 11


set_channel Demo_IndustrialGT_GG_Target_ISO, 12500
set_channel Demo_IndustrialGT_PT_Target_ISO, 12000
do_fullset 0
result "Going to GG speed ISO target = " &cv_Demo_IndustrialGT_GG_Target_ISO &" rpm and PT speed ISO target = " &cv_Demo_IndustrialGT_PT_Target_ISO &" rpm", REPORT & "Set Point", BLACK
'delay 1

result "     * Estimated GG speed target = " &cv_Demo_IndustrialGT_GG_Target &" rpm", REPORT & "Set Point", BLUE
result "     * Estimated GG speed target = " &cv_Demo_IndustrialGT_PT_Target &" rpm", REPORT & "Set Point", BLUE
set_channel Sim_IndustrialGT_N_GG, cv_Demo_IndustrialGT_GG_Target
set_channel Sim_IndustrialGT_N_PT, cv_Demo_IndustrialGT_PT_Target


set_channel Sim_IndustrialGT_N_GG, 12655
set_channel Sim_IndustrialGT_N_PT, 12198
set_channel Sim_IndustrialGT_N_Generator, 7680
set_channel Sim_IndustrialGT_T_M, 5486.4
set_channel Sim_IndustrialGT_ZI_0404030, 5.1
set_channel Sim_IndustrialGT_P_Baro, 1.015
set_channel Sim_IndustrialGT_ME_0405690, 54
set_channel Sim_IndustrialGT_PDT_2210, -1.96
set_channel Sim_IndustrialGT_PDT_400X, 0.043


set_channel Sim_IndustrialGT_TE_0404000_A, 24.1
set_channel Sim_IndustrialGT_TE_0404000_B, 23.8
set_channel Sim_IndustrialGT_PD_Inlet_A, -0.0071
set_channel Sim_IndustrialGT_PD_Inlet_B, -0.0077
set_channel Sim_IndustrialGT_PT_0404000, 0.0097
set_channel Sim_IndustrialGT_TE_0404900, 377.4
set_channel Sim_IndustrialGT_PT_0404900, 10.87535
set_channel Sim_IndustrialGT_TE_040461X, 620.766666666667
set_channel Sim_IndustrialGT_PT_040460X, 1.69135
set_channel Sim_IndustrialGT_TE_0404650, 453.71875
set_channel Sim_IndustrialGT_PT_0404650, -0.00435
set_channel Sim_IndustrialGT_TT_040_2001, 30.3
set_channel Sim_IndustrialGT_PT_040_2001, 24.3625
set_channel Sim_IndustrialGT_FT_040_2001, 1744.2
set_channel Sim_IndustrialGT_T_O_in, 46
set_channel Sim_IndustrialGT_T_O_GG_fr_out, 57.5
set_channel Sim_IndustrialGT_T_O_GG_re_out, 73.3
set_channel Sim_IndustrialGT_T_O_PT_out, 72.1
set_channel Sim_IndustrialGT_P_O_GG_fr, 2.2175
set_channel Sim_IndustrialGT_P_O_GG_re, 2.067
set_channel Sim_IndustrialGT_P_O_PT, 1.9623
set_channel Sim_IndustrialGT_F_O_GG_fr, 229.5
set_channel Sim_IndustrialGT_F_O_GG_re, 48.8
set_channel Sim_IndustrialGT_F_O_PT, 178.9

set_channel Sim_IndustrialGT_TE_0401110_A, 83
set_channel Sim_IndustrialGT_TE_0401110_B, 85.7
set_channel Sim_IndustrialGT_TE_0401120_A, 68.8
set_channel Sim_IndustrialGT_TE_0401120_B, 68.7
set_channel Sim_IndustrialGT_TE_0401130_A, 68.4
set_channel Sim_IndustrialGT_TE_0401130_B, 67.5
set_channel Sim_IndustrialGT_TE_0401140_A, 67.1
set_channel Sim_IndustrialGT_TE_0401140_B, 67.2
set_channel Sim_IndustrialGT_TE_0401310_A, 64.5
set_channel Sim_IndustrialGT_TE_0401310_B, 66.3
set_channel Sim_IndustrialGT_TE_0401320_A, 77.1
set_channel Sim_IndustrialGT_TE_0401320_B, 74.3
set_channel Sim_IndustrialGT_TE_0401330_A, 68.5
set_channel Sim_IndustrialGT_TE_0401330_B, 66.3
set_channel Sim_IndustrialGT_TE_0401340_A, 63.8
set_channel Sim_IndustrialGT_TE_0401340_B, 63.2


set_channel Sim_IndustrialGT_T_O_LG_in, 46.3
set_channel Sim_IndustrialGT_T_O_LG_out, 61.5
set_channel Sim_IndustrialGT_F_O_LG, 303.2


wait "Demo_IndustrialGT_N_GG_ISO = " &cv_Demo_IndustrialGT_GG_Target_ISO, 20, 20
wait "Demo_IndustrialGT_N_PT_ISO = " &cv_Demo_IndustrialGT_PT_Target_ISO, 20, 20



'delay 8
beep 1


set_channel Demo_IndustrialGT_GG_PT_Status, 21
result "Stabilizing - Minimum 5 minutes ...", REPORT & "Stabilization", BLACK
'delay 1
result "Stabilization completed", REPORT & "Stabilization", GREEN
'delay 1

set_channel Demo_IndustrialGT_GG_PT_Status, 22
'delay 1
do_fullset 1, "Thermodynamic measurement: N_GG3 N_PT4", "GG3_PT4"
result "A steady-state measurement has been taken automatically", REPORT & "Fullset", BLACK
result "     * GG speed ISO =" &fv_Demo_IndustrialGT_N_GG_ISO &" rpm", REPORT & "Fullset", BLUE
'result "         ** GG target offset =" &FormatNumber(fv_Demo_IndustrialGT_N_GG_ISO-fv_Demo_IndustrialGT_GG_Target_ISO,0) & " rpm", REPORT & "Fullset", RED
result "     * PT speed ISO =" &fv_Demo_IndustrialGT_N_PT_ISO &" rpm", REPORT & "Fullset", BLUE
'result "         ** PT target offset =" &FormatNumber(fv_Demo_IndustrialGT_N_PT_ISO-fv_Demo_IndustrialGT_PT_Target_ISO,0) & " rpm", REPORT & "Fullset", RED
result "     * Power ISO =" &fv_Demo_IndustrialGT_Pow_ISO &" kW", REPORT & "Fullset", BLUE
result "     * Efficiency ISO =" &fv_Demo_IndustrialGT_Eta_ISO &" %", REPORT & "Fullset", BLUE
result "     * T4 ISO =" &fv_Demo_IndustrialGT_T4_ISO &" degC", REPORT & "Fullset", BLUE
set_channel Demo_IndustrialGT_GG_PT_Status, 23
'delay 1
result "Thermodynamic measurement GG3_PT4 completed", REPORT & "Fullset", GREEN
result " ", REPORT
result " ", REPORT
result " *** All GG3 measurements have been completed ***", REPORT & "Fullset", GREEN
result " ", REPORT
result " ", REPORT



'******************************************************************************
'************************************ GG4 *************************************
'******************************************************************************


note "GG4"

'************************************ PT1 *************************************


note "Going to GG4_PT1"

set_channel Demo_IndustrialGT_GG_PT_Selector, 12
set_channel Demo_IndustrialGT_GG_PT_Status, 12


set_channel Demo_IndustrialGT_GG_Target_ISO, 12700
set_channel Demo_IndustrialGT_PT_Target_ISO, 7200
do_fullset 0
result "Going to GG speed ISO target = " &cv_Demo_IndustrialGT_GG_Target_ISO &" rpm and PT speed ISO target = " &cv_Demo_IndustrialGT_PT_Target_ISO &" rpm", REPORT & "Set Point", BLACK
'delay 1

result "     * Estimated GG speed target = " &cv_Demo_IndustrialGT_GG_Target &" rpm", REPORT & "Set Point", BLUE
result "     * Estimated GG speed target = " &cv_Demo_IndustrialGT_PT_Target &" rpm", REPORT & "Set Point", BLUE
set_channel Sim_IndustrialGT_N_GG, cv_Demo_IndustrialGT_GG_Target
set_channel Sim_IndustrialGT_N_PT, cv_Demo_IndustrialGT_PT_Target


set_channel Sim_IndustrialGT_N_GG, 12945
set_channel Sim_IndustrialGT_N_PT, 7331
set_channel Sim_IndustrialGT_N_Generator, 4613
set_channel Sim_IndustrialGT_T_M, 10759.3
set_channel Sim_IndustrialGT_ZI_0404030, 1.8
set_channel Sim_IndustrialGT_P_Baro, 1.0148
set_channel Sim_IndustrialGT_ME_0405690, 50.9
set_channel Sim_IndustrialGT_PDT_2210, -2.2
set_channel Sim_IndustrialGT_PDT_400X, 0.0494


set_channel Sim_IndustrialGT_TE_0404000_A, 24.3
set_channel Sim_IndustrialGT_TE_0404000_B, 24
set_channel Sim_IndustrialGT_PD_Inlet_A, -0.0079
set_channel Sim_IndustrialGT_PD_Inlet_B, -0.0088
set_channel Sim_IndustrialGT_PT_0404000, 0.011
set_channel Sim_IndustrialGT_TE_0404900, 394.9
set_channel Sim_IndustrialGT_PT_0404900, 11.97575
set_channel Sim_IndustrialGT_TE_040461X, 654.858333333333
set_channel Sim_IndustrialGT_PT_040460X, 1.92785
set_channel Sim_IndustrialGT_TE_0404650, 479.825
set_channel Sim_IndustrialGT_PT_0404650, -0.00345
set_channel Sim_IndustrialGT_TT_040_2001, 32.1
set_channel Sim_IndustrialGT_PT_040_2001, 24.201
set_channel Sim_IndustrialGT_FT_040_2001, 1975.1
set_channel Sim_IndustrialGT_T_O_in, 47.7
set_channel Sim_IndustrialGT_T_O_GG_fr_out, 59.3
set_channel Sim_IndustrialGT_T_O_GG_re_out, 76.7
set_channel Sim_IndustrialGT_T_O_PT_out, 65.7
set_channel Sim_IndustrialGT_P_O_GG_fr, 2.243
set_channel Sim_IndustrialGT_P_O_GG_re, 2.105
set_channel Sim_IndustrialGT_P_O_PT, 1.9901
set_channel Sim_IndustrialGT_F_O_GG_fr, 231.6
set_channel Sim_IndustrialGT_F_O_GG_re, 49.1
set_channel Sim_IndustrialGT_F_O_PT, 180.7

set_channel Sim_IndustrialGT_TE_0401110_A, 84.2
set_channel Sim_IndustrialGT_TE_0401110_B, 87.1
set_channel Sim_IndustrialGT_TE_0401120_A, 70.2
set_channel Sim_IndustrialGT_TE_0401120_B, 70.1
set_channel Sim_IndustrialGT_TE_0401130_A, 70.6
set_channel Sim_IndustrialGT_TE_0401130_B, 69.6
set_channel Sim_IndustrialGT_TE_0401140_A, 68.2
set_channel Sim_IndustrialGT_TE_0401140_B, 68.2
set_channel Sim_IndustrialGT_TE_0401310_A, 57.6
set_channel Sim_IndustrialGT_TE_0401310_B, 59
set_channel Sim_IndustrialGT_TE_0401320_A, 66.3
set_channel Sim_IndustrialGT_TE_0401320_B, 64.3
set_channel Sim_IndustrialGT_TE_0401330_A, 57.5
set_channel Sim_IndustrialGT_TE_0401330_B, 56.4
set_channel Sim_IndustrialGT_TE_0401340_A, 61.8
set_channel Sim_IndustrialGT_TE_0401340_B, 61.3


set_channel Sim_IndustrialGT_T_O_LG_in, 47.8
set_channel Sim_IndustrialGT_T_O_LG_out, 55.4
set_channel Sim_IndustrialGT_F_O_LG, 294.2


'delay 8
beep 1


set_channel Demo_IndustrialGT_GG_PT_Status, 21
result "Stabilizing - Minimum 10 minutes ...", REPORT & "Stabilization", BLACK
'delay 1
result "Halfway - 5 more minutes ...", REPORT & "Stabilization", BLACK
'delay 1
result "Stabilization completed", REPORT & "Stabilization", GREEN
'delay 1

set_channel Demo_IndustrialGT_GG_PT_Status, 22
'delay 1
do_fullset 1, "Thermodynamic measurement: N_GG4 N_PT1", "GG4_PT1"
result "A steady-state measurement has been taken automatically", REPORT & "Fullset", BLACK
result "     * GG speed ISO =" &fv_Demo_IndustrialGT_N_GG_ISO &" rpm", REPORT & "Fullset", BLUE
'result "         ** GG target offset =" &FormatNumber(fv_Demo_IndustrialGT_N_GG_ISO-fv_Demo_IndustrialGT_GG_Target_ISO,0) & " rpm", REPORT & "Fullset", RED
result "     * PT speed ISO =" &fv_Demo_IndustrialGT_N_PT_ISO &" rpm", REPORT & "Fullset", BLUE
'result "         ** PT target offset =" &FormatNumber(fv_Demo_IndustrialGT_N_PT_ISO-fv_Demo_IndustrialGT_PT_Target_ISO,0) & " rpm", REPORT & "Fullset", RED
result "     * Power ISO =" &fv_Demo_IndustrialGT_Pow_ISO &" kW", REPORT & "Fullset", BLUE
result "     * Efficiency ISO =" &fv_Demo_IndustrialGT_Eta_ISO &" %", REPORT & "Fullset", BLUE
result "     * T4 ISO =" &fv_Demo_IndustrialGT_T4_ISO &" degC", REPORT & "Fullset", BLUE
set_channel Demo_IndustrialGT_GG_PT_Status, 23
'delay 1
result "Thermodynamic measurement GG4_PT1 completed", REPORT & "Fullset", GREEN
result " ", REPORT
result " ", REPORT


'************************************ PT2 *************************************


note "Going to GG4_PT2"


set_channel Demo_IndustrialGT_GG_PT_Selector, 13
set_channel Demo_IndustrialGT_GG_PT_Status, 13


set_channel Demo_IndustrialGT_GG_Target_ISO, 12700
set_channel Demo_IndustrialGT_PT_Target_ISO, 9600
do_fullset 0
result "Going to GG speed ISO target = " &cv_Demo_IndustrialGT_GG_Target_ISO &" rpm and PT speed ISO target = " &cv_Demo_IndustrialGT_PT_Target_ISO &" rpm", REPORT & "Set Point", BLACK
'delay 1


result "     * Estimated GG speed target = " &cv_Demo_IndustrialGT_GG_Target &" rpm", REPORT & "Set Point", BLUE
result "     * Estimated GG speed target = " &cv_Demo_IndustrialGT_PT_Target &" rpm", REPORT & "Set Point", BLUE
set_channel Sim_IndustrialGT_N_GG, cv_Demo_IndustrialGT_GG_Target
set_channel Sim_IndustrialGT_N_PT, cv_Demo_IndustrialGT_PT_Target

set_channel Sim_IndustrialGT_N_GG, 12945
set_channel Sim_IndustrialGT_N_PT, 9756
set_channel Sim_IndustrialGT_N_Generator, 6143
set_channel Sim_IndustrialGT_T_M, 8704.9
set_channel Sim_IndustrialGT_ZI_0404030, 1.8
set_channel Sim_IndustrialGT_P_Baro, 1.0147
set_channel Sim_IndustrialGT_ME_0405690, 52.7
set_channel Sim_IndustrialGT_PDT_2210, -2.19
set_channel Sim_IndustrialGT_PDT_400X, 0.0494


set_channel Sim_IndustrialGT_TE_0404000_A, 24.3
set_channel Sim_IndustrialGT_TE_0404000_B, 23.9
set_channel Sim_IndustrialGT_PD_Inlet_A, -0.0081
set_channel Sim_IndustrialGT_PD_Inlet_B, -0.0087
set_channel Sim_IndustrialGT_PT_0404000, 0.01105
set_channel Sim_IndustrialGT_TE_0404900, 394.95
set_channel Sim_IndustrialGT_PT_0404900, 11.9895
set_channel Sim_IndustrialGT_TE_040461X, 657.483333333333
set_channel Sim_IndustrialGT_PT_040460X, 1.9414
set_channel Sim_IndustrialGT_TE_0404650, 467.61875
set_channel Sim_IndustrialGT_PT_0404650, -0.00375
set_channel Sim_IndustrialGT_TT_040_2001, 32.4
set_channel Sim_IndustrialGT_PT_040_2001, 24.197
set_channel Sim_IndustrialGT_FT_040_2001, 1989.4
set_channel Sim_IndustrialGT_T_O_in, 48
set_channel Sim_IndustrialGT_T_O_GG_fr_out, 59.6
set_channel Sim_IndustrialGT_T_O_GG_re_out, 77.1
set_channel Sim_IndustrialGT_T_O_PT_out, 69.8
set_channel Sim_IndustrialGT_P_O_GG_fr, 2.2211
set_channel Sim_IndustrialGT_P_O_GG_re, 2.0878
set_channel Sim_IndustrialGT_P_O_PT, 1.9716
set_channel Sim_IndustrialGT_F_O_GG_fr, 230.5
set_channel Sim_IndustrialGT_F_O_GG_re, 48.9
set_channel Sim_IndustrialGT_F_O_PT, 179.9


set_channel Sim_IndustrialGT_TE_0401110_A, 84.4
set_channel Sim_IndustrialGT_TE_0401110_B, 87.2
set_channel Sim_IndustrialGT_TE_0401120_A, 70.4
set_channel Sim_IndustrialGT_TE_0401120_B, 70.4
set_channel Sim_IndustrialGT_TE_0401130_A, 70.9
set_channel Sim_IndustrialGT_TE_0401130_B, 69.8
set_channel Sim_IndustrialGT_TE_0401140_A, 68.7
set_channel Sim_IndustrialGT_TE_0401140_B, 68.7
set_channel Sim_IndustrialGT_TE_0401310_A, 61.4
set_channel Sim_IndustrialGT_TE_0401310_B, 63
set_channel Sim_IndustrialGT_TE_0401320_A, 72
set_channel Sim_IndustrialGT_TE_0401320_B, 69.5
set_channel Sim_IndustrialGT_TE_0401330_A, 63.1
set_channel Sim_IndustrialGT_TE_0401330_B, 61.7
set_channel Sim_IndustrialGT_TE_0401340_A, 64.4
set_channel Sim_IndustrialGT_TE_0401340_B, 63.6


set_channel Sim_IndustrialGT_T_O_LG_in, 48.2
set_channel Sim_IndustrialGT_T_O_LG_out, 59.1
set_channel Sim_IndustrialGT_F_O_LG, 299.4


'delay 8
beep 1


set_channel Demo_IndustrialGT_GG_PT_Status, 21
result "Stabilizing - Minimum 5 minutes ...", REPORT & "Stabilization", BLACK
'delay 1
result "Stabilization completed", REPORT & "Stabilization", GREEN
'delay 1

set_channel Demo_IndustrialGT_GG_PT_Status, 22
'delay 1
do_fullset 1, "Thermodynamic measurement: N_GG4 N_PT2", "GG4_PT2"
result "A steady-state measurement has been taken automatically", REPORT & "Fullset", BLACK
result "     * GG speed ISO =" &fv_Demo_IndustrialGT_N_GG_ISO &" rpm", REPORT & "Fullset", BLUE
'result "         ** GG target offset =" &FormatNumber(fv_Demo_IndustrialGT_N_GG_ISO-fv_Demo_IndustrialGT_GG_Target_ISO,0) & " rpm", REPORT & "Fullset", RED
result "     * PT speed ISO =" &fv_Demo_IndustrialGT_N_PT_ISO &" rpm", REPORT & "Fullset", BLUE
'result "         ** PT target offset =" &FormatNumber(fv_Demo_IndustrialGT_N_PT_ISO-fv_Demo_IndustrialGT_PT_Target_ISO,0) & " rpm", REPORT & "Fullset", RED
result "     * Power ISO =" &fv_Demo_IndustrialGT_Pow_ISO &" kW", REPORT & "Fullset", BLUE
result "     * Efficiency ISO =" &fv_Demo_IndustrialGT_Eta_ISO &" %", REPORT & "Fullset", BLUE
result "     * T4 ISO =" &fv_Demo_IndustrialGT_T4_ISO &" degC", REPORT & "Fullset", BLUE
set_channel Demo_IndustrialGT_GG_PT_Status, 23
'delay 1
result "Thermodynamic measurement GG4_PT2 completed", REPORT & "Fullset", GREEN
result " ", REPORT
result " ", REPORT



'************************************ PT3 *************************************

note "Going to GG4_PT3"

set_channel Demo_IndustrialGT_GG_PT_Selector, 14
set_channel Demo_IndustrialGT_GG_PT_Status, 14

set_channel Demo_IndustrialGT_GG_Target_ISO, 12700
set_channel Demo_IndustrialGT_PT_Target_ISO, 12000
do_fullset 0
result "Going to GG speed ISO target = " &cv_Demo_IndustrialGT_GG_Target_ISO &" rpm and PT speed ISO target = " &cv_Demo_IndustrialGT_PT_Target_ISO &" rpm", REPORT & "Set Point", BLACK
'delay 1


result "     * Estimated GG speed target = " &cv_Demo_IndustrialGT_GG_Target &" rpm", REPORT & "Set Point", BLUE
result "     * Estimated GG speed target = " &cv_Demo_IndustrialGT_PT_Target &" rpm", REPORT & "Set Point", BLUE
set_channel Sim_IndustrialGT_N_GG, cv_Demo_IndustrialGT_GG_Target
set_channel Sim_IndustrialGT_N_PT, cv_Demo_IndustrialGT_PT_Target


set_channel Sim_IndustrialGT_N_GG, 12944
set_channel Sim_IndustrialGT_N_PT, 12208
set_channel Sim_IndustrialGT_N_Generator, 7689
set_channel Sim_IndustrialGT_T_M, 6661.6
set_channel Sim_IndustrialGT_ZI_0404030, 1.9
set_channel Sim_IndustrialGT_P_Baro, 1.0147
set_channel Sim_IndustrialGT_ME_0405690, 51.3
set_channel Sim_IndustrialGT_PDT_2210, -2.16
set_channel Sim_IndustrialGT_PDT_400X, 0.0492


set_channel Sim_IndustrialGT_TE_0404000_A, 24.6
set_channel Sim_IndustrialGT_TE_0404000_B, 24.2
set_channel Sim_IndustrialGT_PD_Inlet_A, -0.0079
set_channel Sim_IndustrialGT_PD_Inlet_B, -0.0087
set_channel Sim_IndustrialGT_PT_0404000, 0.01095
set_channel Sim_IndustrialGT_TE_0404900, 394.7
set_channel Sim_IndustrialGT_PT_0404900, 11.9397
set_channel Sim_IndustrialGT_TE_040461X, 650.833333333333
set_channel Sim_IndustrialGT_PT_040460X, 1.90835
set_channel Sim_IndustrialGT_TE_0404650, 464.56875
set_channel Sim_IndustrialGT_PT_0404650, -0.00435
set_channel Sim_IndustrialGT_TT_040_2001, 32.6
set_channel Sim_IndustrialGT_PT_040_2001, 24.211
set_channel Sim_IndustrialGT_FT_040_2001, 1958.7
set_channel Sim_IndustrialGT_T_O_in, 48.7
set_channel Sim_IndustrialGT_T_O_GG_fr_out, 60.2
set_channel Sim_IndustrialGT_T_O_GG_re_out, 77.5
set_channel Sim_IndustrialGT_T_O_PT_out, 74.7
set_channel Sim_IndustrialGT_P_O_GG_fr, 2.1905
set_channel Sim_IndustrialGT_P_O_GG_re, 2.0643
set_channel Sim_IndustrialGT_P_O_PT, 1.9449
set_channel Sim_IndustrialGT_F_O_GG_fr, 229.1
set_channel Sim_IndustrialGT_F_O_GG_re, 48.6
set_channel Sim_IndustrialGT_F_O_PT, 179.3


set_channel Sim_IndustrialGT_TE_0401110_A, 84.6
set_channel Sim_IndustrialGT_TE_0401110_B, 87.5
set_channel Sim_IndustrialGT_TE_0401120_A, 70.9
set_channel Sim_IndustrialGT_TE_0401120_B, 70.8
set_channel Sim_IndustrialGT_TE_0401130_A, 71.3
set_channel Sim_IndustrialGT_TE_0401130_B, 70.2
set_channel Sim_IndustrialGT_TE_0401140_A, 69.6
set_channel Sim_IndustrialGT_TE_0401140_B, 69.6
set_channel Sim_IndustrialGT_TE_0401310_A, 66.5
set_channel Sim_IndustrialGT_TE_0401310_B, 68
set_channel Sim_IndustrialGT_TE_0401320_A, 78
set_channel Sim_IndustrialGT_TE_0401320_B, 75.5
set_channel Sim_IndustrialGT_TE_0401330_A, 70.4
set_channel Sim_IndustrialGT_TE_0401330_B, 68.4
set_channel Sim_IndustrialGT_TE_0401340_A, 67
set_channel Sim_IndustrialGT_TE_0401340_B, 66.5


set_channel Sim_IndustrialGT_T_O_LG_in, 48.9
set_channel Sim_IndustrialGT_T_O_LG_out, 64.1
set_channel Sim_IndustrialGT_F_O_LG, 303.7


'delay 8
beep 1


set_channel Demo_IndustrialGT_GG_PT_Status, 21
result "Stabilizing - Minimum 5 minutes ...", REPORT & "Stabilization", BLACK
'delay 1
result "Stabilization completed", REPORT & "Stabilization", GREEN
'delay 1

set_channel Demo_IndustrialGT_GG_PT_Status, 22
'delay 1
do_fullset 1, "Thermodynamic measurement: N_GG4 N_PT3", "GG4_PT3"
result "A steady-state measurement has been taken automatically", REPORT & "Fullset", BLACK
result "     * GG speed ISO =" &fv_Demo_IndustrialGT_N_GG_ISO &" rpm", REPORT & "Fullset", BLUE
'result "         ** GG target offset =" &FormatNumber(fv_Demo_IndustrialGT_N_GG_ISO-fv_Demo_IndustrialGT_GG_Target_ISO,0) & " rpm", REPORT & "Fullset", RED
result "     * PT speed ISO =" &fv_Demo_IndustrialGT_N_PT_ISO &" rpm", REPORT & "Fullset", BLUE
'result "         ** PT target offset =" &FormatNumber(fv_Demo_IndustrialGT_N_PT_ISO-fv_Demo_IndustrialGT_PT_Target_ISO,0) & " rpm", REPORT & "Fullset", RED
result "     * Power ISO =" &fv_Demo_IndustrialGT_Pow_ISO &" kW", REPORT & "Fullset", BLUE
result "     * Efficiency ISO =" &fv_Demo_IndustrialGT_Eta_ISO &" %", REPORT & "Fullset", BLUE
result "     * T4 ISO =" &fv_Demo_IndustrialGT_T4_ISO &" degC", REPORT & "Fullset", BLUE
set_channel Demo_IndustrialGT_GG_PT_Status, 23
'delay 1
result "Thermodynamic measurement GG4_PT3 completed", REPORT & "Fullset", GREEN
result " ", REPORT
result " ", REPORT



'************************************ PT4 *************************************

note "Going to GG4_PT4"


set_channel Demo_IndustrialGT_GG_PT_Selector, 15
set_channel Demo_IndustrialGT_GG_PT_Status, 15

set_channel Demo_IndustrialGT_GG_Target_ISO, 12700
set_channel Demo_IndustrialGT_PT_Target_ISO, 12600
do_fullset 0
result "Going to GG speed ISO target = " &cv_Demo_IndustrialGT_GG_Target_ISO &" rpm and PT speed ISO target = " &cv_Demo_IndustrialGT_PT_Target_ISO &" rpm", REPORT & "Set Point", BLACK
'delay 1

result "     * Estimated GG speed target = " &cv_Demo_IndustrialGT_GG_Target &" rpm", REPORT & "Set Point", BLUE
result "     * Estimated GG speed target = " &cv_Demo_IndustrialGT_PT_Target &" rpm", REPORT & "Set Point", BLUE
set_channel Sim_IndustrialGT_N_GG, cv_Demo_IndustrialGT_GG_Target
set_channel Sim_IndustrialGT_N_PT, cv_Demo_IndustrialGT_PT_Target


set_channel Sim_IndustrialGT_N_GG, 12945
set_channel Sim_IndustrialGT_N_PT, 12807
set_channel Sim_IndustrialGT_N_Generator, 8066
set_channel Sim_IndustrialGT_T_M, 6174.5
set_channel Sim_IndustrialGT_ZI_0404030, 1.9
set_channel Sim_IndustrialGT_P_Baro, 1.0147
set_channel Sim_IndustrialGT_ME_0405690, 51.8
set_channel Sim_IndustrialGT_PDT_2210, -2.22
set_channel Sim_IndustrialGT_PDT_400X, 0.0492


set_channel Sim_IndustrialGT_TE_0404000_A, 24.5
set_channel Sim_IndustrialGT_TE_0404000_B, 24.2
set_channel Sim_IndustrialGT_PD_Inlet_A, -0.0079
set_channel Sim_IndustrialGT_PD_Inlet_B, -0.009
set_channel Sim_IndustrialGT_PT_0404000, 0.01105
set_channel Sim_IndustrialGT_TE_0404900, 394.4
set_channel Sim_IndustrialGT_PT_0404900, 11.904
set_channel Sim_IndustrialGT_TE_040461X, 647.125
set_channel Sim_IndustrialGT_PT_040460X, 1.89015
set_channel Sim_IndustrialGT_TE_0404650, 464.5
set_channel Sim_IndustrialGT_PT_0404650, -0.00445
set_channel Sim_IndustrialGT_TT_040_2001, 32.7
set_channel Sim_IndustrialGT_PT_040_2001, 24.2199
set_channel Sim_IndustrialGT_FT_040_2001, 1944.8
set_channel Sim_IndustrialGT_T_O_in, 49.6
set_channel Sim_IndustrialGT_T_O_GG_fr_out, 60.9
set_channel Sim_IndustrialGT_T_O_GG_re_out, 78.2
set_channel Sim_IndustrialGT_T_O_PT_out, 76.6
set_channel Sim_IndustrialGT_P_O_GG_fr, 2.1768
set_channel Sim_IndustrialGT_P_O_GG_re, 2.0539
set_channel Sim_IndustrialGT_P_O_PT, 1.9326
set_channel Sim_IndustrialGT_F_O_GG_fr, 228.8
set_channel Sim_IndustrialGT_F_O_GG_re, 48.5
set_channel Sim_IndustrialGT_F_O_PT, 179.5


set_channel Sim_IndustrialGT_TE_0401110_A, 85.1
set_channel Sim_IndustrialGT_TE_0401110_B, 88
set_channel Sim_IndustrialGT_TE_0401120_A, 71.5
set_channel Sim_IndustrialGT_TE_0401120_B, 71.3
set_channel Sim_IndustrialGT_TE_0401130_A, 72.1
set_channel Sim_IndustrialGT_TE_0401130_B, 70.9
set_channel Sim_IndustrialGT_TE_0401140_A, 70.3
set_channel Sim_IndustrialGT_TE_0401140_B, 70.3
set_channel Sim_IndustrialGT_TE_0401310_A, 68.4
set_channel Sim_IndustrialGT_TE_0401310_B, 69.7
set_channel Sim_IndustrialGT_TE_0401320_A, 79.7
set_channel Sim_IndustrialGT_TE_0401320_B, 77.3
set_channel Sim_IndustrialGT_TE_0401330_A, 73.1
set_channel Sim_IndustrialGT_TE_0401330_B, 70.9
set_channel Sim_IndustrialGT_TE_0401340_A, 69.1
set_channel Sim_IndustrialGT_TE_0401340_B, 68.8


set_channel Sim_IndustrialGT_T_O_LG_in, 49.7
set_channel Sim_IndustrialGT_T_O_LG_out, 66.3
set_channel Sim_IndustrialGT_F_O_LG, 304.3


'delay 8
beep 1


set_channel Demo_IndustrialGT_GG_PT_Status, 21
result "Stabilizing - Minimum 5 minutes ...", REPORT & "Stabilization", BLACK
'delay 1
result "Stabilization completed", REPORT & "Stabilization", GREEN
'delay 1

set_channel Demo_IndustrialGT_GG_PT_Status, 22
'delay 1
do_fullset 1, "Thermodynamic measurement: N_GG4 N_PT4", "GG4_PT4"
result "A steady-state measurement has been taken automatically", REPORT & "Fullset", BLACK
result "     * GG speed ISO =" &fv_Demo_IndustrialGT_N_GG_ISO &" rpm", REPORT & "Fullset", BLUE
'result "         ** GG target offset =" &FormatNumber(fv_Demo_IndustrialGT_N_GG_ISO-fv_Demo_IndustrialGT_GG_Target_ISO,0) & " rpm", REPORT & "Fullset", RED
result "     * PT speed ISO =" &fv_Demo_IndustrialGT_N_PT_ISO &" rpm", REPORT & "Fullset", BLUE
'result "         ** PT target offset =" &FormatNumber(fv_Demo_IndustrialGT_N_PT_ISO-fv_Demo_IndustrialGT_PT_Target_ISO,0) & " rpm", REPORT & "Fullset", RED
result "     * Power ISO =" &fv_Demo_IndustrialGT_Pow_ISO &" kW", REPORT & "Fullset", BLUE
result "     * Efficiency ISO =" &fv_Demo_IndustrialGT_Eta_ISO &" %", REPORT & "Fullset", BLUE
result "     * T4 ISO =" &fv_Demo_IndustrialGT_T4_ISO &" degC", REPORT & "Fullset", BLUE
set_channel Demo_IndustrialGT_GG_PT_Status, 23
'delay 1
result "Thermodynamic measurement GG4_PT4 completed", REPORT & "Fullset", GREEN
result " ", REPORT
result " ", REPORT
result " *** All GG4 measurements have been completed ***", REPORT & "Fullset", GREEN
result " ", REPORT
result " ", REPORT


'******************************************************************************
'************************************ GG5 *************************************
'******************************************************************************
caution "GG5"
'************************************ PT1 *************************************


note "Going to GG5_PT1"


set_channel Demo_IndustrialGT_GG_PT_Selector, 16
set_channel Demo_IndustrialGT_GG_PT_Status, 16

set_channel Demo_IndustrialGT_GG_Target_ISO, -88888
set_channel Demo_IndustrialGT_PT_Target_ISO, 6000
do_fullset 0

result "Going to GG speed ISO target = " &cv_Demo_IndustrialGT_GG_Target_ISO &" rpm and PT speed ISO target = " &cv_Demo_IndustrialGT_PT_Target_ISO &" rpm", REPORT & "Set Point", BLACK
delay 1


result "     * Estimated GG speed target = " &cv_Demo_IndustrialGT_GG_Target &" rpm", REPORT & "Set Point", BLUE
result "     * Estimated PT speed target = " &cv_Demo_IndustrialGT_PT_Target &" rpm", REPORT & "Set Point", BLUE



set_channel Sim_IndustrialGT_N_GG, 13336
set_channel Sim_IndustrialGT_N_PT, 7348
set_channel Sim_IndustrialGT_N_Generator, 4624
set_channel Sim_IndustrialGT_T_M, 12895.5
set_channel Sim_IndustrialGT_ZI_0404030, -2.4
set_channel Sim_IndustrialGT_P_Baro, 1.0144
set_channel Sim_IndustrialGT_ME_0405690, 49.3
set_channel Sim_IndustrialGT_PDT_2210, -2.56
set_channel Sim_IndustrialGT_PDT_400X, 0.0584


set_channel Sim_IndustrialGT_TE_0404000_A, 25
set_channel Sim_IndustrialGT_TE_0404000_B, 24.7
set_channel Sim_IndustrialGT_PD_Inlet_A, -0.0094
set_channel Sim_IndustrialGT_PD_Inlet_B, -0.0103
set_channel Sim_IndustrialGT_PT_0404000, 0.01285
set_channel Sim_IndustrialGT_TE_0404900, 419.55
set_channel Sim_IndustrialGT_PT_0404900, 13.48055
set_channel Sim_IndustrialGT_TE_040461X, 702.575
set_channel Sim_IndustrialGT_PT_040460X, 2.2343
set_channel Sim_IndustrialGT_TE_0404650, 508.75
set_channel Sim_IndustrialGT_PT_0404650, -0.0037
set_channel Sim_IndustrialGT_TT_040_2001, 33.5
set_channel Sim_IndustrialGT_PT_040_2001, 24.0543
set_channel Sim_IndustrialGT_FT_040_2001, 2313.1
set_channel Sim_IndustrialGT_T_O_in, 49.5
set_channel Sim_IndustrialGT_T_O_GG_fr_out, 61.6
set_channel Sim_IndustrialGT_T_O_GG_re_out, 81.8
set_channel Sim_IndustrialGT_T_O_PT_out, 69
set_channel Sim_IndustrialGT_P_O_GG_fr, 2.2167
set_channel Sim_IndustrialGT_P_O_GG_re, 2.0871
set_channel Sim_IndustrialGT_P_O_PT, 1.9701
set_channel Sim_IndustrialGT_F_O_GG_fr, 230.5
set_channel Sim_IndustrialGT_F_O_GG_re, 48.8
set_channel Sim_IndustrialGT_F_O_PT, 180.7


set_channel Sim_IndustrialGT_TE_0401110_A, 85.5
set_channel Sim_IndustrialGT_TE_0401110_B, 88.7
set_channel Sim_IndustrialGT_TE_0401120_A, 72.1
set_channel Sim_IndustrialGT_TE_0401120_B, 72.1
set_channel Sim_IndustrialGT_TE_0401130_A, 73
set_channel Sim_IndustrialGT_TE_0401130_B, 71.9
set_channel Sim_IndustrialGT_TE_0401140_A, 70.4
set_channel Sim_IndustrialGT_TE_0401140_B, 70.1
set_channel Sim_IndustrialGT_TE_0401310_A, 59.1
set_channel Sim_IndustrialGT_TE_0401310_B, 60.6
set_channel Sim_IndustrialGT_TE_0401320_A, 68.1
set_channel Sim_IndustrialGT_TE_0401320_B, 66
set_channel Sim_IndustrialGT_TE_0401330_A, 59.1
set_channel Sim_IndustrialGT_TE_0401330_B, 57.9
set_channel Sim_IndustrialGT_TE_0401340_A, 64.8
set_channel Sim_IndustrialGT_TE_0401340_B, 66


set_channel Sim_IndustrialGT_T_O_LG_in, 49.6
set_channel Sim_IndustrialGT_T_O_LG_out, 57.4
set_channel Sim_IndustrialGT_F_O_LG, 294.8


'delay 8
beep 1

set_channel Demo_IndustrialGT_GG_PT_Status, 21
result "Stabilizing - Minimum 10 minutes ...", REPORT & "Stabilization", BLACK
'delay 1
result "Halfway - 5 more minutes ...", REPORT & "Stabilization", BLACK
'delay 1
result "Stabilization completed", REPORT & "Stabilization", GREEN
'delay 1

set_channel Demo_IndustrialGT_GG_PT_Status, 22
'delay 1
do_fullset 1, "Thermodynamic measurement: N_GG5 N_PT1", "GG5_PT1"
result "A steady-state measurement has been taken automatically", REPORT & "Fullset", BLACK
result "     * GG speed ISO =" &fv_Demo_IndustrialGT_N_GG_ISO &" rpm", REPORT & "Fullset", BLUE
result "     * PT speed ISO =" &fv_Demo_IndustrialGT_N_PT_ISO &" rpm", REPORT & "Fullset", BLUE
result "     * Power ISO =" &fv_Demo_IndustrialGT_Pow_ISO &" kW", REPORT & "Fullset", BLUE
result "     * Efficiency ISO =" &fv_Demo_IndustrialGT_Eta_ISO &" %", REPORT & "Fullset", BLUE
result "     * T4 ISO =" &fv_Demo_IndustrialGT_T4_ISO &" degC", REPORT & "Fullset", BLUE
set_channel Demo_IndustrialGT_GG_PT_Status, 23
'delay 1
result "Thermodynamic measurement GG5_PT1 completed", REPORT & "Fullset", GREEN
result " ", REPORT
result " ", REPORT



'************************************ PT2 *************************************

note "Going to GG5_PT2"

set_channel Demo_IndustrialGT_GG_PT_Selector, 17
set_channel Demo_IndustrialGT_GG_PT_Status, 17

set_channel Demo_IndustrialGT_GG_Target_ISO, -88888
set_channel Demo_IndustrialGT_PT_Target_ISO, 8400
do_fullset 0
result "Going to GG speed ISO target = " &cv_Demo_IndustrialGT_GG_Target_ISO &" rpm and PT speed ISO target = " &cv_Demo_IndustrialGT_PT_Target_ISO &" rpm", REPORT & "Set Point", BLACK
'delay 1


result "     * Estimated GG speed target = " &cv_Demo_IndustrialGT_GG_Target &" rpm", REPORT & "Set Point", BLUE
result "     * Estimated PT speed target = " &cv_Demo_IndustrialGT_PT_Target &" rpm", REPORT & "Set Point", BLUE



set_channel Sim_IndustrialGT_N_GG, 13335
set_channel Sim_IndustrialGT_N_PT, 8565
set_channel Sim_IndustrialGT_N_Generator, 5392
set_channel Sim_IndustrialGT_T_M, 11702.4
set_channel Sim_IndustrialGT_ZI_0404030, -2.3
set_channel Sim_IndustrialGT_P_Baro, 1.0144
set_channel Sim_IndustrialGT_ME_0405690, 48
set_channel Sim_IndustrialGT_PDT_2210, -2.55
set_channel Sim_IndustrialGT_PDT_400X, 0.0585


set_channel Sim_IndustrialGT_TE_0404000_A, 25.2
set_channel Sim_IndustrialGT_TE_0404000_B, 24.8
set_channel Sim_IndustrialGT_PD_Inlet_A, -0.0094
set_channel Sim_IndustrialGT_PD_Inlet_B, -0.0103
set_channel Sim_IndustrialGT_PT_0404000, 0.01285
set_channel Sim_IndustrialGT_TE_0404900, 419.4
set_channel Sim_IndustrialGT_PT_0404900, 13.4985
set_channel Sim_IndustrialGT_TE_040461X, 702.383333333333
set_channel Sim_IndustrialGT_PT_040460X, 2.2389
set_channel Sim_IndustrialGT_TE_0404650, 498.78125
set_channel Sim_IndustrialGT_PT_0404650, -0.00395
set_channel Sim_IndustrialGT_TT_040_2001, 33.5
set_channel Sim_IndustrialGT_PT_040_2001, 24.0472
set_channel Sim_IndustrialGT_FT_040_2001, 2311.5
set_channel Sim_IndustrialGT_T_O_in, 49.2
set_channel Sim_IndustrialGT_T_O_GG_fr_out, 61.5
set_channel Sim_IndustrialGT_T_O_GG_re_out, 81.6
set_channel Sim_IndustrialGT_T_O_PT_out, 70.8
set_channel Sim_IndustrialGT_P_O_GG_fr, 2.2132
set_channel Sim_IndustrialGT_P_O_GG_re, 2.0812
set_channel Sim_IndustrialGT_P_O_PT, 1.9666
set_channel Sim_IndustrialGT_F_O_GG_fr, 230.2
set_channel Sim_IndustrialGT_F_O_GG_re, 48.7
set_channel Sim_IndustrialGT_F_O_PT, 180.2


set_channel Sim_IndustrialGT_TE_0401110_A, 85.5
set_channel Sim_IndustrialGT_TE_0401110_B, 88.6
set_channel Sim_IndustrialGT_TE_0401120_A, 72
set_channel Sim_IndustrialGT_TE_0401120_B, 71.9
set_channel Sim_IndustrialGT_TE_0401130_A, 72.8
set_channel Sim_IndustrialGT_TE_0401130_B, 71.7
set_channel Sim_IndustrialGT_TE_0401140_A, 70.3
set_channel Sim_IndustrialGT_TE_0401140_B, 69.9
set_channel Sim_IndustrialGT_TE_0401310_A, 60.6
set_channel Sim_IndustrialGT_TE_0401310_B, 62
set_channel Sim_IndustrialGT_TE_0401320_A, 70.3
set_channel Sim_IndustrialGT_TE_0401320_B, 68
set_channel Sim_IndustrialGT_TE_0401330_A, 61.4
set_channel Sim_IndustrialGT_TE_0401330_B, 60
set_channel Sim_IndustrialGT_TE_0401340_A, 65
set_channel Sim_IndustrialGT_TE_0401340_B, 65.9


set_channel Sim_IndustrialGT_T_O_LG_in, 49.3
set_channel Sim_IndustrialGT_T_O_LG_out, 58.7
set_channel Sim_IndustrialGT_F_O_LG, 297.2

'delay 8
beep 1

set_channel Demo_IndustrialGT_GG_PT_Status, 21
result "Stabilizing - Minimum 5 minutes ...", REPORT & "Stabilization", BLACK
'delay 1
result "Stabilization completed", REPORT & "Stabilization", GREEN
'delay 1

set_channel Demo_IndustrialGT_GG_PT_Status, 22
'delay 1
do_fullset 1, "Thermodynamic measurement: N_GG5 N_PT2", "GG5_PT2"
result "A steady-state measurement has been taken automatically", REPORT & "Fullset", BLACK

result "     * PT speed ISO =" &fv_Demo_IndustrialGT_N_PT_ISO &" rpm", REPORT & "Fullset", BLUE
result "         ** GG target offset =" &FormatNumber(fv_Demo_IndustrialGT_N_PT_ISO-fv_Demo_IndustrialGT_PT_Target_ISO,0) & " rpm", REPORT & "Fullset", RED
result "     * Power ISO =" &fv_Demo_IndustrialGT_Pow_ISO &" kW", REPORT & "Fullset", BLUE
result "     * Efficiency ISO =" &fv_Demo_IndustrialGT_Eta_ISO &" %", REPORT & "Fullset", BLUE
result "     * T4 ISO =" &fv_Demo_IndustrialGT_T4_ISO &" degC", REPORT & "Fullset", BLUE
set_channel Demo_IndustrialGT_GG_PT_Status, 23
'delay 1
result "Thermodynamic measurement GG5_PT2 completed", REPORT & "Fullset", GREEN
result " ", REPORT
result " ", REPORT



'************************************ PT3 *************************************

note "Going to GG5_PT3"

set_channel Demo_IndustrialGT_GG_PT_Selector, 18
set_channel Demo_IndustrialGT_GG_PT_Status, 18

set_channel Demo_IndustrialGT_GG_Target_ISO, -88888
set_channel Demo_IndustrialGT_PT_Target_ISO, 10800
do_fullset 0
result "Going to GG speed ISO target = " &cv_Demo_IndustrialGT_GG_Target_ISO &" rpm and PT speed ISO target = " &cv_Demo_IndustrialGT_PT_Target_ISO &" rpm", REPORT & "Set Point", BLACK
'delay 1


result "     * Estimated GG speed target = " &cv_Demo_IndustrialGT_GG_Target &" rpm", REPORT & "Set Point", BLUE
result "     * Estimated GG speed target = " &cv_Demo_IndustrialGT_PT_Target &" rpm", REPORT & "Set Point", BLUE




set_channel Sim_IndustrialGT_N_GG, 13334
set_channel Sim_IndustrialGT_N_PT, 11011
set_channel Sim_IndustrialGT_N_Generator, 6934
set_channel Sim_IndustrialGT_T_M, 9505.7
set_channel Sim_IndustrialGT_ZI_0404030, -2.3
set_channel Sim_IndustrialGT_P_Baro, 1.0143
set_channel Sim_IndustrialGT_ME_0405690, 47.8
set_channel Sim_IndustrialGT_PDT_2210, -2.53
set_channel Sim_IndustrialGT_PDT_400X, 0.0583


set_channel Sim_IndustrialGT_TE_0404000_A, 25.5
set_channel Sim_IndustrialGT_TE_0404000_B, 25.2
set_channel Sim_IndustrialGT_PD_Inlet_A, -0.0092
set_channel Sim_IndustrialGT_PD_Inlet_B, -0.0103
set_channel Sim_IndustrialGT_PT_0404000, 0.01275
set_channel Sim_IndustrialGT_TE_0404900, 420.1
set_channel Sim_IndustrialGT_PT_0404900, 13.48125
set_channel Sim_IndustrialGT_TE_040461X, 704.366666666667
set_channel Sim_IndustrialGT_PT_040460X, 2.24095
set_channel Sim_IndustrialGT_TE_0404650, 489
set_channel Sim_IndustrialGT_PT_0404650, -0.00455
set_channel Sim_IndustrialGT_TT_040_2001, 33.6
set_channel Sim_IndustrialGT_PT_040_2001, 24.0451
set_channel Sim_IndustrialGT_FT_040_2001, 2319
set_channel Sim_IndustrialGT_T_O_in, 48.5
set_channel Sim_IndustrialGT_T_O_GG_fr_out, 61
set_channel Sim_IndustrialGT_T_O_GG_re_out, 81.3
set_channel Sim_IndustrialGT_T_O_PT_out, 74.6
set_channel Sim_IndustrialGT_P_O_GG_fr, 2.1908
set_channel Sim_IndustrialGT_P_O_GG_re, 2.0599
set_channel Sim_IndustrialGT_P_O_PT, 1.9456
set_channel Sim_IndustrialGT_F_O_GG_fr, 228.5
set_channel Sim_IndustrialGT_F_O_GG_re, 48.4
set_channel Sim_IndustrialGT_F_O_PT, 178.7


set_channel Sim_IndustrialGT_TE_0401110_A, 85.2
set_channel Sim_IndustrialGT_TE_0401110_B, 88.2
set_channel Sim_IndustrialGT_TE_0401120_A, 71.6
set_channel Sim_IndustrialGT_TE_0401120_B, 71.5
set_channel Sim_IndustrialGT_TE_0401130_A, 72.4
set_channel Sim_IndustrialGT_TE_0401130_B, 71.1
set_channel Sim_IndustrialGT_TE_0401140_A, 70
set_channel Sim_IndustrialGT_TE_0401140_B, 69.6
set_channel Sim_IndustrialGT_TE_0401310_A, 64.3
set_channel Sim_IndustrialGT_TE_0401310_B, 65.9
set_channel Sim_IndustrialGT_TE_0401320_A, 75.6
set_channel Sim_IndustrialGT_TE_0401320_B, 72.8
set_channel Sim_IndustrialGT_TE_0401330_A, 67.2
set_channel Sim_IndustrialGT_TE_0401330_B, 65.3
set_channel Sim_IndustrialGT_TE_0401340_A, 67.8
set_channel Sim_IndustrialGT_TE_0401340_B, 67.1


set_channel Sim_IndustrialGT_T_O_LG_in, 48.6
set_channel Sim_IndustrialGT_T_O_LG_out, 62.2
set_channel Sim_IndustrialGT_F_O_LG, 300.6


'delay 8
beep 1

set_channel Demo_IndustrialGT_GG_PT_Status, 21
result "Stabilizing - Minimum 5 minutes ...", REPORT & "Stabilization", BLACK
'delay 1
result "Stabilization completed", REPORT & "Stabilization", GREEN
'delay 1

set_channel Demo_IndustrialGT_GG_PT_Status, 22
'delay 1
do_fullset 1, "Thermodynamic measurement: N_GG5 N_PT3", "GG5_PT3"
result "A steady-state measurement has been taken automatically", REPORT & "Fullset", BLACK
result "     * GG speed ISO =" &fv_Demo_IndustrialGT_N_PT_ISO &" rpm", REPORT & "Fullset", BLUE
result "         ** GG target offset =" &FormatNumber(fv_Demo_IndustrialGT_N_PT_ISO-fv_Demo_IndustrialGT_PT_Target_ISO,0) & " rpm", REPORT & "Fullset", RED
result "     * Power ISO =" &fv_Demo_IndustrialGT_Pow_ISO &" kW", REPORT & "Fullset", BLUE
result "     * Efficiency ISO =" &fv_Demo_IndustrialGT_Eta_ISO &" %", REPORT & "Fullset", BLUE
result "     * T4 ISO =" &fv_Demo_IndustrialGT_T4_ISO &" degC", REPORT & "Fullset", BLUE
set_channel Demo_IndustrialGT_GG_PT_Status, 23
'delay 1
result "Thermodynamic measurement GG5_PT3 completed", REPORT & "Fullset", GREEN
result " ", REPORT
result " ", REPORT



'************************************ PT4 *************************************

note "Going to GG5_PT4"

set_channel Demo_IndustrialGT_GG_PT_Selector, 19
set_channel Demo_IndustrialGT_GG_PT_Status, 19

set_channel Demo_IndustrialGT_GG_Target_ISO, -88888
set_channel Demo_IndustrialGT_PT_Target_ISO, 12000
do_fullset 0
result "Going to GG speed ISO target = " &cv_Demo_IndustrialGT_GG_Target_ISO &" rpm and PT speed ISO target = " &cv_Demo_IndustrialGT_PT_Target_ISO &" rpm", REPORT & "Set Point", BLACK
'delay 1


result "     * Estimated GG speed target = " &cv_Demo_IndustrialGT_GG_Target &" rpm", REPORT & "Set Point", BLUE
result "     * Estimated GG speed target = " &cv_Demo_IndustrialGT_PT_Target &" rpm", REPORT & "Set Point", BLUE


set_channel Sim_IndustrialGT_N_GG, 13335
set_channel Sim_IndustrialGT_N_PT, 12226
set_channel Sim_IndustrialGT_N_Generator, 7701
set_channel Sim_IndustrialGT_T_M, 8415.8
set_channel Sim_IndustrialGT_ZI_0404030, -2.3
set_channel Sim_IndustrialGT_P_Baro, 1.0142
set_channel Sim_IndustrialGT_ME_0405690, 48.2
set_channel Sim_IndustrialGT_PDT_2210, -2.53
set_channel Sim_IndustrialGT_PDT_400X, 0.0582


set_channel Sim_IndustrialGT_TE_0404000_A, 25.4
set_channel Sim_IndustrialGT_TE_0404000_B, 25.1
set_channel Sim_IndustrialGT_PD_Inlet_A, -0.0094
set_channel Sim_IndustrialGT_PD_Inlet_B, -0.0102
set_channel Sim_IndustrialGT_PT_0404000, 0.0129
set_channel Sim_IndustrialGT_TE_0404900, 419.75
set_channel Sim_IndustrialGT_PT_0404900, 13.4433
set_channel Sim_IndustrialGT_TE_040461X, 699.725
set_channel Sim_IndustrialGT_PT_040460X, 2.21805
set_channel Sim_IndustrialGT_TE_0404650, 485.8375
set_channel Sim_IndustrialGT_PT_0404650, -0.00435
set_channel Sim_IndustrialGT_TT_040_2001, 33.7
set_channel Sim_IndustrialGT_PT_040_2001, 24.0629
set_channel Sim_IndustrialGT_FT_040_2001, 2298.5
set_channel Sim_IndustrialGT_T_O_in, 48.5
set_channel Sim_IndustrialGT_T_O_GG_fr_out, 61
set_channel Sim_IndustrialGT_T_O_GG_re_out, 81.2
set_channel Sim_IndustrialGT_T_O_PT_out, 76.5
set_channel Sim_IndustrialGT_P_O_GG_fr, 2.1825
set_channel Sim_IndustrialGT_P_O_GG_re, 2.0554
set_channel Sim_IndustrialGT_P_O_PT, 1.937
set_channel Sim_IndustrialGT_F_O_GG_fr, 228.1
set_channel Sim_IndustrialGT_F_O_GG_re, 48.3
set_channel Sim_IndustrialGT_F_O_PT, 178.6


set_channel Sim_IndustrialGT_TE_0401110_A, 85.2
set_channel Sim_IndustrialGT_TE_0401110_B, 88.2
set_channel Sim_IndustrialGT_TE_0401120_A, 71.5
set_channel Sim_IndustrialGT_TE_0401120_B, 71.5
set_channel Sim_IndustrialGT_TE_0401130_A, 72.2
set_channel Sim_IndustrialGT_TE_0401130_B, 71.1
set_channel Sim_IndustrialGT_TE_0401140_A, 69.8
set_channel Sim_IndustrialGT_TE_0401140_B, 69.5
set_channel Sim_IndustrialGT_TE_0401310_A, 66.6
set_channel Sim_IndustrialGT_TE_0401310_B, 68.1
set_channel Sim_IndustrialGT_TE_0401320_A, 77.9
set_channel Sim_IndustrialGT_TE_0401320_B, 75.3
set_channel Sim_IndustrialGT_TE_0401330_A, 70.7
set_channel Sim_IndustrialGT_TE_0401330_B, 68.7
set_channel Sim_IndustrialGT_TE_0401340_A, 68.5
set_channel Sim_IndustrialGT_TE_0401340_B, 67.8


set_channel Sim_IndustrialGT_T_O_LG_in, 48.7
set_channel Sim_IndustrialGT_T_O_LG_out, 64.7
set_channel Sim_IndustrialGT_F_O_LG, 302.5


'delay 8
beep 1

set_channel Demo_IndustrialGT_GG_PT_Status, 21
result "Stabilizing - Minimum 5 minutes ...", REPORT & "Stabilization", BLACK
'delay 1
result "Stabilization completed", REPORT & "Stabilization", GREEN
'delay 1

set_channel Demo_IndustrialGT_GG_PT_Status, 22
'delay 1
do_fullset 1, "Thermodynamic measurement: N_GG5 N_PT4", "GG5_PT4"
result "A steady-state measurement has been taken automatically", REPORT & "Fullset", BLACK
result "     * GG speed ISO =" &fv_Demo_IndustrialGT_N_PT_ISO &" rpm", REPORT & "Fullset", BLUE
result "         ** GG target offset =" &FormatNumber(fv_Demo_IndustrialGT_N_PT_ISO-fv_Demo_IndustrialGT_PT_Target_ISO,0) & " rpm", REPORT & "Fullset", RED
result "     * Power ISO =" &fv_Demo_IndustrialGT_Pow_ISO &" kW", REPORT & "Fullset", BLUE
result "     * Efficiency ISO =" &fv_Demo_IndustrialGT_Eta_ISO &" %", REPORT & "Fullset", BLUE
result "     * T4 ISO =" &fv_Demo_IndustrialGT_T4_ISO &" degC", REPORT & "Fullset", BLUE
set_channel Demo_IndustrialGT_GG_PT_Status, 23
'delay 1
result "Thermodynamic measurement GG5_PT4 completed", REPORT & "Fullset", GREEN
result " ", REPORT
result " ", REPORT



'************************************ PT5 *************************************

note "Going to GG5_PT5"

set_channel Demo_IndustrialGT_GG_PT_Selector, 20
set_channel Demo_IndustrialGT_GG_PT_Status, 20

set_channel Demo_IndustrialGT_GG_Target_ISO, -88888
set_channel Demo_IndustrialGT_PT_Target_ISO, 12600
do_fullset 0
result "Going to GG speed ISO target = " &cv_Demo_IndustrialGT_GG_Target_ISO &" rpm and PT speed ISO target = " &cv_Demo_IndustrialGT_PT_Target_ISO &" rpm", REPORT & "Set Point", BLACK
'delay 1

result "     * Estimated GG speed target = " &cv_Demo_IndustrialGT_GG_Target &" rpm", REPORT & "Set Point", BLUE
result "     * Estimated GG speed target = " &cv_Demo_IndustrialGT_PT_Target &" rpm", REPORT & "Set Point", BLUE



set_channel Sim_IndustrialGT_N_GG, 13334
set_channel Sim_IndustrialGT_N_PT, 12844
set_channel Sim_IndustrialGT_N_Generator, 8090
set_channel Sim_IndustrialGT_T_M, 7834.8
set_channel Sim_IndustrialGT_ZI_0404030, -2.1
set_channel Sim_IndustrialGT_P_Baro, 1.0141
set_channel Sim_IndustrialGT_ME_0405690, 45.3
set_channel Sim_IndustrialGT_PDT_2210, -2.55
set_channel Sim_IndustrialGT_PDT_400X, 0.0581


set_channel Sim_IndustrialGT_TE_0404000_A, 26.3
set_channel Sim_IndustrialGT_TE_0404000_B, 26
set_channel Sim_IndustrialGT_PD_Inlet_A, -0.0091
set_channel Sim_IndustrialGT_PD_Inlet_B, -0.0101
set_channel Sim_IndustrialGT_PT_0404000, 0.01275
set_channel Sim_IndustrialGT_TE_0404900, 420.45
set_channel Sim_IndustrialGT_PT_0404900, 13.3839
set_channel Sim_IndustrialGT_TE_040461X, 696.933333333333
set_channel Sim_IndustrialGT_PT_040460X, 2.1938
set_channel Sim_IndustrialGT_TE_0404650, 485.48125
set_channel Sim_IndustrialGT_PT_0404650, -0.00445
set_channel Sim_IndustrialGT_TT_040_2001, 33.8
set_channel Sim_IndustrialGT_PT_040_2001, 24.0802
set_channel Sim_IndustrialGT_FT_040_2001, 2274.2
set_channel Sim_IndustrialGT_T_O_in, 49.5
set_channel Sim_IndustrialGT_T_O_GG_fr_out, 61.6
set_channel Sim_IndustrialGT_T_O_GG_re_out, 81.8
set_channel Sim_IndustrialGT_T_O_PT_out, 78.3
set_channel Sim_IndustrialGT_P_O_GG_fr, 2.1687
set_channel Sim_IndustrialGT_P_O_GG_re, 2.0501
set_channel Sim_IndustrialGT_P_O_PT, 1.9256
set_channel Sim_IndustrialGT_F_O_GG_fr, 227.8
set_channel Sim_IndustrialGT_F_O_GG_re, 48.2
set_channel Sim_IndustrialGT_F_O_PT, 178.8


set_channel Sim_IndustrialGT_TE_0401110_A, 85.6
set_channel Sim_IndustrialGT_TE_0401110_B, 88.5
set_channel Sim_IndustrialGT_TE_0401120_A, 72.1
set_channel Sim_IndustrialGT_TE_0401120_B, 72.1
set_channel Sim_IndustrialGT_TE_0401130_A, 73
set_channel Sim_IndustrialGT_TE_0401130_B, 71.8
set_channel Sim_IndustrialGT_TE_0401140_A, 70.4
set_channel Sim_IndustrialGT_TE_0401140_B, 70.2
set_channel Sim_IndustrialGT_TE_0401310_A, 68.3
set_channel Sim_IndustrialGT_TE_0401310_B, 69.8
set_channel Sim_IndustrialGT_TE_0401320_A, 79.5
set_channel Sim_IndustrialGT_TE_0401320_B, 77.1
set_channel Sim_IndustrialGT_TE_0401330_A, 73.3
set_channel Sim_IndustrialGT_TE_0401330_B, 71.3
set_channel Sim_IndustrialGT_TE_0401340_A, 70.5
set_channel Sim_IndustrialGT_TE_0401340_B, 69.4


set_channel Sim_IndustrialGT_T_O_LG_in, 49.7
set_channel Sim_IndustrialGT_T_O_LG_out, 67
set_channel Sim_IndustrialGT_F_O_LG, 303.3


'delay 8
beep 1

set_channel Demo_IndustrialGT_GG_PT_Status, 21
result "Stabilizing - Minimum 5 minutes ...", REPORT & "Stabilization", BLACK
'delay 1
result "Stabilization completed", REPORT & "Stabilization", GREEN
'delay 1

set_channel Demo_IndustrialGT_GG_PT_Status, 22
'delay 1
do_fullset 1, "Thermodynamic measurement: N_GG5 N_PT5", "GG5_PT5"
result "A steady-state measurement has been taken automatically", REPORT & "Fullset", BLACK
result "     * GG speed ISO =" &fv_Demo_IndustrialGT_N_PT_ISO &" rpm", REPORT & "Fullset", BLUE
result "         ** GG target offset =" &FormatNumber(fv_Demo_IndustrialGT_N_PT_ISO-fv_Demo_IndustrialGT_PT_Target_ISO,0) & " rpm", REPORT & "Fullset", RED
result "     * Power ISO =" &fv_Demo_IndustrialGT_Pow_ISO &" kW", REPORT & "Fullset", BLUE
result "     * Efficiency ISO =" &fv_Demo_IndustrialGT_Eta_ISO &" %", REPORT & "Fullset", BLUE
result "     * T4 ISO =" &fv_Demo_IndustrialGT_T4_ISO &" degC", REPORT & "Fullset", BLUE
set_channel Demo_IndustrialGT_GG_PT_Status, 23
'delay 1
result "Thermodynamic measurement GG5_PT5 completed", REPORT & "Fullset", GREEN
result " ", REPORT
result " ", REPORT
result " *** All GG5 measurements have been completed ***", REPORT & "Fullset", GREEN
result " ", REPORT
result " ", REPORT



' *********************************************************************
' ******************** REINI ********************
' *********************************************************************

note "Reinitialization"

result " ***** THERMODYNAMIC VERIFICATION TEST has been completed *****", REPORT & "Fullset", RED

set_channel Demo_IndustrialGT_GG_PT_Selector, 0
set_channel Demo_IndustrialGT_GG_PT_Status, 0

set_channel Demo_IndustrialGT_GG_Target_ISO, -88888
set_channel Demo_IndustrialGT_PT_Target_ISO, -88888

set_channel Sim_IndustrialGT_N_GG, 11000
set_channel Sim_IndustrialGT_N_PT, 5500
set_channel Sim_IndustrialGT_N_Generator, 3816
set_channel Sim_IndustrialGT_T_M, 8000
set_channel Sim_IndustrialGT_ZI_0404030, 14
set_channel Sim_IndustrialGT_P_Baro, 1.0155
set_channel Sim_IndustrialGT_ME_0405690, 64
set_channel Sim_IndustrialGT_PDT_2210, -1.3
set_channel Sim_IndustrialGT_PDT_400X, 0.0272
'set_channel Sim_IndustrialGT_TE_400X, 21
set_channel Sim_IndustrialGT_TE_0404000_A, 21.6
set_channel Sim_IndustrialGT_TE_0404000_B, 21.4
set_channel Sim_IndustrialGT_PD_Inlet_A, -0.0047
set_channel Sim_IndustrialGT_PD_Inlet_B, -0.0052
set_channel Sim_IndustrialGT_PT_0404000, 0.00645
set_channel Sim_IndustrialGT_TE_0404900, 320.9
set_channel Sim_IndustrialGT_PT_0404900, 7.91
set_channel Sim_IndustrialGT_TE_040461X, 539.666666666667
set_channel Sim_IndustrialGT_PT_040460X, 1.1304
set_channel Sim_IndustrialGT_TE_0404650, 421.38125
set_channel Sim_IndustrialGT_PT_0404650, -0.00265
set_channel Sim_IndustrialGT_TT_040_2001, 20
set_channel Sim_IndustrialGT_PT_040_2001, 23
set_channel Sim_IndustrialGT_FT_040_2001, 1000
set_channel Sim_IndustrialGT_T_O_in, 41.6
set_channel Sim_IndustrialGT_T_O_GG_fr_out, 50.7
set_channel Sim_IndustrialGT_T_O_GG_re_out, 63
set_channel Sim_IndustrialGT_T_O_PT_out, 54.4
set_channel Sim_IndustrialGT_P_O_GG_fr, 2.3329
set_channel Sim_IndustrialGT_P_O_GG_re, 2.1272
set_channel Sim_IndustrialGT_P_O_PT, 2.0498
set_channel Sim_IndustrialGT_F_O_GG_fr, 233.5
set_channel Sim_IndustrialGT_F_O_GG_re, 49.9
set_channel Sim_IndustrialGT_F_O_PT, 181.7
'set_channel Sim_IndustrialGT_VE_0401060_X, 21
'set_channel Sim_IndustrialGT_VE_0401060_Y, 19
'set_channel Sim_IndustrialGT_VE_0401061_X, 15
'set_channel Sim_IndustrialGT_VE_0401061_Y, 13
'set_channel Sim_IndustrialGT_VE_0401260_X, 11
'set_channel Sim_IndustrialGT_VE_0401260_Y, 11
'set_channel Sim_IndustrialGT_VE_0401261_X, 13
'set_channel Sim_IndustrialGT_VE_0401261_Y, 12
'set_channel Sim_IndustrialGT_ZE_0401050_A, 0.04
'set_channel Sim_IndustrialGT_ZE_0401050_B, 0.04
'set_channel Sim_IndustrialGT_ZE_0401250_A, -0.01
'set_channel Sim_IndustrialGT_ZE_0401250_B, -0.03
set_channel Sim_IndustrialGT_TE_0401110_A, 79.2
set_channel Sim_IndustrialGT_TE_0401110_B, 81.9
set_channel Sim_IndustrialGT_TE_0401120_A, 63.6
set_channel Sim_IndustrialGT_TE_0401120_B, 63.2
set_channel Sim_IndustrialGT_TE_0401130_A, 61.8
set_channel Sim_IndustrialGT_TE_0401130_B, 61.3
set_channel Sim_IndustrialGT_TE_0401140_A, 56.3
set_channel Sim_IndustrialGT_TE_0401140_B, 57.3
set_channel Sim_IndustrialGT_TE_0401310_A, 50.7
set_channel Sim_IndustrialGT_TE_0401310_B, 52.1
set_channel Sim_IndustrialGT_TE_0401320_A, 58.7
set_channel Sim_IndustrialGT_TE_0401320_B, 56.9
set_channel Sim_IndustrialGT_TE_0401330_A, 49.3
set_channel Sim_IndustrialGT_TE_0401330_B, 48.8
set_channel Sim_IndustrialGT_TE_0401340_A, 51.7
set_channel Sim_IndustrialGT_TE_0401340_B, 50.9
'set_channel Sim_IndustrialGT_VE_9001000_X, 26
'set_channel Sim_IndustrialGT_VE_9001000_Y, 22
set_channel Sim_IndustrialGT_T_O_LG_in, 41.9
set_channel Sim_IndustrialGT_T_O_LG_out, 46.9
set_channel Sim_IndustrialGT_F_O_LG, 287.4

stop_log "Demo_Report"
result "A Transient Log recording the speeds has been stopped", REPORT & "Log", BLACK