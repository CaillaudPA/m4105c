#!usr/bin/env python3

import json

from Activity import Activity

class ReadActivity:

	def __init__(self):
		self.collection_activity = []

	def readActivityMethod(self):
		with open("json/dataActivite.paysdelaloire.fr.json") as data:
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








