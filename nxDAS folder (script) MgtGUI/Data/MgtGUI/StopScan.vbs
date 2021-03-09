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
'******************************************************************************

Option Explicit

On Error Resume Next

Dim RTDPCNames
Dim AlarmSumDispPC
Dim InfoSumDispPC
Dim ARINCDispPC

Dim remCtrl 

'COM Objects
Dim oOpcode, oAPI, oTrace


'***************************START CHANGE***************************************
AlarmSumDispPC = "gates_mgt"
InfoSumDispPC = "gates_mgt"
ARINCDispPC    = "gates_mgt"
RTDPCNames     = "gates_mgt, gates_rtd1"


'Initialise Strings and parameters
Const strTraceFile = "C:\\proDAS\\Data\\Trace\\StopScanTrace.txt"
Const strHost = "rtehost"
Const strService = "ui_serv"
Const ScriptName = "StopScan.vbs"

'FOR TESTING
'MsgBox "StopScan script running"
'***************************END CHANGE*****************************************



'***************************DO NOT CHANGE**************************************

'*******************************************************
'**** 1. Stop Alarm Summary Display
'*******************************************************
Dim objCommands

Set objCommands = CreateObject("ALARMSUMSERVER.Commands", AlarmSumDispPC)
If Err.Number <> 0 Then
   MsgBox "Failed to stop the Alarm Summary Display on '" & AlarmSumDispPC & "' : " & Err.Description
   Err.Number = 0
Else
   objCommands.Stop
   Set objCommands = Nothing
End If

'*******************************************************
'**** 1.5. Stop Info Summary Display
'*******************************************************
Set objCommands = CreateObject("ALARMSUMSERVER2.Commands", InfoSumDispPC)
If Err.Number <> 0 Then
   MsgBox "Failed to stop the Info Summary Display on '" & InfoSumDispPC & "' : " & Err.Description
   Err.Number = 0
Else
   objCommands.Stop
   Set objCommands = Nothing
End If

'*******************************************************
'**** 2. Stop ARINC Display
'*******************************************************
Set objCommands = CreateObject("ARINCDISPLAYSERVER.Commands", ARINCDispPC )
If Err.Number <> 0 Then
   MsgBox "Failed to stop the ARINC Display on '" & ARINCDispPC & "' : " & Err.Description
   Err.Number = 0
Else
   objCommands.Stop
   Set objCommands = Nothing
End If

'*******************************************************
'**** 2.1. Stop OMS GUI (T800 or T700) // serge
'*******************************************************
'Set remCtrl = CreateObject( "MDS.Remoting.RemotingClient" )
'remCtrl.ShutdownProcess ARINCDispPC, "OmsGUI", False
'Set remCtrl = Nothing

'*******************************************************
'**** 3. Stop Real Time Display
'*******************************************************
dim arrPCNames
arrPCNames = split (RTDPCNames, ",")

dim PCcount    ' the current number of PCs on which the app is to be started
PCcount = ubound (arrPCNames)

' terminate the app on the given computers
const Force = TRUE   ' enforce termination even if other clients still hold a connection

dim i
For i = 0 to PCcount
   dim RTDDriver
   If arrPCNames(i) = "" Then
      Set RTDDriver = CreateObject("proDAS.RTDDriver")          ' local
	'WScript.sleep 1000
      If Err.Number <> 0 And Err.Number <> 424 Then
         MsgBox "Failed to stop the RTD Driver on the local computer: " & Err.Description
         Err.Number = 0
      End If
   Else
      
      set RTDDriver = CreateObject ("proDAS.RTDDriver", arrPCNames(i)) ' remote
      'WScript.sleep 1000
      'MsgBox "error number is " &Err.number
      If Err.Number <> 0 And Err.Number <> 424 Then
         MsgBox "Failed to stop the RTD Driver on '" & arrPCNames(i) & "': " & Err.Description
         Err.Number = 0
      End If
   End If

   dim Errors
   set Errors = RTDDriver.Errors
   CheckErrors

   RTDDriver.Terminate Force
next
'delay 5

'*******************************************************
'**** 4. Send PBS OpCode 156 = PBS_CONT_LOW_PURGE
'*******************************************************
'Dim argSubSystems, argSubSystemIDs, arrSubSystems, arrSubSystemIDs, PBSSubSysID

'argSubSystems = GetArg ("subsystem")
'arrSubSystems = Split (argSubSystems, ",")
'argSubSystemIDs = GetArg ("subsystemIDs")
'arrSubSystemIDs = Split (argSubSystemIDs, ",")


