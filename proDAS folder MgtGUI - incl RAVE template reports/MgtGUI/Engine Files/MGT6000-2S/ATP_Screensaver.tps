Option Explicit

'* <script.tps>
'******************************************************************************
'*  AUTHOR: Joachim Agou
'*
'*  DESCRIPTION:
'*  Demostrate visual alarm and warning state.
'*
'*  DATE: 25/10/2018
'*
'*  MODIFICATIONS:
'*    DATE         WHO  NCR    DESCRIPTION
'*    ----------   ---  -----  --------------------------------------------------
'*    20181025   JOA         Initial version
'******************************************************************************

' *********************************************************************
' ******************** LOCAL VARIABLE DECLARATIONS ********************
' *********************************************************************
dim Cycle, Big_Cycle
channel "Math_Float1, Math_Float2, Math_Float3, Math_Float4, Math_Float5, Math_Bool1, Math_Bool2"

' *********************************************************************
' ******************** DEMO ********************
' *********************************************************************

note "*** DEMO VISUAL ALARM/WARNING STATE ***"

Big_Cycle = 1
While Cycle<=10

set_channel Math_Float1, 0
set_channel Math_Float2, 5
set_channel Math_Bool1, 1
set_channel Math_Bool2, 0

show_view "MRKT1_MGT", "View 0", "Demo_Alarms.v"
result "Real-Time Display has been loaded", REPORT & "RTD page", BLACK

delay 5

Cycle = 1
While Cycle<=2

set_channel Math_Float1, 11
set_channel Math_Float2, 5
set_channel Math_Bool1, 0
set_channel Math_Bool2, 0

delay 10

set_channel Math_Float1, -99
set_channel Math_Float2, 5
set_channel Math_Bool1, 0
set_channel Math_Bool2, 0

delay 10

set_channel Math_Float1, -86
set_channel Math_Float2, 21
set_channel Math_Bool1, 0
set_channel Math_Bool2, 1

delay 10

set_channel Math_Float1, -250
set_channel Math_Float2, 0
set_channel Math_Bool1, 1
set_channel Math_Bool2, 1

delay 1

set_channel Math_Float1, -250
set_channel Math_Float2, -10
set_channel Math_Bool1, 1
set_channel Math_Bool2, 1

delay 1

set_channel Math_Float1, -250
set_channel Math_Float2, -20
set_channel Math_Bool1, 1
set_channel Math_Bool2, 1

delay 1

set_channel Math_Float1, -250
set_channel Math_Float2, -30
set_channel Math_Bool1, 1
set_channel Math_Bool2, 1

delay 1

set_channel Math_Float1, -250
set_channel Math_Float2, -40
set_channel Math_Bool1, 1
set_channel Math_Bool2, 1

delay 5

set_channel Math_Float1, -250
set_channel Math_Float2, -201
set_channel Math_Bool1, 1
set_channel Math_Bool2, 1

delay 10

set_channel Math_Float1, -250
set_channel Math_Float2, -199
set_channel Math_Bool1, 1
set_channel Math_Bool2, 1

delay 10

set_channel Math_Float1, -250
set_channel Math_Float2, -196
set_channel Math_Bool1, 1
set_channel Math_Bool2, 1

delay 10

set_channel Math_Float1, -250
set_channel Math_Float2, -195
set_channel Math_Bool1, 1
set_channel Math_Bool2, 1

delay 10

set_channel Math_Float1, -250
set_channel Math_Float2, -194
set_channel Math_Bool1, 1
set_channel Math_Bool2, 1

delay 10

result "Cycle Alarms completed", REPORT & "Alarm cycle", BLUE

Cycle = Cycle + 1

Wend

result "All cycles Alarms completed", REPORT & "Alarm cycle", RED


show_view "MRKT1_MGT", "View 0", "Demo_Calculations.v"
result "Real-Time Display has been loaded", REPORT & "RTD page", BLACK


delay 5

Cycle = 1
While Cycle<=2

set_channel Math_Float1, 1
set_channel Math_Float2, 2
set_channel Math_Float3, 3
set_channel Math_Float4, 4
set_channel Math_Float5, 5
set_channel Math_Bool1, 0
set_channel Math_Bool2, 0

