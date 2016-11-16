from pylab  import *

varis = {1   : {"name" : "ICPSR STUDY NUMBER",
                "type" : int},
         2   : {"name" : "ICPSR EDITION NUMBER",
                "type" : int},
         3   : {"name" : "ICPSR PART NUMBER",
                "type" : int},
         4   : {"name" : "ICPSR SEQUENTIAL CASE IDENTIFICATION NUMBER",
                "type" : int},
         5   : {"name" : "STATE CODE",
                "type" : int},
         6   : {"name" : "AGENCY CODE (ORI CODE)",
                "type" : str},
         7   : {"name" : "GROUP",
                "type" : int},
         8   : {"name" : "SUB-GROUP",
                "type" : int},
         9   : {"name" : "GEOGRAPHIC DIVISION",
                "type" : int},
         10  : {"name" : "YEAR",
                "type" : int},
         11  : {"name" : "POPULATION",
                "type" : int},
         12  : {"name" : "COUNTY",
                "type" : int},
         13  : {"name" : "SMSA [AGENCY CODE]",
                "type" : int},
         14  : {"name" : "SMSA INDICATION",
                "type" : int},
         15  : {"name" : "AGENCY NAME",
                "type" : str},
         16  : {"name" : "AGENCY STATE",
                "type" : str},
         17  : {"name" : "MONTH THE OFFENSE OCCURRED",
                "type" : int},
         18  : {"name" : "LAST UPDATE",
                "type" : int},
         19  : {"name" : "TYPE",
                "type" : int},
         20  : {"name" : "HOMICIDE",
                "type" : int},
         21  : {"name" : "INCIDENT NUMBER",
                "type" : int},
         22  : {"name" : "SITUATION",
                "type" : int},
         23  : {"name" : "VICTIM COUNT",
                "type" : int},
         24  : {"name" : "OFFENDER COUNT",
                "type" : int},
         25  : {"name" : "AGE OF VICTIM - FIRST VICTIM",
                "type" : int},
         26  : {"name" : "AGE OF VICTIM - SECOND VICTIM",
                "type" : int},
         27  : {"name" : "AGE OF VICTIM - THIRD VICTIM",
                "type" : int},
         28  : {"name" : "AGE OF VICTIM - FOURTH VICTIM",
                "type" : int},
         29  : {"name" : "AGE OF VICTIM - FIFTH VICTIM",
                "type" : int},
         30  : {"name" : "AGE OF VICTIM - SIXTH VICTIM",
                "type" : int},
         31  : {"name" : "AGE OF VICTIM - SEVENTH VICTIM",
                "type" : int},
         32  : {"name" : "AGE OF VICTIM - EIGHTH VICTIM",
                "type" : int},
         33  : {"name" : "AGE OF VICTIM - NINTH VICTIM",
                "type" : int},
         34  : {"name" : "AGE OF VICTIM - TENTH VICTIM",
                "type" : int},
         35  : {"name" : "GENDER OF VICTIM - FIRST VICTIM",
                "type" : int},
         36  : {"name" : "GENDER OF VICTIM - SECOND VICTIM",
                "type" : int},
         37  : {"name" : "GENDER OF VICTIM - THIRD VICTIM",
                "type" : int},
         38  : {"name" : "GENDER OF VICTIM - FOURTH VICTIM",
                "type" : int},
         39  : {"name" : "GENDER OF VICTIM - FIFTH VICTIM",
                "type" : int},
         40  : {"name" : "GENDER OF VICTIM - SIXTH VICTIM",
                "type" : int},
         41  : {"name" : "GENDER OF VICTIM - SEVENTH VICTIM",
                "type" : int},
         42  : {"name" : "GENDER OF VICTIM - EIGHTH VICTIM",
                "type" : int},
         43  : {"name" : "GENDER OF VICTIM - NINTH VICTIM",
                "type" : int},
         44  : {"name" : "GENDER OF VICTIM - TENTH VICTIM",
                "type" : int},
         45  : {"name" : "RACE OF VICTIM - FIRST VICTIM",
                "type" : int},
         46  : {"name" : "RACE OF VICTIM - SECOND VICTIM",
                "type" : int},
         47  : {"name" : "RACE OF VICTIM - THIRD VICTIM",
                "type" : int},
         48  : {"name" : "RACE OF VICTIM - FOURTH VICTIM",
                "type" : int},
         49  : {"name" : "RACE OF VICTIM - FIFTH VICTIM",
                "type" : int},
         50  : {"name" : "RACE OF VICTIM - SIXTH VICTIM",
                "type" : int},
         51  : {"name" : "RACE OF VICTIM - SEVENTH VICTIM",
                "type" : int},
         52  : {"name" : "RACE OF VICTIM - EIGHTH VICTIM",
                "type" : int},
         53  : {"name" : "RACE OF VICTIM - NINTH VICTIM",
                "type" : int},
         54  : {"name" : "RACE OF VICTIM - TENTH VICTIM",
                "type" : int},
         55  : {"name" : "ETHNIC ORIGIN OF VICTIM - FIRST VICTIM",
                "type" : int},
         56  : {"name" : "ETHNIC ORIGIN OF VICTIM - SECOND VICTIM",
                "type" : int},
         57  : {"name" : "ETHNIC ORIGIN OF VICTIM - THIRD VICTIM",
                "type" : int},
         58  : {"name" : "ETHNIC ORIGIN OF VICTIM - FOURTH VICTIM",
                "type" : int},
         59  : {"name" : "ETHNIC ORIGIN OF VICTIM - FIFTH VICTIM",
                "type" : int},
         60  : {"name" : "ETHNIC ORIGIN OF VICTIM - SIXTH VICTIM",
                "type" : int},
         61  : {"name" : "ETHNIC ORIGIN OF VICTIM - SEVENTH VICTIM",
                "type" : int},
         62  : {"name" : "ETHNIC ORIGIN OF VICTIM - EIGHTH VICTIM",
                "type" : int},
         63  : {"name" : "ETHNIC ORIGIN OF VICTIM - NINTH VICTIM",
                "type" : int},
         64  : {"name" : "ETHNIC ORIGIN OF VICTIM - TENTH VICTIM",
                "type" : int},
         65  : {"name" : "AGE OF OFFENDER - FIRST OFFENDER",
                "type" : int},
         66  : {"name" : "AGE OF OFFENDER - SECOND OFFENDER",
                "type" : int},
         67  : {"name" : "AGE OF OFFENDER - THIRD OFFENDER",
                "type" : int},
         68  : {"name" : "AGE OF OFFENDER - FOURTH OFFENDER",
                "type" : int},
         69  : {"name" : "AGE OF OFFENDER - FIFTH OFFENDER",
                "type" : int},
         70  : {"name" : "AGE OF OFFENDER - SIXTH OFFENDER",
                "type" : int},
         71  : {"name" : "AGE OF OFFENDER - SEVENTH OFFENDER",
                "type" : int},
         72  : {"name" : "AGE OF OFFENDER - EIGHTH OFFENDER",
                "type" : int},
         73  : {"name" : "AGE OF OFFENDER - NINTH OFFENDER",
                "type" : int},
         74  : {"name" : "AGE OF OFFENDER - TENTH OFFENDER",
                "type" : int},
         75  : {"name" : "AGE OF OFFENDER - ELEVENTH OFFENDER",
                "type" : int},
         76  : {"name" : "GENDER OF OFFENDER - FIRST OFFENDER",
                "type" : int},
         77  : {"name" : "GENDER OF OFFENDER - SECOND OFFENDER",
                "type" : int},
         78  : {"name" : "GENDER OF OFFENDER - THIRD OFFENDER",
                "type" : int},
         79  : {"name" : "GENDER OF OFFENDER - FOURTH OFFENDER",
                "type" : int},
         80  : {"name" : "GENDER OF OFFENDER - FIFTH OFFENDER",
                "type" : int},
         81  : {"name" : "GENDER OF OFFENDER - SIXTH OFFENDER",
                "type" : int},
         82  : {"name" : "GENDER OF OFFENDER - SEVENTH OFFENDER",
                "type" : int},
         83  : {"name" : "GENDER OF OFFENDER - EIGHTH OFFENDER",
                "type" : int},
         84  : {"name" : "GENDER OF OFFENDER - NINTH OFFENDER",
                "type" : int},
         85  : {"name" : "GENDER OF OFFENDER - TENTH OFFENDER",
                "type" : int},
         86  : {"name" : "GENDER OF OFFENDER - ELEVENTH OFFENDER",
                "type" : int},
         87  : {"name" : "RACE OF OFFENDER - FIRST OFFENDER",
                "type" : int},
         88  : {"name" : "RACE OF OFFENDER - SECOND OFFENDER",
                "type" : int},
         89  : {"name" : "RACE OF OFFENDER - THIRD OFFENDER",
                "type" : int},
         90  : {"name" : "RACE OF OFFENDER - FOURTH OFFENDER",
                "type" : int},
         91  : {"name" : "RACE OF OFFENDER - FIFTH OFFENDER",
                "type" : int},
         92  : {"name" : "RACE OF OFFENDER - SIXTH OFFENDER",
                "type" : int},
         93  : {"name" : "RACE OF OFFENDER - SEVENTH OFFENDER",
                "type" : int},
         94  : {"name" : "RACE OF OFFENDER - EIGHTH OFFENDER",
                "type" : int},
         95  : {"name" : "RACE OF OFFENDER - NINTH OFFENDER",
                "type" : int},
         96  : {"name" : "RACE OF OFFENDER - TENTH OFFENDER",
                "type" : int},
         97  : {"name" : "RACE OF OFFENDER - ELEVENTH OFFENDER",
                "type" : int},
         98  : {"name" : "ETHNIC ORIGIN OF OFFENDER - FIRST OFFENDER",
                "type" : int},
         99  : {"name" : "ETHNIC ORIGIN OF OFFENDER - SECOND OFFENDER",
                "type" : int},
         100 : {"name" : "ETHNIC ORIGIN OF OFFENDER - THIRD OFFENDER",
                "type" : int},
         101 : {"name" : "ETHNIC ORIGIN OF OFFENDER - FOURTH OFFENDER",
                "type" : int},
         102 : {"name" : "ETHNIC ORIGIN OF OFFENDER - FIFTH OFFENDER",
                "type" : int},
         103 : {"name" : "ETHNIC ORIGIN OF OFFENDER - SIXTH OFFENDER",
                "type" : int},
         104 : {"name" : "ETHNIC ORIGIN OF OFFENDER - SEVENTH OFFENDER",
                "type" : int},
         105 : {"name" : "ETHNIC ORIGIN OF OFFENDER - EIGHTH OFFENDER",
                "type" : int},
         106 : {"name" : "ETHNIC ORIGIN OF OFFENDER - NINTH OFFENDER",
                "type" : int},
         107 : {"name" : "ETHNIC ORIGIN OF OFFENDER - TENTH OFFENDER",
                "type" : int},
         108 : {"name" : "ETHNIC ORIGIN OF OFFENDER - ELEVENTH OFFENDER",
                "type" : int},
         109 : {"name" : "WEAPON - FIRST OFFENDER",
                "type" : int},
         110 : {"name" : "WEAPON - SECOND OFFENDER",
                "type" : int},
         111 : {"name" : "WEAPON - THIRD OFFENDER",
                "type" : int},
         112 : {"name" : "WEAPON - FOURTH OFFENDER",
                "type" : int},
         113 : {"name" : "WEAPON - FIFTH OFFENDER",
                "type" : int},
         114 : {"name" : "WEAPON - SIXTH OFFENDER",
                "type" : int},
         115 : {"name" : "WEAPON - SEVENTH OFFENDER",
                "type" : int},
         116 : {"name" : "WEAPON - EIGHTH OFFENDER",
                "type" : int},
         117 : {"name" : "WEAPON - NINTH OFFENDER",
                "type" : int},
         118 : {"name" : "WEAPON - TENTH OFFENDER",
                "type" : int},
         119 : {"name" : "WEAPON - ELEVENTH OFFENDER",
                "type" : int},
         120 : {"name" : "RELATIONSHIP [OF VICTIM TO OFFENDER] - FIRST OFFENDER",
                "type" : int},
         121 : {"name" : "RELATIONSHIP [OF VICTIM TO OFFENDER] - SECOND OFFENDER",
                "type" : int},
         122 : {"name" : "RELATIONSHIP [OF VICTIM TO OFFENDER] - THIRD OFFENDER",
                "type" : int},
         123 : {"name" : "RELATIONSHIP [OF VICTIM TO OFFENDER] - FOURTH OFFENDER",
                "type" : int},
         124 : {"name" : "RELATIONSHIP [OF VICTIM TO OFFENDER] - FIFTH OFFENDER",
                "type" : int},
         125 : {"name" : "RELATIONSHIP [OF VICTIM TO OFFENDER] - SIXTH OFFENDER",
                "type" : int},
         126 : {"name" : "RELATIONSHIP [OF VICTIM TO OFFENDER] - SEVENTH OFFENDER",
                "type" : int},
         127 : {"name" : "RELATIONSHIP [OF VICTIM TO OFFENDER] - EIGHTH OFFENDER",
                "type" : int},
         128 : {"name" : "RELATIONSHIP [OF VICTIM TO OFFENDER] - NINTH OFFENDER",
                "type" : int},
         129 : {"name" : "RELATIONSHIP [OF VICTIM TO OFFENDER] - TENTH OFFENDER",
                "type" : int},
         130 : {"name" : "RELATIONSHIP [OF VICTIM TO OFFENDER] - ELEVENTH OFFENDER",
                "type" : int},
         131 : {"name" : "CIRCUMSTANCES - FIRST OFFENDER",
                "type" : int},
         132 : {"name" : "CIRCUMSTANCES - SECOND OFFENDER",
                "type" : int},
         133 : {"name" : "CIRCUMSTANCES - THIRD OFFENDER",
                "type" : int},
         134 : {"name" : "CIRCUMSTANCES - FOURTH OFFENDER",
                "type" : int},
         135 : {"name" : "CIRCUMSTANCES - FIFTH OFFENDER",
                "type" : int},
         136 : {"name" : "CIRCUMSTANCES - SIXTH OFFENDER",
                "type" : int},
         137 : {"name" : "CIRCUMSTANCES - SEVENTH OFFENDER",
                "type" : int},
         138 : {"name" : "CIRCUMSTANCES - EIGHTH OFFENDER",
                "type" : int},
         139 : {"name" : "CIRCUMSTANCES - NINTH OFFENDER",
                "type" : int},
         140 : {"name" : "CIRCUMSTANCES - TENTH OFFENDER",
                "type" : int},
         141 : {"name" : "CIRCUMSTANCES - ELEVENTH OFFENDER",
                "type" : int},
         142 : {"name" : "SUB-CIRCUMSTANCE - FIRST OFFENDER",
                "type" : int},
         143 : {"name" : "SUB-CIRCUMSTANCE - SECOND OFFENDER",
                "type" : int},
         144 : {"name" : "SUB-CIRCUMSTANCE - THIRD OFFENDER",
                "type" : int},
         145 : {"name" : "SUB-CIRCUMSTANCE - FOURTH OFFENDER",
                "type" : int},
         146 : {"name" : "SUB-CIRCUMSTANCE - FIFTH OFFENDER",
                "type" : int},
         147 : {"name" : "SUB-CIRCUMSTANCE - SIXTH OFFENDER",
                "type" : int},
         148 : {"name" : "SUB-CIRCUMSTANCE - SEVENTH OFFENDER",
                "type" : int},
         149 : {"name" : "SUB-CIRCUMSTANCE - EIGHTH OFFENDER",
                "type" : int},
         150 : {"name" : "SUB-CIRCUMSTANCE - NINTH OFFENDER",
                "type" : int},
         151 : {"name" : "SUB-CIRCUMSTANCE - TENTH OFFENDER",
                "type" : int},
         152 : {"name" : "SUB-CIRCUMSTANCE - ELEVENTH OFFENDER",
                "type" : int}}

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
         51 : "HAWAII"}

