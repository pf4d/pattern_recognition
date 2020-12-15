from pylab import *

d1976 = load('data/1976.npy')
d1977 = load('data/1977.npy')
d1978 = load('data/1978.npy')
d1979 = load('data/1979.npy')
d1980 = load('data/1980.npy')
d1981 = load('data/1981.npy')
d1982 = load('data/1982.npy')
d1983 = load('data/1983.npy')
d1984 = load('data/1984.npy')
d1985 = load('data/1985.npy')
d1986 = load('data/1986.npy')
d1987 = load('data/1987.npy')
d1988 = load('data/1988.npy')
d1989 = load('data/1989.npy')
d1990 = load('data/1990.npy')
d1991 = load('data/1991.npy')
d1992 = load('data/1992.npy')
d1993 = load('data/1993.npy')
d1994 = load('data/1994.npy')
d1995 = load('data/1995.npy')
d1996 = load('data/1996.npy')
d1997 = load('data/1997.npy')
d1998 = load('data/1998.npy')
d1999 = load('data/1999.npy')
d2000 = load('data/2000.npy')
d2001 = load('data/2001.npy')
d2002 = load('data/2002.npy')
d2003 = load('data/2003.npy')
d2004 = load('data/2004.npy')
d2005 = load('data/2005.npy')
d2006 = load('data/2006.npy')
d2007 = load('data/2007.npy')
d2008 = load('data/2008.npy')
d2009 = load('data/2009.npy')
d2010 = load('data/2010.npy')
d2011 = load('data/2011.npy')
d2012 = load('data/2012.npy')

def groupConvert(g, sg):
	if   g == '0' or g == '0 ' or g == 0:
		return 1
	elif g == '1' or g == '1 ' or g == 1:
		return 2
	elif g == '2' or g == '2 ' or g == 2:
		return 6
	elif g == '3' or g == '3 ' or g == 3:
		return 7
	elif g == '4' or g == '4 ' or g == 4:
		return 8
	elif g == '5' or g == '5 ' or g == 5:
		return 9
	elif g == '6' or g == '6 ' or g == 6:
		return 10
	elif g == '7' or g == '7 ' or g == 7:
		return 11
	elif g == '8' or g == '8 ' or g == 8:
		return 12
	elif g == '9' or g == '9 ' or g == 9:
		return 18

	if   sg == '0' or sg == '0 ' or sg == 0:
		return 1
	elif sg == '1' or sg == '1 ' or sg == 1:
		return 2
	elif sg == '11' or sg == '1A' or sg == 11:
		return 3
	elif sg == '12' or sg == '1B' or sg == 12:
		return 4
	elif sg == '13' or sg == '1C' or sg == 13:
		return 5
	elif sg == '20' or sg == 20 or sg == '2' or sg == '2 ' or sg == 2:
		return 6
	elif sg == '30' or sg == 30 or sg == '3' or sg == '3 ' or sg == 3:
		return 7
	elif sg == '40' or sg == 40 or sg == '4' or sg == '4 ' or sg == 4:
		return 8
	elif sg == '50' or sg == 50 or sg == '5' or sg == '5 ' or sg == 5:
		return 9
	elif sg == '60' or sg == 60 or sg == '6' or sg == '6 ' or sg == 6:
		return 10
	elif sg == '70' or sg == 70 or sg == '7' or sg == '7 ' or sg == 7:
		return 11
	elif sg == '80' or sg == 80 or sg == '8' or sg == '8 ' or sg == 8:
		return 12
	elif sg == '81' or sg == '8A' or sg == 81:
		return 13
	elif sg == '82' or sg == '8B' or sg == 82:
		return 14
	elif sg == '83' or sg == '8C' or sg == 83:
		return 15
	elif sg == '84' or sg == '8D' or sg == 84:
		return 16
	elif sg == '85' or sg == '8E' or sg == 85:
		return 17
	elif sg == '90' or sg == 90 or sg == '9' or sg == '9 ' or sg == 9:
		return 18
	elif sg == '91' or sg == '9A' or sg == 91:
		return 19
	elif sg == '92' or sg == '9B' or sg == 92:
		return 20
	elif sg == '93' or sg == '9C' or sg == 93:
		return 21
	elif sg == '94' or sg == '9D' or sg == 94:
		return 22
	elif sg == '95' or sg == '9E' or sg == 95:
		return 23
	else:
		print 'group:', type(g), g, 'subgroup:', type(sg), sg

def typeConvert(t):
	if t == '1' or t == 'A' or t == 1:
		return 1
	elif t == '2' or t == 'B' or t == 2:
		return 2
	else:
		print 'type:', type(t), t

def sitConvert(s):
	if s == '1' or s == 'A' or s == 1:
		return 1
	elif s == '2' or s == 'B' or s == 2:
		return 2
	elif s == '3' or s == 'C' or s == 3:
		return 3
	elif s == '4' or s == 'D' or s == 4:
		return 4
	elif s == '5' or s == 'E' or s == 5:
		return 5
	elif s == '6' or s == 'F' or s == 6:
		return 6
	else:
		print 'situation:', type(s), s

def convSex(s):
	if s == '1' or s == 'M' or s == 1:
		return 1
	elif s == '2' or s == 'F' or s == 2:
		return 2
	elif s == '9' or s == '8' or s is None or s == 'U' \
		or s == 9 or s == 8:
		return 3
	else:
		print 'sex:', type(s), s

def convRace(r):
	if r == '1':
		return 'W'
	elif r == '2':
		return 'B'
	elif r == '3':
		return 'I'
	elif r == '4':
		return 'A'
	elif r == '9':
		return 'U'
	else:
		print 'race:', type(r), r

def convWeap(w):
	if w == '11' or w == 11:
		return 1
	elif w == '12' or w == 12:
		return 2
	elif w == '13' or w == 13:
		return 3
	elif w == '14' or w == 14:
		return 4
	elif w == '15' or w == 15:
		return 5
	elif w == '20' or w == 20:
		return 6
	elif w == '30' or w == 30:
		return 7
	elif w == '40' or w == 40:
		return 8
	elif w == '50' or w == 50:
		return 9
	elif w == '55' or w == 55:
		return 10
	elif w == '60' or w == 60:
		return 11
	elif w == '65' or w == 65:
		return 12
	elif w == '70' or w == 70:
		return 13
	elif w == '75' or w == 75:
		return 14
	elif w == '80' or w == 80:
		return 15
	elif w == '85' or w == 85:
		return 16
	elif w == '90' or w == '98' or w == '99' \
		or w == 90 or w == 98 or w == 99 or w is None:
		return 17
	else:
		print 'weapon:', type(w), w

def convRelation(r):
	if r == '1' or r == 'HU' or r == 1:
		return 1
	elif r == '2' or r == 'WI' or r == 2:
		return 2
	elif r == '3' or r == 'CH' or r == 3:
		return 3
	elif r == '4' or r == 'CW' or r == 4:
		return 4
	elif r == '5' or r == 'MO' or r == 5:
		return 5
	elif r == '6' or r == 'FA' or r == 6:
		return 6
	elif r == '7' or r == 'SO' or r == 7:
		return 7
	elif r == '8' or r == 'DA' or r == 8:
		return 8
	elif r == '9' or r == 'BR' or r == 9:
		return 9
	elif r == '10' or r == 'SI' or r == 10:
		return 10
	elif r == '11' or r == 'IL' or r == 11:
		return 11
	elif r == '12' or r == 'SF' or r == 12:
		return 12
	elif r == '13' or r == 'SM' or r == 13:
		return 13
	elif r == '14' or r == 'SS' or r == 14:
		return 14
	elif r == '15' or r == 'SD' or r == 15:
		return 15
	elif r == '16' or r == 'OF' or r == 16:
		return 16
	elif r == '17' or r == 'NE' or r == 17:
		return 17
	elif r == '18' or r == 'AQ' or r == 18:
		return 18
	elif r == '19' or r == 'BF' or r == 19:
		return 19
	elif r == '20' or r == 'GF' or r == 20:
		return 20
	elif r == '21' or r == 'XH' or r == 21:
		return 21
	elif r == '22' or r == 'XW' or r == 22:
		return 22
	elif r == '23' or r == 'EE' or r == 23:
		return 23
	elif r == '24' or r == 'ER' or r == 24:
		return 24
	elif r == '25' or r == 'FR' or r == 25:
		return 25
	elif r == '26' or r == 'HO' or r == 26:
		return 26
	elif r == '27' or r == 'OK' or r == 27:
		return 27
	elif r == '28' or r == 'ST' or r == 28:
		return 28
	elif r == '99' or r == 'UN' or r == 99 or r == '98' or r == 98 \
		or r == '88' or r == 88 or r is None:
		return 29
	else:
		print 'relation:', type(r), r

