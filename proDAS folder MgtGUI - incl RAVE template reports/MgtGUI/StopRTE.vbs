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

' These scripts are executed by nxDAS NXIF.SERVICE (see c:\nxDAS\Data\MgtGUI)
