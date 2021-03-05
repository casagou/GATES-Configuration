
'******************************************************************************
'*  AUTHOR: <A. Wisniewski>
'*
'*  DESCRIPTION:
'*  vb script launched to demonstrate channel alarm action 'invoke-script'
'*
'*  DATE: 2020/01/08 14:40
'*
'*  MODIFICATIONS:
'*    DATE         WHO  NCR    DESCRIPTION
'*    ----------   ---  -----  --------------------------------------------------
'*    20-Janc-08   AW    n/a   Original
'******************************************************************************
'*
'*
'*  This script opens a web browser to the MDS home page and opens a msgbox to
'*  confirm to the user that the web browser opening was caused by the channel
'*  limit violation.
'*
'******************************************************************************

'CreateObject("WScript.Shell").Run www.mdsaero.com
'CreateObject("WScript.Shell").Run """" & C:\Program Files (x86)\Google\Chrome\Application\chrome.exe & """ www.mdsaero.com"

MsgBox "Script ActionAlarm was launched due to alBool1 channel alarm. This message box appearing on the MgtGUI PC is the direct result of alBool1 channel alarm."