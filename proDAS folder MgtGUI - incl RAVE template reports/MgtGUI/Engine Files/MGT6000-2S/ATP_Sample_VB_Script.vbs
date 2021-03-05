Option Explicit

dim x: x=1
dim msgtext
select case x
	Case 1
		msgtext = "Sample VB script call. x equals 1"
	Case 2
		msgtext = "Sample VB script call. x equals 2"
	Case 3
		msgtext = "Sample VB script call. x equals 3"
	Case Else
		msgtext = "Sample VB script call. x is not equal 1,2 or 3"
end select

if x<0 then
	msgtext = msgtext + " which is less than 0"
elseif 	x=0 then
	msgtext = msgtext + " which is 0"
else 
	msgtext = msgtext + " which is larger than 0"
end if

MsgBox msgtext