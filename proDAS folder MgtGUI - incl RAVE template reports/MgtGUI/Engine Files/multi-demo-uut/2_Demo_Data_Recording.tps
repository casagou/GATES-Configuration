Option Explicit

'* <script.tps>
'******************************************************************************
'*  AUTHOR: <Joachim Agou>
'*
'*  DESCRIPTION:
'*  <Record a transient log, save a critical log, save a fullset.>
'*
'*  DATE: 07/01/2008
'*
'*  MODIFICATIONS:
'*    DATE         WHO  VERSION   DESCRIPTION
'*    ----------   ---  --------  --------------------------------------------------
'*    20191225     JOA  1.0       Initial version
'*    20200110     JOA  2.0       Modified Instrucations. (minor)
'******************************************************************************



'******************************************************************************
'************************* LOCAL VARIABLE DECLARATIONS ************************
'******************************************************************************

dim Boo1
channel "Math_Float1, Math_Float2, Math_Float3, Math_Float4, Math_Float5, Math_Bool1, Math_Bool2"



'******************************************************************************
'******************************** PREREQUISITES *******************************
'******************************************************************************

note "*** DEMO DATA RECORDING ***"
note " "



'******************************************************************************
instruction "Start a steady-state point (Fullset)."

do_fullset 10, "proDAS ATP", "start fullset"



'******************************************************************************
instruction "Start a a Critical Log"

save_log



'******************************************************************************
instruction "Start a Transient Log."

start_log "Demo_Report"

delay 10

stop_log "Demo_Report"


