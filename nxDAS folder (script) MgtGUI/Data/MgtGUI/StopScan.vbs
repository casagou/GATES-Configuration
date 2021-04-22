'******************************************************************************
'* RTEStopScan.vbs
'******************************************************************************
'*  AUTHOR: Fereshteh Mahvarsayyad
'*
'*  DESCRIPTION:
'*    This script stops Alarm Summary, ARINC Display, and the Real Time Display(s)
'*    on the specied Pcs
'*
'*  DATE: 31-Sep-03 8:31:03 AM
'*
'*  NOTE:
'*    1) Update the "AlarmSumDispPC" variable, to name the Pc where the
'*    Alarm Summary Disply is to be stoped. This variable shall match the variable
'*    with the same name in the "RTEStartScan.vbs"
'*
'*    5) Update the "ARINCDispPC" variable, to name the Pc where the
'*    ARINC Disply is to be stoped. This variable shall match the variable
'*    with the same name in the "RTEStartScan.vbs".
'*
'*    6) Update the "RTDPCNames" variable to list the name of the Pcs where the
'*    Real Time Disply(s) are to be stoped. PC names shall be separated by comma
'*    with no space
'*
'*    7) The "RTDPCNames" shall match the variable with the same name in the
'*    "RTEStartScan.vbs" file.
'*
'*
'*  MODIFICATIONS:
'*    DATE         REV     INITIALS  DESCRIPTION
'*    ----------   -----   --------  --------------------------------------------------
'*    08-DEC-03            FM        Added Error handling
'*    26-APR-07    V2.01   DP        Moved startup of ARINC to RTD1
'******************************************************************************

Option Explicit

'On Error Resume Next

Dim RTDPCNames
Dim AlarmSumDispPC
Dim InfoSumDispPC
Dim ARINCDispPC

Dim remCtrl 

'COM Objects
Dim rte, oTrace

'***************************START CHANGE***************************************

AlarmSumDispPC = "gates_mgt"
InfoSumDispPC = "gates_mgt"
ARINCDispPC    = "gates_mgt"
RTDPCNames     = "gates_mgt,gates_rtd1"

'Initialise Strings and parameters
Const strTraceFile = "C:\\proDAS\\Data\\Trace\\StopScanTrace.txt"
Const strHost = "rtehost"
Const strService = "ui_serv"
Const ScriptName = "StopScan.vbs"
'***************************END CHANGE*****************************************



'***************************DO NOT CHANGE**************************************


'*******************************************************
'**** 1. Stop Alarm Summary Display
'*******************************************************
Dim objCommands

Set objCommands = CreateObject("ALARMSUMSERVER.Commands", AlarmSumDispPC)
If Err.Number <> 0 Then
   MsgBox "Failed to stop the Alarm Summary Display on '"+AlarmSumDispPC+ "' : "+Err.Description
   Err.Number = 0
Else
   objCommands.Stop
   Set objCommands = Nothing
End If

'*******************************************************
'**** 2. Stop Info Summary Display
'*******************************************************
Set objCommands = CreateObject("ALARMSUMSERVER2.Commands", InfoSumDispPC)
If Err.Number <> 0 Then
   MsgBox "Failed to stop the Info Summary Display on '"+InfoSumDispPC+ "' : "+Err.Description
   Err.Number = 0
Else
   objCommands.Stop
   Set objCommands = Nothing
End If

'*******************************************************
'**** 3. Stop ARINC Display
'*******************************************************
Set objCommands = CreateObject("ARINCDISPLAYSERVER.Commands", ARINCDispPC )
If Err.Number <> 0 Then
   MsgBox "Failed to stop the ARINC Display on '"+ARINCDispPC+ "' : "+Err.Description
   Err.Number = 0
Else
   objCommands.Stop
   Set objCommands = Nothing
End If

'*******************************************************
'**** 3.1. Stop OMS GUI (T800 or T700) 
'*******************************************************
'Set remCtrl = CreateObject( "MDS.Remoting.RemotingClient" )
'remCtrl.ShutdownProcess "STN1_RTD3", "OmsGUI", False


'*******************************************************
'**** 4. Stop Real Time Display
'*******************************************************
dim arrPCNames
arrPCNames = split (RTDPCNames, ",")

