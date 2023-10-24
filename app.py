
## IN THIS FILE YOU WILL ONLY READ FROM THE JSON DATA USING CLASSES
import json
# Open the JSON file of pokemon data
test = open("data.json", encoding="utf8")
# create variable "data" that represents the enitre pokedex list
data = json.load(test)
