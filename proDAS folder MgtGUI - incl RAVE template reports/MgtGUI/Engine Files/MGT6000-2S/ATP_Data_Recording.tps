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

' Channel Registration

'Dim bCmdSuccessful
'Dim strComment


instruction "Press PLAY to start a steady state point (Fullset)."

do_fullset 10, "proDAS ATP", "start fullset"


instruction "Press PLAY to start a Critical Log"

save_log


instruction "Press PLAY to start a Transient Log."

start_log "Demo_Report"

delay 10

stop_log "Demo_Report"


