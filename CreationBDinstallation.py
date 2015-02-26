#!usr/bin/env python3

import sqlite3

class CreationBDinstallation:

	def __init__(self):
		self.conn = sqlite3.connect('bd/installation.db')
		self.c = self.conn.cursor()

	def creationTableInstallation(self):
		self.c.execute("DROP TABLE IF EXISTS installations")
		self.c.execute('''CREATE TABLE installations
		             (town text, insee text, zipCode text, locality text, numbPath text, libellePath text, namePath text,
					 longitude real, latitude real, accessibilityNothing text, accessibiliteHandiMoteur text, accessibiliteHandiSens text,
					 empriseFonciere text, gardiennee text, multiCommune text, nbPlaceParking text, nbPlaceParkingHandi text, 
					 particularInstalation text, transportMetro text, transportBus text, transportTram text, transportTrain text, transportBoat text,
					 otherTransport text, number_Equipements text, number_FicheEquipemenDateMaj text)''')

		self.conn.commit()
		self.conn.close()


tmp = CreationBDinstallation()
tmp.creationTableInstallation()