group = {1 : "ALL CITIES 250,000 OR OVER",
         2 : "CITIES BETWEEN 100,000 AND 249,999",
         3 : "CITIES BETWEEN 50,000 AND 99,999",
         4 : "CITIES BETWEEN 25,000 AND 49,999",
         5 : "CITIES BETWEEN 10,000 AND 24,999",
         6 : "CITIES BETWEEN 2,500 AND 9,999",
         7 : "CITIES UNDER 2,500",
         8 : "NON-SMSA COUNTIES",
         9 : "SMSA COUNTIES"}

subgroup = {11 : "ALL CITIES 1,000,000 OR OVER",
            12 : "CITIES BETWEEN 500,000 AND 999,999",
            13 : "CITIES BETWEEN 250,000 AND 499,999",
            20 : "CITIES BETWEEN 100,000 AND 249,999",
            30 : "CITIES BETWEEN 50,000 AND 99,999",
            40 : "CITIES BETWEEN 25,000 AND 49,999",
            50 : "CITIES BETWEEN 10,000 AND 24,999",
            60 : "CITIES BETWEEN 2,500 AND 9,999",
            70 : "CITIES UNDER 2,500",
            81 : "NON-SMSA COUNTIES 100,000 OR OVER",
            82 : "NON-SMSA COUNTIES BETWEEN 25,000 AND 99,999",
            83 : "NON-SMSA COUNTIES BETWEEN 10,000 AND 24,999",
            84 : "NON-SMSA COUNTIES UNDER 10,000",
            91 : "SMSA COUNTIES 100,000 OR OVER",
            92 : "SMSA COUNTIES BETWEEN 25,000 AND 99,999",
            93 : "SMSA COUNTIES BETWEEN 10,000 AND 24,999",
            94 : "SMSA COUNTIES UNDER 10,000"}

