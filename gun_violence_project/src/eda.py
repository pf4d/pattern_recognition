from pylab    import *
from matrices import *

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

dims   = ['year',
          'month',
          'state',
          'group',
          'population',
          'agency code',
          'agency name',
          'MSA indication',
          'MSA code',
          'type of homicide',
          'situation',
          'victim count',
          'offender count',
          'victim 1 age',
          'victim 1 sex',
          'victim 2 age',
          'victim 2 sex',
          'victim 3 age',
          'victim 3 sex',
          'victim 4 age',
          'victim 4 sex',
          'victim 5 age',
          'victim 5 sex',
          'victim 6 age',
          'victim 6 sex',
          'victim 7 age',
          'victim 7 sex',
          'victim 8 age',
          'victim 8 sex',
          'victim 9 age',
          'victim 9 sex',
          'victim 10 age',
          'victim 10 sex',
          'victim 11 age',
          'victim 11 sex',
          'offender 1 age',
          'offender 1 sex',
          'offender 1 weapon',
          'offender 1 relationship to victim 1',
          'offender 1 circumstance',
          'offender 1 sub-circumstance',
          'offender 2 age',
          'offender 2 sex',
          'offender 2 weapon',
          'offender 2 relationship to victim 1',
          'offender 2 circumstance',
          'offender 2 sub-circumstance',
          'offender 3 age',
          'offender 3 sex',
          'offender 3 weapon',
          'offender 3 relationship to victim 1',
          'offender 3 circumstance',
          'offender 3 sub-circumstance',
          'offender 4 age',
          'offender 4 sex',
          'offender 4 weapon',
          'offender 4 relationship to victim 1',
          'offender 4 circumstance',
          'offender 4 sub-circumstance',
          'offender 5 age',
          'offender 5 sex',
          'offender 5 weapon',
          'offender 5 relationship to victim 1',
          'offender 5 circumstance',
          'offender 5 sub-circumstance',
          'offender 6 age',
          'offender 6 sex',
          'offender 6 weapon',
          'offender 6 relationship to victim 1',
          'offender 6 circumstance',
          'offender 6 sub-circumstance',
          'offender 7 age',
          'offender 7 sex',
          'offender 7 weapon',
          'offender 7 relationship to victim 1',
          'offender 7 circumstance',
          'offender 7 sub-circumstance',
          'offender 8 age',
          'offender 8 sex',
          'offender 8 weapon',
          'offender 8 relationship to victim 1',
          'offender 8 circumstance',
          'offender 8 sub-circumstance',
          'offender 9 age',
          'offender 9 sex',
          'offender 9 weapon',
          'offender 9 relationship to victim 1',
          'offender 9 circumstance',
          'offender 9 sub-circumstance',
          'offender 10 age',
          'offender 10 sex',
          'offender 10 weapon',
          'offender 10 relationship to victim 1',
          'offender 10 circumstance',
          'offender 10 sub-circumstance',
          'offender 11 age',
          'offender 11 sex',
          'offender 11 weapon',
          'offender 11 relationship to victim 1',
          'offender 11 circumstance',
          'offender 11 sub-circumstance']

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

situation = {1 : "SINGLE VICTIM - SINGLE OFFENDER",
             2 : "SINGLE VICTIM - UNKNOWN OFFENDER(S)",
             3 : "SINGLE VICTIM - MULTIPLE OFFENDERS",
             4 : "MULTIPLE VICTIMS - SINGLE OFFENDER",
             5 : "MULTIPLE VICTIMS - MULTIPLE OFFENDERS",
             6 : "MULTIPLE VICTIMS - UNKNOWN OFFENDER(S)"}

age = { 00  : 'UNKNOWN',
       'BB' : "7 DAYS OLD TO 364 DAYS OLD",
       'NB' : "BIRTH TO 6 DAYS OLD"}

sex = {1 : "MALE",
       2 : "FEMALE",
       3 : "UNKNOWN"}

