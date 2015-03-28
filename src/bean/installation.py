#!usr/bin/env python3

class Installation:


	def __init__(self, town, insee, zip_code, locality, numb_path, libelle_path, name_path,
				longitude, latitude, accessibility_nothing, accessibility_handi_moteur, accessibility_handi_sens,
				emprise_fonciere, gardiennee, multi_commune, nb_place_parking, nb_place_parking_handi, 
				particular_instalation, transport_metro, transport_bus, transport_tram, transport_train, transport_boat,
				other_transport, number_equipements, number_fiche_equipment_date_maj):
		
		self.town = town
		self.insee = insee
		self.zip_code = zip_code
		self.locality = locality
		self.numb_path = numb_path
		self.libelle_path = libelle_path
		self.name_path = name_path
		self.longitude = longitude
		self.latitude = latitude
		self.accessibility_nothing = accessibility_nothing
		self.accessibility_handi_moteur = accessibility_handi_moteur
		self.accessibility_handi_sens = accessibility_handi_sens
		self.emprise_fonciere = emprise_fonciere
		self.gardiennee = gardiennee
		self.multi_commune = multi_commune
		self.nb_place_parking = nb_place_parking
		self.nb_place_parking_handi = nb_place_parking_handi
		self.particular_instalation = particular_instalation
		self.transport_metro = transport_metro
		self.transport_bus = transport_bus
		self.transport_tram = transport_tram
		self.transport_train = transport_train
		self.transport_boat = transport_boat
		self.other_transport = other_transport
		self.number_equipements = number_equipements
		self.number_fiche_equipment_date_maj = number_fiche_equipment_date_maj

	def __str__(self):
		return self.town 
				

