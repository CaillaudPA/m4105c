#!usr/bin/env python3

import sqlite3
from installation import Installation

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
		#self.conn.close()

	def ajoutInstallation(self, ins):
		print('''INSERT INTO installations VALUES
					   (\"{0}\", \"{1}\", \"{2}\", \"{3}\", \"{4}\", \"{5}\", {6}, {7}, {8}, \"{9}\", \"{10}\", \"{11}\", \"{12}\", \"{13}\", \"{14}\", \"{15}\", \"{16}\", 
					   \"{17}\", \"{18}\", \"{19}\", \"{20}\", \"{21}\", \"{22}\", \"{23}\", \"{24}\", \"{25}\")'''.format(ins.town, ins.insee, ins.zipCode, ins.locality, ins.numbPath, ins.libellePath, ins.namePath,
					   ins.longitude, ins.latitude, ins.accessibilityNothing, ins.accessibiliteHandiMoteur, ins.accessibiliteHandiSens,
					   ins.empriseFonciere, ins.gardiennee, ins.multiCommune, ins.nbPlaceParking, ins.nbPlaceParkingHandi,
					   ins.particularInstalation, ins.transportMetro, ins.transportBus, ins.transportTram, ins.transportTrain, ins.transportBoat,
					   ins.otherTransport, ins.number_Equipements, ins.number_FicheEquipemenDateMaj))
		self.c.execute('''INSERT INTO installations VALUES
					   (\"{0}\", \"{1}\", \"{2}\", \"{3}\", \"{4}\", \"{5}\", {6}, {7}, {8}, \"{9}\", \"{10}\", \"{11}\", \"{12}\", \"{13}\", \"{14}\", \"{15}\", \"{16}\", 
					   \"{17}\", \"{18}\", \"{19}\", \"{20}\", \"{21}\", \"{22}\", \"{23}\", \"{24}\", \"{25}\")'''.format(ins.town, ins.insee, ins.zipCode, ins.locality, ins.numbPath, ins.libellePath, ins.namePath,
					   ins.longitude, ins.latitude, ins.accessibilityNothing, ins.accessibiliteHandiMoteur, ins.accessibiliteHandiSens,
					   ins.empriseFonciere, ins.gardiennee, ins.multiCommune, ins.nbPlaceParking, ins.nbPlaceParkingHandi,
					   ins.particularInstalation, ins.transportMetro, ins.transportBus, ins.transportTram, ins.transportTrain, ins.transportBoat,
					   ins.otherTransport, ins.number_Equipements, ins.number_FicheEquipemenDateMaj))
		self.conn.commit()

tmp = CreationBDinstallation()
tmp.creationTableInstallation()

newInsta = Installation("hjio1", "hjio2", "hjio3", "hjio4", "hjio5", "h6jio", "7", 1.0, 1.2, "hj8io", "hji9o", 
						"hji10o", "hj11io", "hj12io", "hji13o", "h14jio", "hj15io", "hji16o", "hji17o", "hj18io", "h19jio", 
						"hji20o", "hji21o", "hjio22", "hjio23", "hjio24")



tmp.ajoutInstallation(newInsta)


