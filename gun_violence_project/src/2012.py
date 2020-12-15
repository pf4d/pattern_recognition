from pylab import *

varis = {1   : {'name' : "IDENTIFIER CODE",
                'type' : int},
         2   : {'name' : "STATE CODE",
                'type' : int},
         3   : {'name' : "ORI CODE",
                'type' : str},
         4   : {'name' : "GROUP",
                'type' : str},
         5   : {'name' : "GEOGRAPHIC DIVISION",
                'type' : int},
         6   : {'name' : "YEAR",
                'type' : int},
         7   : {'name' : "POPULATION OF JURISDICTION",
                'type' : int},
         8   : {'name' : "COUNTY",
                'type' : int},
         9   : {'name' : "MSA [AGENCY CODE]",
                'type' : int},
         10  : {'name' : "MSA INDICATION",
                'type' : int},
         11  : {'name' : "LAW ENFORCEMENT AGENCY NAME",
                'type' : str},
         12  : {'name' : "AGENCY STATE",
                'type' : str},
         13  : {'name' : "MONTH THE OFFENSE OCCURRED",
                'type' : int},
         14  : {'name' : "DATE OF LAST UPDATE",
                'type' : int},
         15  : {'name' : "TYPE OF ACTION OF DATA RECORD",
                'type' : int},
         16  : {'name' : "TYPE OF HOMICIDE",
                'type' : str},
         17  : {'name' : "INCIDENT NUMBER",
                'type' : int},
         18  : {'name' : "SITUATION: VICTIMS AND OFFENDERS IN HOMICIDE",
                'type' : str},
         19  : {'name' : "AGE OF VICTIM - FIRST VICTIM",
                'type' : str},
         20  : {'name' : "GENDER OF VICTIM - FIRST VICTIM",
                'type' : str},
         21  : {'name' : "RACE OF VICTIM - FIRST VICTIM",
                'type' : str},
         22  : {'name' : "ETHNIC ORIGIN OF VICTIM - FIRST VICTIM",
                'type' : str},
         23  : {'name' : "AGE OF OFFENDER - FIRST OFFENDER",
                'type' : int},
         24  : {'name' : "GENDER OF OFFENDER - FIRST OFFENDER",
                'type' : str},
         25  : {'name' : "RACE OF OFFENDER - FIRST OFFENDER",
                'type' : str},
         26  : {'name' : "ETHNIC ORIGIN OF OFFENDER - FIRST OFFENDER",
                'type' : str},
         27  : {'name' : "WEAPON - FIRST OFFENDER",
                'type' : int},
         28  : {'name' : "RELATIONSHIP OF FIRST OFFENDER TO FIRST VICTIM",
                'type' : str},
         29  : {'name' : "CIRCUMSTANCES SURROUNDING HOMICIDE - FIRST OFFENDER",
                'type' : int},
         30  : {'name' : "SUB-CIRCUMSTANCES: JUSTIFIABLE HOMICIDES - FIRST OFFENDER",
                'type' : str},
         31  : {'name' : "ADDITIONAL VICTIM COUNT",
                'type' : int},
         32  : {'name' : "ADDITIONAL OFFENDER COUNT",
                'type' : int},
         33  : {'name' : "AGE OF VICTIM - SECOND VICTIM",
                'type' : str},
         34  : {'name' : "GENDER OF VICTIM - SECOND VICTIM",
                'type' : str},
         35  : {'name' : "RACE OF VICTIM - SECOND VICTIM",
                'type' : str},
         36  : {'name' : "ETHNIC ORIGIN OF VICTIM - SECOND VICTIM",
                'type' : str},
         37  : {'name' : "AGE OF VICTIM - THIRD VICTIM",
                'type' : str},
         38  : {'name' : "GENDER OF VICTIM - THIRD VICTIM",
                'type' : str},
         39  : {'name' : "RACE OF VICTIM - THIRD VICTIM",
                'type' : str},
         40  : {'name' : "ETHNIC ORIGIN OF VICTIM - THIRD VICTIM",
                'type' : str},
         41  : {'name' : "AGE OF VICTIM - FOURTH VICTIM",
                'type' : str},
         42  : {'name' : "GENDER OF VICTIM - FOURTH VICTIM",
                'type' : str},
         43  : {'name' : "RACE OF VICTIM - FOURTH VICTIM",
                'type' : str},
         44  : {'name' : "ETHNIC ORIGIN OF VICTIM - FOURTH VICTIM",
                'type' : str},
         45  : {'name' : "AGE OF VICTIM - FIFTH VICTIM",
                'type' : str},
         46  : {'name' : "GENDER OF VICTIM - FIFTH VICTIM",
                'type' : str},
         47  : {'name' : "RACE OF VICTIM - FIFTH VICTIM",
                'type' : str},
         48  : {'name' : "ETHNIC ORIGIN OF VICTIM - FIFTH VICTIM",
                'type' : str},
         49  : {'name' : "AGE OF VICTIM - SIXTH VICTIM",
                'type' : str},
         50  : {'name' : "GENDER OF VICTIM - SIXTH VICTIM",
                'type' : str},
         51  : {'name' : "RACE OF VICTIM - SIXTH VICTIM",
                'type' : str},
         52  : {'name' : "ETHNIC ORIGIN OF VICTIM - SIXTH VICTIM",
                'type' : str},
         53  : {'name' : "AGE OF VICTIM - SEVENTH VICTIM",
                'type' : str},
         54  : {'name' : "GENDER OF VICTIM - SEVENTH VICTIM",
                'type' : str},
         55  : {'name' : "RACE OF VICTIM - SEVENTH VICTIM",
                'type' : str},
         56  : {'name' : "ETHNIC ORIGIN OF VICTIM - SEVENTH VICTIM",
                'type' : str},
         57  : {'name' : "AGE OF VICTIM - EIGHTH VICTIM",
                'type' : str},
         58  : {'name' : "GENDER OF VICTIM - EIGHTH VICTIM",
                'type' : str},
         59  : {'name' : "RACE OF VICTIM - EIGHTH VICTIM",
                'type' : str},
         60  : {'name' : "ETHNIC ORIGIN OF VICTIM - EIGHTH VICTIM",
                'type' : str},
         61  : {'name' : "AGE OF VICTIM - NINTH VICTIM",
                'type' : str},
         62  : {'name' : "GENDER OF VICTIM - NINTH VICTIM",
                'type' : str},
         63  : {'name' : "RACE OF VICTIM - NINTH VICTIM",
                'type' : str},
         64  : {'name' : "ETHNIC ORIGIN OF VICTIM - NINTH VICTIM",
                'type' : str},
         65  : {'name' : "AGE OF VICTIM - TENTH VICTIM",
                'type' : str},
         66  : {'name' : "GENDER OF VICTIM - TENTH VICTIM",
                'type' : str},
         67  : {'name' : "RACE OF VICTIM - TENTH VICTIM",
                'type' : str},
         68  : {'name' : "ETHNIC ORIGIN OF VICTIM - TENTH VICTIM",
                'type' : str},
         69  : {'name' : "AGE OF VICTIM - ELEVENTH VICTIM",
                'type' : str},
         70  : {'name' : "GENDER OF VICTIM - ELEVENTH VICTIM",
                'type' : str},
         71  : {'name' : "RACE OF VICTIM - ELEVENTH VICTIM",
                'type' : str},
         72  : {'name' : "ETHNIC ORIGIN OF VICTIM - ELEVENTH VICTIM",
                'type' : str},
         73  : {'name' : "AGE OF OFFENDER - SECOND OFFENDER",
                'type' : int},
         74  : {'name' : "GENDER OF OFFENDER - SECOND OFFENDER",
                'type' : str},
         75  : {'name' : "RACE OF OFFENDER - SECOND OFFENDER",
                'type' : str},
         76  : {'name' : "ETHNIC ORIGIN OF OFFENDER - SECOND OFFENDER",
                'type' : str},
         77  : {'name' : "WEAPON - SECOND OFFENDER",
                'type' : int},
         78  : {'name' : "RELATIONSHIP OF FIRST VICTIM TO SECOND OFFENDER",
                'type' : str},
         79  : {'name' : "CIRCUMSTANCES SURROUNDING HOMICIDE - SECOND OFFENDER",
                'type' : int},
         80  : {'name' : "SUB-CIRCUMSTANCES: JUSTIFIABLE HOMICIDES - SECOND OFFENDER",
                'type' : str},
         81  : {'name' : "AGE OF OFFENDER - THIRD OFFENDER",
                'type' : int},
         82  : {'name' : "GENDER OF OFFENDER - THIRD OFFENDER",
                'type' : str},
         83  : {'name' : "RACE OF OFFENDER - THIRD OFFENDER",
                'type' : str},
         84  : {'name' : "ETHNIC ORIGIN OF OFFENDER - THIRD OFFENDER",
                'type' : str},
         85  : {'name' : "WEAPON - THIRD OFFENDER",
                'type' : int},
         86  : {'name' : "RELATIONSHIP OF FIRST VICTIM TO THIRD OFFENDER",
                'type' : str},
         87  : {'name' : "CIRCUMSTANCES SURROUNDING HOMICIDE - THIRD OFFENDER",
                'type' : int},
         88  : {'name' : "SUB-CIRCUMSTANCES: JUSTIFIABLE HOMICIDES - THIRD OFFENDER",
                'type' : str},
         89  : {'name' : "AGE OF OFFENDER - FOURTH OFFENDER",
                'type' : int},
         90  : {'name' : "GENDER OF OFFENDER - FOURTH OFFENDER",
                'type' : str},
         91  : {'name' : "RACE OF OFFENDER - FOURTH OFFENDER",
                'type' : str},
         92  : {'name' : "ETHNIC ORIGIN OF OFFENDER - FOURTH OFFENDER",
                'type' : str},
         93  : {'name' : "WEAPON - FOURTH OFFENDER",
                'type' : int},
         94  : {'name' : "RELATIONSHIP OF FIRST VICTIM TO FOURTH OFFENDER",
                'type' : str},
         95  : {'name' : "CIRCUMSTANCES SURROUNDING HOMICIDE - FOURTH OFFENDER",
                'type' : int},
         96  : {'name' : "SUB-CIRCUMSTANCES: JUSTIFIABLE HOMICIDES - FOURTH OFFENDER",
                'type' : str},
         97  : {'name' : "AGE OF OFFENDER - FIFTH OFFENDER",
                'type' : int},
         98  : {'name' : "GENDER OF OFFENDER - FIFTH OFFENDER",
                'type' : str},
         99  : {'name' : "RACE OF OFFENDER - FIFTH OFFENDER",
                'type' : str},
         100 : {'name' : "ETHNIC ORIGIN OF OFFENDER - FIFTH OFFENDER",
                'type' : str},
         101 : {'name' : "WEAPON - FIFTH OFFENDER",
                'type' : int},
         102 : {'name' : "RELATIONSHIP OF FIRST VICTIM TO FIFTH OFFENDER",
                'type' : str},
         103 : {'name' : "CIRCUMSTANCES SURROUNDING HOMICIDE - FIFTH OFFENDER",
                'type' : int},
         104 : {'name' : "SUB-CIRCUMSTANCES: JUSTIFIABLE HOMICIDES - FIFTH OFFENDER",
                'type' : str},
         105 : {'name' : "AGE OF OFFENDER - SIXTH OFFENDER",
                'type' : int},
         106 : {'name' : "GENDER OF OFFENDER - SIXTH OFFENDER",
                'type' : str},
         107 : {'name' : "RACE OF OFFENDER - SIXTH OFFENDER",
                'type' : str},
         108 : {'name' : "ETHNIC ORIGIN OF OFFENDER - SIXTH OFFENDER",
                'type' : str},
         109 : {'name' : "WEAPON - SIXTH OFFENDER",
                'type' : int},
         110 : {'name' : "RELATIONSHIP OF FIRST VICTIM TO SIXTH OFFENDER",
                'type' : str},
         111 : {'name' : "CIRCUMSTANCES SURROUNDING HOMICIDE - SIXTH OFFENDER",
                'type' : int},
         112 : {'name' : "SUB-CIRCUMSTANCES: JUSTIFIABLE HOMICIDES - SIXTH OFFENDER",
                'type' : str},
         113 : {'name' : "AGE OF OFFENDER - SEVENTH OFFENDER",
                'type' : int},
         114 : {'name' : "GENDER OF OFFENDER - SEVENTH OFFENDER",
                'type' : str},
         115 : {'name' : "RACE OF OFFENDER - SEVENTH OFFENDER",
                'type' : str},
         116 : {'name' : "ETHNIC ORIGIN OF OFFENDER - SEVENTH OFFENDER",
                'type' : str},
         117 : {'name' : "WEAPON - SEVENTH OFFENDER",
                'type' : int},
         118 : {'name' : "RELATIONSHIP OF FIRST VICTIM TO SEVENTH OFFENDER",
                'type' : str},
         119 : {'name' : "CIRCUMSTANCES SURROUNDING HOMICIDE - SEVENTH OFFENDER",
                'type' : int},
         120 : {'name' : "SUB-CIRCUMSTANCES: JUSTIFIABLE HOMICIDES - SEVENTH OFFENDER",
                'type' : str},
         121 : {'name' : "AGE OF OFFENDER - EIGHTH OFFENDER",
                'type' : int},
         122 : {'name' : "GENDER OF OFFENDER - EIGHTH OFFENDER",
                'type' : str},
         123 : {'name' : "RACE OF OFFENDER - EIGHTH OFFENDER",
                'type' : str},
         124 : {'name' : "ETHNIC ORIGIN OF OFFENDER - EIGHTH OFFENDER",
                'type' : str},
         125 : {'name' : "WEAPON - EIGHTH OFFENDER",
                'type' : int},
         126 : {'name' : "RELATIONSHIP OF FIRST VICTIM TO EIGHTH OFFENDER",
                'type' : str},
         127 : {'name' : "CIRCUMSTANCES SURROUNDING HOMICIDE - EIGHTH OFFENDER",
                'type' : int},
         128 : {'name' : "SUB-CIRCUMSTANCES: JUSTIFIABLE HOMICIDES - EIGHTH OFFENDER",
                'type' : str},
         129 : {'name' : "AGE OF OFFENDER - NINTH OFFENDER",
                'type' : int},
         130 : {'name' : "GENDER OF OFFENDER - NINTH OFFENDER",
                'type' : str},
         131 : {'name' : "RACE OF OFFENDER - NINTH OFFENDER",
                'type' : str},
         132 : {'name' : "ETHNIC ORIGIN OF OFFENDER - NINTH OFFENDER",
                'type' : str},
         133 : {'name' : "WEAPON - NINTH OFFENDER",
                'type' : int},
         134 : {'name' : "RELATIONSHIP OF FIRST VICTIM TO NINTH OFFENDER",
                'type' : str},
         135 : {'name' : "CIRCUMSTANCES SURROUNDING HOMICIDE - NINTH OFFENDER",
                'type' : int},
         136 : {'name' : "SUB-CIRCUMSTANCES: JUSTIFIABLE HOMICIDES - NINTH OFFENDER",
                'type' : str},
         137 : {'name' : "AGE OF OFFENDER - TENTH OFFENDER",
                'type' : int},
         138 : {'name' : "GENDER OF OFFENDER - TENTH OFFENDER",
                'type' : str},
         139 : {'name' : "RACE OF OFFENDER - TENTH OFFENDER",
                'type' : str},
         140 : {'name' : "ETHNIC ORIGIN OF OFFENDER - TENTH OFFENDER",
                'type' : str},
         141 : {'name' : "WEAPON - TENTH OFFENDER",
                'type' : int},
         142 : {'name' : "RELATIONSHIP OF FIRST VICTIM TO TENTH OFFENDER",
                'type' : str},
         143 : {'name' : "CIRCUMSTANCES SURROUNDING HOMICIDE - TENTH OFFENDER",
                'type' : int},
         144 : {'name' : "SUB-CIRCUMSTANCES: JUSTIFIABLE HOMICIDES - TENTH OFFENDER",
                'type' : str},
         145 : {'name' : "AGE OF OFFENDER - ELEVENTH OFFENDER",
                'type' : int},
         146 : {'name' : "GENDER OF OFFENDER - ELEVENTH OFFENDER",
                'type' : str},
         147 : {'name' : "RACE OF OFFENDER - ELEVENTH OFFENDER",
                'type' : str},
         148 : {'name' : "ETHNIC ORIGIN OF OFFENDER - ELEVENTH OFFENDER",
                'type' : str},
         149 : {'name' : "WEAPON - ELEVENTH OFFENDER",
                'type' : int},
         150 : {'name' : "RELATIONSHIP OF FIRST VICTIM TO ELEVENTH OFFENDER",
                'type' : str},
         151 : {'name' : "CIRCUMSTANCES SURROUNDING HOMICIDE - ELEVENTH OFFENDER",
                'type' : int},
         152 : {'name' : "SUB-CIRCUMSTANCES: JUSTIFIABLE HOMICIDES - ELEVENTH OFFENDER",
                'type' : str}}

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

