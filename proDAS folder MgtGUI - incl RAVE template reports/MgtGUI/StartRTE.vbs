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

' These scripts are executed by nxDAS NXIF.SERVICE (see c:\nxDAS\Data\MgtGUI)
