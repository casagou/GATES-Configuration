Option Explicit

'* <script.tps>
'******************************************************************************
'*  AUTHOR: <Joachim Agou>
'*
'*  DESCRIPTION:
'*  <Convert an integer in decimal format to octal and hexadecimal format.>
'*
'*  DATE: 12/24/2019
'*
'*  MODIFICATIONS:
'*    DATE         WHO  VERSION   DESCRIPTION
'*    ----------   ---  --------  --------------------------------------------------
'*    20191225     JOA  1.0       Initial version
'*    20191228     JOA  2.0       Added prerequisites section
'******************************************************************************



'******************************************************************************
'************************* LOCAL VARIABLE DECLARATIONS ************************
'******************************************************************************

dim tempvar1, tempvar2, tempvar3, boo1
channel "Math_Float1"



'******************************************************************************
'******************************** PREREQUISITES *******************************
'******************************************************************************

note "*** CONVERT DECIMAL TO OCTAL & HEXADECIMAL ***"
note" "

Caution "Ensure the corresponding RTD page is loaded."
instruction "Read the instructions below:",SKIP

If skipGV = True Then
result "Instructions skipped!", REPORT & "Convert Dec Oct Hex", RED
End If

note" "
caution "The purpose of this Test Procedure is to convert decimal value into:"
caution ".   octal string"
caution ".   hexadecimal string"
note" "


prompt_boo "Did you understand the instructions?",boo1
	If boo1 = false Then
	result "Demonstration Canceled!", REPORT & "Convert Dec Oct Hex", RED
	quit
	End If



'******************************************************************************
'************************************ DEMO ************************************
'******************************************************************************

 instruction "Convert from decimal to octal and hexadecimal"
 
 prompt_num "Enter a decimal value to be converted to octal and hexadecimal", tempvar1, 0, 1000, 20

 tempvar2 = Oct(tempvar1)
 tempvar3 = Hex(tempvar1)
 result "Decimal value=" & tempvar1 & "     Octal value=" & tempvar2 & "     Hexadecimal value=" & tempvar3, REPORT & "Convert Dec Oct Hex", BLUE