region = {1 : "NORTHEAST - NEW ENGLAND AND MIDDLE ATLANTIC STATES",
          2 : "NORTH CENTRAL - EAST NORTH CENTRAL AND WEST NORTH CENTRAL STATES",
          3 : "SOUTH - SOUTH ATLANTIC, EAST SOUTH CENTRAL, AND WEST SOUTH CENTRAL STATES",
          4 : "WEST - MOUNTAIN AND PACIFIC STATES"}

division = {1 : "NEW ENGLAND STATES - CONNECTICUT, MAINE, MASSACHUSETTS, NEW HAMPSHIRE, RHODE ISLAND, VERMONT",
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

homicide = {1 : "MURDER AND NONNEGLIGENT MANSLAUGHTER",
            2 : "MANSLAUGHTER BY NEGLIGENCE"}
situation = {1 : "SINGLE VICTIM/SINGLE OFFENDER",
             2 : "SINGLE VICTIM/UNKNOWN OFFENDER OR OFFENDERS",
             3 : "SINGLE VICTIM/MULTIPLE OFFENDERS",
             4 : "MULTIPLE VICTIMS/SINGLE OFFENDER",
             5 : "MULTIPLE VICTIMS/MULTIPLE OFFENDERS",
             6 : "MULTIPLE VICTIMS/UNKNOWN OFFENDER OR OFFENDERS"}

sex = {1 : "MALE",
       2 : "FEMALE",
       9 : "UNKNOWN"}

race = {1 : "WHITE (INCLUDES MEXICAN-AMERICANS)",
        2 : "BLACK",
        3 : "AMERICAN INDIAN OR ALASKAN NATIVE",
        4 : "ASIAN OR PACIFIC ISLANDER",
        9 : "UNKNOWN"}

ethnic = {1 : "HISPANIC ORIGIN",
          2 : "NOT OF HISPANIC ORIGIN",
          9 : "UNKNOWN"}

weapon = {11 : "FIREARM, TYPE NOT STATED (DOES NOT INCLUDE MECHANIC'S GREASE GUN OR CAULKING GUN)",
          12 : "HANDGUN - PISTOL, REVOLVER, ETC.",
          13 : "RIFLE",
          14 : "SHOTGUN",
          15 : "OTHER GUN / UNKNOWN GUN",
          20 : "KNIFE OR CUTTING INSTRUMENT - INCLUDES ICEPICK, SCREWDRIVER, AX, ETC.",
          30 : "BLUNT OBJECT - HAMMER, CLUB, ETC. FACTS MUST SUGGEST WEAPON WAS NOT HANDS AND FEET.",
          40 : "PERSONAL WEAPONS - INCLUDES BEATING BY HANDS, FEET, AND OTHER BODY MEMBERS OR USE OF TEETH",
          50 : "POISON - DOES NOT INCLUDE GAS",
          60 : "EXPLOSIVES",
          65 : "FIRE",
          70 : "NARCOTICS AND DRUGS - INCLUDES SLEEPING PILLS",
          75 : "DROWNING",
          80 : "STRANGULATION - HANGING.",
          85 : "ASPHYXIATION - INCLUDES ASPHYXIATION OR DEATH BY GAS",
          99 : "OTHER- TYPE OF WEAPON NOT DESIGNED OR TYPE UNKNOWN"}

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
                99 : "DK, ALL INSTANCES WHERE RELATIONSHIP OF VICTIM TO OFFENDER CANNOT BE DETERMINED"}

