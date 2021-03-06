Option Explicit

'* <script.tps>
'******************************************************************************
'*  AUTHOR: <JOACHIM AGOU>
'*
'*  DESCRIPTION:
'*  <Convert decimal to octal and hexadecimal>
'*
'*
'*  REVISION HYSTORY:
'*    DATE               WHO   REV    DESCRIPTION
'*    2017/11/15    JOA     V1.0    Initial
'*
'******************************************************************************

' *********************************************************************
' ******************** LOCAL VARIABLE DECLARATIONS ********************
' *********************************************************************

 Dim tempvar1
 Dim tempvar2
 Dim tempvar3
 
' *********************************************************************
' ******************** proDAS CHANNEL DECLARATIONS ********************
' *********************************************************************

 channel "Math_Float1"

' *******************************************************
' ******************** PREREQUISITES ********************
' *******************************************************

instruction "Read the instructions below:",SKIP

If skipGV = True Then
result "Instructions skipped!", REPORT & "Convert Dec Oct Hex", RED
End If

 note" "
 caution "The purpose of this Test Procedure is to convert decimal value into:"
 caution ".   octal string"
 caution ".   hexadecimal string"
 note" "


' **********************************************
' ******************** CORE ********************
' **********************************************

 instruction "Convert from decimal to octal and hexadecimal"
 
 prompt_num "Enter a decimal value to be converted to octal and hexadecimal", tempvar1, 0, 1000, 20

 tempvar2 = Oct(tempvar1)
 tempvar3 = Hex(tempvar1)
 result "Decimal value=" & tempvar1 & "     Octal value=" & tempvar2 & "     Hexadecimal value=" & tempvar3, REPORT & "Convert Dec Oct Hex", BLUE

