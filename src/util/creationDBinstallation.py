#!usr/bin/env python3

import sqlite3
from installation import Installation

class CreationDBinstallation:

	def __init__(self):
		self.conn = sqlite3.connect('bd/installation.db')
		self.c = self.conn.cursor()

	def creation_table_installation(self):
		self.c.execute("DROP TABLE IF EXISTS installations")
		self.c.execute('''CREATE TABLE installations
		             (town text, insee text, zip_code text, locality text, numb_path text, libelle_path text, name_path text,
					 longitude real, latitude real, accessibility_nothing text, accessibility_handi_moteur text, accessibility_handi_sens text,
					 emprise_fonciere text, gardiennee text, multi_commune text, nb_place_parking text, nb_place_parking_handi text, 
					 particular_instalation text, transport_metro text, transport_bus text, transport_tram text, transport_train text, transport_boat text,
					 other_transport text, number_equipements text, number_fiche_equipment_date_maj text)''')

		self.conn.commit()
		#self.conn.close()

	def add_installation(self, ins):
		self.c.execute('''INSERT INTO installations VALUES
					   (\"{0}\", \"{1}\", \"{2}\", \"{3}\", \"{4}\", \"{5}\", \"{6}\", \"{7}\", \"{8}\", \"{9}\", \"{10}\", \"{11}\", \"{12}\", \"{13}\", \"{14}\", \"{15}\", \"{16}\", 
					   \"{17}\", \"{18}\", \"{19}\", \"{20}\", \"{21}\", \"{22}\", \"{23}\", \"{24}\", \"{25}\")'''.format(ins.town, ins.insee, ins.zip_code, ins.locality, ins.numb_path, ins.libelle_path, ins.name_path,
					   ins.longitude, ins.latitude, ins.accessibility_nothing, ins.accessibility_handi_moteur, ins.accessibility_handi_sens,
					   ins.emprise_fonciere, ins.gardiennee, ins.multi_commune, ins.nb_place_parking, ins.nb_place_parking_handi,
					   ins.particular_instalation, ins.transport_metro, ins.transport_bus, ins.transport_tram, ins.transport_train, ins.transport_boat,
					   ins.other_transport, ins.number_equipements, ins.number_fiche_equipment_date_maj))
	
	def commit_db(self):
		self.conn.commit()



