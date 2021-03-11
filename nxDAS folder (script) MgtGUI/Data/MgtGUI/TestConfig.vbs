'WScript.Sleep 1000

Set Application = CreateObject ("prodas.Config")

Application.UseInactive = vbTrue
Application.Identify "engineer", "thehelp"
'Application.CurrentConfigurationId = CInt(argConfigID)

'Set Configuration = Application.CurrentConfiguration
'Configuration.Export GetExportFolder & "Configuration.xml", -1

