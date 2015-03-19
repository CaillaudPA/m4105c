#!usr/bin/env python3

import json

from activite import Activity

class ReadActivity:

	def __init__(self):
		self.collectionActivity = []

	def readActivityMethod(self):
		with open("json/dataActivite.paysdelaloire.fr.json") as data:
			self.json_data = json.load(data)

			for item in self.json_data["data"]:
				self.collectionActivity.append(Activity(item["ComInsee"],
														item["ComLib"],
														item["EquipementId"],
														item["EquNbEquIdentique"],
														item["ActCode"],
														item["ActLib"],
														item["EquActivitePraticable"],
														item["EquActivitePratique"],
														item["EquActiviteSalleSpe"],
														item["ActNivLib"]))


tmp = ReadActivity()
tmp.readActivityMethod()


for i in tmp.collectionActivity:
	try:
		print(i.comLib)
		print(len(tmp.collectionActivity))
	except Exception, e:
		print("Valeur introuvable ?")





