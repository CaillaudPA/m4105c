#!usr/bin/env python3

from installation import Installation
from readInstallation import ReadInstallation
from creationDBinstallation import CreationDBinstallation
from equipment import Equipment
from readEquipment import ReadEquipment
from creationDBequipement import CreationDBequipment


allInstallation = ReadInstallation()
allInstallation.read_installation_method()

newDBinstallation = CreationDBinstallation()
newDBinstallation.creation_table_installation()

i = 1
for inst in allInstallation.collection_installation:
	newBDinstallation.ajout_installation(inst)
	i = i + 1
	print(i)

newBDinstallation.commitBD()

print ("BD installation ok")

allEquipment = ReadEquipment()
allEquipment.read_equipment_method()

newBDequipment = CreationBDequipment()
newBDequipment.creation_table_equipment()

i = 1
for equ in allEquipment.collectionEquipment:
	newBDequipment.ajout_equipment(equ)
	i = i + 1
	print(i)

newBDequipment.commit_db()