def convCircum(c):
	if c == '2' or c == 2:
		return 2
	elif c == '3' or c == 3:
		return 3
	elif c == '5' or c == 5:
		return 5
	elif c == '6' or c == 6:
		return 6
	elif c == '7' or c == 7:
		return 7
	elif c == '9' or c == 9:
		return 9
	elif c == '10' or c == 10:
		return 10
	elif c == '17' or c == 17:
		return 17
	elif c == '18' or c == 18:
		return 18
	elif c == '19' or c == 19:
		return 19
	elif c == '26' or c == 26:
		return 26
	elif c == '32' or c == 32:
		return 32
	elif c == '40' or c == 40:
		return 40
	elif c == '41' or c == 41:
		return 41
	elif c == '42' or c == 42:
		return 42
	elif c == '43' or c == 43:
		return 43
	elif c == '44' or c == 44:
		return 44
	elif c == '45' or c == 45:
		return 45
	elif c == '46' or c == 46:
		return 46
	elif c == '47' or c == 47:
		return 47
	elif c == '48' or c == 48:
		return 48
	elif c == '49' or c == 49:
		return 49
	elif c == '50' or c == 50:
		return 50
	elif c == '51' or c == 51:
		return 51
	elif c == '52' or c == 52:
		return 52
	elif c == '53' or c == 53:
		return 53
	elif c == '59' or c == 59:
		return 59
	elif c == '60' or c == 60:
		return 60
	elif c == '70' or c == 70:
		return 70
	elif c == '80' or c == 80:
		return 80
	elif c == '81' or c == 81:
		return 81
	elif c == '99' or c == 99 or c == 88 or c == '88' or c == '98' or c == 98 \
		or c == '998' or c == 998:
		return 99
	elif c is None:
		return 99
	else:
		print 'circumstance:', type(c), c

def convSubCircum(c):
	if c == '1' or c == 'A' or c == 1:
		return 1
	elif c == '2' or c == 'B' or c == 2:
		return 2
	elif c == '3' or c == 'C' or c == 3:
		return 3
	elif c == '4' or c == 'D' or c == 4:
		return 4
	elif c == '5' or c == 'E' or c == 5:
		return 5
	elif c == '6' or c == 'F' or c == 6:
		return 6
	elif c == '0' or c == 'G' or c == '9' or c == '8' or c == '7' \
		  or c == 0 or c == 7 or c == 8 or c == 9 or c is None:
		return 7
	else:
		print 'subcircumstance:', type(c), c

def convAge(a):
	if a == 'BB' or a == 'NB' or a == '100' or a == '101':
		return 0
	elif a is None or a == '998':
		return 999
	else:
		return int(a)

def convMSACode(c):
	if c is None:
		return 9999
	else:
		return int(c)

def convCount(c):
	if c is None:
		return 0
	else:
		return int(c)

header = {0  : 'year',
          1  : 'month',
          2  : 'state',
          3  : 'group',
          4  : 'population',
          5  : 'MSA indication',
          6  : 'MSA code',
          7  : 'type of homicide',
          8  : 'situation',
          9  : 'victim count',
          10 : 'offender count',
          11 : 'victim 1 age',
          12 : 'victim 1 sex',
          13 : 'victim 2 age',
          14 : 'victim 2 sex',
          15 : 'victim 3 age',
          16 : 'victim 3 sex',
          17 : 'victim 4 age',
          18 : 'victim 4 sex',
          19 : 'victim 5 age',
          20 : 'victim 5 sex',
          21 : 'victim 6 age',
          22 : 'victim 6 sex',
          23 : 'victim 7 age',
          24 : 'victim 7 sex',
          25 : 'victim 8 age',
          26 : 'victim 8 sex',
          27 : 'victim 9 age',
          28 : 'victim 9 sex',
          29 : 'victim 10 age',
          30 : 'victim 10 sex',
          31 : 'victim 11 age',
          32 : 'victim 11 sex',
          33 : 'offender 1 age',
          34 : 'offender 1 sex',
          35 : 'offender 1 weapon',
          36 : 'offender 1 relationship to victim 1',
          37 : 'offender 1 circumstance',
          38 : 'offender 1 sub-circumstance',
          39 : 'offender 2 age',
          40 : 'offender 2 sex',
          41 : 'offender 2 weapon',
          42 : 'offender 2 relationship to victim 1',
          43 : 'offender 2 circumstance',
          44 : 'offender 2 sub-circumstance',
          45 : 'offender 3 age',
          46 : 'offender 3 sex',
          47 : 'offender 3 weapon',
          48 : 'offender 3 relationship to victim 1',
          49 : 'offender 3 circumstance',
          50 : 'offender 3 sub-circumstance',
          51 : 'offender 4 age',
          52 : 'offender 4 sex',
          53 : 'offender 4 weapon',
          54 : 'offender 4 relationship to victim 1',
          55 : 'offender 4 circumstance',
          56 : 'offender 4 sub-circumstance',
          57 : 'offender 5 age',
          58 : 'offender 5 sex',
          59 : 'offender 5 weapon',
          60 : 'offender 5 relationship to victim 1',
          61 : 'offender 5 circumstance',
          62 : 'offender 5 sub-circumstance',
          63 : 'offender 6 age',
          64 : 'offender 6 sex',
          65 : 'offender 6 weapon',
          66 : 'offender 6 relationship to victim 1',
          67 : 'offender 6 circumstance',
          68 : 'offender 6 sub-circumstance',
          69 : 'offender 7 age',
          70 : 'offender 7 sex',
          71 : 'offender 7 weapon',
          72 : 'offender 7 relationship to victim 1',
          73 : 'offender 7 circumstance',
          74 : 'offender 7 sub-circumstance',
          75 : 'offender 8 age',
          76 : 'offender 8 sex',
          77 : 'offender 8 weapon',
          78 : 'offender 8 relationship to victim 1',
          79 : 'offender 8 circumstance',
          80 : 'offender 8 sub-circumstance',
          81 : 'offender 9 age',
          82 : 'offender 9 sex',
          83 : 'offender 9 weapon',
          84 : 'offender 9 relationship to victim 1',
          85 : 'offender 9 circumstance',
          86 : 'offender 9 sub-circumstance',
          87 : 'offender 10 age',
          88 : 'offender 10 sex',
          89 : 'offender 10 weapon',
          90 : 'offender 10 relationship to victim 1',
          91 : 'offender 10 circumstance',
          92 : 'offender 10 sub-circumstance',
          93 : 'offender 11 age',
          94 : 'offender 11 sex',
          95 : 'offender 11 weapon',
          96 : 'offender 11 relationship to victim 1',
          97 : 'offender 11 circumstance',
          98 : 'offender 11 sub-circumstance'}

group = {1  : "POSSESSIONS",
         2  : "ALL CITIES 250,000 OR OVER",
         3  : "ALL CITIES 1,000,000 OR OVER",
         4  : "CITIES BETWEEN 500,000 AND 999,999",
         5  : "CITIES BETWEEN 250,000 AND 499,999",
         6  : "CITIES BETWEEN 100,000 AND 249,999",
         7  : "CITIES BETWEEN 50,000 AND 99,999",
         8  : "CITIES BETWEEN 25,000 AND 49,999",
         9  : "CITIES BETWEEN 10,000 AND 24,999",
         10 : "CITIES BETWEEN 2,500 AND 9,999",
         11 : "CITIES UNDER 2,500",
         12 : "NON-MSA COUNTIES",
         13 : "NON-MSA COUNTIES 100,000 OR OVER",
         14 : "NON-MSA COUNTIES BETWEEN 25,000 AND 99,999",
         15 : "NON-MSA COUNTIES BETWEEN 10,000 AND 24,999",
         16 : "NON-MSA COUNTIES UNDER 10,000",
         17 : "NON-MSA STATE POLICE",
         18 : "MSA COUNTIES",
         19 : "MSA COUNTIES 100,000 OR OVER",
         20 : "MSA COUNTIES BETWEEN 25,000 AND 99,999",
         21 : "MSA COUNTIES BETWEEN 10,000 AND 24,999",
         22 : "MSA COUNTIES UNDER 10,000",
         23 : "MSA STATE POLICE"}


state = {1  : "ALABAMA",
         2  : "ARIZONA",
         3  : "ARKANSAS",
         4  : "CALIFORNIA",
         5  : "COLORADO",
         6  : "CONNETICUT",
         7  : "DELAWARE",
         8  : "WASHINGTON, D.C.",
         9  : "FLORIDA",
         10 : "GEORGIA",
         11 : "IDAHO",
         12 : "ILLINOIS",
         13 : "INDIANA",
         14 : "IOWA",
         15 : "KANSAS",
         16 : "KENTUCKY",
         17 : "LOUISIANA",
         18 : "MAINE",
         19 : "MARYLAND",
         20 : "MASSACHUSETTS",
         21 : "MICHIGAN",
         22 : "MINNESOTA",
         23 : "MISSISSIPPI",
         24 : "MISSOURI",
         25 : "MONTANA",
         26 : "NEBRASKA",
         27 : "NEVADA",
         28 : "NEW HAMPSHIRE",
         29 : "NEW JERSEY",
         30 : "NEW MEXICO",
         31 : "NEW YORK",
         32 : "NORTH CAROLINA",
         33 : "NORTH DAKOTA",
         34 : "OHIO",
         35 : "OKLAHOMA",
         36 : "OREGON",
         37 : "PENNSYLVANIA",
         38 : "RHODE ISLAND",
         39 : "SOUTH CAROLINA",
         40 : "SOUTH DAKOTA",
         41 : "TENNESSEE",
         42 : "TEXAS",
         43 : "UTAH",
         44 : "VERMONT",
         45 : "VIRGINIA",
         46 : "WASHINGTON",
         47 : "WEST VIRGINIA",
         48 : "WISCONSIN",
         49 : "WYOMING",
         50 : "ALASKA",
         51 : "HAWAII",
         52 : "CANAL ZONE",
         53 : "PUERTO RICO",
         54 : "AMERICAN SAMOA",
         55 : "GUAM",
         62 : "VIRGIN ISLANDS"}

