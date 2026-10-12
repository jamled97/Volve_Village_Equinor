# Data Dictionary — Volve Hugin Project

## 1\. Petrophysical well log

File:
WLC\_PETRO\_COMPUTED\_OUTPUT\_1.LAS

Format:
LAS

Well Info:
Mnemonic	Unit	Value	Description
STRT	M	3271	START
STOP	M	3631.9	STOP
STEP	M	0.1	STEP
NULL		-999.25	NULL VALUE
COMP		Statoil Petroleum	Company
WELL		15/9-F-1	Well
FLD		VOLVE	Field
LOC		Maersk Inspirer	Location
PROV			Province
CNTY			County
STATE			State
CTRY			Country
DATE			Log Date
SRVC			Service Company
UWI			Unique Well Identifier
API			API Number
LATI		058 26' 29.907" N    DMS	Latitude
LONG		001 53' 14.708" E    DMS	Longtitude
PD		MSL	Permanent Datum
ELZ	M	0	Elev. Log Zero



Depth index:
Curves Depth Range:	from 3271.0 to last 3631.9



Curves:

Mnemonic	Unit	Description
DEPTH	M	0  Depth
BVW	V/V	1  Bound Volume Water
COAL\_FLAG	unitless	2  Coal Flag
KLOGH	MD	3  Calculated Horizontal PERMEABILITY from logs
PHIF	V/V	4  Final porosity
SAND\_FLAG	unitless	5  Sand Flag
SW	V/V	6  Water Saturation (Archie)
VCARB	V/V	7  Volume of calcite; dolomite and siderite from log analysis; repo
VSH	V/V	8  (GR-15)/(250-15)





File:
WLC\_PETRO\_COMPUTED\_INPUT\_1.LAS



Format:
LAS



Well info:

Mnemonic	Unit	Value	Description

STRT	M	145.9	START

STOP	M	3631.9	STOP

STEP	M	0.1	STEP

NULL		-999.25	NULL VALUE

COMP		Statoil Petroleum	Company

WELL		15/9-F-1	Well

FLD		VOLVE	Field

LOC		Maersk Inspirer	Location

PROV			Province

CNTY			County

STATE			State

CTRY			Country

DATE			Log Date

SRVC			Service Company

UWI			Unique Well Identifier

API			API Number

LATI		"058 26' 29.907"" N    DMS"	Latitude

LONG		"001 53' 14.708"" E    DMS"	Longtitude

PD		MSL	Permanent Datum

ELZ	M	0.0	Elev. Log Zero



Depth index:
Curves Depth Range:	from 145.9 to last 3631.9



Curves:

Mnemonic	Unit	Description

DEPTH	M	0  Depth

ABDCQF01	g/cm3	v1

ABDCQF02	g/cm3	v1

ABDCQF03	g/cm3	v1

ABDCQF04	g/cm3	v1

BS	inches	v1

CALI	inches	v1

DRHO	g/cm3	v1

DT	us/ft	v1

GR	API	v1

NPHI	v/v	v1

PEF	b/elec	v1

RACEHM	ohm.m	v1

RACELM	ohm.m	v1

RD	ohm.m	v1

RHOB	g/cm3	v1

RM	ohm.m	v1

ROP	m/hr	v1

RPCEHM	ohm.m	v1

RPCELM	ohm.m	v1

RT	ohm.m	v1



File:
15\_9-19\_BT2\_CPI.las



Format:
LAS



Well info:

Mnemonic	Unit	Value	Description

STRT	M	3768.09	START DEPTH

STOP	M	4249.8264	STOP DEPTH

STEP	M	0.1524	STEP

NULL		-999.25	NULL VALUE

COMP			COMPANY

WELL		NO\_15/9-19\_BT2	WELL

FLD			FIELD

LOC			LOCATION

CTRY			COUNTRY

STAT			STATE

CNTY			COUNTY

SRVC			SERVICE COMPANY

DATE			DATE

API			API NUMBER

UWI			UNIQUE WELL ID



Depth index:
Curves Depth Range:	\[3768.09,4249.8264]



Curves:

Mnemonic	Unit	Description

DEPTH	M

BVW	V/V	PHIF\*SW

CARB\_FLAG	UNITLESS	Values changed using TEXT\_EDIT

COAL\_FLAG	UNITLESS	Coal flag

KLOGH	MD	Values changed using TEXT\_EDIT

KLOGV	MD	Vertical PERMEABILITY calculated from logs

PHIF	V/V	Final porosity

RHOFL	G/CM3	0.9

RHOMA	G/CM3	Fixed RHOMA

RW	OHMM	Formation Resistivity

SAND\_FLAG	UNITLESS	Values changed using TEXT\_EDIT

SW	V/V	Water Saturation

TEMP	DEGC	Calculated temperature curve

VSH	V/V	(GR-8)/(100-8)



File:
NO\_15\_9-19\_BT2\_KLOGH\_NEW.las



Format:
LAS



Well info:

Mnemonic	Unit	Value	Description

STRT	M	4035.7622	START DEPTH

STOP	M	4178.8657	STOP DEPTH

STEP	M	0.0	STEP

NULL		-999.25	NULL VALUE

COMP			COMPANY

WELL		NO\_15/9-19\_BT2	WELL

FLD			FIELD

LOC			LOCATION

CTRY			COUNTRY

STAT			STATE

CNTY			COUNTY

SRVC			SERVICE COMPANY

DATE			DATE

API			API NUMBER

UWI			UNIQUE WELL ID



Depth index:
Curves Depth Range:	 \[4035.7622,4178.8657]



Curves:

Mnemonic	Unit	Description

DEPTH	M	Measured Depth

KLOGH\_NEW	UNKNOWN	v1



## 2\. Hugin top depth horizon

File:
Hugin\_Fm\_Top+ST10010ZC11\_Near\_190314\_adj2\_2760\_EasyDC+STAT+DEPTH.dat



Format:
DAT



Coordinate fields:
x, y



Horizontal CRS:
ST\_ED50\_UTM31N\_P23031\_T1133



Vertical values:
Depth (unit and reference to verify)



Intended use:
Map and visualize the interpreted top of Hugin.





## 3\. Hugin base depth horizon



File:

Hugin\_Fm\_Base+ST10010ZC11\_Near\_190314\_adj\_2999\_EasyDC+STAT+DEPTH.dat



Format:

DAT



Coordinate fields:

x, y



Horizontal CRS:

ST\_ED50\_UTM31N\_P23031\_T1133



Vertical values:

Depth (unit and reference to verify)



Intended use:

Map and visualize the interpreted base of Hugin.





## 4\. Well picks

File:
Well\_picks\_Volve\_v1.dat



Format:
DAT



Well identifier:

15/9-F-1



Formation name:

To verify



Depth reference:

To verify



Intended use:

Tie the well log to the Hugin interval.



## 5\. Fault interpretations

File:

Volve\_Official\_Faults.dat



Format:

DAT



Coordinate fields:

See fault README



Horizontal CRS:

See fault README



Vertical coordinate:

To verify (time or depth)



Intended use:

Display interpreted fault geometry.



## Metadata status

Unknown:
Any units, datums, or coordinate references not
explicitly confirmed by the source documentation.

Verification needed:
Resolve unknowns before integrating the datasets.

