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

instruction "Press PLAY to initiate a steady state data recording (Fullset)."

do_fullset 10, "nxDAS SST ATP Demo Fullset", "Record fullset"

result "nxDAS Fullset recording of 10second duration was completed successfully."

instruction "Press PLAY to initiate a transient data recording (Log)."

start_log "All_Channels_10Hz",, "nxDAS SST ATP Demo Log - Record log"

delay 10

stop_log "All_Channels_10Hz"

result "nxDAS Log recording of 10second duration was completed successfully."

delay 5

result "The Demo Recording test procedure has been executed successfully."


