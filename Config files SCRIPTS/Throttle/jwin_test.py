import nxtps
import time
from enum import Enum

class AutoModeStatus(Enum):
  UNKNOWN = 0
  NOT_IN_AUTO_MODE = 1
  IDLE  = 2
  LEVER1_MOVE_IN_PROG = 3
  LEVER2_MOVE_IN_PROG = 4
  BOTH_LEVER_MOVE_IN_PROG = 5
  MOVE_PAUSED = 6
  OPEN_LOOP = 7


class AtcStatus(Enum):
  OK = 0
  UNKNOWN_ERROR = 1
  UNKNOWN_CLIENT = 2
  UNKNOWN_CONFIG = 3
  IN_AUTO_MODE = 4
  NOT_IN_AUTO_MODE = 5
  AUTO_MODE_DISABLED = 6
  MISSION_NOT_READY = 7
  INVALID_TAG_NAME = 8
  INVALID_CHANNEL_ALIAS = 9
  FAILED_TO_SET_CHANNEL = 10
  START_BEFORE_MOVE_DELAY = 11


status = AtcStatus (AtcStatus.OK)


status = AtcStatus(nxtps.at_run_mission(r"C:\UECU500\missions\Dual_Resolver\000PrimalMission.mscript"))
nxtps.result("run_mission() Status: " + str(status))
quit()


# Start Auto Mode
status = AtcStatus(nxtps.at_start_auto_mode())

if (status != AtcStatus.OK):
  nxtps.result("Status: " + str(status))
  nxtps.result("An error occured while trying to start auto mode with the "
      "UECU-500 Mark 3 system. TPS will exit.")
  quit()


# Check 'tripPosition' channel is valid (should be True)
is_chan_valid = nxtps.at_is_channel_valid("tripPosition")

if (not is_chan_valid):
  nxtps.result("The UECU-500 Mark 3 channel 'tripPosition' was not found and "
      "was expected. TPS will exit.")
  quit()


"""
(ret,val) = nxtps.at_get_float_channel("tripPosition")

if (AtcStatus(ret) != AtcStatus.OK):
  nxtps.result("Unexpected return code while trying to get value of "
      "'tripPosition' float channel.")
  quit()
else:
  nxtps.result("The value of 'tripPosition' channel is '" + str(val) + "'.")
"""


# Check 'whatyatalkinabeet' channel is not valid (should be False)
is_chan_valid = nxtps.at_is_channel_valid("whatyatalkinabeet")

if (is_chan_valid):
  nxtps.result("The UECU-500 Mark 3 channel 'whatyatalkinabeet' was found "
    "and was not expected. TPS will exit.")
  quit()


# Move TLA to 50 Deg, with a tolerance of 0.5, over a ramp time of 5 seconds and
# allow a further 5 seconds to ellapse before returning.
status = AtcStatus(nxtps.at_move("TLA", 50, 5.0, 10.0, 0.5, 10.0))

if (status != AtcStatus.OK):
  nxtps.result("Failed to undertake successful auto-throttle manoeuvre. "
    "TPS will exit.")
  quit()


# Attempt to do a delayed move start operation prior to specifying a delayed
# move.  Should return an int value of 11.
status = AtcStatus(nxtps.at_delayed_move_start(10.0, 10.0))

if (status != AtcStatus.START_BEFORE_MOVE_DELAY):
  nxtps.result("Unexpected return code. TPS will not exit.")
  quit()


# Specify delayed move of TLA to 63 Deg, with a tolerance of 0.5, and period of
# 10 seconds.
status = AtcStatus(nxtps.at_delayed_move("TLA", 63, 0.5, 10.0))

if (status != AtcStatus.OK):
    nxtps.result("Unexpected return code. TPS will exit.")
    quit()


# Start delayed move of TLA over ramp time of 5 seconds and a timeout of
# 20 seconds.
status = AtcStatus(nxtps.at_delayed_move_start(5.0, 20.0))

if (status != AtcStatus.OK):
    nxtps.result("Unexpected return code. TPS will not exit.")
    quit()


# Async move TLA to 100 Deg, with a tolerance of 0.5, over a ramp time of 20
# seconds, and allow a further 10 seconds to ellapse before completion of auto
# mode move.
status = AtcStatus(nxtps.at_move_async("TLA", 100, 20.0, 30.0, 0.5, 30.0))
if (status != AtcStatus.OK):
  nxtps.result("Failed to undertake successful auto-throttle manoeuvre. "
    "TPS will exit.")
  quit()


# Poll for Auto Mode Status, while async move is in progress.  Move has been
# cancelled if NOT_IN_AUTO_MODE returned (e.g., 'Cancel' button selected on GUI,
# or lever moved by operator, etc) or move has completed.
while (True):
  am_status = AutoModeStatus(nxtps.at_get_status())
  if (am_status == AutoModeStatus.LEVER1_MOVE_IN_PROG 
      or am_status == AutoModeStatus.LEVER2_MOVE_IN_PROG):
    nxtps.result("A lever move is in progress with an async op.")
  elif (am_status == AutoModeStatus.MOVE_PAUSED):
    nxtps.result("An async op has been paused.")
  elif (am_status == AutoModeStatus.IDLE):
    nxtps.result("The levers are idle with an async op.")
    break
  elif (am_status == AutoModeStatus.NOT_IN_AUTO_MODE):
    nxtps.result("The async op has been completed or cancelled.")
    break

  time.sleep(1)


status = AtcStatus(nxtps.at_delayed_move("TLA", 33, 0.5, 10.0))

if (status != AtcStatus.OK):
  nxtps.result("Unexpected return code. TPS will exit.")
  quit()


status = AtcStatus(nxtps.at_delayed_move_start_async(5.0, 20.0))

if (status != AtcStatus.OK):
  nxtps.result("Unexpected return code. TPS will not exit.")
  quit()

while (True):
  am_status = AutoModeStatus(nxtps.at_get_status())
  
  if (am_status == AutoModeStatus.LEVER1_MOVE_IN_PROG
    or am_status == AutoModeStatus.LEVER2_MOVE_IN_PROG):
    nxtps.result("A lever move is in progress with an async op.")
  elif (am_status == AutoModeStatus.MOVE_PAUSED):
    nxtps.result("An async op has been paused.")
  elif (am_status == AutoModeStatus.IDLE):
    nxtps.result("The levers are idle with an async op.")
    break
  elif (am_status == AutoModeStatus.NOT_IN_AUTO_MODE):
    nxtps.result("The async op has been completed or cancelled.")
    break

  time.sleep(1)


status = AtcStatus(nxtps.at_stop_auto_mode())