circumstances = {2  : "RAPE",
                 3  : "ROBBERY",
                 5  : "BURGLARY",
                 6  : "LARCENY",
                 7  : "MOTOR VEHICLE THEFT",
                 9  : "ARSON",
                 10 : "PROSTITUTION AND COMMERCIALIZED VICE",
                 17 : "OTHER SEX OFFENSE",
                 18 : "NARCOTIC DRUG LAWS",
                 19 : "GAMBLING",
                 20 : "ABORTION",
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

subCircum = {1 : "FELON ATTACK POLICE OFFICER",
             2 : "FELON ATTACKED FELLOW POLICE OFFICER",
             3 : "FELON ATTACKED CIVILIAN",
             4 : "FELON ATTEMPTED FLIGHT FROM CRIME",
             5 : "FELON KILLED IN COMMISSION OF CRIME",
             6 : "FELON RESISTED ARREST",
             0 : "INAP., NOT A JUSTIFIABLE HOMICIDE",
             9 : "NOT ENOUGH INFORMATION TO DETERMINE"}


data = open('../data/SHC/1985/ICPSR_09028/DS0037/09028-0037-Data.txt')

wid = [4,1,2,5,2,7,1,2,1,2,8,3,3,1,24,6,2,6,1,1,3,1,2,2,
       2,2,2,2,2,2,2,2,2,2,
       1,1,1,1,1,1,1,1,1,1,
       1,1,1,1,1,1,1,1,1,1,
       1,1,1,1,1,1,1,1,1,1,
       2,2,2,2,2,2,2,2,2,2,2,
       1,1,1,1,1,1,1,1,1,1,1,
       1,1,1,1,1,1,1,1,1,1,1,
       1,1,1,1,1,1,1,1,1,1,1,
       2,2,2,2,2,2,2,2,2,2,2,
       2,2,2,2,2,2,2,2,2,2,2,
       2,2,2,2,2,2,2,2,2,2,2,
       1,1,1,1,1,1,1,1,1,1,1]

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
save('data/1985', data_n)



