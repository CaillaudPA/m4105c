#!usr/bin/env python3

import sqlite3
from equipment import Equipment

class CreationDBequipment:

	def __init__(self):
		self.conn = sqlite3.connect('bd/installation.db')
		self.c = self.conn.cursor()

	def creation_table_equipment(self):
		self.c.execute('DROP TABLE IF EXISTS equipements')
		self.c.execute('''CREATE TABLE equipements
					  (insee text, town text, equipment_id text, equipment_nb text, act_code text, act_lib text)''')
		self.conn.commit()

	def add_equipment(self, equ):
		self.c.execute('''INSERT INTO equipements VALUES
					  (\"{0}\", \"{1}\", \"{2}\", \"{3}\", \"{4}\", \"{5}\")'''.format(equ.insee, equ.town, equ.equipment_id,
					   equ.equipment_nb, equ.act_code, equ.act_lib))

	def commit_db(self):
		self.conn.commit()