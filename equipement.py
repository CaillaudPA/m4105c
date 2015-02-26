class Equipement:
	'''
		This class represent an installation
		The 10 attribut are String

	'''


	def __init__(self, insee, town, equipementTypeLib, equipementFiche, familleFicheLib):
		self.insee = insee
		self.town = town
		self.equipTypeLib = equipementTypeLib
		self.equipFiche = equipementFiche
		self.familyFicheLib = familleFicheLib
		

	def __str__(self):
		return "Code Insee : " + self.insee + ", Commune : " + self.town