group = {1  : "POSSESSIONS",
         2  : "ALL CITIES 250,000 OR OVER",
         3  : "ALL CITIES 1,000,000 OR OVER",
         4  : "CITIES BETWEEN 500,000 AND 999,999",
         5  : "CITIES BETWEEN 250,000 AND 499,999",
         6  : "CITIES BETWEEN 100,000 AND 249,999",
         7  : "CITIES BETWEEN 50,000 AND 99,999",
         8  : "CITIES BETWEEN 25,000 AND 49,999",
         9  : "CITIES BETWEEN 10,000 AND 24,999",
         10 : "CITIES BETWEEN 2,500 AND 9,999",
         11 : "CITIES UNDER 2,500",
         12 : "NON-MSA COUNTIES",
         13 : "NON-MSA COUNTIES 100,000 OR OVER",
         14 : "NON-MSA COUNTIES BETWEEN 25,000 AND 99,999",
         15 : "NON-MSA COUNTIES BETWEEN 10,000 AND 24,999",
         16 : "NON-MSA COUNTIES UNDER 10,000",
         17 : "NON-MSA STATE POLICE",
         18 : "MSA COUNTIES",
         19 : "MSA COUNTIES 100,000 OR OVER",
         20 : "MSA COUNTIES BETWEEN 25,000 AND 99,999",
         21 : "MSA COUNTIES BETWEEN 10,000 AND 24,999",
         22 : "MSA COUNTIES UNDER 10,000",
         23 : "MSA STATE POLICE"}

suburban = {0 : "NON-SUBURBAN",
            1 : "SUBURBAN"}

months = {1  : "JANUARY",
          2  : "FEBRUARY",
          3  : "MARCH",
          4  : "APRIL",
          5  : "MAY",
          6  : "JUNE",
          7  : "JULY",
          8  : "AUGUST",
          9  : "SEPTEMBER",
          10 : "OCTOBER",
          11 : "NOVEMBER",
          12 : "DECEMBER",
          99 : "UNKNOWN"}

ageUnder12mo = {1 : "BIRTH TO ONE WEEK OLD (INCLUDES \"ABANDONED INFANT\")",
                2 : "ONE WEEK TO TWELVE MONTHS OLD",
                9 : "INAP., NOT CODED 0 IN REF 23"}

homicide = {1 : "MURDER AND NONNEGLIGENT MANSLAUGHTER",
            2 : "MANSLAUGHTER BY NEGLIGENCE"}

situation = {1 : "SINGLE VICTIM; SINGLE OFFENDER",
             2 : "SINGLE VICTIM; UNKNOWN OFFENDER(S)",
             3 : "SINGLE VICTIM; MULTIPLE OFFENDERS",
             4 : "MULTIPLE VICTIMS; SINGLE OFFENDER",
             5 : "MULTIPLE VICTIMS; MULTIPLE OFFENDERS",
             6 : "MULTIPLE VICTIMS; UNKNOWN OFFENDER(S)"}

age = { 00  : 'UNKNOWN',
       'BB' : "7 DAYS OLD TO 364 DAYS OLD",
       'NB' : "BIRTH TO 6 DAYS OLD"}

sex = {1 : "MALE",
       2 : "FEMALE",
       3 : "UNKNOWN"}

weapon = {1  : "FIREARM, TYPE NOT STATED (DOES NOT INCLUDE MECHANIC'S GREASE GUN OR CAULKING GUN)",
          2  : "HANDGUN - PISTOL, REVOLVER, ETC.",
          3  : "RIFLE",
          4  : "SHOTGUN",
          5  : "OTHER GUN / UNKNOWN GUN",
          6  : "KNIFE OR CUTTING INSTRUMENT - INCLUDES ICEPICK, SCREWDRIVER, AX, ETC.",
          7  : "BLUNT OBJECT - HAMMER, CLUB, ETC. FACTS MUST SUGGEST WEAPON WAS NOT HANDS AND FEET.",
          8  : "PERSONAL WEAPONS - INCLUDES BEATING BY HANDS, FEET, AND OTHER BODY MEMBERS OR USE OF TEETH",
          9  : "POISON - DOES NOT INCLUDE GAS",
          10 : "PUSHED OR THROWN OUT WINDOW",
          11 : "EXPLOSIVES",
          12 : "FIRE",
          13 : "NARCOTICS AND DRUGS - INCLUDES SLEEPING PILLS",
          14 : "DROWNING",
          15 : "STRANGULATION - HANGING.",
          16 : "ASPHYXIATION - INCLUDES ASPHYXIATION OR DEATH BY GAS",
          17 : "OTHER- TYPE OF WEAPON NOT DESIGNED OR TYPE UNKNOWN"}

relationship = {1  : "HUSBAND",
                2  : "WIFE",
                3  : "COMMON-LAW HUSBAND",
                4  : "COMMON-LAW WIFE",
                5  : "MOTHER",
                6  : "FATHER",
                7  : "SON",
                8  : "DAUGHTER",
                9  : "BROTHER",
                10 : "SISTER",
                11 : "IN-LAW",
                12 : "STEPFATHER",
                13 : "STEPMOTHER",
                14 : "STEPSON",
                15 : "STEPDAUGHTER",
                16 : "OTHER FAMILY",
                17 : "NEIGHBOR",
                18 : "ACQUAINTANCE",
                19 : "BOYFRIEND",
                20 : "GIRLFRIEND",
                21 : "EX-HUSBAND",
                22 : "EX-WIFE",
                23 : "EMPLOYEE",
                24 : "EMPLOYER",
                25 : "FRIEND",
                26 : "HOMOSEXUAL RELATIONSHIP",
                27 : "OTHER - KNOWN TO VICTIM",
                28 : "STRANGER",
                29 : "UNKNOWN"}

circumstances = {2  : "RAPE",
                 3  : "ROBBERY",
                 5  : "BURGLARY",
                 6  : "LARCENY",
                 7  : "MOTOR VEHICLE THEFT",
                 9  : "ARSON",
                 10 : "PROSTITUTION AND COMMERCIALIZED VICE",
                 17 : "OTHER SEX OFFENSE",
                 18 : "NARCOTIC DRUG LAWS",
                 32 : "ABORTION",
                 19 : "GAMBLING",
                 26 : "OTHER - FELONY TYPE",
                 40 : "LOVER'S TRIANGLE",
                 41 : "CHILD KILLED BY BABYSITTER",
                 42 : "BRAWL DUE TO INFLUENCE OF ALCOHOL",
                 43 : "BRAWL DUE TO INFLUENCE OF NARCOTICS",
                 44 : "ARGUMENT OVER MONEY OR PROPERTY",
                 45 : "OTHER ARGUMENTS",
                 46 : "GANGLAND KILLINGS",
                 47 : "JUVENILE GANG KILLINGS",
                 48 : "INSTITUTIONAL KILLINGS",
                 49 : "SNIPER ATTACK",
                 50 : "VICTIM SHOT IN HUNTING ACCIDENT",
                 51 : "GUNCLEANING DEATH OTHER THAN SELF-INFLICTED",
                 52 : "CHILDREN PLAYING WITH GUN",
                 53 : "OTHER NEGLIGENT HANDLING OF GUN WHICH RESULTS IN DEATH",
                 59 : "ALL OTHER MANSLAUGHTER BY NEGLIGENCE",
                 60 : "OTHER NON-FELONY TYPE",
                 70 : "ALL SUSPECTED FELONY TYPE",
                 80 : "JUSTIFIABLE HOMICIDE - CIVILIAN",
                 81 : "JUSTIFIABLE HOMICIDE - POLICE",
                 99 : "ALL INSTANCES WHERE FACTS PROVIDED DO NOT PERMIT DETERMINATION"}

subCircum = {1 : "FELON ATTACKED POLICE OFFICER",
             2 : "FELON ATTACKED FELLOW POLICE OFFICER",
             3 : "FELON ATTACKED CIVILIAN",
             4 : "FELON ATTEMPTED FLIGHT FROM CRIME",
             5 : "FELON KILLED IN COMMISSION OF CRIME",
             6 : "FELON RESISTED ARREST",
             7 : "NOT ENOUGH INFORMATION TO DETERMINE"}

