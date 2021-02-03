# GATES-Configuration

*GATES-Configuration* provides simulated channels, limit/alarm monitoring, view pages, report templates, test procedures to demonstrate the data acquisition capabilities of nxDAS.

> Before starting to copying or merging the files, backup your system so you can revert any mistake.

## Version History

### 1.0.0
Features and Improvements:
- Update DAS Configuration (see diagram *GATES-Configuration.pdf* for details)
	- **Subsystems**
		- Calculated (100%)
		- ARINC (90%)
		- PBS (100%)
			- PBS21270
			- PBS21271
		- DTS (100%)
			- DTS1124
			- DTS1125
			- DTS1126
			- DTS1127
		- FCS1 (100%)
		- FCS2 (100%)
		- iDDS + iDDSnodes (90%)
			- MDS
				- nxCollector
				- 18:1-10000:r 19:10001-10500:r 20:10501-11000:r 21:11001-11500:r
				- CL_Enable
			- UEI
				- IOM-225593 (standard)
					- Cube1
					- rate = 20
					- Card 1
					- Card 2
					- Card 3
						- num_teeth = 60
						- cntr_latch = 1
				- IOM-226128 (rugged)
					- Cube2
					- rate = 20
					- Card 1
					- Card 2
					- Card 3
					- Card 4
				IOM-225763 (rugged)
					- Cube3
					- rate = 20
					- Card 1
					- Card 2
					- Card 3
					- Card 4
		- Throttle (100%)
		- Vibration (100%)
	- **Channels**
		- **ATP_Calibration**
			- PBS (100%) - Tested Comm OK @100Hz - Purge Commd OK
				- Update all GID
			- DTS (100%) - Tested Comm OK @40Hz - AD Cal OK
				- Update all GID
			- ARINC_Simulator (100%)
				- Add Mariusz ARINC loopback channel definition - Tested Comm OK
				- Update all GID
			- Cubes (100%)
				- Cube 1 Standard - Prototype (225593) - Tested Comm OK
					- Add all Channels
					- Update all GID
				- Cube 2 Rugged - Prototype (226128) - NOT AVAILABLE
					- Add all Channels
					- Update all GID
				- Cube 3 Rugged - Prototype (225763) - NOT AVAILABLE
					- Add all Channels
					- Update all GID
			- FCS (100%)
				- Add FCS1 and FC2 channels - Tested Comm OK ~3-5Hz
					- Update all GID
			- Calculated
				- Add mandatory for RTE and DAS
					- Alarms Buzz Ack
					- Fullset Status
					- CL
					- Num Fullset Log
					- Flip Clock
					- PBS Purge
					- DAS runtime
					- Fullset Log CR SW
				- Update all GID
	- **Transient Logs**
		- ATP_Calibration
			- Add DTS_Log 40Hz
			- Add PBS_Log 100Hz
			- Add Demo_Log_xxxHz from 1Hz to 200Hz
		- **CFM56-5B**
			- Nothing yet (0%)
		- **CFM56-7B**
			- Nothing yet (0%)
		- **CF6-80C2**
			- Nothing yet (0%)
	- Engineering Units
		- Standardize units for nxDAS - V13 (100%)
- RTE .config
	- Add PBS
	- Add arinc429
	- Add FCS1
	- Add FCS2
	- Update TRACE_DEST to Trace.rte

- RTE ethers
	- Add PB21270 and PB21271 MAC addresses
- RTE host
	- Add FCS HMI IP address
	- Add NAS IP address
	- Add Printer IP address
	- Add all cubes IP address
	- Add all DTS IP address
	- Add all PBS IP address
	- Add FCS PLC IP address
	- Include IP address shift for reserved IP
- Ini Files
	- MgtGUI.ini
		- Update PBS purge vent channel
- Invoke Script
	- None
- Test Procedure
	- None
- MgtGUI Scripts
	- None
- RAVE Report Templates
	- None
- RTD Pages
	- ATP_Calibration (10%)
- Palettes
	- OK (100%)
- Media
	- Add Pictures
	- Add Engineering Units

### 1.0.0-alpha
Features and Improvements:
- DAS Configuration
	- Subsystem
		- Calculated (100%)
		- PBS (100%)
		- DTS (100%)
		- FCS (100%)
		- iDDS + iDDSnodes (95%)
	- Channels
		- PBS (100%)
		- DTS (100%)
		- Cubes (1%) demo channel (not working)
		- FCS (0%)
- Ini Files
	- None
- Invoke Script
	- None
- Test Procedure
	- None
- MgtGUI Scripts
	- None
- RAVE Report Templates
	- None
- RTD Pages
	- None
- Palettes
	- None
- Media
	- None
	









