#!usr/bin/env python3

from installation import Installation
from readInstallation import ReadInstallation
from creationDBinstallation import CreationDBinstallation
from equipment import Equipment
from readEquipment import ReadEquipment
from creationDBequipement import CreationDBequipment
from activity import Activity
from readActivity import ReadActivity
from creationDBactivity import CreationDBactivity



allInstallation = ReadInstallation()
allInstallation.read_installation_method()

newDBinstallation = CreationDBinstallation()
newDBinstallation.creation_table_installation()

i = 1
for inst in allInstallation.collection_installation:
	newDBinstallation.add_installation(inst)
	i = i + 1
	print(i)

newDBinstallation.commit_db()

print ("DB installation ok")

allEquipment = ReadEquipment()
allEquipment.read_equipment_method()

newDBequipment = CreationDBequipment()
newDBequipment.creation_table_equipment()

i = 1
for equ in allEquipment.collection_equipment:
	newDBequipment.add_equipment(equ)
	i = i + 1
	print(i)

newDBequipment.commit_db()

print ("DB equipment ok")

all_activity = ReadActivity()
all_activity.read_activity_method()

new_db_activity = CreationDBactivity()
new_db_activity.creation_table_activity()

i = 1
for act in all_activity.collection_activity:
	new_db_activity.add_activity(act)
	i = i + 1
	print (i)

new_db_activity.commit_db()

print("DB activity ok")