Option Explicit

'* <script.tps>
'******************************************************************************
'*  AUTHOR: <Joachim Agou>
'*
'*  DESCRIPTION:
'*  Auto Start
'*
'*  DATE: 2 Dec 2016
'*
'*  MODIFICATIONS:
'*    DATE             WHO  NCR    DESCRIPTION
'*    -------------   ---  -----  --------------------------------------------------
'*  V0.1   2Dec2016   JOA          Initial
'*
'******************************************************************************

' Channel Registration
' channel "_Start, _FR, _RW, _Play, _FW, _RS, n_GG, StartReset, _Start, Start"
channel "_Start, _FR, _RW, _Play, _FW, _RS, n_GG, V_G_N"

'*  note 100% N2 = 14460 rpm; 100% N1 = 4784 rpm.
'*   *  *
instruction "Reset start calculations"
' set_channel "_Start, 0"
' set_channel Start, 0

' set_channel "_FR", 0
' set_channel "_RW", 0
' set_channel "_Play", 0
' set_channel "_FW", 0
' set_channel "_FW", 0

instruction "set _RS to 1"
' set_channel "_RS", 1
delay 2
instruction "set _RS to 0"
