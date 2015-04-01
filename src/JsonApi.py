import urllib2
import sys
import json

"""
	Methode de recherche avec l'api 
"""
def requeteApiInstallation(filtre,donnee):
	try:
		req = urllib2.urlopen('http://data.paysdelaloire.fr/api/publication/23440003400026_J335/installations_table/content?filter={''"'+filtre+'"'':{"$eq":''"'+donnee+'"''}}')
		html = json.loads(req.read().decode(req.info().getparam('charset') or 'utf-8'))
		data = html["data"]
		cpt = 0
		for line in data:
			numero = (data[cpt]["InsNumeroInstall"])
			nom = (data[cpt]["geo"]["name"]).encode('utf8',errors='ignore')
			cp = (data[cpt]["InsCodePostal"])
			ville = (data[cpt]["ComLib"]).encode('utf8',errors='ignore')
			cpt = cpt +1
			"""Affichage des resultats"""
			print("|--------------------------------|")
			print("Numero installation: " + numero)
			print("Nom : " + nom)
			print("Code Postale : " + cp)
			print("Commune : " + ville)
		print("|--------------------------------|")	
	except Exception as e:
		print("Probleme dans la requete avec l'api ")
		print(e)

def requetteApiEquipement(filtre,donnee):
	try:

		req = urllib2.urlopen('http://data.paysdelaloire.fr/api/publication/23440003400026_J336/equipements_table/content?filter={''"'+filtre+'"'':{"$eq":''"'+donnee+'"''}}')
		html = json.loads(req.read().decode(req.info().getparam('charset') or 'utf-8'))
		print("ok")
		data = html["data"]
		cpt = 0

		for line in data:
			numero = (data[cpt]["InsNumeroInstall"])
			nom = (data[cpt]["InsNom"]).encode('utf8',errors='ignore')
			nomEquipment = (data[cpt]["EquNom"])
			cp = (data[cpt]["ComInsee"])
			ville = (data[cpt]["ComLib"]).encode('utf8',errors='ignore')
			cpt = cpt +1
			
			print("|--------------------------------|")
			print("Numero : " + numero)
			print("Nom : " + nom)
			print("Nom equipement : " + nomEquipment)
			print("Code Postale : " + cp)
			print("Ville : " + ville)
		print("|--------------------------------|")
	except Exception as e:		
		print("Probleme dans la requete avec l'api ")
		print(e)

def requetteApiActivity(filtre,donnee):
	try:

		req = urllib2.urlopen('http://data.paysdelaloire.fr/api/publication/23440003400026_J334/equipements_activites_table/content ?filter={''"'+filtre+'"'':{"$eq":''"'+donnee+'"''}}')
		html = json.loads(req.read().decode(req.info().getparam('charset') or 'utf-8'))
		print("ok")
		data = html["data"]
		cpt = 0

		for line in data:
			insee = (data[cpt]["ComInsee"]).encode('utf8',errors='ignore')
			commune = (data[cpt]["ComLib"]).encode('utf8',errors='ignore')
			id_equ = (data[cpt]["EquipementId"]).encode('utf8',errors='ignore')
			code_act = (data[cpt]["ActCode"]).encode('utf8',errors='ignore')
			lib_act = (data[cpt]["ActLib"]).encode('utf8',errors='ignore')
			level_act = (data[cpt]["ActNivLib"]).encode('utf8',errors='ignore')
			
			cpt = cpt +1
			
			print("|--------------------------------|")
			print("Code INSEE : " + insee)
			print("Commune : " + commune)
			print("ID equipement : " + id_equ)
			print("Code activite : " + code_act)
			print("Libelle activite : " + lib_act)
			print("Niveau effectivement pratique : " + level_act)
		print("|--------------------------------|")
	except Exception as e:
		print("Probleme dans la requete avec l'api ")
		print(e)

"""print("-----------------Requete ville--------------------------")
requeteApiInstallation("ComLib","Bournezeau")
print("-----------------Requete code Postale-------------------")
requeteApiInstallation("InsCodePostal","85480")
print("-----------------Requete Metro--------------------------")
requeteApiInstallation("InsTransportMetro","Oui")
print("-----------------Requete Multi-commune------------------")
requeteApiInstallation("InsMultiCommune","Oui")"""
#requetteApiActivity("ComLib", "Nantes")
#requeteApiInstallation("ComLib","Bournezeau")

while 1:
	print("\n|-------------------------Recherche API-------------------------|")
	print("\nInstallation : 1 || Equipement : 2 || Activite : 3 || Quitter : 4")
	choix = raw_input("Choix : ")
	if(choix == "1"):
		filtre = raw_input("Attribut : ")
		donnee = raw_input("Donnee : ")
		requeteApiInstallation(filtre,donnee)
	elif(choix == "2"):
		filtre = raw_input("Attribut : ")
		donnee = raw_input("Donnee : ")
		requetteApiEquipement(filtre,donnee)
	elif(choix == "3"):
		filtre = raw_input("Attribut : ")
		donnee = raw_input("Donnee : ")
		requetteApiActivity(filtre,donnee)
	elif(choix == "4"):
		sys.exit()
	else:
		print("\nChoix non reconnue\n")