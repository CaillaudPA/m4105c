#!usr/bin/env python3

import json
from installation import Installation

class ReadInstallation:

	def __init__(self):
		self.collectionInstallation = []

	def readInstallationMethod(self):
		with open("json/dataInstallation.paysdelaloire.fr.json") as data:
			self.json_data = json.load(data)
			
			for item in self.json_data["data"]:
				self.collectionInstallation.append(Installation(item["ComLib"],
																item["ComInsee"],
																item["InsCodePostal"],
																item["InsLieuDit"],
																item["InsNoVoie"],
																item["InsLibelleVoie"],
																item["Longitude"],
																item["Latitude"],
																item["InsAccessibiliteAucun"],
																item["InsAccessibiliteHandiMoteur"],
																item["InsAccessibiliteHandiSens"],
																item["InsEmpriseFonciere"],
																item["InsGardiennee"],
																item["InsMultiCommune"],
																item["InsNbPlaceParking"],
																item["InsNbPlaceParkingHandi"],
																item["InsPartLibelle"],
																item["InsTransportMetro"],
																item["InsTransportBus"],
																item["InsTransportTram"],
																item["InsTransportTrain"],
																item["InsTransportBateau"],
																item["InsTransportAutre"],
																item["Nb_Equipements"],
																item["Nb_FicheEquipement"],
																item["InsDateMaj"]))

	


