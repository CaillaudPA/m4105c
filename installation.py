class Installation:


	def __init__(self, town, insee, zipCode, locality, numbPath, libellePath, namePath,
				longitude, latitude, accessibilityNothing, accessibiliteHandiMoteur, accessibiliteHandiSens,
				empriseFonciere, gardiennee, multiCommune, nbPlaceParking, nbPlaceParkingHandi, 
				particularInstalation, transportMetro, transportBus, transportTram, transportTrain, transportBoat,
				otherTransport, number_Equipements, number_FicheEquipemenDateMaj):
		
		self.town = town
		self.insee = insee
		self.zipCode = zipCode
		self.locality = locality
		self.numbPath = numbPath
		self.libellePath = libellePath
		self.namePath = namePath
		self.longitude = longitude
		self.latitude = latitude
		self.accessibilityNothing = accessibilityNothing
		self.accessibiliteHandiMoteur = accessibiliteHandiMoteur
		self.accessibiliteHandiSens = accessibiliteHandiSens
		self.empriseFonciere = empriseFonciere
		self.gardiennee = gardiennee
		self.multiCommune = multiCommune
		self.nbPlaceParking = nbPlaceParking
		self.nbPlaceParkingHandi = nbPlaceParkingHandi
		self.particularInstalation = particularInstalation
		self.transportMetro = transportMetro
		self.transportBus = transportBus
		self.transportTram = transportTram
		self.transportTrain = transportTrain
		self.transportBoat = transportBoat
		self.otherTransport = otherTransport
		self.number_Equipements = number_Equipements
		self.number_FicheEquipemenDateMaj = number_FicheEquipemenDateMaj

	def __str__(self):
		return self.gardiennee
		

