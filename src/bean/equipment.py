#!usr/bin/env python3

class Equipment:
	'''
		This class represent an installation
		The 10 attribut are String

	'''


	def __init__(self, insee, town, equipment_id, equipment_nb, act_code, act_lib):
		self.insee = insee
		self.town = town
		self.equipment_id = equipment_id
		self.equipment_nb = equipment_nb
		self.act_code = act_code
		self.act_lib = act_lib

	def __str__(self):
		return "Code Insee : " + self.insee + ", Commune : " + self.town