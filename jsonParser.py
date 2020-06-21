import json


#tester function for checking if a hero is ranged or not
def rangeHeroChecker(heroMasterTable,key,value):
  try:
    return heroMasterTable[key]['AttackRange'] == value
  except KeyError:
    return False


class NewClass(object):pass
mydict= NewClass()


class DotAHeroData:
  def __init__(self,HeroID,AttackRange,PrimaryAttribute,HeroName,**Abilities):
    self.HeroID = HeroID
    self.AttackRange = AttackRange
    self.PrimaryAttribute = PrimaryAttribute
    self.HeroName = HeroName
    self.__dict__.update(Abilities)






#Open the active list and assign it to an object. The whitelist tag is from the json list.
with open('/home/aditya/Documents/development/dotaTagPick_python/heroActivelist.json') as f:
  heroWhitelist = json.load(f)["whitelist"]

# Open the heroList file and assign it to an object. The DOTAHeros tag is from the json list.
with open('/home/aditya/Documents/development/dotaTagPick_python/heroList.json') as g:
  heroCompleteData = json.load(g)["DOTAHeroes"]


with open('/home/aditya/Documents/development/dotaTagPick_python/heroAbilities.json') as h:
  heroAbilityData = json.load(h)["DOTAAbilities"]



masterHeroDataContainer = dict()


for key,value in heroWhitelist.items():
  # As every hero in the game has a different number of abilities,we create a temp dict that holds only the ability name information.
  # assign the current value of hero in consideration to a variable for easy access.
  currentHeroABilityKey = heroCompleteData[key]

  loopHeroAbilityValuesDict = dict()
  loopAbilityStore = dict()
  loopAbilityData = dict()
  for heroKey, valueKey in currentHeroABilityKey.items():
    if 'Ability' in heroKey and heroKey != 'AbilityDraftIgnoreCount' and heroKey!= 'AbilityPreview' and heroKey != 'AbilityLayout' and heroKey!= 'AbilityDraftAbilities' and heroKey!= 'AbilityDraftDisabled' and heroKey!='AbilityTalentStart' and heroKey != 'AbilityDraftUniqueAbilities':

      loopAbilityData = heroAbilityData[valueKey]
      loopHeroAbilityValuesDict[valueKey] = loopAbilityData
      loopAbilityStore = {"Abilities" : loopHeroAbilityValuesDict }

  HeroID = currentHeroABilityKey['HeroID']
  HeroName = currentHeroABilityKey['workshop_guide_name']
  PrimaryAttribute = currentHeroABilityKey['AttributePrimary']
  AttackRange = currentHeroABilityKey['AttackCapabilities']

  heroContainer = DotAHeroData(HeroID,AttackRange,PrimaryAttribute,HeroName,**loopAbilityStore)
  masterHeroDataContainer[key] = heroContainer.__dict__





with open('heroMasterTable.json', 'w') as fp:
  json.dump(masterHeroDataContainer, fp,indent=4)




print("update script run!")
