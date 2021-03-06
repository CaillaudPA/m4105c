#!usr/bin/env python3

import json

from bean.activity import Activity

class ReadActivity:
	'''
	Docstring for class ReadActivity
	'''

	def __init__(self):
		self.collection_activity = []

	def read_activity_method(self):
		'''
		Method used to read json file 
		'''
		with open("../../json/dataActivite.paysdelaloire.fr.json") as data:
			self.json_data = json.load(data)

			for item in self.json_data["data"]:
				self.collection_activity.append(Activity(item["ComInsee"],
														item["ComLib"],
														item["EquipementId"],
														item["EquNbEquIdentique"],
														item["ActCode"],
														item["ActLib"],
														item["EquActivitePraticable"],
														item["EquActivitePratique"],
														item["EquActiviteSalleSpe"],
														item["ActNivLib"]))

		