def gather_type_1(d,a,y):
	for m in d:
		n = []
		n.append(y)                       # year
		n.append(int(m[16]))              # month
		n.append(m[4])                    # state
		n.append(groupConvert(m[7],m[8])) # group
		n.append(int(m[10]))              # population
		#n.append(m[5])                    # agency code
		#n.append(m[14])                   # agency name
		n.append(int(m[13]))              # MSA indication
		n.append(int(m[12]))              # MSA code
		n.append(typeConvert(m[19]))      # type of homicide
		n.append(sitConvert(m[21]))       # situation
		n.append(int(m[22]) + 1)          # victim count
		n.append(int(m[23]) + 1)          # offender count

		n.append(int(m[24]))             # victim 1 age
		n.append(convSex(m[34]))         # victim 1 sex
		n.append(int(m[25]))             # victim 2 age
		n.append(convSex(m[35]))         # victim 2 sex
		n.append(int(m[26]))             # victim 3 age
		n.append(convSex(m[36]))         # victim 3 sex
		n.append(int(m[27]))             # victim 4 age
		n.append(convSex(m[37]))         # victim 4 sex
		n.append(int(m[28]))             # victim 5 age
		n.append(convSex(m[38]))         # victim 5 sex
		n.append(int(m[29]))             # victim 6 age
		n.append(convSex(m[39]))         # victim 6 sex
		n.append(int(m[30]))             # victim 7 age
		n.append(convSex(m[40]))         # victim 7 sex
		n.append(int(m[31]))             # victim 8 age
		n.append(convSex(m[41]))         # victim 8 sex
		n.append(int(m[32]))             # victim 9 age
		n.append(convSex(m[42]))         # victim 9 sex
		n.append(int(m[33]))             # victim 10 age
		n.append(convSex(m[43]))         # victim 10 sex
		n.append(convAge(None))          # victim 11 age
		n.append(convSex('9'))           # victim 11 sex

		n.append(int(m[64]))             # offender 1 age
		n.append(convSex(m[75]))         # offender 1 sex
		n.append(convWeap(m[108]))       # offender 1 weapon
		n.append(convRelation(m[119]))   # offender 1 relationship to victim 1
		n.append(convCircum(m[130]))     # offender 1 circumstance
		n.append(convSubCircum(m[141]))  # offender 1 sub-circumstance

		n.append(int(m[65]))             # offender 2 age
		n.append(convSex(m[76]))         # offender 2 sex
		n.append(convWeap(m[109]))       # offender 2 weapon
		n.append(convRelation(m[120]))   # offender 2 relationship to victim 1
		n.append(convCircum(m[131]))     # offender 2 circumstance
		n.append(convSubCircum(m[142]))  # offender 2 sub-circumstance

		n.append(int(m[66]))             # offender 3 age
		n.append(convSex(m[77]))         # offender 3 sex
		n.append(convWeap(m[110]))       # offender 3 weapon
		n.append(convRelation(m[121]))   # offender 3 relationship to victim 1
		n.append(convCircum(m[132]))     # offender 3 circumstance
		n.append(convSubCircum(m[143]))  # offender 3 sub-circumstance

		n.append(int(m[67]))             # offender 4 age
		n.append(convSex(m[78]))         # offender 4 sex
		n.append(convWeap(m[111]))       # offender 4 weapon
		n.append(convRelation(m[122]))   # offender 4 relationship to victim 1
		n.append(convCircum(m[133]))     # offender 4 circumstance
		n.append(convSubCircum(m[144]))  # offender 4 sub-circumstance

		n.append(int(m[68]))             # offender 5 age
		n.append(convSex(m[79]))         # offender 5 sex
		n.append(convWeap(m[112]))       # offender 5 weapon
		n.append(convRelation(m[123]))   # offender 5 relationship to victim 1
		n.append(convCircum(m[134]))     # offender 5 circumstance
		n.append(convSubCircum(m[145]))  # offender 5 sub-circumstance

		n.append(int(m[69]))             # offender 6 age
		n.append(convSex(m[80]))         # offender 6 sex
		n.append(convWeap(m[113]))       # offender 6 weapon
		n.append(convRelation(m[124]))   # offender 6 relationship to victim 1
		n.append(convCircum(m[135]))     # offender 6 circumstance
		n.append(convSubCircum(m[146]))  # offender 6 sub-circumstance

		n.append(int(m[70]))             # offender 7 age
		n.append(convSex(m[81]))         # offender 7 sex
		n.append(convWeap(m[114]))       # offender 7 weapon
		n.append(convRelation(m[125]))   # offender 7 relationship to victim 1
		n.append(convCircum(m[136]))     # offender 7 circumstance
		n.append(convSubCircum(m[147]))  # offender 7 sub-circumstance

		n.append(int(m[71]))             # offender 8 age
		n.append(convSex(m[82]))         # offender 8 sex
		n.append(convWeap(m[115]))       # offender 8 weapon
		n.append(convRelation(m[126]))   # offender 8 relationship to victim 1
		n.append(convCircum(m[137]))     # offender 8 circumstance
		n.append(convSubCircum(m[148]))  # offender 8 sub-circumstance

		n.append(int(m[72]))             # offender 9 age
		n.append(convSex(m[83]))         # offender 9 sex
		n.append(convWeap(m[116]))       # offender 9 weapon
		n.append(convRelation(m[127]))   # offender 9 relationship to victim 1
		n.append(convCircum(m[138]))     # offender 9 circumstance
		n.append(convSubCircum(m[149]))  # offender 9 sub-circumstance

		n.append(int(m[73]))             # offender 10 age
		n.append(convSex(m[84]))         # offender 10 sex
		n.append(convWeap(m[117]))       # offender 10 weapon
		n.append(convRelation(m[128]))   # offender 10 relationship to victim 1
		n.append(convCircum(m[139]))     # offender 10 circumstance
		n.append(convSubCircum(m[150]))  # offender 10 sub-circumstance

		n.append(int(m[74]))             # offender 11 age
		n.append(convSex(m[85]))         # offender 11 sex
		n.append(convWeap(m[118]))       # offender 11 weapon
		n.append(convRelation(m[129]))   # offender 11 relationship to victim 1
		n.append(convCircum(m[140]))     # offender 11 circumstance
		n.append(convSubCircum(m[151]))  # offender 11 sub-circumstance
		a.append(array(n))

def gather_type_2(d,a,y):
	for m in d:
		n = []
		n.append(y)                        # year
		n.append(int(m[16]))               # month
		n.append(m[5])                     # state
		n.append(groupConvert(None,m[7]))  # group
		n.append(int(m[10]))               # population
		#n.append(m[6])                     # agency code
		#n.append(m[14])                    # agency name
		n.append(int(m[13]))               # MSA indication
		n.append(int(m[12]))               # MSA code
		n.append(typeConvert(m[19]))       # type of homicide
		n.append(sitConvert(m[21]))        # situation
		n.append(int(m[22]) + 1)           # victim count
		n.append(int(m[23]) + 1)           # offender count

		n.append(int(m[24]))             # victim 1 age
		n.append(convSex(m[25]))         # victim 1 sex
		n.append(int(m[28]))             # victim 2 age
		n.append(convSex(m[29]))         # victim 2 sex
		n.append(int(m[32]))             # victim 3 age
		n.append(convSex(m[33]))         # victim 3 sex
		n.append(int(m[36]))             # victim 4 age
		n.append(convSex(m[37]))         # victim 4 sex
		n.append(int(m[40]))             # victim 5 age
		n.append(convSex(m[41]))         # victim 5 sex
		n.append(int(m[44]))             # victim 6 age
		n.append(convSex(m[45]))         # victim 6 sex
		n.append(int(m[48]))             # victim 7 age
		n.append(convSex(m[49]))         # victim 7 sex
		n.append(int(m[52]))             # victim 8 age
		n.append(convSex(m[53]))         # victim 8 sex
		n.append(int(m[56]))             # victim 9 age
		n.append(convSex(m[57]))         # victim 9 sex
		n.append(int(m[60]))             # victim 10 age
		n.append(convSex(m[61]))         # victim 10 sex
		n.append(convAge(None))          # victim 11 age
		n.append(convSex('9'))           # victim 11 sex

		n.append(int(m[68]))             # offender 1 age
		n.append(convSex(m[69]))         # offender 1 sex
		n.append(convWeap(m[72]))        # offender 1 weapon
		n.append(convRelation(m[73]))    # offender 1 relationship to victim 1
		n.append(convCircum(m[74]))      # offender 1 circumstance
		n.append(convSubCircum(m[75]))   # offender 1 sub-circumstance

		n.append(int(m[76]))             # offender 2 age
		n.append(convSex(m[77]))         # offender 2 sex
		n.append(convWeap(m[80]))        # offender 2 weapon
		n.append(convRelation(m[81]))    # offender 2 relationship to victim 1
		n.append(convCircum(m[82]))      # offender 2 circumstance
		n.append(convSubCircum(m[83]))   # offender 2 sub-circumstance

		n.append(int(m[84]))             # offender 3 age
		n.append(convSex(m[85]))         # offender 3 sex
		n.append(convWeap(m[88]))        # offender 3 weapon
		n.append(convRelation(m[89]))    # offender 3 relationship to victim 1
		n.append(convCircum(m[90]))      # offender 3 circumstance
		n.append(convSubCircum(m[91]))   # offender 3 sub-circumstance

		n.append(int(m[92]))             # offender 4 age
		n.append(convSex(m[93]))         # offender 4 sex
		n.append(convWeap(m[96]))        # offender 4 weapon
		n.append(convRelation(m[97]))    # offender 4 relationship to victim 1
		n.append(convCircum(m[98]))      # offender 4 circumstance
		n.append(convSubCircum(m[99]))   # offender 4 sub-circumstance

		n.append(int(m[100]))            # offender 5 age
		n.append(convSex(m[101]))        # offender 5 sex
		n.append(convWeap(m[104]))       # offender 5 weapon
		n.append(convRelation(m[105]))   # offender 5 relationship to victim 1
		n.append(convCircum(m[106]))     # offender 5 circumstance
		n.append(convSubCircum(m[107]))  # offender 5 sub-circumstance

		n.append(int(m[108]))            # offender 6 age
		n.append(convSex(m[109]))        # offender 6 sex
		n.append(convWeap(m[112]))       # offender 6 weapon
		n.append(convRelation(m[113]))   # offender 6 relationship to victim 1
		n.append(convCircum(m[114]))     # offender 6 circumstance
		n.append(convSubCircum(m[115]))  # offender 6 sub-circumstance

		n.append(int(m[116]))            # offender 7 age
		n.append(convSex(m[117]))        # offender 7 sex
		n.append(convWeap(m[120]))       # offender 7 weapon
		n.append(convRelation(m[121]))   # offender 7 relationship to victim 1
		n.append(convCircum(m[122]))     # offender 7 circumstance
		n.append(convSubCircum(m[123]))  # offender 7 sub-circumstance

		n.append(int(m[124]))            # offender 8 age
		n.append(convSex(m[125]))        # offender 8 sex
		n.append(convWeap(m[128]))       # offender 8 weapon
		n.append(convRelation(m[129]))   # offender 8 relationship to victim 1
		n.append(convCircum(m[130]))     # offender 8 circumstance
		n.append(convSubCircum(m[131]))  # offender 8 sub-circumstance

		n.append(int(m[132]))            # offender 9 age
		n.append(convSex(m[133]))        # offender 9 sex
		n.append(convWeap(m[136]))       # offender 9 weapon
		n.append(convRelation(m[137]))   # offender 9 relationship to victim 1
		n.append(convCircum(m[138]))     # offender 9 circumstance
		n.append(convSubCircum(m[139]))  # offender 9 sub-circumstance

		n.append(int(m[140]))            # offender 10 age
		n.append(convSex(m[141]))        # offender 10 sex
		n.append(convWeap(m[144]))       # offender 10 weapon
		n.append(convRelation(m[145]))   # offender 10 relationship to victim 1
		n.append(convCircum(m[146]))     # offender 10 circumstance
		n.append(convSubCircum(m[147]))  # offender 10 sub-circumstance

		n.append(int(m[148]))            # offender 11 age
		n.append(convSex(m[149]))        # offender 11 sex
		n.append(convWeap(m[152]))       # offender 11 weapon
		n.append(convRelation(m[153]))   # offender 11 relationship to victim 1
		n.append(convCircum(m[154]))     # offender 11 circumstance
		n.append(convSubCircum(m[155]))  # offender 11 sub-circumstance
		a.append(array(n))

