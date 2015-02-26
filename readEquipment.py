#!usr/bin/env python3

import json
from equipement import Equipement


class readEquipment:


	def __init__(self):
		self.collectionEquipment = []


	def readFileEquipment(self):
		with open("json/dataEquipement.paysdelaloire.fr.json") as data :
			json_data = json.load(data)

			for item in json_data["data"]:
				self.collectionEquipment.append(Equipement(item["ComInsee"],
														   item["ComLib"],
														   item["EquipementTypeLib"],
								  						   item["EquipementFiche"], 
								  						   item["FamilleFicheLib"]))


		
 

	#def createObjectEquipment(self):





tmp = readEquipment()
tmp.readFileEquipment()