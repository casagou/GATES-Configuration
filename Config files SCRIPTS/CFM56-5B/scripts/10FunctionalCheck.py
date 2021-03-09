import sys
import os
import time
from math import *
from nxtps import *

# Global variable definition

#* 10FunctionalCheck.tps
#******************************************************************************
#*  AUTHOR: Nicholas Jeffers
#*
#*  DESCRIPTION: CFM56-5B ESM 72-00-00 TESTING 002
#*  Functional Check & Engine Seal Break-in
#*
#*  Modification History
#*
#*  DATE: 12/16/2020 
#*
#*  MODIFICATIONS:
#*  DATE         WHO  NCR    DESCRIPTION
#*
#*
#******************************************************************************

# ***** LOCAL VARIABLE DECLARATIONS *****
Done = None
VibSurvey = None

# Channel Registration
channel("B1,B2,B3,B4,B5,B6,B7,B8,B9,Eng_On,ID,MultiDevTest,N1K")

channel("N1TOB1,N1TOB2,N1TOB3,N1TOB4,N1TOB5,N1TOB6,N1TOB7,N1TOB8,N1TOB9")

channel("N1MCB1,N1MCB2,N1MCB3,N1MCB4,N1MCB5,N1MCB6,N1MCB7,N1MCB8,N1MCB9")


Done = 0

#* V1.01 MSk start ***************************************************************************
if getCV("MultiDevTest") == 1:
	if getCV("B3") == 1:
		set_channel("ID", 3)

	else:
		if getCV("B2") == 1:
			set_channel("ID", 2)

		else:
			if getCV("B1") == 1:
				set_channel("ID", 1)

			else:
				if getCV("B4") == 1:
					set_channel("ID", 4)

				else:
					if getCV("B7") == 1:
						set_channel("ID", 7)

					else:
						if getCV("B6") == 1:
							set_channel("ID", 6)

						else:
							if getCV("B9") == 1:
								set_channel("ID", 9)

							else:
								if getCV("B5") == 1:
									set_channel("ID", 5)

								else:
									if getCV("B8") == 1:
										set_channel("ID", 8)

										pass
									pass
								pass
							pass
						pass
					pass
				pass
			pass
		pass
	pass
#* V1.01 MSk end *****************************************************************************

#**************************************************
#********** Common to all engines *****************
#**************************************************

instruction("Slowly accelerate the engine speed in 30 s")

note("to reach 3400 rpm N1, hold it there for 5 s and decrease")

note("to 3100 rpm N1 in 10 s.")

wait("N1K = 3400", 30, 10, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "N1 did not reach 3400 rpm in 30 s.")

delay(5)

wait("N1K = 3100", 10, 10, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "N1 did not reach 3100 rpm in 10 s.")


if SkipGV:
	result("Operator skipped 3100 rpm N1 check {} FunctionalCheck ".format(REPORT))

	pass

instruction("Stabilize for 3.5 minutes")

delay(210)

do_fullset(5, "3100 N1", "FuncCheck_1")



#************************************************************
#********** Common to B3, B2, B1, B4 and B7 engines *********
#************************************************************

if getCV("B3") == 1 or getCV("B2") == 1 or getCV("B1") == 1 or getCV("B4") == 1 or getCV("B7") == 1:
	
	instruction("Slowly accelerate the engine speed in 30 s")

	note("to reach 4400 rpm N1, hold it there for 5 s and decrease")

	note("to 4000 rpm N1 in 10 s.")

	wait("N1K = 4400", 30, 10, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "N1 did not reach 4400 rpm in 30 s.")

	delay(5)

	wait("N1K = 4000", 10, 10, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "N1 did not reach 4000 rpm in 10 s.")

	
	if SkipGV:
		result("Operator skipped 4000 rpm N1 check {} FunctionalCheck ".format(REPORT))

		pass
	
	instruction("Stabilize for 3.5 minutes")

	delay(210)

	do_fullset(5, "4000 N1", "FuncCheck_2")

	Done = 1
	pass

#**********************************************************
#********** Common to B6, B9, B5, B8 engines **************
#**********************************************************

