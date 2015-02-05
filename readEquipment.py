#!usr/bin/env python3

import json


class readEquipment:


	def __init__(self):
		self.collectionEquipment = []


	def readFileEquipment(self):
		with open("json/dataEquipement.paysdelaloire.fr.json") as data :
			self.json_data = json.load(data)

			for item in json_data["data"]:
				equip = Equipement(item["ComInsee"], item["ComLib"]), item["EquipementId"], item["EquNbEquIdentique"],
								   item[""], item[""], item[""])


		print(self.json_data["data"][0])
 

	#def createObjectEquipment(self):





tmp = readEquipment()
tmp.readFileEquipment()