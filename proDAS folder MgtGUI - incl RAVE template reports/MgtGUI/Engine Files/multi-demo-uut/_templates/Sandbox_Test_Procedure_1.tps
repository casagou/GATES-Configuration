Option Explicit

'* <script.tps>
'******************************************************************************
'*  AUTHOR: <Joachim Agou>
'*
'*  DESCRIPTION:
'*  <This is a sandbox and a template.>
'*
'*  DATE: 12/24/2019
'*
'*  MODIFICATIONS:
'*    DATE         WHO  VERSION   DESCRIPTION
'*    ----------   ---  --------  --------------------------------------------------
'*    20191225     JOA  1.0       Initial version
'*    20191228     JOA  2.0       Added prerequisites section
'*    20191228     JOA  3.0       Boo1 instead of boo1. Modified Prereq section
'*    20191228     JOA  4.0       Modified Prereq section
'*    20191228     JOA  5.0       Removed report & quote text
'******************************************************************************



'******************************************************************************
'************************* LOCAL VARIABLE DECLARATIONS ************************
'******************************************************************************

dim Boo1
channel "Math_Float1, Math_Float2, Math_Float3, Math_Float4, Math_Float5, Math_Bool1, Math_Bool2"



'******************************************************************************
'******************************** PREREQUISITES *******************************
'******************************************************************************

note "*** SANDBOX TEST PROCEDURE ***"
note" "

'show_view "mangtp5-rtd1", "View 0", "xxxxx.v"
'show_view "prodasrtd1", "View 0", "xxxxx.v"
'show_view "rtd1host", "View 0", "xxxxx.v"
'result "The Real-Time Display page has been loaded", REPORT, BLACK
'delay 5

instruction "Before you start:",SKIP
	If skipGV = True Then
	result "Instructions skipped!", REPORT, RED
	End If

caution "> Verify the corresponding RTD page is loaded."
note "> Load bla bla bla bla."
note "> Set bla bla bla bla."
note " "
note " "
note " "

prompt_boo "Did you understand the instructions?",boo1
	If Boo1 = false Then
	result "Demonstration Canceled!", REPORT, RED
	quit
	End If



'******************************************************************************
'************************************ DEMO ************************************
'******************************************************************************

note "This is a note."
caution "This is a caution."
warning "This is a warning."
result "This is a result in blue.", REPORT, BLUE
result "This is a result in green.", REPORT, GREEN
result "This is a result in red.", REPORT, RED
result "This is a result in black.", REPORT, BLACK
result "This is a result in yellow (hard to read).", REPORT, YELLOW

instruction "Run Instruction #1", skip
	If skipGV = True Then
	result "Instruction is skipped!", REPORT, RED
	End If

result "Instruction #1 is in progress ...", REPORT, BLACK
	delay 5
	result "Instruction #1 is completed.", REPORT, GREEN

instruction "Run Instruction #2", skip
	If skipGV = True Then
	result "Instruction is skipped!", REPORT, RED
	End If

result "Instruction #2 is in progress ...", REPORT, BLACK
	delay 5
	result "Instruction #2 is completed.", REPORT, GREEN

result RTE_Date
result RTE_Time
result "beep - beep - beep - beep - beep", REPORT, BLACK
beep 5