group = {'0 '  : "POSSESSIONS (PUERTO RICO, GUAM, CANAL ZONE, VIRGIN ISLANDS, AND AMERICAN SAMOA)", 
         '1 ' : "ALL CITIES 250,000 OR OVER",
         '1A' : "ALL CITIES 1,000,000 OR OVER",
         '1B' : "CITIES BETWEEN 500,000 AND 999,999",
         '1C' : "CITIES BETWEEN 250,000 AND 499,999",
         '2 ' : "CITIES BETWEEN 100,000 AND 249,999",
         '3 ' : "CITIES BETWEEN 50,000 AND 99,999",
         '4 ' : "CITIES BETWEEN 25,000 AND 49,999",
         '5 ' : "CITIES BETWEEN 10,000 AND 24,999",
         '6 ' : "CITIES BETWEEN 2,500 AND 9,999",
         '7 ' : "CITIES UNDER 2,500",
         '8 ' : "NON-MSA COUNTIES",
         '8A' : "NON-MSA COUNTIES 100,000 OR OVER",
         '8B' : "NON-MSA COUNTIES BETWEEN 25,000 AND 99,999",
         '8C' : "NON-MSA COUNTIES BETWEEN 10,000 AND 24,999",
         '8D' : "NON-MSA COUNTIES UNDER 10,000",
         '8E' : "NON-MSA STATE POLICE",
         '9 ' : "MSA COUNTIES",
         '9A' : "MSA COUNTIES 100,000 OR OVER",
         '9B' : "MSA COUNTIES BETWEEN 25,000 AND 99,999",
         '9C' : "MSA COUNTIES BETWEEN 10,000 AND 24,999",
         '9D' : "MSA COUNTIES UNDER 10,000",
         '9E' : "MSA STATE POLICE"}