def gather_type_3(d,a,y):
	for m in d:
		n = []
		n.append(y)                        # year
		n.append(int(m[12]))               # month
		n.append(m[1])                     # state
		n.append(groupConvert(None,m[3]))  # group
		n.append(int(m[6]))                # population
		#n.append(m[2])                     # agency code
		#n.append(m[10])                    # agency name
		n.append(int(m[9]))                # MSA indication
		n.append(convMSACode(m[8]))        # MSA code
		n.append(typeConvert(m[15]))       # type of homicide
		n.append(sitConvert(m[17]))        # situation
		n.append(int(m[30]) + 1)           # victim count
		n.append(int(m[31]) + 1)           # offender count

		n.append(convAge(m[18]))         # victim 1 age
		n.append(convSex(m[19]))         # victim 1 sex
		n.append(convAge(m[32]))         # victim 2 age
		n.append(convSex(m[33]))         # victim 2 sex
		n.append(convAge(m[36]))         # victim 3 age
		n.append(convSex(m[37]))         # victim 3 sex
		n.append(convAge(m[40]))         # victim 4 age
		n.append(convSex(m[41]))         # victim 4 sex
		n.append(convAge(m[44]))         # victim 5 age
		n.append(convSex(m[45]))         # victim 5 sex
		n.append(convAge(m[48]))         # victim 6 age
		n.append(convSex(m[49]))         # victim 6 sex
		n.append(convAge(m[52]))         # victim 7 age
		n.append(convSex(m[53]))         # victim 7 sex
		n.append(convAge(m[56]))         # victim 8 age
		n.append(convSex(m[57]))         # victim 8 sex
		n.append(convAge(m[60]))         # victim 9 age
		n.append(convSex(m[61]))         # victim 9 sex
		n.append(convAge(m[64]))         # victim 10 age
		n.append(convSex(m[65]))         # victim 10 sex
		n.append(convAge(m[68]))         # victim 11 age
		n.append(convSex(m[69]))         # victim 11 sex

		n.append(convAge(m[22]))         # offender 1 age
		n.append(convSex(m[23]))         # offender 1 sex
		n.append(convWeap(m[26]))        # offender 1 weapon
		n.append(convRelation(m[27]))    # offender 1 relationship to victim 1
		n.append(convCircum(m[28]))      # offender 1 circumstance
		n.append(convSubCircum(m[29]))   # offender 1 sub-circumstance

		n.append(convAge(m[72]))         # offender 2 age
		n.append(convSex(m[73]))         # offender 2 sex
		n.append(convWeap(m[76]))        # offender 2 weapon
		n.append(convRelation(m[77]))    # offender 2 relationship to victim 1
		n.append(convCircum(m[78]))      # offender 2 circumstance
		n.append(convSubCircum(m[79]))   # offender 2 sub-circumstance

		n.append(convAge(m[80]))         # offender 3 age
		n.append(convSex(m[81]))         # offender 3 sex
		n.append(convWeap(m[84]))        # offender 3 weapon
		n.append(convRelation(m[85]))    # offender 3 relationship to victim 1
		n.append(convCircum(m[86]))      # offender 3 circumstance
		n.append(convSubCircum(m[87]))   # offender 3 sub-circumstance

		n.append(convAge(m[88]))         # offender 4 age
		n.append(convSex(m[89]))         # offender 4 sex
		n.append(convWeap(m[92]))        # offender 4 weapon
		n.append(convRelation(m[93]))    # offender 4 relationship to victim 1
		n.append(convCircum(m[94]))      # offender 4 circumstance
		n.append(convSubCircum(m[95]))   # offender 4 sub-circumstance

		n.append(convAge(m[96]))         # offender 5 age
		n.append(convSex(m[97]))         # offender 5 sex
		n.append(convWeap(m[100]))       # offender 5 weapon
		n.append(convRelation(m[101]))   # offender 5 relationship to victim 1
		n.append(convCircum(m[102]))     # offender 5 circumstance
		n.append(convSubCircum(m[103]))  # offender 5 sub-circumstance

		n.append(convAge(m[104]))        # offender 6 age
		n.append(convSex(m[105]))        # offender 6 sex
		n.append(convWeap(m[108]))       # offender 6 weapon
		n.append(convRelation(m[109]))   # offender 6 relationship to victim 1
		n.append(convCircum(m[110]))     # offender 6 circumstance
		n.append(convSubCircum(m[111]))  # offender 6 sub-circumstance

		n.append(convAge(m[112]))        # offender 7 age
		n.append(convSex(m[113]))        # offender 7 sex
		n.append(convWeap(m[116]))       # offender 7 weapon
		n.append(convRelation(m[117]))   # offender 7 relationship to victim 1
		n.append(convCircum(m[118]))     # offender 7 circumstance
		n.append(convSubCircum(m[119]))  # offender 7 sub-circumstance

		n.append(convAge(m[120]))        # offender 8 age
		n.append(convSex(m[121]))        # offender 8 sex
		n.append(convWeap(m[124]))       # offender 8 weapon
		n.append(convRelation(m[125]))   # offender 8 relationship to victim 1
		n.append(convCircum(m[126]))     # offender 8 circumstance
		n.append(convSubCircum(m[127]))  # offender 8 sub-circumstance

		n.append(convAge(m[128]))        # offender 9 age
		n.append(convSex(m[129]))        # offender 9 sex
		n.append(convWeap(m[132]))       # offender 9 weapon
		n.append(convRelation(m[133]))   # offender 9 relationship to victim 1
		n.append(convCircum(m[134]))     # offender 9 circumstance
		n.append(convSubCircum(m[135]))  # offender 9 sub-circumstance

		n.append(convAge(m[136]))        # offender 10 age
		n.append(convSex(m[137]))        # offender 10 sex
		n.append(convWeap(m[140]))       # offender 10 weapon
		n.append(convRelation(m[141]))   # offender 10 relationship to victim 1
		n.append(convCircum(m[142]))     # offender 10 circumstance
		n.append(convSubCircum(m[143]))  # offender 10 sub-circumstance

		n.append(convAge(m[144]))        # offender 11 age
		n.append(convSex(m[145]))        # offender 11 sex
		n.append(convWeap(m[148]))       # offender 11 weapon
		n.append(convRelation(m[149]))   # offender 11 relationship to victim 1
		n.append(convCircum(m[150]))     # offender 11 circumstance
		n.append(convSubCircum(m[151]))  # offender 11 sub-circumstance
		a.append(array(n))

