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

instruction "Press PLAY read channel values from several nodes."

channel "alFloat5, FnMeas, TF125050, PAMB, M1900CLP, PressTriggerOut, GEOptica_Humidity, ROT_Humidity"

result "RTE Node channel values"
result " "

delay 1

result "RTE Calculated channel " & alFloat5 & " value is " & cv_alFloat5
result "RTE Thrust channel " & FnMeas & " value is " & cv_FnMeas
result "RTE TSM channel " & TF125050 & " value is " & cv_TF125050
result "RTE PBS channel " & PAMB & " value is " & cv_PAMB
result " "

delay 1

result "UEI Cube channel values"
result " "

delay 1

result "devCube001, dev02, ch00007 " & M1900CLP & " value is " & cv_M1900CLP
result "devCube023, dev01, ch00021 " & PressTriggerOut & " value is " & cv_PressTriggerOut
result " "

delay 1

result "GE Optica & Rotronic channel values"
result " "

delay 1

result "GE Optica " & GEOptica_Humidity & " value is " & cv_GEOptica_Humidity
result "Rotronic " & ROT_Humidity & " value is " & cv_ROT_Humidity

delay 1

result "Demo Read Value script is complete."