division = {0 : "POSSESSIONS (PUERTO RICO, GUAM, CANAL ZONE, VIRGIN ISLANDS, AND AMERICAN SAMOA)", 
            1 : "NEW ENGLAND STATES - CONNECTICUT, MAINE, MASSACHUSETTS, NEW HAMPSHIRE, RHODE ISLAND, VERMONT",
            2 : "MIDDLE ATLANTIC STATES - NEW JERSEY, NEW YORK, PENNSYLVANIA",
            3 : "EAST NORTH CENTRAL STATES - ILLINOIS, INDIANA, MICHIGAN, OHIO, WISCONSIN",
            4 : "WEST NORTH CENTRAL STATES - IOWA, KANSAS, MINNESOTA, MISSOURI, NEBRASKA, NORTH DAKOTA, SOUTH DAKOTA",
            5 : "SOUTH ATLANTIC STATES - DELAWARE, FLORIDA, GEORGIA, MARYLAND, NORTH CAROLINA, SOUTH CAROLINA, VIRGINIA, WASHINGTON D. C., WEST VIRGINIA",
            6 : "EAST SOUTH CENTRAL STATES - ALABAMA, KENTUCKY, MISSISSIPPI, TENNESSEE",
            7 : "WEST SOUTH CENTRAL STATES - ARKANSAS, LOUISIANA, OKLAHOMA, TEXAS",
            8 : "MOUNTAIN STATES - ARIZONA, COLORADO, IDAHO, MONTANA, NEVADA, NEW MEXICO, UTAH, WYOMING",
            9 : "PACIFIC STATES - ALASKA, CALIFORNIA, HAWAII, OREGON, WASHINGTON"}