dim PCcount    ' the current number of PCs on which the app is to be started
PCcount = ubound (arrPCNames)

' terminate the app on the given computers
const Force = TRUE   ' enforce termination even if other clients still hold a connection

dim i
dim RTDDriver
dim Errors

For i = 0 to PCcount
   Err.Clear
   If arrPCNames(i) = "" Then
      Set RTDDriver = CreateObject("proDAS.RTDDriver")          ' local
      If Err.Number <> 0 Then
         MsgBox "Failed to stop the RTD Driver on the local computer: "+Err.Description
         Err.Number = 0
      End If
      StopRtdDriver
   Else
      'First RTD Driver instance
      set RTDDriver = CreateObject ("proDAS.RTDDriver", arrPCNames(i)) ' remote
      If Err.Number <> 0 Then
         MsgBox "Failed to stop the RTD Driver on '"+arrPCNames(i)+"': "+Err.Description
         Err.Number = 0
      End If
      StopRtdDriver

      'Second RTD Driver instance
     
	  set RTDDriver = CreateObject ("proDAS.RTDDriver2", arrPCNames(i)) ' remote
          If Err.Number <> 0 And Err.Number <> 424 Then
             MsgBox "Failed to stop the RTD Driver on '" & arrPCNames(i) & "': "+Err.Description
             Err.Number = 0
          End If
          StopRtdDriver
 
      
   End If

next
'delay 5

'*******************************************************
'**** 5. Send Save Critical Log OpCode 12 = SAVE_LOG
'*******************************************************
'Call InitialiseCOMobjects		' Creates COM objects
  
'if rte.InitAndConnect() then

	'Dim code

	'code = rte.SendOpcode(12,"")

	'Call oTrace.WriteArgs(ScriptName, "Sendopcode: ", "Opcode 12 status = " & code)
		

'else

	'Call oTrace.WriteArgs(ScriptName, "ConnectToRTE:","Cannot connect to the RTE")

'end if

'Terminate


'*******************************************************
'**  Stop the RTDDriver
'*******************************************************
sub StopRtdDriver
  set Errors = RTDDriver.Errors
  CheckErrors
  set Errors = Nothing

  RTDDriver.Terminate Force
  set RTDDriver = Nothing
end sub

'*******************************************************
'**  check for errors and notify the user, if appropriate
'*******************************************************

sub CheckErrors
   if ( Errors.LastCallHasFailed ) then
      dim msg
      msg = "The following error was encountered: "
      do until Errors.IsEmpty
         msg = msg & vbNewLine & Errors.Message
      loop
      msgbox msg
   end if
end sub

'******************************************************************************
'**** Function GetArg()
'******************************************************************************
Function GetArg (Flag)
On Error Resume Next
    dim retVal, i
    retVal = ""
    Flag = UCase (Flag)
    'MsgBox Flag
    Dim args
    Set args = WScript.Arguments

    If args.Count > 0 Then
      For i = 0 To args.Count-1
        If UCase( args(i) ) = "/" + Flag  Then
          retVal = args(i+1)
          Exit For
        End If
      Next
    End If
    GetArg = retVal
End Function

'******************************************************************************
'**** Sub InitialiseCOMobjects
'******************************************************************************
Sub InitialiseCOMobjects

  
  Err.Clear

  Set rte = CreateObject("RteControlLib.RteControl")
  Set oTrace = CreateObject ("MDSComm.Trace")
  
  Call oTrace.Open (strTraceFile)
  Call oTrace.WriteArgs(ScriptName, "InitialiseCOMobjects()", "")
  
  If  Err.Number <> 0  then   
    MsgBox "Error Number:" & Err.Number & _
      vbCrLf & Err.Description
  End If
  
  Exit Sub
    
End Sub


'******************************************************************************
'**** Sub Terminate
'******************************************************************************
Sub Terminate
  Err.Clear

  Call oTrace.WriteArgs(ScriptName, "Terminate()", "")

  rte.Terminate()

  Set rte = Nothing
  Set oTrace = Nothing
    
  If  Err.Number <> 0  then   
    MsgBox "Error Number:" & Err.Number & _
      vbCrLf & Err.Description
  End If
  
  Exit Sub
End Sub

'***************************DO NOT CHANGE**************************************