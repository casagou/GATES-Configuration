
'******************************************************************************
'*  AUTHOR: <F. Martel>
'*
'*  DESCRIPTION:
'*  vb script equivalent o the show_view test procedure command
'*
'*  DATE: 10/12/2009 3:52:11 PM
'*
'*  MODIFICATIONS:
'*    DATE         WHO  NCR    DESCRIPTION
'*    ----------   ---  -----  --------------------------------------------------
'*    27-Sep-10    DP          some changes
'*    10-Dec-09    FM    n/a   Original
'******************************************************************************
'*
'*
'*  This script accepts the RT Display and the Page name to be displayed
'*
'*  SYNTAX: show_view <RTDisplayPCname> <ViewName> <PageName>
'*
'*
'******************************************************************************

Option Explicit

On Error Resume Next

Dim oView
Dim oDriver

' Command line parameters
Dim argRTDisplayPC
Dim argViewName
Dim argPageName
Dim args

'******************************************************************************
'*
'*  Retrieve the arguments
'*
'******************************************************************************

argRTDisplayPC = "gates_mgt"
argViewName    = "View0"
argPageName    = "\\rtehost\RTE\views\ATP_Calibration\ThrustCalibration.v"

Err.Clear

set oDriver = createobject("proDAS.RTDDriver", argRTDisplayPC)
If Err.Number <> 0 Then
          MsgBox "Failed to create RTDDriver Object: " & Err.Description
          Err.Number = 0
End If
oDriver.Login "sl5","sl5sl5"	
set oView = oDriver.CreateView(argViewName)
If Err.Number <> 0 Then
          MsgBox "Failed to find view: " & argViewName & Err.Description
          Err.Number = 0
End If

oView.PageName = argPageName
oView.SetPosition 0, 0, 1280, 794
set oView = nothing
set oDriver = nothing