suburban = {0 : "NON-SUBURBAN",
            1 : "SUBURBAN"}

agencyCnt = {0 : "U.S. PARK POLICE, STATE POLICE AGENCIES, AND AGENCIES WHICH ARE COVERED BY OTHER AGENCIES.",
             1 : "ALL OTHER AGENCIES"}

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

adjust = {0 : "NORMAL",
          1 : "ADJUSTMENT"}

ageUnder12mo = {1 : "BIRTH TO ONE WEEK OLD (INCLUDES \"ABANDONED INFANT\")",
                2 : "ONE WEEK TO TWELVE MONTHS OLD",
                9 : "INAP., NOT CODED 0 IN REF 23"}

homicide = {'A' : "MURDER AND NONNEGLIGENT MANSLAUGHTER",
            'B' : "MANSLAUGHTER BY NEGLIGENCE"}
situation = {'A' : "SINGLE VICTIM; SINGLE OFFENDER",
             'B' : "SINGLE VICTIM; UNKNOWN OFFENDER(S)",
             'C' : "SINGLE VICTIM; MULTIPLE OFFENDERS",
             'D' : "MULTIPLE VICTIMS; SINGLE OFFENDER",
             'E' : "MULTIPLE VICTIMS; MULTIPLE OFFENDERS",
             'F' : "MULTIPLE VICTIMS; UNKNOWN OFFENDER(S)"}

