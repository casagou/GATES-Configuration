'******************************************************************************
'* RTEStopScan.vbs
'******************************************************************************
'*  AUTHOR: Fereshteh Mahvarsayyad
'*
'*  DESCRIPTION:
'*    This script stops Alarm Summary, ARINC Display, and the Real Time Display(s)
'*    on the specied Pcs
'*
'*  DATE: 31-Sep-03 8:31:03 AM
'*
'*  NOTE:
'*    1) Update the "AlarmSumDispPC" variable, to name the Pc where the
'*    Alarm Summary Disply is to be stoped. This variable shall match the variable
'*    with the same name in the "RTEStartScan.vbs"
'*
'*    5) Update the "ARINCDispPC" variable, to name the Pc where the
'*    ARINC Disply is to be stoped. This variable shall match the variable
'*    with the same name in the "RTEStartScan.vbs".
'*
'*    6) Update the "RTDPCNames" variable to list the name of the Pcs where the
'*    Real Time Disply(s) are to be stoped. PC names shall be separated by comma
'*    with no space
'*
'*    7) The "RTDPCNames" shall match the variable with the same name in the
'*    "RTEStartScan.vbs" file.
'*
'*
'*  MODIFICATIONS:
'*    DATE         REV     INITIALS  DESCRIPTION
'*    ----------   -----   --------  --------------------------------------------------
'*    08-DEC-03            FM        Added Error handling
'******************************************************************************

Option Explicit

' These scripts are executed by nxDAS NXIF.SERVICE (see c:\nxDAS\Data\MgtGUI)
