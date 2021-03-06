Option Explicit

'* <script.tps>
'******************************************************************************
'*  AUTHOR: <Joachim Agou>
'*
'*  DESCRIPTION:
'*  <Records transiemt logs, critical logs, and fullsets continously.>
'*
'*  DATE: 12/28/2019
'*
'*  MODIFICATIONS:
'*    DATE         WHO  VERSION   DESCRIPTION
'*    ----------   ---  --------  --------------------------------------------------
'*    20191228     JOA  1.0       Initial version
'*    20200103     JOA  1.0       Tested in MSIL. Added verbosity. Added Critical Log
'******************************************************************************



'******************************************************************************
'************************* LOCAL VARIABLE DECLARATIONS ************************
'******************************************************************************

dim Cycle, Duration, Remaining_Minutes, Boo1



'******************************************************************************
'******************************** PREREQUISITES *******************************
'******************************************************************************

note "*** CONTINUOUS FULLSET & LOGS RECORDING ***"
note " "



instruction "Read the instructions below:",SKIP
	If skipGV = True Then
	result "Instructions skipped!", REPORT, RED
	End If

note "1) Ensure the transient log of the test procedure is defined in the configuration."
note " "
note " "
note " "

prompt_boo "Did you understand the instructions?",boo1
	If Boo1 = false Then
	result "Demonstration Canceled!", REPORT , RED
	quit
	End If



'******************************************************************************
'************************************ DEMO ************************************
'******************************************************************************

Cycle = 1

note "How many cycle?"
prompt_num "How many cycles would you like to run (1 cycle ~ 1 minute)", Duration, 0, 1440, 20

result Duration &" cycles is about "& Duration/60 &" hours.", REPORT, BLUE
result " ", REPORT
result "The test procedure will run for about " & Duration\60 &" hours " & Duration Mod 60 & " minutes.", REPORT, RED
result " ", REPORT

while Cycle <= Duration

delay 1

result "Cycle #" & Cycle & " started ...", REPORT, GREEN

note "Starting a Transient Log ~55 seconds."
start_log "Demo_Report"
result "*   Starting a Transient Log ~55 seconds.", REPORT, BLUE

delay 2

note "Recording a 30 seconds-fullset."
do_fullset_async 30, "Endurance", "Endurance"
result "*   Recording a 30 seconds-fullset.", REPORT, BLUE

delay 2

note "Saving a Critical Log."
save_log
result "*   Saving a Critical Log.", REPORT, BLUE

delay 54

note "Stopping the Transient Log."
stop_log "Demo_Report"
result "*   Stopping the Transient Log.", REPORT, BLUE

delay 1

note "Cycle is completed."
result "Cycle #" & Cycle &" is completed!", REPORT, GREEN
result " ", REPORT

beep 1

note "Calculating remaining time."
Remaining_Minutes = Duration-Cycle

result ">>>   "& Remaining_Minutes\60 & " hours " & Remaining_Minutes Mod 60 & " minutes until completion", REPORT, BLACK
result " ", REPORT

note "Next cycle."
Cycle=Cycle+1

wend

result "Endurance testing completed", REPORT, RED

beep 5