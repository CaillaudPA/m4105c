#!usr/bin/env python3

import sqlite3
from activite import Activity

class CreationBDactivity:

	def __init__(self):
		self.conn = sqlite3.connect('bd/activity.db')
		self.c = self.conn.cursor()

	def creationTableActivity(self):
		self.c.execute('DROP TABLE IF EXISTS activity')
		self.c.execute('''CREATE TABLE activity
					  (comInsee text, comLib text, equipementId text, actCode text, actLib text, equActivityPraticable text,
					  	equActivityPratique text, equActivitySalleSpe text, actLevelLib text)''')
		self.conn.commit()

	def ajoutActivity(self, act):
		self.c.execute('''INSERT INTO activity VALUES
					  (\"{0}\", \"{1}\", \"{2}\", \"{3}\", \"{4}\", \"{5}\", \"{6}\", \"{7}\", \"{8}\"'''.format(act.comInsee,
					  act.comLib, act.equipementId, act.actCode, act.Lib, act.equActivityPraticable, act.equActivityPratique,
					  act.equActivitySalleSpe, act.actLevelLib))

	def commitBD():
		self.conn.commit()