weapon = {1  : "FIREARM, TYPE NOT STATED",
          2  : "HANDGUN",
          3  : "RIFLE",
          4  : "SHOTGUN",
          5  : "OTHER GUN",
          6  : "KNIFE OR SHARP INSTRUMENT",
          7  : "BLUNT OBJECT",
          8  : "PERSONAL WEAPONS",
          9  : "POISON",
          10 : "PUSHED OR THROWN OUT WINDOW",
          11 : "EXPLOSIVES",
          12 : "FIRE",
          13 : "NARCOTICS AND DRUGS",
          14 : "DROWNING",
          15 : "STRANGULATION AND HANGING",
          16 : "ASPHYXIATION OR GASSING",
          17 : "OTHER WEAPON"}

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

circumstance = {2  : "RAPE",
                3  : "ROBBERY",
                5  : "BURGLARY",
                6  : "LARCENY",
                7  : "MOTOR VEHICLE THEFT",
                9  : "ARSON",
                10 : "PROSTITUTION AND VICE",
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
                51 : "GUNCLEANING DEATH OTHER THAN SELF",
                52 : "CHILDREN PLAYING WITH GUN",
                53 : "OTHER NEGLIGENT HANDLING OF GUN",
                59 : "ALL OTHER MANSLAUGHTER BY NEGLIGENCE",
                60 : "OTHER NON-FELONY TYPE",
                70 : "ALL SUSPECTED FELONY TYPE",
                80 : "JUSTIFIABLE HOMICIDE - CIVILIAN",
                81 : "JUSTIFIABLE HOMICIDE - POLICE",
                99 : "UNKNOWN"}

subCircum = {1 : "FELON ATTACKED POLICE OFFICER",
             2 : "FELON ATTACKED FELLOW POLICE OFFICER",
             3 : "FELON ATTACKED CIVILIAN",
             4 : "FELON ATTEMPTED FLIGHT FROM CRIME",
             5 : "FELON KILLED IN COMMISSION OF CRIME",
             6 : "FELON RESISTED ARREST",
             7 : "NOT ENOUGH INFORMATION TO DETERMINE"}

data = load('data/data.npy')

m1 = logical_or(data[:,37] == 50, data[:,37] == 51)
m1 = logical_or(m1,  data[:,37] == 52)
m1 = logical_or(m1,  data[:,37] == 53)
#m1 = logical_and(m1, data[:,9] == 1)
#m1 = logical_and(m1, data[:,10] == 1)
m1 = logical_and(m1, data[:,35] != 8)
m1 = logical_and(m1, data[:,35] != 17)
m1 = logical_and(m1, data[:,35] != 6)
m1 = logical_and(m1, data[:,35] != 15)
m1 = logical_and(m1, data[:,35] != 7)

gun_accident  = data[m1]

m2 = logical_and(data[:,38] == 3, data[:,37] == 80)
m3 = logical_or(data[:,35] == 1,  data[:,35] == 2)
m3 = logical_or(m3, data[:,35] == 3)
m3 = logical_or(m3, data[:,35] == 4)
m3 = logical_or(m3, data[:,35] == 5)
m2 = logical_and(m2, m3)

gun_justified = data[m2]