age = { 00  : 'UNKNOWN',
       'BB' : "7 DAYS OLD TO 364 DAYS OLD",
       'NB' : "BIRTH TO 6 DAYS OLD"}

sex = {'M' : "MALE",
       'F' : "FEMALE",
       'U' : "UNKNOWN"}

race = {'W' : "WHITE (INCLUDES MEXICAN-AMERICANS)",
        'B' : "BLACK OR AFRICAN AMERICAN",
        'I' : "AMERICAN INDIAN OR ALASKAN NATIVE",
        'A' : "ASIAN",
        'P' : "NATIVE HAWAIIAN OR OTHER PACIFIC ISLANDER",
        'U' : "UNKNOWN"}

ethnic = {'H' : "HISPANIC ORIGIN",
          'N' : "NOT OF HISPANIC ORIGIN",
          'U' : "UNKNOWN"}

weapon = {11 : "FIREARM, TYPE NOT STATED (DOES NOT INCLUDE MECHANIC'S GREASE GUN OR CAULKING GUN)",
          12 : "HANDGUN - PISTOL, REVOLVER, ETC.",
          13 : "RIFLE",
          14 : "SHOTGUN",
          15 : "OTHER GUN / UNKNOWN GUN",
          20 : "KNIFE OR CUTTING INSTRUMENT - INCLUDES ICEPICK, SCREWDRIVER, AX, ETC.",
          30 : "BLUNT OBJECT - HAMMER, CLUB, ETC. FACTS MUST SUGGEST WEAPON WAS NOT HANDS AND FEET.",
          40 : "PERSONAL WEAPONS - INCLUDES BEATING BY HANDS, FEET, AND OTHER BODY MEMBERS OR USE OF TEETH",
          50 : "POISON - DOES NOT INCLUDE GAS",
          55 : "PUSHED OR THROWN OUT WINDOW",
          60 : "EXPLOSIVES",
          65 : "FIRE",
          70 : "NARCOTICS AND DRUGS - INCLUDES SLEEPING PILLS",
          75 : "DROWNING",
          80 : "STRANGULATION - HANGING.",
          85 : "ASPHYXIATION - INCLUDES ASPHYXIATION OR DEATH BY GAS",
          90 : "OTHER- TYPE OF WEAPON NOT DESIGNED OR TYPE UNKNOWN"}

