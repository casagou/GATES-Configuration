import nxtps
import time

status = nxtps.AtcStatus (nxtps.AtcStatus.OK)


################################################################################
# INST 1: Start UECU-500 M3 Auto Mode
################################################################################

nxtps.instruction("Start UECU-500 M3 Auto Mode")

auto_mode_started = False

while (not auto_mode_started):
	
	nxtps.result("Attempting to start UECU-500 M3 Auto Mode.")	
	
	status = nxtps.AtcStatus(nxtps.at_start_auto_mode())
	
	if (status != nxtps.AtcStatus.OK):
		
		nxtps.result("Could not start UECU-500 M3 Auto Mode.")
		nxtps.result("[DIAGNOSTIC] status = " + str(status))
		
		retry_start_auto_mode = nxtps.prompt_boo("Attempt to start UECU-500 "
			"Auto Mode again? Select 'True' to re-try, otherwise select 'False'.")
		
		if (not retry_start_auto_mode):
			nxtps.result("Operator selected not to re-attempt starting of "
				"UECU-500 M3 Auto Mode. TPS will now exit.")
			quit()
		else:
			nxtps.result("Operator selected to re-attempt starting of "
				"UECU-500 M3 Auto Mode.")
		
	else:
		nxtps.result("UECU-500 M3 in Auto Mode.")
		auto_mode_started = True



################################################################################
# INST 2: Synchronous Automated Throttle Move (of TLA)
################################################################################

skip = nxtps.instruction("Synchronous Automated Throttle Move (of TLA)\n\nMove TLA to "
	"50 Deg, with a tolerance of 0.5, over a ramp time of 5 seconds and allow a "
	"further 5 seconds to ellapse before returning.", True)

if (not skip):

	sync_move_done = False

	while (not sync_move_done):

		nxtps.result("Attempting to start synchronous automated throttle move.")

		# Move TLA to 50 Deg, with a tolerance of 0.5, over a ramp time of 5 seconds
		# and allow a further 5 seconds to ellapse before returning.
		status = nxtps.AtcStatus(nxtps.at_move("TLA", 50, 5.0, 10.0, 0.5, 10.0))

		if (status != nxtps.AtcStatus.OK):
		
			nxtps.result("Could not undertake synchronous automated throttle move.")
			nxtps.result("[DIAGNOSTIC] status = " + str(status))
		
			retry_sync_move = nxtps.prompt_boo("Attempt to start synchronous "
				"automated throttle move again? Select 'True' to re-try, otherwise "
				"select 'False'.")
		
			if (not retry_sync_move):
				nxtps.result("Operator selected not to re-attempt synchronous "
				"automated throttle move. TPS will now exit.")
				quit()
			else:
				nxtps.result("Operator selected to re-attempt synchronous automated"
					" throttle move")
	
		else:
			nxtps.result("Synchronous automated throttle move completed.")
			sync_move_done = True



################################################################################
# INST 3: Asynchronous Automated Throttle Move (of TLA)
################################################################################

skip = nxtps.instruction("Asynchronous Automated Throttle Move (of TLA)\n\nMove TLA to "
	"100 Deg, with a tolerance of 0.5, over a ramp time of 20 seconds, and "
	"allow a further 10 seconds to ellapse before completion of auto mode "
	"move.", True)

if (not skip):

	async_move_done = False

	while (not async_move_done):

		nxtps.result("Attempting to start asynchronous automated throttle move.")
	
		# Async move TLA to 100 Deg, with a tolerance of 0.5, over a ramp time of 20
		# seconds, and allow a further 10 seconds to ellapse before completion of 
		# auto mode move.
		status = nxtps.AtcStatus(nxtps.at_move_async("TLA", 100, 20.0, 30.0, 0.5, 30.0))
	
		if (status != nxtps.AtcStatus.OK):
		
			nxtps.result("Could not undertake asynchronous automated throttle move.")
			nxtps.result("[DIAGNOSTIC] status = " + str(status))
		
			retry_async_move = nxtps.prompt_boo("Attempt to start asynchronous "
				"automated throttle move again? Select 'True' to re-try, otherwise "
				"select 'False'.")
	
			if (not retry_async_move):
				nxtps.result("Operator selected not to re-attempt asynchronous "
				"automated throttle move. TPS will now exit.")
				quit()
			else:
				nxtps.result("Operator selected to re-attempt asynchronous automated"
					" throttle move")
	
		else:
			nxtps.result("Asynchronous automated throttle move started.")
			nxtps.result("Asynchronous automated throttle move status polling:")
		
			# Poll for Auto Mode Status, while async move is in progress.  Move has
			# been cancelled if NOT_IN_AUTO_MODE returned (e.g., 'Cancel' button 
			# selected on Throttle GUI, or lever moved by operator, etc) or move has
			# completed.
			while (True):
			
				am_status = nxtps.AutoModeStatus(nxtps.at_get_status())
			
				if (am_status == nxtps.AutoModeStatus.LEVER1_MOVE_IN_PROG 
					or am_status == nxtps.AutoModeStatus.LEVER2_MOVE_IN_PROG):
				
					nxtps.result("A lever move is in progress with an async op.")
					
				elif (am_status == nxtps.AutoModeStatus.MOVE_PAUSED):
					nxtps.result("An async op has been paused.")
				
				elif (am_status == nxtps.AutoModeStatus.IDLE):
					nxtps.result("The levers are idle with an async op.")
					break
				
				elif (am_status == nxtps.AutoModeStatus.NOT_IN_AUTO_MODE):
					nxtps.result("The async op has been completed or cancelled.")
					break

				time.sleep(1)
		
			nxtps.result("Asynchronous automated throttle move status polling ended.")
			async_move_done = True



################################################################################
# INST X: Stop UECU-500 M3 Auto Mode
################################################################################

nxtps.instruction("Stop UECU-500 M3 Auto Mode")

status = nxtps.AtcStatus(nxtps.at_stop_auto_mode())

auto_mode_stopped = False

while (not auto_mode_stopped):

	nxtps.result("Attempting to stop UECU-500 M3 Auto Mode.")	
	
	status = nxtps.AtcStatus(nxtps.at_stop_auto_mode())
	
	if (status != nxtps.AtcStatus.OK and status != nxtps.AtcStatus.NOT_IN_AUTO_MODE):
		
		nxtps.result("Could not stop UECU-500 M3 Auto Mode.")
		nxtps.result("[DIAGNOSTIC] status = " + str(status))
		
		retry_stop_auto_mode = nxtps.prompt_boo("Attempt to stop UECU-500 "
			"Auto Mode again? Select 'True' to re-try, otherwise select 'False'.")
		
		if (not retry_stop_auto_mode):
			nxtps.result("Operator selected not to re-attempt stopping of "
				"UECU-500 M3 Auto Mode. TPS will now exit.")
			quit()
		else:
			nxtps.result("Operator selected to re-attempt stopping of "
				"UECU-500 M3 Auto Mode.")
	
	else:
		nxtps.result("UECU-500 M3 out of Auto Mode.")
		quit()