def gather_type_4(d,a,y):
	for m in d:
		n = []
		n.append(y)                        # year
		n.append(int(m[16]))               # month
		n.append(m[4])                     # state
		n.append(groupConvert(m[7],m[8]))  # group
		n.append(int(m[10]))               # population
		#n.append(m[5])                     # agency code
		#n.append(m[14])                    # agency name
		n.append(int(m[13]))               # MSA indication
		n.append(int(m[12]))               # MSA code
		n.append(typeConvert(m[19]))       # type of homicide
		n.append(sitConvert(m[21]))        # situation
		n.append(int(m[22]) + 1)           # victim count
		n.append(int(m[23]) + 1)           # offender count

		n.append(int(m[24]))             # victim 1 age
		n.append(convSex(m[25]))         # victim 1 sex
		n.append(int(m[28]))             # victim 2 age
		n.append(convSex(m[29]))         # victim 2 sex
		n.append(int(m[32]))             # victim 3 age
		n.append(convSex(m[33]))         # victim 3 sex
		n.append(int(m[36]))             # victim 4 age
		n.append(convSex(m[37]))         # victim 4 sex
		n.append(int(m[40]))             # victim 5 age
		n.append(convSex(m[41]))         # victim 5 sex
		n.append(int(m[44]))             # victim 6 age
		n.append(convSex(m[45]))         # victim 6 sex
		n.append(int(m[48]))             # victim 7 age
		n.append(convSex(m[49]))         # victim 7 sex
		n.append(int(m[52]))             # victim 8 age
		n.append(convSex(m[53]))         # victim 8 sex
		n.append(int(m[56]))             # victim 9 age
		n.append(convSex(m[57]))         # victim 9 sex
		n.append(int(m[60]))             # victim 10 age
		n.append(convSex(m[61]))         # victim 10 sex
		n.append(int(m[64]))             # victim 11 age
		n.append(convSex(m[65]))         # victim 11 sex

		n.append(int(m[68]))             # offender 1 age
		n.append(convSex(m[69]))         # offender 1 sex
		n.append(convWeap(m[72]))        # offender 1 weapon
		n.append(convRelation(m[73]))    # offender 1 relationship to victim 1
		n.append(convCircum(m[74]))      # offender 1 circumstance
		n.append(convSubCircum(m[75]))   # offender 1 sub-circumstance

		n.append(int(m[76]))             # offender 2 age
		n.append(convSex(m[77]))         # offender 2 sex
		n.append(convWeap(m[80]))        # offender 2 weapon
		n.append(convRelation(m[81]))    # offender 2 relationship to victim 1
		n.append(convCircum(m[82]))      # offender 2 circumstance
		n.append(convSubCircum(m[83]))   # offender 2 sub-circumstance

		n.append(int(m[84]))             # offender 3 age
		n.append(convSex(m[85]))         # offender 3 sex
		n.append(convWeap(m[88]))        # offender 3 weapon
		n.append(convRelation(m[89]))    # offender 3 relationship to victim 1
		n.append(convCircum(m[90]))      # offender 3 circumstance
		n.append(convSubCircum(m[91]))   # offender 3 sub-circumstance

		n.append(int(m[92]))             # offender 4 age
		n.append(convSex(m[93]))         # offender 4 sex
		n.append(convWeap(m[96]))        # offender 4 weapon
		n.append(convRelation(m[97]))    # offender 4 relationship to victim 1
		n.append(convCircum(m[98]))      # offender 4 circumstance
		n.append(convSubCircum(m[99]))   # offender 4 sub-circumstance

		n.append(int(m[100]))            # offender 5 age
		n.append(convSex(m[101]))        # offender 5 sex
		n.append(convWeap(m[104]))       # offender 5 weapon
		n.append(convRelation(m[105]))   # offender 5 relationship to victim 1
		n.append(convCircum(m[106]))     # offender 5 circumstance
		n.append(convSubCircum(m[107]))  # offender 5 sub-circumstance

		n.append(int(m[108]))            # offender 6 age
		n.append(convSex(m[109]))        # offender 6 sex
		n.append(convWeap(m[112]))       # offender 6 weapon
		n.append(convRelation(m[113]))   # offender 6 relationship to victim 1
		n.append(convCircum(m[114]))     # offender 6 circumstance
		n.append(convSubCircum(m[115]))  # offender 6 sub-circumstance

		n.append(int(m[116]))            # offender 7 age
		n.append(convSex(m[117]))        # offender 7 sex
		n.append(convWeap(m[120]))       # offender 7 weapon
		n.append(convRelation(m[121]))   # offender 7 relationship to victim 1
		n.append(convCircum(m[122]))     # offender 7 circumstance
		n.append(convSubCircum(m[123]))  # offender 7 sub-circumstance

		n.append(int(m[124]))            # offender 8 age
		n.append(convSex(m[125]))        # offender 8 sex
		n.append(convWeap(m[128]))       # offender 8 weapon
		n.append(convRelation(m[129]))   # offender 8 relationship to victim 1
		n.append(convCircum(m[130]))     # offender 8 circumstance
		n.append(convSubCircum(m[131]))  # offender 8 sub-circumstance

		n.append(int(m[132]))            # offender 9 age
		n.append(convSex(m[133]))        # offender 9 sex
		n.append(convWeap(m[136]))       # offender 9 weapon
		n.append(convRelation(m[137]))   # offender 9 relationship to victim 1
		n.append(convCircum(m[138]))     # offender 9 circumstance
		n.append(convSubCircum(m[139]))  # offender 9 sub-circumstance

		n.append(int(m[140]))            # offender 10 age
		n.append(convSex(m[141]))        # offender 10 sex
		n.append(convWeap(m[144]))       # offender 10 weapon
		n.append(convRelation(m[145]))   # offender 10 relationship to victim 1
		n.append(convCircum(m[146]))     # offender 10 circumstance
		n.append(convSubCircum(m[147]))  # offender 10 sub-circumstance

		n.append(int(m[148]))            # offender 11 age
		n.append(convSex(m[149]))        # offender 11 sex
		n.append(convWeap(m[152]))       # offender 11 weapon
		n.append(convRelation(m[153]))   # offender 11 relationship to victim 1
		n.append(convCircum(m[154]))     # offender 11 circumstance
		n.append(convSubCircum(m[155]))  # offender 11 sub-circumstance
		a.append(array(n))

