Option Explicit

'* <script.tps>
'******************************************************************************
'*  AUTHOR: <Joachim Agou>
'*
'*  DESCRIPTION:
'*  <Demonstrate visual limits/alarms and warning state. Require RTD page.>
'*
'*  DATE: 12/24/2019
'*
'*  MODIFICATIONS:
'*    DATE         WHO  VERSION   DESCRIPTION
'*    ----------   ---  --------  --------------------------------------------------
'*    20191225     JOA  1.0       Initial version
'*    20191225     JOA  2.0       Cleaned up code. Added Verbosity.
'******************************************************************************



'******************************************************************************
'************************* LOCAL VARIABLE DECLARATIONS ************************
'******************************************************************************
dim Cycle
channel "Math_Float1, Math_Float2, Math_Bool1, Math_Bool2"



'******************************************************************************
'************************************ DEMO ************************************
'******************************************************************************

note "*** DEMO VISUAL LIMITS/ALARMS/WARNING STATE ***"

set_channel Math_Float1, 0
set_channel Math_Float2, 5
set_channel Math_Bool1, 1
set_channel Math_Bool2, 0

'show_view "rtd1host", "View 0", "Demo_Alarms.v"
'result "The Real-Time Display page has been loaded", REPORT & "Demo", BLACK

Caution "Load the RTD page Demo_ALarms"
delay 5

Caution "Simulation for 5 cycles"

Cycle = 1

While Cycle<5

result "Cycle #" & Cycle, REPORT & "Demo", BLUE

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

result "Cycle completed", REPORT & "Demo", GREEN

Cycle = Cycle + 1

Wend

Caution "The Test Procedure is completed."