def plot_data_matrix(data, m1_n, m2_n, m1_fs, m2_fs):
  """
  """
  weap = data[:,35]
  rela = data[:,36]
  circ = data[:,37]
  subc = data[:,38]

  weap_u = unique(weap)
  rela_u = unique(rela)
  circ_u = unique(circ)
  subc_u = unique(subc)

  w_nam  = []
  r_nam  = []
  c_nam  = []
  s_nam  = []
  w_cnt  = []
  r_cnt  = []
  c_cnt  = []
  s_cnt  = []

  for k in weap_u:
    w_nam.append(weapon[k])
    w_cnt.append(sum(weap == k))
  w_nam = array(w_nam)

  for k in rela_u:
    r_nam.append(relationship[k])
    r_cnt.append(sum(rela == k))
  r_nam = array(r_nam)

  for k in circ_u:
    c_nam.append(circumstance[k])
    c_cnt.append(sum(circ == k))
  c_nam = array(c_nam)

  for k in subc_u:
    s_nam.append(subCircum[k])
    s_cnt.append(sum(subc == k))
  s_nam = array(s_nam)

  r_idx = argsort(r_cnt)
  w_idx = argsort(w_cnt)[::-1]
  c_idx = argsort(c_cnt)
  s_idx = argsort(s_cnt)

  r_nam = r_nam[r_idx]
  w_nam = w_nam[w_idx]
  c_nam = c_nam[c_idx]
  s_nam = s_nam[s_idx]

  weap_u = weap_u[w_idx]
  rela_u = rela_u[r_idx]
  circ_u = circ_u[c_idx]
  subc_u = subc_u[s_idx]

  mat1 = zeros((len(weap_u), len(rela_u)))
  mat2 = zeros((len(weap_u), len(circ_u)))

  for i,w in enumerate(weap_u):
    for j,r in enumerate(rela_u):
      x = weap == w
      y = rela == r
      z = logical_and(x,y)
      mat1[i,j] = sum(z)

  for i,w in enumerate(weap_u):
    for j,c in enumerate(circ_u):
      x = weap == w
      y = circ == c
      z = logical_and(x,y)
      mat2[i,j] = sum(z)

  plot_matrix(mat1,'', m1_n, continuous=True, cmap='RdGy_r', scale='log',
              xlabel=r_nam, ylabel=w_nam, Mmin=1e-1, direc='../doc/images/',
              figsize=m1_fs)

  plot_matrix(mat2, '', m2_n, continuous=True, cmap='RdGy_r', scale='log',
              xlabel=c_nam, ylabel=w_nam, Mmin=1e-1, direc='../doc/images/',
              figsize=m2_fs)

#plot_data_matrix(data, 'all_data_relation', 'all_data_circum', (19,14), (19,14))
#plot_data_matrix(gun_accident, 'gun_accident_relation', 'gun_accident_circum',
#                 19,14, 19,14)
#plot_data_matrix(gun_justified, 'gun_justified_relation',
#                 'gun_justified_circum',
#                 19,14, 19,14)
#
##===============================================================================
## plot the weapon data :
#weap   = data[:,35]
#weap_n = sort(weapon.keys())
#pos    = arange(len(weapon))
#weap_c = []
#names  = []
#for k in weap_n:
#  names.append(weapon[k])
#  weap_c.append(len(where(weap == k)[0]))
#
#fig = figure(figsize=(9,5))
#ax  = fig.add_subplot(111)
#
#ax.barh(pos, weap_c, color='0.5', log=True, align='center')
#ax.set_yticks(pos)
#ax.set_yticklabels(names)
#ax.grid(axis='x')
#ax.set_ylim([-1, max(pos)+1])
#subplots_adjust(left=0.5)
#tick_params(axis='y', which='both',left='off', right='off',pad=10.0)
##tight_layout()
#savefig('../doc/images/weaps.pdf')
#show()
#close()
#
##===============================================================================
## plot the relationship data :
#rela   = data[:,36]
#rela_n = sort(relationship.keys())
#pos    = arange(len(relationship))
#rela_c = []
#names  = []
#for k in rela_n:
#  names.append(relationship[k])
#  rela_c.append(len(where(rela == k)[0]))
#
#fig = figure(figsize=(9,8))
#ax  = fig.add_subplot(111)
#
#ax.barh(pos, rela_c, color='0.5', log=True, align='center')
#ax.set_yticks(pos)
#ax.set_yticklabels(names)
#ax.grid(axis='x')
#ax.set_ylim([-1, max(pos)+1])
#subplots_adjust(left=0.5)
#tick_params(axis='y', which='both',left='off', right='off',pad=10.0)
##tight_layout()
#savefig('../doc/images/relationship.pdf')
#show()
#close()
#
##===============================================================================
## plot the circumstance data :
#circ   = data[:,37]
#circ_n = sort(circumstance.keys())
#pos    = arange(len(circumstance))
#circ_c = []
#names  = []
#for k in circ_n:
#  names.append(circumstance[k])
#  circ_c.append(len(where(circ == k)[0]))
#
#fig = figure(figsize=(9,8))
#ax  = fig.add_subplot(111)
#
#ax.barh(pos, circ_c, color='0.5', log=True, align='center')
#ax.set_yticks(pos)
#ax.set_yticklabels(names)
#ax.grid(axis='x')
#ax.set_ylim([-1, max(pos)+1])
#subplots_adjust(left=0.5)
#tick_params(axis='y', which='both',left='off', right='off',pad=10.0)
##tight_layout()
#savefig('../doc/images/circumstance.pdf')
#show()
#close()
#
#===============================================================================
## ages :
#vict_age = data[:,13].astype('i')
#offn_age = data[:,33].astype('i')
##keep = where(data[:,11] == 1)[0]
##keep = intersect1d(keep, where(data[:,12] == 1)[0])
#
#fig = figure(figsize=(5,4))
#ax  = fig.add_subplot(111)
#
#ax.hist(vict_age, bins=100, color='0.5')
#ax.set_xlabel('victim age')
#ax.set_ylabel('count')
#grid()
#tight_layout()
#savefig('../nsf_proposal/images/victim_age.pdf')
#close()
##show()
#
#fig = figure(figsize=(5,4))
#ax  = fig.add_subplot(111)
#
#ax.hist(offn_age[offn_age > 1], bins=90, color='0.5')
#ax.set_xlabel('offender age')
#ax.set_ylabel('count')
#grid()
#tight_layout()
#savefig('../doc/images/offender_age.pdf')
#close()
##show()
#
#
#===============================================================================
# data matrix :
m = logical_and(data[:,11] != 900, data[:,11] != 999) 
m = logical_and(m,  data[:,33] != 999)
m = logical_and(m,  data[:,34] != 3)
m = logical_and(m,  data[:,12] != 3)

