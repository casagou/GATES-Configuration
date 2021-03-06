Option Explicit

'* <script.tps>
'******************************************************************************
'*  AUTHOR: <your name goes here>
'*
'*  DESCRIPTION:
'*  <describe the script here>
'*
'*  DATE: 07/01/2008 9:45:32 AM
'*
'*  MODIFICATIONS:
'*    DATE         WHO  NCR    DESCRIPTION
'*    ----------   ---  -----  --------------------------------------------------
'*
'******************************************************************************
clear_window

result "	Arrays"
Dim arr
arr = Array(-1,0,1,2)
result "array arr: " & arr(0) &", " & arr(1) &", " & arr(2) &", " & arr(3)

result "	Data types"
result " - Numbers"
Dim x,y
x=2
y=3
result "variables x = " & x &", y = " & y

result " - Strings"
Dim tstr
tstr = "string variable"
result "example of a " & tstr

result "	Operators"
result " - Arithmetic"
result "x+y=" & x+y
result "x-y=" & x-y
result "x*y=" & x*y
result "x/y=" & x/y
result "y%x=" & y mod x

result " - Assignment"
x=5
result "x=" & x
x=x+5
result "x=x+5=" & x
x=x-6
result "x=x-6=" & x
x=x*2
result "x=x*2=" & x
x=x/2
result "x=x/2=" & x

result " - Comparison"
result "x=" & x
result "x==10=" & (x=10)
result "x!=10=" & (x<>10)
result "x>10=" & (x>10)
result "x<10=" & (x<10)
result "x>=4=" & (x>=4)
result "x<=3=" & (x<=3)

result " - Boolean"
result "True AND False=" & (True AND False)
result "True OR False=" & (True OR False)
result "NOT(True)=" & (NOT(True))

result " - String"
tstr = "test string"
result tstr
tstr = "test string" + " concatenation"
result tstr
tstr = tstr + " and assign"
result tstr

result "	Control structures"
result " - If...Else"
result "x = " & x &", y = " & y
If x>y Then
   result "x is larger than y"
Else
   result "x is not larger than y"
End If

result "	Directives"
if True then
result "Calling another Test Procedure ..."
	Call_TP "ATP_Sample_proDAS_Script"
end if

result "	Commands"
do_fullset 1
result "Fullset command was called"

result "	Functions"
dim VBScriptFilePath: VBScriptFilePath= "C:\proDAS\Data\MgtGUI\Engine Files\MGT6000-2S\ATP_Sample_VB_Script.vbs"
call_script VBScriptFilePath
result "Visual Basic command was called"