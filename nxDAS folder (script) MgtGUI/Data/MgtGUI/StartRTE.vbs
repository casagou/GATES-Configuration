'****************************************************************************** 
'* RTEStart.vbs
'****************************************************************************** 
'*  AUTHOR: Fereshteh Mahvarsayyad
'*                                                                              
'*  DESCRIPTION:                                                                
'*    This script launches the UEL Display(s) in the specified modes and on
'*    the specifed Pcs 
'*                                                                              
'*  DATE: 30-Sep-03 5:24:42 PM                                                           
'*
'*  NOTE:
'*	1) Update the "PCNames" variable to list the name of the Pcs where the UEL 
'*	Disply is to be started. PC names shall be separated by comma with no space
'*	
'*	2) The "PCNames" should match the variable with the same name in the 
'*	"RTEStop.vbs" file
'*
'*	3) Update the "DisplayTypes" variable to list the type of the UEL displays
'*	to be started ( "Main", "Online", "File" )
'*	The Display type list should match the PC names list.
'*	Display types shall be separated by comma with no space
'*                                                                              
'*  MODIFICATIONS:                                                              
'*    DATE         REV     INITIALS  DESCRIPTION
'*    ----------   -----   --------  --------------------------------------------------
'****************************************************************************** 

Option Explicit

On Error Resume Next

Dim PCNames
Dim DisplayTypes


'***************************START CHANGE*************************************** 

PCNames = "gates_mgt"
DisplayTypes= "Main"

'***************************END CHANGE***************************************** 



'***************************DO NOT CHANGE************************************** 
dim arrPCNames
arrPCNames = split (PCNames, ",")

dim arrDispTypes
arrDispTypes = split (DisplayTypes, ",")

dim PCcount, TypeCount
PCcount = ubound (arrPCNames)
TypeCount = ubound (arrDispTypes)

If TypeCount <> PCCount  Then
   MsgBox "The PC List does not match the Display Type List!"
Else
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
        MsgBox "Failed to create the UEL Display on '" & arrPCNames(i) & "' : " & Err.Description
        Err.Number = 0
    Else
       objCommands.Start (arrDispTypes(i)) 'Start the UEL Display in the Given mode
       Set objCommands = Nothing
    End If

   next
End If
'***************************DO NOT CHANGE************************************** 