M  = data[m]

from matplotlib.mlab   import PCA
from scipy.stats       import gaussian_kde
from sklearn.lda       import LDA
import pandas          as pnd
import seaborn.apionly as sns

def plot_lda(X, y, title, label_dict, direc):
  """
  """
  lda = LDA(n_components=2)
  L   = lda.fit_transform(X,y)
  n   = shape(L)[1]
  
  if n == 1:
    xmin = L[:,0].min()
    xmax = L[:,0].max()
    g = sns.distplot(L, hist=False, bins=500)
    sns.plt.grid()
    sns.plt.xlim(xmin, xmax)
    sns.plt.xlabel('LD1')
    sns.plt.ylabel('density')
    sns.plt.tight_layout()
    sns.plt.savefig(direc + 'all' + '.png')
    sns.plt.close()
  else:
    xmin = L[:,0].min()
    xmax = L[:,0].max()
    ymin = L[:,1].min()
    ymax = L[:,1].max()
    g = sns.jointplot(L[:,0], L[:,1], kind='kde', color='k',
                      stat_func=None,
                      xlim=(xmin, xmax), ylim=(ymin, ymax))
    g.set_axis_labels('all classes','')
    g.savefig(direc + 'all' + '.png')

  label = unique(y)
  k     = len(label)
  cols  = cm.rainbow(linspace(0,1,k))
  ax    = plt.subplot(111)
  for l,c in zip(label, cols):
    if n == 1:
      g = sns.distplot(L[y == l], hist=False, bins=500,
                       label=label_dict[l])
    else:
      g = sns.jointplot(L[:,0][y == l],
                        L[:,1][y == l],
                        kind='kde', color='k', stat_func=None,
                        xlim=(xmin, xmax), ylim=(ymin, ymax))
      g.set_axis_labels(label_dict[l],'')
      g.savefig(direc + label_dict[l] + '.png')
      sns.plt.close()
      #plt.scatter(L[:,0][y == l],
      #            L[:,1][y == l],
      #            marker = 'o',
      #            color = c,
      #            alpha=0.2,
      #            label=label_dict[l])

  if n == 1:
    sns.plt.grid()
    sns.plt.xlim(xmin, xmax)
    sns.plt.xlabel('LD1')
    sns.plt.ylabel('density')
    sns.plt.tight_layout()
    sns.plt.savefig(direc + title + '.png')
    sns.plt.close()
  else:
    #leg = plt.legend(loc='upper right', fancybox=True)
    #leg.get_frame().set_alpha(0.5)
    #plt.grid()
    #plt.ylabel('LD2')
    #plt.xlabel('LD1')
    #plt.savefig(direc + title + '.png')
    sns.plt.close()

