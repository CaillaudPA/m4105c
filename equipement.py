class equipement:
	'''
		This class represent an installation
		The 10 attribut are String

	'''


	def __init__(self, insee, town, numbEquip, numbEquipIdentical,
			    codeActi, wordingActi, actiPracticable, roomSpe, levelPractice):
		self.insee = insee
		self.town = town
		self.numbEquip = numbEquip
		self.numbEquipIdentical = numbEquipIdentical
		self.codeActi = codeActi
		self.wordingActi = wordingActi
		self.actiPracticable = actiPracticable
		self.roomSpe = roomSpe
		self.levelPractice = levelPractice

	def __str__(self):
		return "Code Insee : " + self.insee + ", Commune : " + self.town