if getCV("B6") == 1 or getCV("B9") == 1 or getCV("B5") == 1 or getCV("B8") == 1:
	if Done == 0:
		instruction("Slowly accelerate the engine speed in 30 s")

		note("to reach 4100 rpm N1, hold it there for 5 s and decrease")

		note("to 3800 rpm N1 in 10 s.")

		wait("N1K = 4100", 30, 10, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "N1 did not reach 4100 rpm in 30 s.")

		delay(5)

		wait("N1K = 3800", 10, 10, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "N1 did not reach 3800 rpm in 10 s.")

		
		if SkipGV:
			result("Operator skipped 3800 rpm N1R check {} FunctionalCheck ".format(REPORT))

			pass
		
		instruction("Stabilize for 3.5 minutes")

		delay(210)

		do_fullset(5, "3800 N1", "FuncCheck_2")

		pass
	pass

#**********************************************************
#******************For B3, B2, B1 Only*********************
#**********************************************************

if getCV("B3") == 1 or getCV("B2") == 1 or getCV("B1") == 1:
	instruction("Slowly accelerate the engine speed in 30 s")

	note("to reach 4762 rpm N1, hold it there for 5 s and decrease")

	note("to 4400 rpm N1 in 10 s.")

	wait("N1K = 4762", 30, 10, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "N1 did not reach 4762 rpm in 30 s.")

	delay(5)

	wait("N1K = 4400", 10, 10, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "N1 did not reach 4400 rpm in 10 s.")

	
	if SkipGV:
		result("Operator skipped 4400 rpm N1 check {} FunctionalCheck ".format(REPORT))

		pass
	
	instruction("Stabilize for 3.5 minutes")

	delay(210)

	do_fullset(5, "4400 N1", "FuncCheck_2")

	pass

#**********************************************************
#*****************T/O break-in Points ***********
#**********************************************************

if getCV("B3") == 1:
	
	instruction("Slowly accelerate the engine speed in 30 s")

	note("to reach B3 Take Off rating +\- 10 rpm, hold it there for 5 s and decrease")

	note("to 4762 rpm N1 in 10 s.")

	wait("N1K = " +str(getCV("N1TOB3")) , 30, 10, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "N1 did not reach B3 Take Off in 30 s.")

	delay(5)

#	wait "N1K = 4762", 10, 10, , , , , , MSG, "N1 did not reach 4762 rpm in 10 s."
	wait("N1K = " +str(getCV("N1MCB3")) , 10, 10, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "N1 did not reach B3 Max Cont in 10 s.")

	
	if SkipGV:
		result("Operator skipped 4762 rpm N1 check {} FunctionalCheck ".format(REPORT))

		pass
	
	instruction("Stabilize for 3.5 minutes")

	delay(210)

	do_fullset(5, "4762 N1", "FuncCheck_2")

	
	Done = 1
else:
	if getCV("B2") == 1 and Done == 0:
		
		instruction("Slowly accelerate the engine speed in 30 s")

		note("to reach B2 Take Off rating +\- 10 rpm, hold it there for 5 s and decrease")

		note("to 4762 rpm N1 in 10 s.")

		wait("N1K = "+str(getCV("N1TOB2")) , 30, 10, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "N1 did not reach B2 Take Off in 30 s.")

		delay(5)

#		wait "N1K = 4762", 10, 10, , , , , , MSG, "N1 did not reach 4762 rpm in 10 s."
		wait("N1K = "+str(getCV("N1MCB2")) , 10, 10, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "N1 did not reach B2 Max Cont in 10 s.")

		
		if SkipGV:
			result("Operator skipped 4762 rpm N1 check {} FunctionalCheck ".format(REPORT))

			pass
		
		instruction("Stabilize for 3.5 minutes")

		delay(210)

		do_fullset(5, "4762 N1", "FuncCheck_2")

		Done = 1
	else:
		if getCV("B1") == 1 and Done == 0:
			
			instruction("Slowly accelerate the engine speed in 30 s")

			note("to reach B1 Take Off rating +\- 10 rpm, hold it there for 5 s and decrease")

			note("to 4762 rpm N1 in 10 s.")

			wait("N1K = "+str(getCV("N1TOB1")) , 30, 10, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "N1 did not reach B1 Take Off in 30 s.")

			delay(5)

