#!usr/bin/env python3

import sqlite3
from equipement import Equipement

class CreationBDequipement:

	def __init__(self):
		self.conn = sqlite3.connect('bd/installation.db')
		self.c = self.conn.cursor()

	def creationTableEquipement(self):
		self.c.execute('DROP TABLE IF EXISTS equipements')
		self.c.execute('''CREATE TABLE equipements
					  (insee text, town text, equipTypeLib text, equipFiche text, familyFicheLib text)''')
		self.conn.commit()

	def ajoutEquipement(self, equ):
		self.c.execute('''INSERT INTO equipements VALUES
					  (\"{0}\", \"{1}\", \"{2}\", \"{3}\", \"{4}\"'''.format(equ.insee, equ.town, equ.equipTypeLib,
					   equ.equipFiche, equ.familyFicheLib))

	def commitBD():
		self.conn.commit()