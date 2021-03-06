Option Explicit

'* <script.tps>
'******************************************************************************
'*  AUTHOR: <JOACHIM AGOU>
'*
'*  DESCRIPTION:
'*  <Demomonstration for ATP_Calibration MAN>
'*
'*
'*  REVISION HYSTORY:
'*    DATE         WHO  REV    DESCRIPTION
'*    2017/10/26   JOA  V1.0   Initial
'*
'******************************************************************************


' *********************************************************************
' ******************** LOCAL VARIABLE DECLARATIONS ********************
' *********************************************************************

Dim boo1


' *******************************************************
' ******************** PREREQUISITES ********************
' *******************************************************

'show_view "GTP5_RTD3", "View 0", "Demo_RTD_Page1.v"
delay 5

instruction "Read the instructions below:",SKIP

If skipGV = True Then
result "Instructions skipped!", REPORT & "German Characters", RED
End If

note" "

caution "The purpose of this Test Procedure is to demonstrate compliance with German characters öäüÖÄÜß"
caution ".   ö"
caution ".   ä"
caution ".   ü"
caution ".   Ö"
caution ".   Ä"
caution ".   Ü"
caution ".   ß"
note" "

prompt_boo "Did you understand the instructions?",boo1
If boo1 = false Then
result "Demonstration Canceled!", REPORT & "German characters", RED
quit
End If


instruction "Dies ist ein proDAS-Abnahmetestverfahren (ATP) öäüÖÄÜß", SKIP
If skipGV = True Then
quit
result "Result = Dies ist ein proDAS-Abnahmetestverfahren (ATP) öäüÖÄÜß", REPORT & "Dies ist ein proDAS-Abnahmetestverfahren (ATP) öäüÖÄÜß", BLUE
End If
caution "Caution = Dies ist ein proDAS-Abnahmetestverfahren (ATP) öäüÖÄÜß"
warning "Warning = Dies ist ein proDAS-Abnahmetestverfahren (ATP) öäüÖÄÜß"
note "Note = Dies ist ein proDAS-Abnahmetestverfahren (ATP) öäüÖÄÜß"
result "Result = Dies ist ein proDAS-Abnahmetestverfahren (ATP) öäüÖÄÜß", REPORT & "Dies ist ein proDAS-Abnahmetestverfahren (ATP) öäüÖÄÜß", BLUE
delay 10

