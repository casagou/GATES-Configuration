Option Explicit

'* <script.tps>
'******************************************************************************
'*  AUTHOR: <Joachim Agou>
'*
'*  DESCRIPTION:
'*  <Demonstrate German specific characters support in Test Procedure Script.>
'*
'*  DATE: 12/24/2019
'*
'*  MODIFICATIONS:
'*    DATE         WHO  VERSION   DESCRIPTION
'*    ----------   ---  --------  --------------------------------------------------
'*    20191225     JOA  1.0       Initial version
'*    20191228     JOA  2.0       Cleanup code.
'******************************************************************************



'******************************************************************************
'************************* LOCAL VARIABLE DECLARATIONS ************************
'******************************************************************************

dim Boo1



'******************************************************************************
'******************************** PREREQUISITES *******************************
'******************************************************************************

note "*** DEMO GERMAN SPECIFIC CHARACTERS ***"
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

caution "> The purpose of this Test Procedure is to demonstrate compliance with German characters öäüÖÄÜß"
caution ".   ö"
caution ".   ä"
caution ".   ü"
caution ".   Ö"
caution ".   Ä"
caution ".   Ü"
caution ".   ß"
caution "> Verify the corresponding RTD page is loaded."
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

instruction "Dies ist ein proDAS-Abnahmetestverfahren (ATP) öäüÖÄÜß", SKIP
	If skipGV = True Then
	quit
	result "Result = Dies ist ein proDAS-Abnahmetestverfahren (ATP) öäüÖÄÜß", REPORT & "Dies ist ein proDAS-Abnahmetestverfahren (ATP) öäüÖÄÜß", BLUE
	End If

caution "Caution = Dies ist ein proDAS-Abnahmetestverfahren (ATP) öäüÖÄÜß"
warning "Warning = Dies ist ein proDAS-Abnahmetestverfahren (ATP) öäüÖÄÜß"
note "Note = Dies ist ein proDAS-Abnahmetestverfahren (ATP) öäüÖÄÜß"
result "Result = Dies ist ein proDAS-Abnahmetestverfahren (ATP) öäüÖÄÜß", REPORT & "Dies ist ein proDAS-Abnahmetestverfahren (ATP) öäüÖÄÜß", BLUE

delay 5

