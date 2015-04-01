#!usr/bin/env python3

class Activity:
	'''
	This class represent an activity
	All attribut are String
	'''
	def __init__(self, com_insee, com_lib, equipment_id, equ_nb_equ_identique, act_code, act_lib, equ_activity_praticable, equ_activity_pratique,
				equ_activity_salle_spe, act_level_lib):
		self.com_insee = com_insee
		self.com_lib = com_lib
		self.equipment_id = equipment_id
		self.equ_nb_equ_identique = equ_nb_equ_identique
		self.act_code = act_code
		self.act_lib = act_lib
		self.equ_activity_praticable =  equ_activity_praticable 
		self.equ_activity_pratique = equ_activity_pratique
		self.equ_activity_salle_spe = equ_activity_salle_spe
		self.act_level_lib = act_level_lib