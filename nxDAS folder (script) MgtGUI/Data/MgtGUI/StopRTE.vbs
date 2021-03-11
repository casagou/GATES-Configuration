'****************************************************************************** 
'* RTEStop.vbs
'****************************************************************************** 
'*  AUTHOR: Fereshteh Mahvarsayyad
'*                                                                              
'*  DESCRIPTION:                                                                
'*    This script terminates the UEL Display(s) on the specifed Pcs 
'*                                                                              
'*  DATE: 30-Sep-03 5:34:23 PM                                                           
'*
'*  NOTE:
'*	1) Update the "PCNames" variable to list the name of the Pcs where the UEL 
'*	Disply is to be terminated. PC names shall be separated by comma with no space
'*	
'*	2) The "PCNames" should match the variable with the same name in the 
'*	"RTEStart.vbs" file
'*
'*  MODIFICATIONS:                                                              
'*    DATE         REV     INITIALS  DESCRIPTION
'*    ----------   -----   --------  --------------------------------------------------
'****************************************************************************** 

Option Explicit

On Error Resume Next

Dim PCNames


'***************************START CHANGE*************************************** 

PCNames = "gates_mgt"

'***************************END CHANGE***************************************** 



'***************************DO NOT CHANGE************************************** 
dim arrPCNames
arrPCNames = split (PCNames, ",")


dim PCcount
PCcount = ubound (arrPCNames)

' launch the UEL Display on the given computers
Dim objCommands
dim i
For i = 0 to PCcount
    Err.Number = 0
    If arrPCNames(i) = "" Then
       Set objCommands = CreateObject("UELDISPLAYSERVER.Commands" ) ' local
    Else
       Set objCommands  = CreateObject ("UELDISPLAYSERVER.Commands", arrPCNames(i)) ' remote
    End If

    If Err.Number <> 0 Then
       MsgBox "Failed to stop the UEL Display on '" & arrPCNames(i) & "' : " & Err.Description
       Err.Number = 0
    Else
       objCommands.Stop  ("main")  'Stop the UEL Display 
       Set objCommands = Nothing
    End If
next
'***************************DO NOT CHANGE************************************** 