relationship = {'HU' : "HUSBAND",
                'WI' : "WIFE",
                'CH' : "COMMON-LAW HUSBAND",
                'CW' : "COMMON-LAW WIFE",
                'MO' : "MOTHER",
                'FA' : "FATHER",
                'SO' : "SON",
                'DA' : "DAUGHTER",
                'BR' : "BROTHER",
                'SI' : "SISTER",
                'IL' : "IN-LAW",
                'SF' : "STEPFATHER",
                'SM' : "STEPMOTHER",
                'SS' : "STEPSON",
                'SD' : "STEPDAUGHTER",
                'OF' : "OTHER FAMILY",
                'NE' : "NEIGHBOR",
                'AQ' : "ACQUAINTANCE",
                'BF' : "BOYFRIEND",
                'GF' : "GIRLFRIEND",
                'XH' : "EX-HUSBAND",
                'XW' : "EX-WIFE",
                'EE' : "EMPLOYEE",
                'ER' : "EMPLOYER",
                'FR' : "FRIEND",
                'HO' : "HOMOSEXUAL RELATIONSHIP",
                'OK' : "OTHER - KNOWN TO VICTIM",
                'ST' : "STRANGER",
                'UN' : "DK, ALL INSTANCES WHERE RELATIONSHIP OF VICTIM TO OFFENDER CANNOT BE DETERMINED"}

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