def gather_type_5(d,a,y):
	for m in d:
		n = []
		n.append(y)                        # year
		n.append(int(m[16]))               # month
		n.append(m[5])                     # state
		n.append(groupConvert(None,m[7]))  # group
		n.append(int(m[10]))               # population
		#n.append(m[6])                     # agency code
		#n.append(m[14])                    # agency name
		n.append(int(m[13]))               # MSA indication
		n.append(int(m[12]))               # MSA code
		n.append(typeConvert(m[19]))       # type of homicide
		n.append(sitConvert(m[21]))        # situation
		n.append(int(m[22]) + 1)           # victim count
		n.append(int(m[23]) + 1)           # offender count

		n.append(convAge(m[24]))         # victim 1 age
		n.append(convSex(m[25]))         # victim 1 sex
		n.append(convAge(m[28]))         # victim 2 age
		n.append(convSex(m[29]))         # victim 2 sex
		n.append(convAge(m[32]))         # victim 3 age
		n.append(convSex(m[33]))         # victim 3 sex
		n.append(convAge(m[36]))         # victim 4 age
		n.append(convSex(m[37]))         # victim 4 sex
		n.append(convAge(m[40]))         # victim 5 age
		n.append(convSex(m[41]))         # victim 5 sex
		n.append(convAge(m[44]))         # victim 6 age
		n.append(convSex(m[45]))         # victim 6 sex
		n.append(convAge(m[48]))         # victim 7 age
		n.append(convSex(m[49]))         # victim 7 sex
		n.append(convAge(m[52]))         # victim 8 age
		n.append(convSex(m[53]))         # victim 8 sex
		n.append(convAge(m[56]))         # victim 9 age
		n.append(convSex(m[57]))         # victim 9 sex
		n.append(convAge(m[60]))         # victim 10 age
		n.append(convSex(m[61]))         # victim 10 sex
		n.append(convAge(m[64]))         # victim 11 age
		n.append(convSex(m[65]))         # victim 11 sex

		n.append(int(m[68]))             # offender 1 age
		n.append(convSex(m[69]))         # offender 1 sex
		n.append(convWeap(m[72]))        # offender 1 weapon
		n.append(convRelation(m[73]))    # offender 1 relationship to victim 1
		n.append(convCircum(m[74]))      # offender 1 circumstance
		n.append(convSubCircum(m[75]))   # offender 1 sub-circumstance

		n.append(int(m[76]))             # offender 2 age
		n.append(convSex(m[77]))         # offender 2 sex
		n.append(convWeap(m[80]))        # offender 2 weapon
		n.append(convRelation(m[81]))    # offender 2 relationship to victim 1
		n.append(convCircum(m[82]))      # offender 2 circumstance
		n.append(convSubCircum(m[83]))   # offender 2 sub-circumstance

		n.append(int(m[84]))             # offender 3 age
		n.append(convSex(m[85]))         # offender 3 sex
		n.append(convWeap(m[88]))        # offender 3 weapon
		n.append(convRelation(m[89]))    # offender 3 relationship to victim 1
		n.append(convCircum(m[90]))      # offender 3 circumstance
		n.append(convSubCircum(m[91]))   # offender 3 sub-circumstance

		n.append(int(m[92]))             # offender 4 age
		n.append(convSex(m[93]))         # offender 4 sex
		n.append(convWeap(m[96]))        # offender 4 weapon
		n.append(convRelation(m[97]))    # offender 4 relationship to victim 1
		n.append(convCircum(m[98]))      # offender 4 circumstance
		n.append(convSubCircum(m[99]))   # offender 4 sub-circumstance

		n.append(int(m[100]))            # offender 5 age
		n.append(convSex(m[101]))        # offender 5 sex
		n.append(convWeap(m[104]))       # offender 5 weapon
		n.append(convRelation(m[105]))   # offender 5 relationship to victim 1
		n.append(convCircum(m[106]))     # offender 5 circumstance
		n.append(convSubCircum(m[107]))  # offender 5 sub-circumstance

		n.append(int(m[108]))            # offender 6 age
		n.append(convSex(m[109]))        # offender 6 sex
		n.append(convWeap(m[112]))       # offender 6 weapon
		n.append(convRelation(m[113]))   # offender 6 relationship to victim 1
		n.append(convCircum(m[114]))     # offender 6 circumstance
		n.append(convSubCircum(m[115]))  # offender 6 sub-circumstance

		n.append(int(m[116]))            # offender 7 age
		n.append(convSex(m[117]))        # offender 7 sex
		n.append(convWeap(m[120]))       # offender 7 weapon
		n.append(convRelation(m[121]))   # offender 7 relationship to victim 1
		n.append(convCircum(m[122]))     # offender 7 circumstance
		n.append(convSubCircum(m[123]))  # offender 7 sub-circumstance

		n.append(int(m[124]))            # offender 8 age
		n.append(convSex(m[125]))        # offender 8 sex
		n.append(convWeap(m[128]))       # offender 8 weapon
		n.append(convRelation(m[129]))   # offender 8 relationship to victim 1
		n.append(convCircum(m[130]))     # offender 8 circumstance
		n.append(convSubCircum(m[131]))  # offender 8 sub-circumstance

		n.append(int(m[132]))            # offender 9 age
		n.append(convSex(m[133]))        # offender 9 sex
		n.append(convWeap(m[136]))       # offender 9 weapon
		n.append(convRelation(m[137]))   # offender 9 relationship to victim 1
		n.append(convCircum(m[138]))     # offender 9 circumstance
		n.append(convSubCircum(m[139]))  # offender 9 sub-circumstance

		n.append(int(m[140]))            # offender 10 age
		n.append(convSex(m[141]))        # offender 10 sex
		n.append(convWeap(m[144]))       # offender 10 weapon
		n.append(convRelation(m[145]))   # offender 10 relationship to victim 1
		n.append(convCircum(m[146]))     # offender 10 circumstance
		n.append(convSubCircum(m[147]))  # offender 10 sub-circumstance

		n.append(int(m[148]))            # offender 11 age
		n.append(convSex(m[149]))        # offender 11 sex
		n.append(convWeap(m[152]))       # offender 11 weapon
		n.append(convRelation(m[153]))   # offender 11 relationship to victim 1
		n.append(convCircum(m[154]))     # offender 11 circumstance
		n.append(convSubCircum(m[155]))  # offender 11 sub-circumstance
		a.append(array(n))

def gather_type_6(d,a,y):
	for m in d:
		n = []
		n.append(y)                        # year
		n.append(int(m[16]))               # month
		n.append(m[5])                     # state
		n.append(groupConvert(None,m[7]))  # group
		n.append(int(m[10]))               # population
		#n.append(m[6])                     # agency code
		#n.append(m[14])                    # agency name
		n.append(int(m[13]))               # MSA indication
		n.append(int(m[12]))               # MSA code
		n.append(typeConvert(m[19]))       # type of homicide
		n.append(sitConvert(m[21]))        # situation
		n.append(int(m[34]) + 1)           # victim count
		n.append(int(m[35]) + 1)           # offender count
		oc = n[-1]

		n.append(convAge(m[22]))         # victim 1 age
		n.append(convSex(m[23]))         # victim 1 sex
		n.append(convAge(m[36]))         # victim 2 age
		n.append(convSex(m[37]))         # victim 2 sex
		n.append(convAge(m[40]))         # victim 3 age
		n.append(convSex(m[41]))         # victim 3 sex
		n.append(convAge(m[44]))         # victim 4 age
		n.append(convSex(m[45]))         # victim 4 sex
		n.append(convAge(m[48]))         # victim 5 age
		n.append(convSex(m[49]))         # victim 5 sex
		n.append(convAge(m[52]))         # victim 6 age
		n.append(convSex(m[53]))         # victim 6 sex
		n.append(convAge(m[56]))         # victim 7 age
		n.append(convSex(m[57]))         # victim 7 sex
		n.append(convAge(m[69]))         # victim 8 age
		n.append(convSex(m[61]))         # victim 8 sex
		n.append(convAge(m[64]))         # victim 9 age
		n.append(convSex(m[65]))         # victim 9 sex
		n.append(convAge(m[68]))         # victim 10 age
		n.append(convSex(m[69]))         # victim 10 sex
		n.append(convAge(m[72]))         # victim 11 age
		n.append(convSex(m[73]))         # victim 11 sex

		n.append(int(m[26]))             # offender 1 age
		n.append(convSex(m[27]))         # offender 1 sex
		n.append(convWeap(m[30]))        # offender 1 weapon
		n.append(convRelation(m[31]))    # offender 1 relationship to victim 1
		n.append(convCircum(m[32]))      # offender 1 circumstance
		n.append(convSubCircum(m[33]))   # offender 1 sub-circumstance

		n.append(int(m[76]))             # offender 2 age
		n.append(convSex(m[77]))         # offender 2 sex
		n.append(convWeap(m[80]))        # offender 2 weapon
		n.append(convRelation(m[81]))    # offender 2 relationship to victim 1
		n.append(convCircum(m[82]))      # offender 2 circumstance
		n.append(convSubCircum(m[83]))   # offender 2 sub-circumstance

		n.append(int(m[84]))             # offender 3 age
		n.append(convSex(m[85]))         # offender 3 sex
		n.append(convWeap(m[88]))        # offender 3 weapon
		n.append(convRelation(m[89]))    # offender 3 relationship to victim 1
		n.append(convCircum(m[90]))      # offender 3 circumstance
		n.append(convSubCircum(m[91]))   # offender 3 sub-circumstance

		n.append(int(m[92]))             # offender 4 age
		n.append(convSex(m[93]))         # offender 4 sex
		n.append(convWeap(m[96]))        # offender 4 weapon
		n.append(convRelation(m[97]))    # offender 4 relationship to victim 1
		n.append(convCircum(m[98]))      # offender 4 circumstance
		n.append(convSubCircum(m[99]))   # offender 4 sub-circumstance

		n.append(int(m[100]))            # offender 5 age
		n.append(convSex(m[101]))        # offender 5 sex
		n.append(convWeap(m[104]))       # offender 5 weapon
		n.append(convRelation(m[105]))   # offender 5 relationship to victim 1
		n.append(convCircum(m[106]))     # offender 5 circumstance
		n.append(convSubCircum(m[107]))  # offender 5 sub-circumstance

		n.append(int(m[108]))            # offender 6 age
		n.append(convSex(m[109]))        # offender 6 sex
		n.append(convWeap(m[112]))       # offender 6 weapon
		n.append(convRelation(m[113]))   # offender 6 relationship to victim 1
		n.append(convCircum(m[114]))     # offender 6 circumstance
		n.append(convSubCircum(m[115]))  # offender 6 sub-circumstance

		n.append(int(m[116]))            # offender 7 age
		n.append(convSex(m[117]))        # offender 7 sex
		n.append(convWeap(m[120]))       # offender 7 weapon
		n.append(convRelation(m[121]))   # offender 7 relationship to victim 1
		n.append(convCircum(m[122]))     # offender 7 circumstance
		n.append(convSubCircum(m[123]))  # offender 7 sub-circumstance

		n.append(int(m[124]))            # offender 8 age
		n.append(convSex(m[125]))        # offender 8 sex
		n.append(convWeap(m[128]))       # offender 8 weapon
		n.append(convRelation(m[129]))   # offender 8 relationship to victim 1
		n.append(convCircum(m[130]))     # offender 8 circumstance
		n.append(convSubCircum(m[131]))  # offender 8 sub-circumstance

		n.append(int(m[132]))            # offender 9 age
		n.append(convSex(m[133]))        # offender 9 sex
		n.append(convWeap(m[136]))       # offender 9 weapon
		n.append(convRelation(m[137]))   # offender 9 relationship to victim 1
		n.append(convCircum(m[138]))     # offender 9 circumstance
		n.append(convSubCircum(m[139]))  # offender 9 sub-circumstance

		n.append(int(m[140]))            # offender 10 age
		n.append(convSex(m[141]))        # offender 10 sex
		n.append(convWeap(m[144]))       # offender 10 weapon
		n.append(convRelation(m[145]))   # offender 10 relationship to victim 1
		n.append(convCircum(m[146]))     # offender 10 circumstance
		n.append(convSubCircum(m[147]))  # offender 10 sub-circumstance

		n.append(int(m[148]))            # offender 11 age
		n.append(convSex(m[149]))        # offender 11 sex
		n.append(convWeap(m[152]))       # offender 11 weapon
		n.append(convRelation(m[153]))   # offender 11 relationship to victim 1
		n.append(convCircum(m[154]))     # offender 11 circumstance
		n.append(convSubCircum(m[155]))  # offender 11 sub-circumstance
		a.append(array(n))

