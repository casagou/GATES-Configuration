'Option Explicit


'Command line parameters
Dim argHostName
Dim argServiceName
Dim argUserName
Dim argPassword
Dim argTestCell
Dim argEngineType
Dim argSerialNumber
Dim argTestID
Dim argEngStandard
Dim argCustomer
Dim argSubSystems
Dim arrSubSystems
Dim argTestName
Dim argConfigID



'***************************START CHANGE*************************************** 
Const OverwriteExisting = True
Dim sAbsoluteFolder


'***************************END CHANGE***************************************** 


'****************************************************************************** 
'*** 1. Retrieve the arguments
'****************************************************************************** 


argConfigID	= GetArg ("TestConfigID")
argHostName 	= GetArg ("HostName")
argServiceName	= GetArg ("Servicename")
argUserName	= GetArg ("UserName")
argPassword	= GetArg ("Password")
argTestCell	= GetArg ("Testcell")
argEngineType	= GetArg ("Enginetype")
argSerialNumber = GetArg ("Serialnumber")
argTestID	= GetArg ("Testid")
argTestName	= GetArg ("TestName")
argEngStandard	= GetArg ("Standard")
argCustomer	= GetArg ("Customer")
argSubSystems	= GetArg ("subsystem")

'DumpArgs


'****************************************************************************** 
'*** 2. Export the XML file
'******************************************************************************

WScript.Sleep 1000
Set Application = CreateObject ("prodas.Config")

Application.UseInactive = vbTrue
Application.Identify argUserName, argPassword
Application.CurrentConfigurationId = CInt(argConfigID)

Set Configuration = Application.CurrentConfiguration
Configuration.Export GetExportFolder & "Configuration.xml", -1

set Subsystems = Application.Subsystems
Subsystems.Export GetExportFolder & "Subsystems.xml", -1 

Set channels = Application.Channels
Channels.Export GetExportFolder & "Channels.xml", -1

Set EngineeringUnits = Application.EngineeringUnits
EngineeringUnits.Export GetExportFolder & "EngineeringUnits.xml"

set Polynomials = Application.Polynomials
Polynomials.Export GetExportFolder & "Polynomials.xml", -1 

Set BreakPointTables = Application.BreakPointTables
BreakPointTables.Export GetExportFolder & "BreakPointTables.xml", -1

set Macros = Application.Macros
Macros.Export GetExportFolder & "Macros.xml", -1 

Set TextOutputPages = Application.TextOutputPages
TextOutputPages.Export GetExportFolder & "TextOutputPages.xml", -1

set TransientLogDefs = Application.TransientLogDefs
TransientLogDefs.Export GetExportFolder & "TransientLogDefs.xml", -1 

Set Options = Application.Options
Options.Export GetExportFolder & "Options.xml", -1

set UserFunctions = Application.UserFunctions
UserFunctions.Export GetExportFolder & "UserFunctions.xml", -1 

Set SiteSpecificChannelAttributes = Application.SiteSpecificChannelAttributes
SiteSpecificChannelAttributes.Export GetExportFolder & "SiteSpecificChannelAttributes.xml", -1

   
'****************************************************************************** 
'**** Copy file to RTE
'****************************************************************************** 
Set objFSO = WScript.CreateObject("Scripting.FileSystemObject")
  
    dstDirectory = "\\" + argHostName + "\logs\" + argEngineType+ "\"
    dstDirectory1 = dstDirectory + argTestName + "\"
    dstDirectory2 = dstDirectory1 + "Configuration\"
    dstDirectory3 = dstDirectory2 + GetDate(Now, "") + "_" + argConfigID + "\"

    engDir    = "/users/RTE/logs/" + argEngineType
    testDir   = engDir  + "/" + argTestName
    configDir = testDir + "/Configuration" + "/"
    configDir2= configDir + GetDate(Now, "") + "_" + argConfigID + "/"
    Set WshShell = CreateObject("WScript.Shell")
    rshCmd       = "rsh " + argHostName + " -l engineer -n chmod 777 "
    

     If Not objFSO.FolderExists(dstDirectory) Then
        Set configFolder = objFSO.CreateFolder(dstDirectory)
'        WshShell.Run rshCmd + engDir
        WScript.Sleep 100
     End If
     
     If Not objFSO.FolderExists(dstDirectory1) Then
        Set configFolder = objFSO.CreateFolder(dstDirectory1)
'        WshShell.Run rshCmd + testDir
        WScript.Sleep 100
     End If
     
     If Not objFSO.FolderExists(dstDirectory2) Then
        Set configFolder = objFSO.CreateFolder(dstDirectory2)
