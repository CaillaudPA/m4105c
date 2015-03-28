#!usr/bin/env python3

import sqlite3
from bean.installation import Installation
from bean.equipment import Equipment
from bean.activity import Activity 

class DB():
	"""docstring for DB"""
	def __init__(self):
		self.conn = sqlite3.connect('../bd/DB.db')
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

	def creation_table_activity(self):
		self.c.execute('DROP TABLE IF EXISTS activity')
		self.c.execute('''CREATE TABLE activity
					  (com_insee text, com_lib text, equipment_id text, equ_nb_equ_identique text, 
					  act_code text, act_lib text, equ_activity_praticable text, equ_activity_pratique text,
					  equ_activity_salle_spe text, act_level_lib text)''')
		self.conn.commit()

	def add_activity(self, act):
		self.c.execute('''INSERT INTO activity VALUES
					  (\"{0}\", \"{1}\", \"{2}\", \"{3}\", \"{4}\", \"{5}\", \"{6}\", \"{7}\", \"{8}\", \"{8}\")'''.format(act.com_insee,
					  act.com_lib, act.equipment_id, act.equ_nb_equ_identique, act.act_code, act.act_lib, act.equ_activity_praticable, act.equ_activity_pratique,
					  act.equ_activity_salle_spe, act.act_level_lib))

	def creation_table_equipment(self):
		self.c.execute('DROP TABLE IF EXISTS equipements')
		self.c.execute('''CREATE TABLE equipements
					  (insee text, town text, equipment_id text, equipment_nb text, act_code text, act_lib text)''')
		self.conn.commit()

	def add_equipment(self, equ):
		self.c.execute('''INSERT INTO equipements VALUES
					  (\"{0}\", \"{1}\", \"{2}\", \"{3}\", \"{4}\", \"{5}\")'''.format(equ.insee, equ.town, equ.equipment_id,
					   equ.equipment_nb, equ.act_code, equ.act_lib))

	def attribute_installation_to_array(self,attribute):
		"""
		Method used to obtain an array which contain all elements for a given attribute
		Return an array with all the elements for the attribute given in parameters
		"""
		res = self.c.execute('''SELECT {} FROM installations'''.format(attribute))
		return res.fetchall()

	def select_installation_tuple_from_pk(self, key):
		"""
		Method used to select a tuple from Installation with the primary key
		Return a tuple from Installation table
		"""
		res = self.c.execute('''SELECT * FROM installations WHERE number_equipements={}'''.format(key))
		return res.fetchone()

	def select_all_from(self, table):
		res = self.c.execute('''SELECT * FROM {}'''.format(table))
		return res.fetchall()