subCircum = {'A' : "FELON ATTACKED POLICE OFFICER",
             'B' : "FELON ATTACKED FELLOW POLICE OFFICER",
             'C' : "FELON ATTACKED CIVILIAN",
             'D' : "FELON ATTEMPTED FLIGHT FROM CRIME",
             'E' : "FELON KILLED IN COMMISSION OF CRIME",
             'F' : "FELON RESISTED ARREST",
             'G' : "NOT ENOUGH INFORMATION TO DETERMINE"}

data = open('../data/SHC/2012/ICPSR_35023/DS0001/35023-0001-Data.txt')

wid = [1,2,7,2,1,4,9,3,3,1,24,6,2,6,1,1,3,1,
       2,1,1,1,
       2,1,1,1,2,2,2,1,
       3,3,
       2,1,1,1,
       2,1,1,1,
       2,1,1,1,
       2,1,1,1,
       2,1,1,1,
       2,1,1,1,
       2,1,1,1,
       2,1,1,1,
       2,1,1,1,
       2,1,1,1,
       2,1,1,1,2,2,2,1,
       2,1,1,1,2,2,2,1,
       2,1,1,1,2,2,2,1,
       2,1,1,1,2,2,2,1,
       2,1,1,1,2,2,2,1,
       2,1,1,1,2,2,2,1,
       2,1,1,1,2,2,2,1,
       2,1,1,1,2,2,2,1,
       2,1,1,1,2,2,2,1,
       2,1,1,1,2,2,2,1]

data_n = []

# fill the arrays values from the .txt file :
for l in data.readlines():
	j = 0
	g = []
	for i,w in enumerate(wid):
		t = l[j:j+w]
		if t.isspace():
			g.append(None)
		else:
			g.append(varis[i+1]['type'](t))
		j += w
	data_n.append(array(g))
data.close()

data_n = array(data_n)
save('data/2012', data_n)