#			wait "N1K = 4762", 10, 10, , , , , , MSG, "N1 did not reach 4762 rpm in 10 s."
			wait("N1K = "+str(getCV("N1MCB1")) , 10, 10, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "N1 did not reach B1 Max Cont in 10 s.")

			
			if SkipGV:
				result("Operator skipped 4762 rpm N1 check {} FunctionalCheck ".format(REPORT))

				pass
			
			instruction("Stabilize for 3.5 minutes")

			delay(210)

			do_fullset(5, "4762 N1", "FuncCheck_2")

			Done = 1
			
		else:
			
			if getCV("B4") == 1 and Done == 0:
				
				instruction("Slowly accelerate the engine speed in 30 s")

				note("to reach B4 Take Off rating +\- 10 rpm, hold it there for 5 s and decrease")

				note("to 4405 rpm N1 in 10 s.")

				wait("N1K = "+str(getCV("N1TOB4")) , 30, 10, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "N1 did not reach B4 Take Off in 30 s.")

				delay(5)

#				wait "N1K = 4405", 10, 10, , , , , , MSG, "N1 did not reach 4405 rpm in 10 s."
				wait("N1K = "+str(getCV("N1MCB4")) , 10, 10, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "N1 did not reach B4 Max Cont in 10 s.")

				
				if SkipGV:
					result("Operator skipped 4405 rpm N1 check {} FunctionalCheck ".format(REPORT))

					pass
				
				instruction("Stabilize for 3.5 minutes")

				delay(210)

				do_fullset(5, "4405 N1", "FuncCheck_2")

				Done = 1
				
			else:
				
				if getCV("B7") == 1 and Done == 0:
					
					instruction("Slowly accelerate the engine speed in 30 s")

					note("to reach B7 Take Off rating +\- 10 rpm, hold it there for 5 s and decrease")

					note("to 4405 rpm N1 in 10 s.")

					wait("N1K = "+str(getCV("N1TOB7")) , 30, 10, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "N1 did not reach B7 Take Off in 30 s.")

					delay(5)

#					wait "N1K = 4405", 10, 10, , , , , , MSG, "N1 did not reach 4405 rpm in 10 s."
					wait("N1K = "+str(getCV("N1MCB7")) , 10, 10, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "N1 did not reach B7 Max Cont in 10 s.")

					
					if SkipGV:
						result("Operator skipped 4405 rpm N1 check {} FunctionalCheck ".format(REPORT))

						pass
					
					instruction("Stabilize for 3.5 minutes")

					delay(210)

					do_fullset(5, "4405 N1", "FuncCheck_2")

					Done = 1
					
				else:
					
					if getCV("B6") == 1 and Done == 0:
						
						instruction("Slowly accelerate the engine speed in 30 s")

						note("to reach B6 Take Off rating +\- 10 rpm, hold it there for 5 s and decrease")

						note("to 4100 rpm N1 in 10 s.")

						wait("N1K = "+str(getCV("N1TOB6")) , 30, 10, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "N1 did not reach B6 Take Off  in 30 s.")

						delay(5)

#						wait "N1K = 4100", 10, 10, , , , , , MSG, "N1 did not reach 4100 rpm in 10 s."
						wait("N1K = "+str(getCV("N1MCB6")) , 10, 10, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "N1 did not reach B6 Max Cont in 10 s.")

						
						if SkipGV:
							result("Operator skipped 4100 rpm N1 check {} FunctionalCheck ".format(REPORT))

							pass
						
						instruction("Stabilize for 3.5 minutes")

						delay(210)

						do_fullset(5, "4100 N1", "FuncCheck_2")

						Done = 1
						
					else:
						
						if getCV("B9") == 1 and Done == 0:
							
							instruction("Slowly accelerate the engine speed in 30 s")

							note("to reach B9 Take Off +\- 10 rpm, hold it there for 5 s and decrease")

							note("to 4100 rpm N1 in 10 s.")

							wait("N1K = "+str(getCV("N1TOB9")) , 30, 10, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "N1 did not reach B9 Take Off in 30 s.")

							delay(5)