'Match PBS SubSystem to correponding ID from Command Line Paramaters
'For i = 0 To ubound(arrSubSystems)
'  If arrSubSystems(i) = "PBS" Then
'    PBSSubSysID = arrSubSystemIDs(i)
'    Exit For
'  End If
'Next

'Ensure we have a PBS Sub System ID
'If isEmpty(PBSSubSysID) Then
'  MsgBox "Can't find PBS Sub System ID in Command Line Argumets!" &_
'    vbNewLine & "Not Sending PBS_CONT_LOW_PURGE OpCode"
'Else
  'MsgBox PBSSubSysID
'  Call InitialiseCOMobjects		' Creates COM objects
  
  'Connect to RTE and Send OpCode if successful
'  If Not ConnectToRTE Then
'    MsgBox "Unable to connect to RTE host: '" & strHost & "' and service: '" & strService & "'"
'  Else
'    Call SendOpCode(156, PBSSubSysID)
'  End If

'End If

'Call Terminate		' Deletes COM objects

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
      For i = 0 To args.Count
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

  On Error Resume Next
  
  Set oApi = CreateObject("MDSComm.WinApi")
  Set oOpcode = CreateObject("OSSCom.Opcode")
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
'**** Function ConnectToRTE()
'******************************************************************************
Function ConnectToRTE()
  Dim theResult : theResult = False

  Err.Clear

  Call oOpcode.InitConnection(oTrace.TraceFileName, strHost, strService)
  If Err.Number <> 0 Then
    Call oTrace.WriteArgs(ScriptName, "ConnectToRTE()", "oOPcode.InitConnection(%s, %s, %s) failed. Err.Number = 0x%x", oTrace.TraceFileName, strHost, strService, Err.Number)
  Else
    Call oTrace.WriteArgs(ScriptName, "ConnectToRTE()", "Connection successful!")
    theResult = True
  End If

  ConnectToRTE = theResult
End Function

'******************************************************************************
'**** Function SendOpCode()
'******************************************************************************
Function SendOpCode(theOpCode, theMessage)
  Err.Clear
  On Error Resume Next

  Dim Index, Reply, Timeout
  
  If Not oTrace Is Nothing Then

    Call oTrace.WriteArgs(ScriptName, "SendOpCode", "Entering Function")
   
    'Send the message
    Index = oOpcode.SendMessage (theOpCode, theMessage )
  
    ' On error trace message
    If Err.Number <> 0 Then
      Call oTrace.WriteArgs(ScriptName, "SendOpCode", "SendMessage() error [0x0%x]", Err.Number)
  
    ' Otherwise wait for reply
    Else
      Reply = Space(50)
      Timeout = 10000
      Call oOpcode.GetReplyVariant (Index, Reply, Timeout )
  
      ' Check for an error
      If Err.Number <> 0 Then
          Call oTrace.WriteArgs(ScriptName, "SendOpCode", "Error during GetReplyVariant. [0x0%x]", Err.Number)
      Else
      
        ' Be sure that the reply is the same as the opcode message to not have error
        If Trim(UCase(Reply)) <> "OK" Then
          Call oTrace.WriteArgs(ScriptName, "SendOpCode", "Reply is not correct. [%s]", Reply)
        End If
      End If
    End If
      'sleep for 1000 msec
    oApi.Sleep(1000)
  Else
    Call oTrace.WriteArgs(ScriptName, "SendOpCode", "COM Object(s) NOT Initialized")
  End If

  
  If  Err.Number <> 0  then   
    Call oTrace.WriteArgs(ScriptName, "SendOpCode() Error " & Err.Number & Err.Description, "")
    MsgBox "Error Number:" & Err.Number & _
      vbCrLf & Err.Description
  End If
  
  Exit Function
  
End Function

'******************************************************************************
'**** Sub Terminate
'******************************************************************************
Sub Terminate
  Err.Clear
  On Error Resume Next

  Call oTrace.WriteArgs(ScriptName, "Terminate()", "")
  Set oOpcode = Nothing
  Set oTrace = Nothing
  Set oApi = Nothing
  Exit Sub
  
  
  If  Err.Number <> 0  then   
    MsgBox "Error Number:" & Err.Number & _
      vbCrLf & Err.Description
  End If
  
  Exit Sub
End Sub
'***************************DO NOT CHANGE**************************************
