sComputerName = "."
Set objWMIService = GetObject("winmgmts:\\" & sComputerName & "\root\cimv2")
sQuery = "SELECT * FROM Win32_Process WHERE Name LIKE '%RTDDriver.exe%'"
Set objItems = objWMIService.ExecQuery(sQuery)
'iterate all item(s)
For Each objItem In objItems
   WScript.Echo "Process [Name:" & objItem.Name & "]"
Next