#							wait "N1K = 4100", 10, 10, , , , , , MSG, "N1 did not reach 4100 rpm in 10 s."
							wait("N1K = "+str(getCV("N1MCB9")) , 10, 10, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "N1 did not reach B9 Max Cont in 10 s.")

							
							if SkipGV:
								result("Operator skipped 4100 rpm N1 check {} FunctionalCheck ".format(REPORT))

								pass
							
							instruction("Stabilize for 3.5 minutes")

							delay(210)

							do_fullset(5, "4100 N1", "FuncCheck_2")

							Done = 1
							
						else:
							
							if getCV("B5") == 1 and Done == 0:
								
								instruction("Slowly accelerate the engine speed in 30 s")

								note("to reach B5 Take Off rating +\- 10 rpm, hold it there for 5 s and decrease")

								note("to 4100 rpm N1 in 10 s.")

								wait("N1K = "+str(getCV("N1TOB5")) , 30, 10, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "N1 did not reach B5 Take Off in 30 s.")

								delay(5)

#								wait "N1K = 4100", 10, 10, , , , , , MSG, "N1 did not reach 4100 rpm in 10 s."
								wait("N1K = "+str(getCV("N1MCB5")) , 10, 10, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "N1 did not reach B5 Max Cont in 10 s.")

								
								if SkipGV:
									result("Operator skipped 4100 rpm N1 check {} FunctionalCheck ".format(REPORT))

									pass
								
								instruction("Stabilize for 3.5 minutes")

								delay(210)

								do_fullset(5, "4100 N1", "FuncCheck_2")

								Done = 1
								
							else:
								
								if getCV("B8") == 1 and Done == 0:
									
									instruction("Slowly accelerate the engine speed in 30 s")

									note("to reach B8 Take Off rating +\- 10 rpm, hold it there for 5 s and decrease")

									note("to 4100 rpm N1 in 10 s.")

									wait("N1K = "+str(getCV("N1TOB8")) , 30, 10, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "N1 did not reach B8 Take Off in 30 s.")

									delay(5)

#									wait "N1K = 4100", 10, 10, , , , , , MSG, "N1 did not reach 4100 rpm in 10 s."
									wait("N1K = "+str(getCV("N1MCB8")) , 10, 10, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "N1 did not reach B8 Max Cont in 10 s.")

									
									if SkipGV:
										result("Operator skipped 4100 rpm N1 check {} FunctionalCheck ".format(REPORT))

										pass
									
									instruction("Stabilize for 3.5 minutes")

									delay(210)

									do_fullset(5, "4100 N1", "FuncCheck_2")

									Done = 1
									
									pass
								pass
							pass
						pass
					pass
				pass
			pass
		pass
	pass

instruction("Slowly decrease the engine speed in 120 s")

note("to reach min Idle")

wait("TLA = 0", 120, 10, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "N1 did not reach idle in 120 s.")

instruction("Stabilize for 7 minutes")

delay(300)

delay(120)

do_fullset(5, "Idle", "FuncCheck_GI")


instruction("Accelerate to Aproach Idle")

#wait "TLA = 0", 120, 10, , , , , , MSG, "N1 did not reach idle in 120 s." this should be a discrete from PLA
wait("AIFlag = 1", 2, 0.1, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, SKIP, "Failed to reach AI in 120 s")

instruction("Stabilize for 5 minutes")

delay(300)

do_fullset(5, "Flight Idle", "FuncCheck_2")


instruction("Decelerate to Ground Idle")

#wait "TLA = 0", 120, 10, , , , , , MSG, "N1 did not reach idle in 120 s." this should be a discrete from PLA
wait("GIFlag = 1", 5, 0.1, WAIT_PARAM3_DFT, WAIT_PARAM4_DFT, WAIT_PARAM5_DFT, WAIT_PARAM6_DFT, WAIT_PARAM7_DFT, MSG, "Engine is not at GI after 120 s")

instruction("Stabilize for 3 minutes")

delay(180)

do_fullset(5, "Ground Idle", "FuncCheck_GI")


VibSurvey = prompt_boo("Do you want to perform the Vibration Survey at this time?")


if VibSurvey:
	autostart("11VibrationSurvey")

	pass
