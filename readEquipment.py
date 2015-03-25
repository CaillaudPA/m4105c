#!usr/bin/env python3

import json
from equipment import Equipment


class ReadEquipment:


	def __init__(self):
		self.collection_equipment = []


	def read_equipment_method(self):
		with open("json/dataEquipement.paysdelaloire.fr.json") as data :
			json_data = json.load(data)

			for item in json_data["data"]:
				self.collection_equipment.append(Equipment(item["ComInsee"],
														   item["ComLib"],
														   item["EquipementId"],
								  						   item["EquNbEquIdentique"], 
								  						   item["ActCode"],
								  						   item["ActLib"]))


		
 
