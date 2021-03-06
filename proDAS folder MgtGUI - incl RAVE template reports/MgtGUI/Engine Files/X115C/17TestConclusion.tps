Option Explicit

'* <script.tps>
'******************************************************************************
'*  AUTHOR: Don Pereira
'*
'*  DESCRIPTION:
'*  <describe the script here>
'*
'*  DATE: 9/15/2005 8:48:57 AM
'*
'*  MODIFICATIONS:
'*    DATE         WHO  NCR    DESCRIPTION
'*    ----------   ---  -----  --------------------------------------------------
'*  V1.01  11/09/2001  RH   Initial
'*  V1.02  19/04/2002  JN   Added if logic to check if IDG installed
'*  V1.03  18/07/2002  TC   Removed ref tofuel preservation system and IDG Scav filter
'*  V1.04  15/09/2005  JC   Converted to phase 3 format
'*  V1.05  16/03/2015  SG   Added for Throttle Mark Three auto control
'******************************************************************************

' ***** LOCAL VARIABLE DECLARATIONS *****
Dim Conclude, CSDFilOK, EngFilInst, EngFilOK, EngFuelFilOK
Dim FuelLk, IDGReEng, In_ExhOK, lvMCDOK, OilLevelOK
Dim OilLk, RotorRot, TestEqRem

channel "Eng_On,IDG, FuelEnable"

'V1.05 set channel since in the auto mode Fuel_Enable will be set seperately to FuelOn
set_channel FuelEnable, 0
instruction "Make sure fuel is turned off on the Throttle Control page"

If cv_Eng_On = 1 Then
quit
End If

prompt_boo "Do you want to conclude this engine test?", Conclude
If Conclude = 0 Then
quit
End If

instruction "Check engine for leaks"
prompt_boo "Are there fuel leaks?", FuelLk
If FuelLk = TRUE Then
result "There are fuel leaks", REPORT & "LeaksCheck"
Else
result "There are no fuel leaks", REPORT & "LeaksCheck"
End If

prompt_boo "Are there oil leaks?", OilLk
If OilLk = TRUE Then
result "There are oil leaks", REPORT & "LeaksCheck"
Else
result "There are no oil leaks", REPORT & "LeaksCheck"
End If

instruction "Check magnetic chip detectors"
prompt_boo "Were all Magnetic Chip Detectors OK during test?", lvMCDOK
If lvMCDOK = TRUE Then
result "Magnetic Chip Detectors OK", REPORT & "MCDCheck"
Else
result "Magnetic Chip Detectors NOT OK", REPORT & "MCDCheck"
End If

instruction "Check engine fuel filter"
prompt_boo "Is engine fuel filter OK?", EngFuelFilOK
If EngFuelFilOK = TRUE Then
result "Engine fuel filter is OK", REPORT & "FuelFilterChk"
Else
result "Engine fuel filter is not OK", REPORT & "FuelFilterChk"
End If

instruction "Check engine oil filter"
prompt_boo "Is engine filter OK?", EngFilOK
If EngFilOK = TRUE Then
result "Engine filter is OK", REPORT & "OilFilterChk"
Else
result "Engine filter is not OK", REPORT & "OilFilterChk"
End If

instruction "Install new engine oil filter if necessary"
prompt_boo "Is engine filter installed?", EngFilInst
If EngFilInst = TRUE Then
result "New engine filter is installed", REPORT & "NewOilFilter"
Else
result "New engine filter is not installed", REPORT & "NewOilFilter"
End If

'*  V1.02 added if logic for IDG
If cv_IDG = 1 Then
'*  V1.02 instruction "Check IDG oil filter"
instruction "Check IDG oil filter if applicable"
prompt_boo "Is IDG filter OK?", CSDFilOK
If CSDFilOK = TRUE Then
result "IDG filter is OK", REPORT & "OilFilterChk"
Else
result "IDG filter is not OK", REPORT & "OilFilterChk"
End If

'*  V1.02 instruction "Re-Engage IDG."
instruction "Re-Engage IDG if applicable."
prompt_boo "Did you Re-Engange IDG?.", IDGReEng
If IDGReEng = TRUE Then
result "The IDG was Re-Engaged.", REPORT & "Shutdown_Check"
Else
result "The IDG was not Re-Engaged.", REPORT & "Shutdown_Check"
End If
'*  V1.02 added endif
End If

instruction " Check all oil levels"
prompt_boo "Were oil levels checked and topped up as required?", OilLevelOK
If OilLevelOK = TRUE Then
result "Oil levels were checked and retopped", REPORT & "OilLevelCheck"
Else
result "Oil levels are not satisfactory", REPORT & "OilLevelCheck"
End If

instruction "Check intake and exhaust."
prompt_boo "Was intake and exhaust check satisfactory?", In_ExhOK
If In_ExhOK = TRUE Then
result "Intake and exhaust checked OK.", REPORT & "IntakeExhaustCheck"
Else
result "A problem was found in the intake or exhaust.", REPORT & "IntakeExhaustCheck"
End If

instruction "Check rotors for freedom of rotation."
prompt_boo "Were rotors rotation found satisfactory when checked?", RotorRot
If RotorRot = TRUE Then
result "Rotors rotation found satisfactory.", REPORT & "RotorRotation"
Else
result "Rotors rotation were not satisfactory", REPORT & "RotorRotation"
End If

instruction "Remove all test equipment"
prompt_boo "Is test equipment removed?", TestEqRem
If TestEqRem = TRUE Then
result "Test equipment is removed", REPORT & "TestEquipment"
Else
result "Test equipment is not removed", REPORT & "TestEquipment"
End If

'do_fullset 1, "Test finish", "TestConclusion"
do_fullset 1, "Fullset_TestConclusion", "TestConclusion"
