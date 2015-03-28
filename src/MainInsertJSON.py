#!usr/bin/env python3

from bean.installation import Installation
from util.readInstallation import ReadInstallation

from bean.equipment import Equipment
from util.readEquipment import ReadEquipment

from bean.activity import Activity
from util.readActivity import ReadActivity


from dao.DB import DB

class InsertAll():


	"""docstring for InsertALl"""
	def __init__(self):
		
		self.new_db = DB()		
		allInstallation = ReadInstallation()
		allInstallation.read_installation_method()

		
		self.new_db.creation_table_installation()

		i = 1
		for inst in allInstallation.collection_installation:
			self.new_db.add_installation(inst)
			i = i + 1
			print(i)

		self.new_db.commit_db()

		print ("DB installation ok")

		allEquipment = ReadEquipment()
		allEquipment.read_equipment_method()

		self.new_db.creation_table_equipment()

		i = 1
		for equ in allEquipment.collection_equipment:
			self.new_db.add_equipment(equ)
			i = i + 1
			print(i)

		self.new_db.commit_db()

		print ("DB equipment ok")

		all_activity = ReadActivity()
		all_activity.read_activity_method()


		self.new_db.creation_table_activity()

		i = 1
		for act in all_activity.collection_activity:
			self.new_db.add_activity(act)
			i = i + 1
			print (i)

		self.new_db.commit_db()

		print("DB activity ok")

