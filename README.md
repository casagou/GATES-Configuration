# GATES-Configuration 

*GATES-Configuration* provides simulated channels, limit/alarm monitoring, view pages, report templates, test procedures to demonstrate the data acquisition capabilities of nxDAS.

> Before starting to copying or merging the files, backup your system so you can revert any mistake.

## Version History

### 1.2.1

Features and Improvements:

- Nick started importing/merging engine channels to GATES system (1 tree)
- Renames Level 3 "MDS" by "ATP_Calibration" to comply with MVIB engine type convention
- Updates DAS Configuration (see diagram *GATES-Configuration.pdf* for details)
	- **Channels**
		- **ATP_Calibration**
			- Throttle (80%) - Tested Comm FAIL - Network config issue on PLC side
			- Vibration (80%)
				- Adds all PBS-4100 channels per MVIB_config file
				- Adds dummy calculated lockout channel
- RTE .config
	- Removes TSM
	- Adds Throttle (via Modbus Ethernet)
	- Adds Vibration (via MVIB)
		- text_config TRUE
- RTE host
	- Adds all Throttle devices
	- Adds temporary PBS-4100 corporate IP address for in-house testing only
	- Adds Printer
- Adds MVIB_config directory
	- Updates chassis_name by gates-pbs4100
	- Updates pbs_type by 7
- Updates GID convention per Nick request - See diagram
	
----

### 1.1.2

Bug Fixes:
- Modifies README structure

----

### 1.1.1

Bug Fixes:

- Modifies README structure

----

### 1.1.0

Features and Improvements:

- Updates DAS Configuration (see diagram *GATES-Configuration.pdf* for details)
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
				- Updates all GID
			- DTS (100%) - Tested Comm OK @40Hz - AD Cal OK
				- Updates all GID
			- ARINC_Simulator (100%)
				- Adds Mariusz ARINC loopback channel definition - Tested Comm OK
				- Updates all GID
			- Cubes (100%)
				- Cube 1 Standard - Prototype (225593) - Tested Comm OK
					- Adds all Channels
					- Updates all GID
				- Cube 2 Rugged - Prototype (226128) - NOT AVAILABLE
					- Adds all Channels
					- Updates all GID
				- Cube 3 Rugged - Prototype (225763) - NOT AVAILABLE
					- Adds all Channels
					- Updates all GID
			- FCS (100%)
				- Adds FCS1 and FC2 channels - Tested Comm OK ~3-5Hz
					- Updates all GID
			- Calculated
				- Adds mandatory for RTE and DAS
					- Alarms Buzz Ack
					- Fullset Status
					- CL
					- Num Fullset Log
					- Flip Clock
					- PBS Purge
					- DAS runtime
					- Fullset Log CR SW
				- Adds demo calculation simulation channels
				- Adds all Math channels
				- Updates all GID
	- **Transient Logs**
		- ATP_Calibration
			- Adds DTS_Log 40Hz
			- Adds PBS_Log 100Hz
			- Adds Demo_Log_xxxHz from 1Hz to 200Hz
		- **CFM56-5B**
			- Nothing yet (0%)
		- **CFM56-7B**
			- Nothing yet (0%)
		- **CF6-80C2**
			- Nothing yet (0%)
	- **bpts**
		- ATP_Calibration
			- Adds Demo BPT for demo calculations
			- Adds Demo BPT for RTD Overlays
			- Adds the 36 RTD thermocouple conversion tables
	- **polynomials**
		- ATP_Calibration
			- Adds Demo BPT for demo calculations
			- Adds Demo BPT for RTD Overlays
	- Engineering Units
		- Standardize units for nxDAS - V13 (100%)
- RTE .config
	- Adds PBS
	- Adds arinc429
	- Adds FCS1
	- Adds FCS2
	- Updates TRACE_DEST to Trace.rte
- RTE ethers
	- Adds PB21270 and PB21271 MAC addresses
- RTE host
	- Adds FCS HMI IP address
	- Adds NAS IP address
	- Adds Printer IP address
	- Adds all cubes IP address
	- Adds all DTS IP address
	- Adds all PBS IP address
	- Adds FCS PLC IP address
	- Include IP address shift for reserved IP
- Ini Files
	- MgtGUI.ini
		- Updates PBS purge vent channel
- Invoke Script
	- None
- Test Procedure
	- None
- MgtGUI Scripts
	- None
- RAVE Report Templates
	- None
- RTD Pages
	- ATP_Calibration (10%) - Wrong aspect ratio
- Palettes
	- OK (100%)
- Media
	- Adds Pictures - In-house testing hardware
	- Adds Engineering Units

----

### 1.1.0-alpha

Features and Improvements:

- DAS Configuration (see diagram *GATES-Configuration.pdf* for details)
	- Subsystem
		- Calculated (100%)
		- ARINC (20%)
		- PBS (100%)
		- DTS (100%)
		- FCS (90%)
		- iDDS + iDDSnodes (90%)
	- Channels
		- PBS (100%)
		- DTS (100%)
		- ARINC (0%)
		- Cubes (20%) (comm not working yet)
		- FCS (10%)
		- Calculated
			- Mandatory for RTE and DAS.
	- Engineering Units
		- V13 (100%)
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
	- ATP_Calibration (10%)
- Palettes
	- OK (100%)
- Media
	- None

----

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
	
----
