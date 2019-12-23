import json
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get("https://dex.pokemonshowdown.com/pokemon/")
search_input = browser.find_element_by_class_name("searchbox")

file = open("./pokemon-data/pokemon-gen1-data.csv", 'w')
file.write("Pokemon, Number, Type1, Type2, Ability1, Ability2, Ability3, HP, Attack, Defense, Sp. Atk, Sp. Def, Speed, Sprite\n")

with open('./names.json') as f:
  pokemon_names = json.loads(f.read())

for name in pokemon_names[0:151]:
  search_input.clear()
  search_input.send_keys(name)
  search_input.send_keys(Keys.RETURN)

  pokemon = name
  number = browser.find_element_by_tag_name("code").text.replace("#", "")

  types = browser.find_elements_by_class_name("type")
  type1 = types[0].text
  if len(types) == 2:
    type2 = types[1].text
  else:
    type2 = 'none'

  abilities = browser.find_elements_by_css_selector("dd.imgentry > a")
  ability1 = abilities[0].text
  if len(abilities) >= 2:
    ability2 = abilities[1].text
  else:
    ability2 = 'none'

  if len(abilities) == 3:
    ability3 = abilities[2].text
  else:
    ability3 = 'none'

  base_stats = browser.find_elements_by_class_name('stat')
  hp = base_stats[0].text
  attack = base_stats[1].text
  defense = base_stats[2].text
  special_atk = base_stats[3].text
  special_def = base_stats[4].text
  speed = base_stats[5].text
  sprite = browser.find_element_by_class_name("sprite").get_attribute("src")

  file.write(pokemon + "," + number + "," + 
    type1 + "," + type2 + "," + ability1 + "," 
    + ability2 + "," + ability3 + "," + hp + "," 
    + attack + "," + defense + "," + special_atk 
    + "," + special_def + "," + speed + "," + sprite 
    + "\n")

browser.close()
file.close()