'	WshShell.Run rshCmd + configDir
        WScript.Sleep 100
     End If
     
     If Not objFSO.FolderExists(dstDirectory3) Then 
        Set idfolder = objFSO.CreateFolder(dstDirectory3)
'	WshShell.Run rshCmd + configDir2
	WScript.Sleep 500
     End If 
	
    set objsrcDirectory = objFSO.GetFolder(sAbsoluteFolder)
    Set colFiles = objsrcDirectory.Files
    For Each objFile in colFiles
    	srcFile = sAbsoluteFolder + objFile.name
        objFSO.CopyFile srcFile,dstDirectory3,OverwriteExisting
        WScript.Sleep 100
    Next
    

'****************************************************************************** 
'**** Function GetExportFolder()
'****************************************************************************** 
' Get the absolute name of the Export folder
function GetExportFolder

   Set ExportFolderFSO = CreateObject("Scripting.FileSystemObject")

   sAbsoluteFolder = ExportFolderFSO.GetFolder(".\") + "\Export\"

  if (ExportFolderFSO.FolderExists(sAbsoluteFolder) = false) then
      ExportFolderFSO.CreateFolder sAbsoluteFolder
   end if

 GetExportFolder = sAbsoluteFolder

end function

'****************************************************************************** 
'**** Function GetArg()
'****************************************************************************** 
Function GetArg (Flag)
   dim retVal 
   retVal = ""
   Flag = UCase (Flag)
   
   dim args
   set args = Wscript.Arguments

   For i=0 to args.Count-1
   'WScript.Echo args(i)
       If UCase(args(i) ) = "/" + Flag  Then
          retVal = args(i+1)
          Exit For	
       End If	 		
   Next
   GetArg = retVal
End Function


'****************************************************************************** 
'**** Function GetDate()
'****************************************************************************** 
Function GetDate(dateVal, delimiter)

	Dim dateHour, dateMinute, dateSecond
	
	dateVal = CDate(dateVal) 
		
	delimiter = CStr(delimiter)

	
	dateMonth = Month(dateVal)
 	dateDay = Day(dateVal)
 	dateHour = Hour(dateVal)
 	dateMinute = Minute(dateVal)
 	dateSecond = Second(dateVal)
 	
	
	GetDate = CStr(Year(dateVal)) & delimiter
	
	If dateMonth < 10 Then
		GetDate = GetDate & "0" 
	End If
	
	GetDate = GetDate & CStr(dateMonth) & delimiter

	If dateDay < 10 Then
		GetDate = GetDate & "0"
	End If
	
	GetDate = GetDate & CStr(dateDay) + "_"
	
	If dateHour < 10 Then
		GetDate = GetDate & "0"
	End If
	
	GetDate = GetDate & Cstr(dateHour)
	
	If dateMinute < 10 Then
		GetDate = GetDate & "0"
	End If
	GetDate = GetDate & Cstr(dateMinute)
	
	If dateSecond < 10 Then
		GetDate = GetDate & "0"
	End If
	
	GetDate = GetDate & Cstr(dateSecond)
	
End Function 



'****************************************************************************** 
'**** Sub DumpArgs() 
'**** Debugging tool
'****************************************************************************** 

Sub DumpArgs()
   Dim strDump
   
   strDump = "Arguments  Received from MGT GUI: "
   strDump =  strDump + "argConfigID = " + argConfigID
   strDump =  strDump + "argHostName = " + argHostName 
   strDump =  strDump + "; argServiceName = " + argServiceName
   strDump =  strDump + "; argUserName = " + argUserName
   strDump =  strDump + "; argPassword = " + argPassword
   strDump =  strDump + "; argTestCell = " + argTestCell
   strDump =  strDump + "; argEngineType = " + argEngineType
   strDump =  strDump + "; argSerialNumber = " + argSerialNumber
   strDump =  strDump + "; argTestID = " + argTestID	
   strDump =  strDump + "; argEngStandard = " + argEngStandard	
   strDump =  strDump + "; argCustomer = " + argCustomer	
   strDump =  strDump + "; argSubSystems = " + argSubSystems	

End Sub

'********* END of ExportXML.vbs ***************************

'********* BEGINNING of OnConfig.vbs ***********************************

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


'***************************START CHANGE***************************************
Const ventValveAppName = "/users/RTE/bin/exe/updateplc /users/RTE/bin/exe/config.plc"
Const rteHost = "rrd61-rte"
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