def gather_type_7(d,a,y):
	for m in d:
		n = []
		n.append(y)                         # year
		n.append(int(m[12]))                # month
		n.append(m[1])                      # state
		n.append(groupConvert(None,m[3]))   # group
		n.append(int(m[6]))                 # population
		#n.append(m[2])                      # agency code
		#n.append(m[10])                     # agency name
		n.append(int(m[9]))                 # MSA indication
		n.append(convMSACode(m[8]))         # MSA code
		n.append(typeConvert(m[15]))        # type of homicide
		n.append(sitConvert(m[17]))         # situation
		n.append(int(m[30]) + 1)            # victim count
		n.append(int(m[31]) + 1)            # offender count

		n.append(convAge(m[18]))         # victim 1 age
		n.append(convSex(m[19]))         # victim 1 sex
		n.append(convAge(m[32]))         # victim 2 age
		n.append(convSex(m[33]))         # victim 2 sex
		n.append(convAge(m[36]))         # victim 3 age
		n.append(convSex(m[37]))         # victim 3 sex
		n.append(convAge(m[40]))         # victim 4 age
		n.append(convSex(m[41]))         # victim 4 sex
		n.append(convAge(m[44]))         # victim 5 age
		n.append(convSex(m[45]))         # victim 5 sex
		n.append(convAge(m[48]))         # victim 6 age
		n.append(convSex(m[49]))         # victim 6 sex
		n.append(convAge(m[52]))         # victim 7 age
		n.append(convSex(m[53]))         # victim 7 sex
		n.append(convAge(m[56]))         # victim 8 age
		n.append(convSex(m[57]))         # victim 8 sex
		n.append(convAge(m[60]))         # victim 9 age
		n.append(convSex(m[61]))         # victim 9 sex
		n.append(convAge(m[64]))         # victim 10 age
		n.append(convSex(m[65]))         # victim 10 sex
		n.append(convAge(m[68]))         # victim 11 age
		n.append(convSex(m[69]))         # victim 11 sex

		n.append(convAge(m[22]))         # offender 1 age
		n.append(convSex(m[23]))         # offender 1 sex
		n.append(convWeap(m[26]))        # offender 1 weapon
		n.append(convRelation(m[27]))    # offender 1 relationship to victim 1
		n.append(convCircum(m[28]))      # offender 1 circumstance
		n.append(convSubCircum(m[29]))   # offender 1 sub-circumstance

		n.append(convAge(m[72]))         # offender 2 age
		n.append(convSex(m[73]))         # offender 2 sex
		n.append(convWeap(m[76]))        # offender 2 weapon
		n.append(convRelation(m[77]))    # offender 2 relationship to victim 1
		n.append(convCircum(m[78]))      # offender 2 circumstance
		n.append(convSubCircum(m[79]))   # offender 2 sub-circumstance

		n.append(convAge(m[80]))         # offender 3 age
		n.append(convSex(m[81]))         # offender 3 sex
		n.append(convWeap(m[84]))        # offender 3 weapon
		n.append(convRelation(m[85]))    # offender 3 relationship to victim 1
		n.append(convCircum(m[86]))      # offender 3 circumstance
		n.append(convSubCircum(m[87]))   # offender 3 sub-circumstance

		n.append(convAge(m[88]))         # offender 4 age
		n.append(convSex(m[89]))         # offender 4 sex
		n.append(convWeap(m[92]))        # offender 4 weapon
		n.append(convRelation(m[93]))    # offender 4 relationship to victim 1
		n.append(convCircum(m[94]))      # offender 4 circumstance
		n.append(convSubCircum(m[95]))   # offender 4 sub-circumstance

		n.append(convAge(m[96]))         # offender 5 age
		n.append(convSex(m[97]))         # offender 5 sex
		n.append(convWeap(m[100]))       # offender 5 weapon
		n.append(convRelation(m[101]))   # offender 5 relationship to victim 1
		n.append(convCircum(m[102]))     # offender 5 circumstance
		n.append(convSubCircum(m[103]))  # offender 5 sub-circumstance

		n.append(convAge(m[104]))        # offender 6 age
		n.append(convSex(m[105]))        # offender 6 sex
		n.append(convWeap(m[108]))       # offender 6 weapon
		n.append(convRelation(m[109]))   # offender 6 relationship to victim 1
		n.append(convCircum(m[110]))     # offender 6 circumstance
		n.append(convSubCircum(m[111]))  # offender 6 sub-circumstance

		n.append(convAge(m[112]))        # offender 7 age
		n.append(convSex(m[113]))        # offender 7 sex
		n.append(convWeap(m[116]))       # offender 7 weapon
		n.append(convRelation(m[117]))   # offender 7 relationship to victim 1
		n.append(convCircum(m[118]))     # offender 7 circumstance
		n.append(convSubCircum(m[119]))  # offender 7 sub-circumstance

		n.append(convAge(m[120]))        # offender 8 age
		n.append(convSex(m[121]))        # offender 8 sex
		n.append(convWeap(m[124]))       # offender 8 weapon
		n.append(convRelation(m[125]))   # offender 8 relationship to victim 1
		n.append(convCircum(m[126]))     # offender 8 circumstance
		n.append(convSubCircum(m[127]))  # offender 8 sub-circumstance

		n.append(convAge(m[128]))        # offender 9 age
		n.append(convSex(m[129]))        # offender 9 sex
		n.append(convWeap(m[132]))       # offender 9 weapon
		n.append(convRelation(m[133]))   # offender 9 relationship to victim 1
		n.append(convCircum(m[134]))     # offender 9 circumstance
		n.append(convSubCircum(m[135]))  # offender 9 sub-circumstance

		n.append(convAge(m[136]))        # offender 10 age
		n.append(convSex(m[137]))        # offender 10 sex
		n.append(convWeap(m[140]))       # offender 10 weapon
		n.append(convRelation(m[141]))   # offender 10 relationship to victim 1
		n.append(convCircum(m[142]))     # offender 10 circumstance
		n.append(convSubCircum(None))    # offender 10 sub-circumstance

		n.append(convAge(None))          # offender 11 age
		n.append(convSex('9'))           # offender 11 sex
		n.append(convWeap(None))         # offender 11 weapon
		n.append(convRelation('99'))     # offender 11 relationship to victim 1
		n.append(convCircum(None))       # offender 11 circumstance
		n.append(convSubCircum(None))    # offender 11 sub-circumstance
		a.append(array(n))



data = []
gather_type_1(d1976, data, 1976)
gather_type_1(d1977, data, 1977)
gather_type_1(d1978, data, 1978)
gather_type_1(d1979, data, 1979)
gather_type_2(d1980, data, 1980)
gather_type_2(d1981, data, 1981)
gather_type_2(d1982, data, 1982)
gather_type_3(d1983, data, 1983)
gather_type_1(d1984, data, 1984)
gather_type_1(d1985, data, 1985)
gather_type_1(d1986, data, 1986)
gather_type_4(d1987, data, 1987)
gather_type_4(d1988, data, 1988)
gather_type_4(d1989, data, 1989)
gather_type_4(d1990, data, 1990)
gather_type_4(d1991, data, 1991)
gather_type_4(d1992, data, 1992)
gather_type_5(d1993, data, 1993)
gather_type_6(d1994, data, 1994)
gather_type_6(d1995, data, 1995)
gather_type_6(d1996, data, 1996)
gather_type_6(d1997, data, 1997)
gather_type_3(d1998, data, 1998)
gather_type_3(d1999, data, 1999)
gather_type_3(d2000, data, 2000)
gather_type_3(d2001, data, 2001)
gather_type_7(d2002, data, 2002)
gather_type_7(d2003, data, 2003)
gather_type_7(d2004, data, 2004)
gather_type_7(d2005, data, 2005)
gather_type_7(d2006, data, 2006)
gather_type_7(d2007, data, 2007)
gather_type_7(d2008, data, 2008)
gather_type_7(d2009, data, 2009)
gather_type_7(d2010, data, 2010)
gather_type_7(d2011, data, 2011)
gather_type_7(d2012, data, 2012)

data = array(data).astype('i')
save('data/data', data)



