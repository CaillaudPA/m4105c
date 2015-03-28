#!usr/bin/env python3

from bean.installation import Installation
from readInstallation import ReadInstallation
from creationDBinstallation import CreationDBinstallation
from equipment import Equipment
from readEquipment import ReadEquipment
from creationDBequipement import CreationDBequipment
from activity import Activity
from readActivity import ReadActivity
from creationDBactivity import CreationDBactivity

from DB import DB



allInstallation = ReadInstallation()
allInstallation.read_installation_method()

newDB = DB()
newDB.creation_table_installation()

i = 1
for inst in allInstallation.collection_installation:
	newDB.add_installation(inst)
	i = i + 1
	print(i)

newDB.commit_db()

print ("DB installation ok")

allEquipment = ReadEquipment()
allEquipment.read_equipment_method()

newDB.creation_table_equipment()

i = 1
for equ in allEquipment.collection_equipment:
	newDB.add_equipment(equ)
	i = i + 1
	print(i)

newDB.commit_db()

print ("DB equipment ok")

all_activity = ReadActivity()
all_activity.read_activity_method()


newDB.creation_table_activity()

i = 1
for act in all_activity.collection_activity:
	newDB.add_activity(act)
	i = i + 1
	print (i)

newDB.commit_db()

print("DB activity ok")