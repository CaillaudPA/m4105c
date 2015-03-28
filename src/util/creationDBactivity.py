#!usr/bin/env python3

import sqlite3
from activity import Activity

class CreationDBactivity:

	def __init__(self):
		self.conn = sqlite3.connect('bd/activity.db')
		self.c = self.conn.cursor()

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

	def commit_db(self):
		self.conn.commit()