delay 10

set_channel Math_Float1, 1
set_channel Math_Float2, 10
set_channel Math_Float3, 100
set_channel Math_Float4, 1000
set_channel Math_Float5, 10000
set_channel Math_Bool1, 1
set_channel Math_Bool2, 1

delay 10

set_channel Math_Float1, -86
set_channel Math_Float2, 21
set_channel Math_Float3, 3
set_channel Math_Float4, 4
set_channel Math_Float5, 5
set_channel Math_Bool1, 0
set_channel Math_Bool2, 1

delay 10

set_channel Math_Float1, -250
set_channel Math_Float2, 0
set_channel Math_Float3, 3
set_channel Math_Float4, 4
set_channel Math_Float5, 5
set_channel Math_Bool1, 1
set_channel Math_Bool2, 1

delay 1

set_channel Math_Float1, -250
set_channel Math_Float2, -10
set_channel Math_Float3, 3
set_channel Math_Float4, 4
set_channel Math_Float5, 5
set_channel Math_Bool1, 1
set_channel Math_Bool2, 1

delay 1

set_channel Math_Float1, -250
set_channel Math_Float2, -20
set_channel Math_Float3, 3
set_channel Math_Float4, 4
set_channel Math_Float5, 5
set_channel Math_Bool1, 1
set_channel Math_Bool2, 1

delay 1

set_channel Math_Float1, -250
set_channel Math_Float2, -30
set_channel Math_Float3, 3
set_channel Math_Float4, 4
set_channel Math_Float5, 5
set_channel Math_Bool1, 1
set_channel Math_Bool2, 1

delay 1

set_channel Math_Float1, -250
set_channel Math_Float2, -40
set_channel Math_Float3, 3
set_channel Math_Float4, 4
set_channel Math_Float5, 5
set_channel Math_Bool1, 1
set_channel Math_Bool2, 1

delay 5

set_channel Math_Float1, -250
set_channel Math_Float2, -201
set_channel Math_Float3, 3
set_channel Math_Float4, 4
set_channel Math_Float5, 5
set_channel Math_Bool1, 1
set_channel Math_Bool2, 1

delay 10

set_channel Math_Float1, -250
set_channel Math_Float2, -199
set_channel Math_Float3, 3
set_channel Math_Float4, 4
set_channel Math_Float5, 5
set_channel Math_Bool1, 1
set_channel Math_Bool2, 1

delay 10

set_channel Math_Float1, -250
set_channel Math_Float2, -196
set_channel Math_Float3, 3
set_channel Math_Float4, 4
set_channel Math_Float5, 5
set_channel Math_Bool1, 1
set_channel Math_Bool2, 1

delay 10

set_channel Math_Float1, -250
set_channel Math_Float2, -195
set_channel Math_Float3, 3
set_channel Math_Float4, 4
set_channel Math_Float5, 5
set_channel Math_Bool1, 1
set_channel Math_Bool2, 1

delay 10

set_channel Math_Float1, -250
set_channel Math_Float2, -194
set_channel Math_Float3, 3
set_channel Math_Float4, 4
set_channel Math_Float5, 5
set_channel Math_Bool1, 1
set_channel Math_Bool2, 1

delay 10

result "Cycle Calculations completed", REPORT & "Calculations cycle", BLUE

Cycle = Cycle + 1

Wend

result "All cycles Calculations completed", REPORT & "Calculations cycle", RED



show_view "MRKT1_MGT", "View 0", "Demo_Simulations.v"
result "Real-Time Display has been loaded", REPORT & "RTD page", BLACK

delay 60


show_view "MRKT1_MGT", "View 0", "Demo_Conversion_DecHexBin.v"
result "Real-Time Display has been loaded", REPORT & "RTD page", BLACK

delay 60

show_view "MRKT1_MGT", "View 0", "clock.v"
result "Real-Time Display has been loaded", REPORT & "RTD page", BLACK

delay 600

Wend

result "All cycles done", REPORT & "Cycles", GREEN