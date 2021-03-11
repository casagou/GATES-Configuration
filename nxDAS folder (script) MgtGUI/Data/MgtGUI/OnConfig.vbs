'******************************************************************************
'* OnApplyBtn.vbs
'******************************************************************************
'*  AUTHOR: Marc Crandall
'*
'*  DESCRIPTION:
'*    This script is called when the MgtGUI Apply button is pressed. ...
'*
'*  DATE: 08-Jun-2007
'*
'*  NOTE:
'*    1) 
'*
'*
'*  MODIFICATIONS:
'*    DATE         REV     INITIALS  DESCRIPTION
'*    ----------   -----   --------  --------------------------------------------------
'*    
'******************************************************************************
Option Explicit

'***************************START CHANGE***************************************
Const ventValveAppName = "/users/RTE/bin/exe/updateplc /users/RTE/bin/exe/config.plc"
Const rteHost = "rtehost"
Const user = "engineer"

'FOR TESTING
'MsgBox "config script running"
'***************************END CHANGE*****************************************


'***************************DO NOT CHANGE**************************************
Call SendRemoteCmd(rteHost, user, ventValveAppName)

Function SendRemoteCmd(theHost, theUser, theCommand)  
  Err.Clear
  On Error Resume Next  
  
    Dim oWSHShell, cmdString, returnVal
    
    cmdString = "rsh " & theHost & " -l " & theUser & " " & theCommand    
    Set oWSHShell = WScript.CreateObject("WScript.Shell")
    returnVal = oWSHShell.Run(cmdString, 1, true)
    Set oWSHShell = Nothing 

  If Err.Number <> 0 Then
    MsgBox "Error" & Err.Number & _
      vbCrLf & Err.Description & vbCrLf & " Return Number: " & returnVal
  End If
  
  Exit Function
End Function