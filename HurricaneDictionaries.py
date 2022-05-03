# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# 1
# Update Recorded Damages
conversion = {"M": 1000000,
              "B": 1000000000}

# test function by updating damages
updated_damages = []
for i in damages:
  if 'M' in i:
    updated_damages.append((float(i.strip('M')) * conversion["M"]))
  elif 'B' in i:
    updated_damages.append((float(i.strip('B')) * conversion["B"]))
  else:
    updated_damages.append(i)
#print(updated_damages)    

# 2 
# Create a Table
zipped_data = zip(names, months, years, max_sustained_winds, areas_affected, updated_damages, deaths)

# Create and view the hurricanes dictionary
hurricanes = {
  name: {
    "Name": name,
    "Month": month,
    "Year" : year,
    "Max Sustained Wind": wind,
    "Areas Affected": area,
    "Damage": damage,
    "Deaths": deaths,
  } for name, month, year, wind, area, damage, deaths in zipped_data
}
#print(hurricanes)
# 3
# Organizing by Year
# create a new dictionary of hurricanes with year and key
def hurricanesByYear(hurricane_dict):
  hurricanes_by_year = {}
  for i in range(0, len(hurricane_dict)):
    currentCane = list(hurricane_dict.values())[i]
    #print(currentCane)
    currentYear = currentCane['Year']
    #print(currentYear)
    #print(currentYear in hurricanes_by_year)
    if currentYear in hurricanes_by_year:
      tempList = hurricanes_by_year[currentYear]
      #print(tempList)
      tempList.append(currentCane)
      hurricanes_by_year[currentYear] = tempList
    else:
      tempList = []
      tempList.append(currentCane)
      hurricanes_by_year[currentYear] = tempList
  return hurricanes_by_year


hurricanes_by_year = hurricanesByYear(hurricanes)

#print(hurricanes_by_year.keys())
#print(len(hurricanes_by_year.keys()))
#print(len(hurricanes))
#print(hurricanes_by_year[1932])
# 4
# Counting Damaged Areas
# create dictionary of areas to store the number of hurricanes involved in
def countDamagedAreas(dictionary_data):
  tempDic = {}
  for key in dictionary_data:
    for area in dictionary_data[key]['Areas Affected']:
      #print(area)
      if area not in tempDic:
        tempDic[area] = 1
      else:
        tempDic[area] += 1
  return tempDic
areasAffectedDictionary = countDamagedAreas(hurricanes)
#print(areasAffectedDictionary)
#print(list(areasAffectedDictionary.values()))
def findMostAffected(areasData):
  maxCount = 0
  maxKey = ''
  for key in areasData:
    #print(key)
    #print(areasData[key])
    currentKey = key
    currentCount = areasData[key]
    if currentCount > maxCount:
      maxCount = currentCount
      maxKey = currentKey
  retDic = {maxKey: maxCount}
  return retDic
# 5 
# Calculating Maximum Hurricane Count
# find most frequently affected area and the number of hurricanes involved in

#print(findMostAffected(areasAffectedDictionary))

# 6
# Calculating the Deadliest Hurricane
# find highest mortality hurricane and the number of deaths

def findMaxDeaths(hurricaneDic):
  maxKey = ''
  maxDeaths = 0
  for key in hurricaneDic:
    currentKey = key
    currentDeaths = hurricaneDic[key]['Deaths']
    if currentDeaths > maxDeaths:
      maxKey = currentKey
      maxDeaths = currentDeaths
  retDic = {maxKey: maxDeaths}
  return retDic
#print(findMaxDeaths(hurricanes))
# 7
# Rating Hurricanes by Mortality
mortality_scale = {0: 0,
                   1: 100,
                   2: 500,
                   3: 1000,
                   4: 10000}
def rateHurricanes(hurricaneDic):
  tempKeyList = [0, 1, 2, 3, 4, 5]
  temp0= []
  temp1= []
  temp2= []
  temp3= []
  temp4= []
  temp5= []
  for key in hurricaneDic:
    currentDeaths = hurricaneDic[key]['Deaths']
    if currentDeaths < mortality_scale[0]:
      temp0.append(hurricaneDic[key])
    elif currentDeaths < mortality_scale[1]:
      temp1.append(hurricaneDic[key])
    elif currentDeaths < mortality_scale[2]:
      temp2.append(hurricaneDic[key])
    elif currentDeaths < mortality_scale[3]:
      temp3.append(hurricaneDic[key])
    elif currentDeaths < mortality_scale[4]:
      temp4.append(hurricaneDic[key])
    else:
      temp5.append(hurricaneDic[key])
  tempValues = [temp0, temp1, temp2, temp3, temp4, temp5]
  retDic = {key:value for key, value in zip(tempKeyList, tempValues)}
  return retDic    
#print(rateHurricanes(hurricanes))

# categorize hurricanes in new dictionary with mortality severity as key
mortalityDic = rateHurricanes(hurricanes)
# 8 Calculating Hurricane Maximum Damage
def findMaxDamage(hurricaneDic):
  maxDamage = 0
  maxDamageKey = ''
  for key in hurricaneDic:
    if isinstance(hurricaneDic[key]['Damage'], str):
      continue 
    if maxDamage < hurricaneDic[key]['Damage']:
      maxDamage = hurricaneDic[key]['Damage']
      maxDamageKey = key
  retDic = {maxDamageKey: maxDamage}
  return retDic
# find highest damage inducing hurricane and its total cost
#print(findMaxDamage(hurricanes))

# 9
# Rating Hurricanes by Damage
damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}
#print(damage_scale[4])               
def rateByDamage(hurricaneDic):
  retDic = {
    0: [],
    1: [],
    2: [],
    3: [],
    4: [],
    5: []
  }
  for key in hurricaneDic:
    dam = hurricaneDic[key]['Damage']
    if isinstance(dam, str):
      continue
    if dam < damage_scale[0]:
      retDic[0].append(hurricaneDic[key])
    elif dam < damage_scale[1]:
      retDic[1].append(hurricaneDic[key])
    elif dam < damage_scale[2]:
      retDic[2].append(hurricaneDic[key])
    elif dam < damage_scale[3]:
      retDic[3].append(hurricaneDic[key])
    elif dam < damage_scale[4]:
      retDic[4].append(hurricaneDic[key])
    else:
      retDic[5].append(hurricaneDic[key])
  return retDic
# categorize hurricanes in new dictionary with damage severity as key
print(rateByDamage(hurricanes)[1])
