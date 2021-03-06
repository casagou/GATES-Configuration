Option Explicit

'* <script.tps>
'******************************************************************************
'*  AUTHOR: <your name goes here>
'*
'*  DESCRIPTION:
'*  <describe the script here>
'*
'*  DATE: 07/01/2008 10:05:05 AM
'*
'*  MODIFICATIONS:
'*    DATE         WHO  NCR    DESCRIPTION
'*    ----------   ---  -----  --------------------------------------------------
'*
'******************************************************************************

instruction "Press PLAY to set a calculated channel value which will change an iDDS output channel."

result "Calculated channel AO_SlaveAnOut16 value will be changed to 5."
result "iDDS output channel SlaveAnOut16 value will change to 5 as a result."

Dim calc_curr_val, iDDS_curr_val

channel "AO_SlaveAnOut16, SlaveAnOut16"

calc_curr_val = cv_AO_SlaveAnOut16
iDDS_curr_val = cv_SlaveAnOut16

msgbox "Current value of AO_SlaveAnOut16 is " & calc_curr_val
msgbox "Current value of SlaveAnOut16 is " & iDDS_curr_val

set_channel AO_SlaveAnOut16, 5

calc_curr_val = cv_AO_SlaveAnOut16
iDDS_curr_val = cv_SlaveAnOut16

result "Calculated channel AO_SlaveAnOut16 value has been set to 5."

msgbox "Current value of AO_SlaveAnOut16 is " & calc_curr_val
msgbox "Current value of SlaveAnOut16 is " & iDDS_curr_val

instruction "Press PLAY to reset calculated channel value."

set_channel AO_SlaveAnOut16, 0

calc_curr_val = cv_AO_SlaveAnOut16
iDDS_curr_val = cv_SlaveAnOut16

result "Calculated channel AO_SlaveAnOut16 value has been reset to 0."

msgbox "Current value of AO_SlaveAnOut16 is " & calc_curr_val
msgbox "Current value of SlaveAnOut16 is " & iDDS_curr_val

result "Demo Set Value script is complete."

