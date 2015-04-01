#!usr/bin/env python3

class Equipment:
	'''
		This class represent an equipment
		The 5 attribut are String
	'''


	def __init__(self, insee, town, equipment_id, equipment_nb, equ_nom):
		self.insee = insee
		self.town = town
		self.equipment_id = equipment_id
		self.equipment_nb = equipment_nb
		self.equ_nom = equ_nom

	def __str__(self):
		return "Code Insee : " + self.insee + ", Commune : " + self.town