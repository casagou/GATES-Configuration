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

instruction "Press PLAY to initiate purge of all non-continuous purge enabled bricks."

result "30 second purge of all non-continuous purge enabled bricks will occur in 10 seconds."

delay 10

pbs_purge 30

result "Purge complete."

delay 5

result "Demo Purge script is complete."

