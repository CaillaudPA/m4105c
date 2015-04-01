import cherrypy
import sqlite3

import os
import sys
from mako.template import Template
from mako.lookup import TemplateLookup


dir = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, dir + "/../../src/")

from MainInsertJSON import InsertAll


sys.path.insert(0, dir + "/../../src/dao")
from DB import DB


lookup = TemplateLookup(directories=['html'])

class ServiceCherrypy:
	"""Docstring for ServiceCherrypy"""
	@cherrypy.expose
	def index(self):
		"""Method who show the page index.html"""

		self.db = DB()
		activityTuple = self.db.select_all_from("activity")[1]
		tmpl = lookup.get_template("index.html")
		return (tmpl.render(activity=activityTuple))

	@cherrypy.expose
	def all_installation(self):
		"""Method who show the page allInstallation.html"""
		self.db = DB()
		installation_all = self.db.select_all_from("installations")
		tmpl = lookup.get_template("installation.html")
		return (tmpl.render(installation=installation_all))

	@cherrypy.expose
	def all_activity(self):
		"""Method who show the page allActivity.html"""
		self.db = DB()
		activity_all = self.db.select_all_from("activity")
		tmpl = lookup.get_template("activity.html")
		return (tmpl.render(activity=activity_all))

	@cherrypy.expose
	def all_equipment(self):
		"""Method who show the page allEquipment.html"""
		self.db = DB()
		activity_all = self.db.select_all_from("equipment")
		tmpl = lookup.get_template("equipment.html")
		return (tmpl.render(equipment=activity_all))


i = InsertAll()
cherrypy.quickstart(ServiceCherrypy())