i   = [0,1,2,3,4,5,6,7,8,9,10,11,12,33,34,36,37,38]
y   = M[:,35]
X   = M[:,i]

#plot_lda(X, y, 'weapon', weapon, '../doc/images/weapon/')
#
#m1    = logical_or(y == 1, y == 2)
#m1    = logical_or(m1,     y == 3)
#m1    = logical_or(m1,     y == 4)
#m1    = logical_or(m1,     y == 5)
#m2    = logical_not(m1)
#y[m1] = 1
#y[m2] = 2
#
#plot_lda(X, y, 'gun', {1:'GUN', 2:'OTHER'}, '../doc/images/gun/')
#
#i   = [0,1,2,3,4,5,6,7,8,9,10,11,12,33,34,35,36,37]
#y   = M[:,38]
#X   = M[:,i]
#
#plot_lda(X, y, 'sub-circumstance', subCircum, '../doc/images/subcircum/')
#
#i   = [0,1,2,3,4,6,7,8,9,10,11,12,33,34,35,36,37,38]
#y   = M[:,5]
#X   = M[:,i]
#
#plot_lda(X, y, 'suburban', suburban, '../doc/images/suburban/')
#
#i   = [0,1,2,3,4,5,6,8,9,10,11,12,33,34,35,36,37,38]
#y   = M[:,7]
#X   = M[:,i]
#
#plot_lda(X, y, 'type', homicide, '../doc/images/homicide/')
#
#i   = [0,1,2,3,4,5,6,7,8,9,10,11,12,33,35,36,37,38]
#y   = M[:,34]
#X   = M[:,i]
#
#plot_lda(X, y, 'offn_sex', sex, '../doc/images/offn_sex/')
#
#i   = [0,1,2,3,4,5,6,7,8,9,10,11,12,33,34,35,36,37,38]
#y   = M[:,12]
#X   = M[:,i]
#
#plot_lda(X, y, 'vict_sex', sex, '../doc/images/vict_sex/')
#
##===============================================================================
#i   = [0,1,2,3,4,5,6,7,8,9,10,11,12,33,34,35,36,37,38]
#X   = M[:,i]
#p   = PCA(M)
#plot(p.Y[:,0], p.Y[:,1], 'o', color='k', alpha=0.5)
#plt.xlabel(r'PC1')
#plt.ylabel(r'PC2')
#plt.grid()
#plt.tight_layout()
#savefig('../doc/images/PCA.png')
#plt.show()
#
#===============================================================================
#weap = M[:,35]
#rela = M[:,36]
#circ = M[:,37]
#subc = M[:,38]
#vict = M[:,11]
#offn = M[:,33]
#X = vstack((weap, rela, circ, vict, offn)).T
#
#Xp = {'weapon'       : weap,
#      'relationship' : rela,
#      'circumstance' : circ,
#      'victim age'   : vict,
#      'offender age' : offn}
#df = pnd.DataFrame(Xp)
#g  = sns.pairplot(df)
##g.savefig('../doc/images/pairplot.png', dpi=200)
#show()
##savefig('../doc/images/pairplot.pdf')
#close()

## population stuff :
#ass = unique(data[:,5])
#pss = []
#vss = []
#for a in ass:
#  k = where(data[:,5] == a)[0]
#  p = data[k,  4]
#  v = sum(data[k, 11])
#  pss.append(p[0])
#  vss.append(v)
#pss = array(pss)
#vss = array(vss)



