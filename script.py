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

# write your update damages function here:
def clean_damages(damages):
  cleaned = []
  for amount in damages:
    if amount == "Damages not recorded":
      cleaned.append(amount)
    elif amount.find("M") != -1:
      cleaned.append(float(amount.strip('M'))*1000000)
    elif amount.find("B") != -1:
      cleaned.append(float(amount.strip('B'))*1000000000)
  return cleaned

cleaned_damages = clean_damages(damages)
#print(cleaned_damages)

# write your construct hurricane dictionary function here:
def make_dict_name(names, months, years, max_sustained_winds, areas_affected, damage, deaths):
  hurricanes = {}
  for i in range(len(names)):
    hurricanes.update({names[i]: {"Name": names[i], "Month": months[i], "Year": years[i], "Max Sustained Wind": max_sustained_winds[i], "Areas Affected": areas_affected[i], "Damage": damage[i], "Death": deaths[i]}})
  return hurricanes

hurricanes = make_dict_name(names, months, years, max_sustained_winds, areas_affected, cleaned_damages, deaths)
#print(hurricanes)

# write your construct hurricane by year dictionary function here:
def make_dict_year(hurricanes):
  new_dict = {}
  for key in hurricanes:
    if hurricanes[key]["Year"] not in new_dict:
      new_dict[hurricanes[key]["Year"]] = [hurricanes[key]]
    else:
      new_dict[hurricanes[key]["Year"]].append(hurricanes[key])
  return new_dict

hurricanes_by_year = make_dict_year(hurricanes)
#print(hurricanes_by_year)

# write your count affected areas function here:
def count_area(hurricanes):
  count_areas = {}
  for name in hurricanes:
    for area in hurricanes[name]["Areas Affected"]:
      if area not in count_areas:
        count_areas[area] = 1
      else:
        count_areas[area] += 1
  return count_areas

areas_count = count_area(hurricanes)
#print(areas_count)

# write your find most affected area function here:
def most_affected(areas):
  maximum = 0
  for key, value in areas.items():
    if value > maximum:
      maximum = value
      most_affected = key
  return most_affected, maximum

most_affected_area = most_affected(areas_count)
#print(most_affected_area)

# write your greatest number of deaths function here:
def most_deaths(hurricane):
  maximum = 0
  for key in hurricane:
    value = hurricane[key]["Death"]
    if value > maximum:
      maximum = value
      most_death = key
  return most_death, maximum

highest_deaths = most_deaths(hurricanes)
#print(highest_deaths)

# write your catgeorize by mortality function here:
def mortality_ranking(hurricane):
  hurricanes_by_mortality = {0:[],1:[],2:[],3:[],4:[],5:[]}
  for cane in hurricane:
    if hurricane[cane]["Death"] == 0:
      hurricanes_by_mortality[0].append(hurricane[cane])
    elif hurricane[cane]["Death"] <= 100:
      hurricanes_by_mortality[1].append(hurricane[cane])
    elif hurricane[cane]["Death"] <= 500:
      hurricanes_by_mortality[2].append(hurricane[cane])
    elif hurricane[cane]["Death"] <= 1000:
      hurricanes_by_mortality[3].append(hurricane[cane])
    elif hurricane[cane]["Death"] <= 10000:
      hurricanes_by_mortality[4].append(hurricane[cane])
    else:
      hurricanes_by_mortality[5].append(hurricane[cane])
  return hurricanes_by_mortality

mortality_rank = mortality_ranking(hurricanes)
#print(mortality_rank)

# write your greatest damage function here:
def highest_damage(hurricane):
  maximum = 0
  for key in hurricane:
    value = hurricane[key]["Damage"]
    if type(value) == float and value > maximum:
      maximum = value
      most_damage = key
  return most_damage, maximum

greatest_damage = highest_damage(hurricanes)
#print(greatest_damage)

# write your catgeorize by damage function here:
def damage_ranking(hurricane):
  hurricanes_by_damage = {0:[],1:[],2:[],3:[],4:[],5:[]}
  for cane in hurricane:
    if type(hurricane[cane]["Damage"]) == float:
      if hurricane[cane]["Damage"] == 0:
        hurricanes_by_damage[0].append(hurricane[cane])
      elif hurricane[cane]["Damage"] <= 100000000:
        hurricanes_by_damage[1].append(hurricane[cane])
      elif hurricane[cane]["Damage"] <= 1000000000:
        hurricanes_by_damage[2].append(hurricane[cane])
      elif hurricane[cane]["Damage"] <= 10000000000:
        hurricanes_by_damage[3].append(hurricane[cane])
      elif hurricane[cane]["Damage"] <= 50000000000:
        hurricanes_by_damage[4].append(hurricane[cane])
      else:
        hurricanes_by_damage[5].append(hurricane[cane])
  return hurricanes_by_damage

damage_rank = damage_ranking(hurricanes)
print(damage_rank)