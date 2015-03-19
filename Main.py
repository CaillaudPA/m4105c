#!usr/bin/env python3

from installation import Installation
from readInstallation import ReadInstallation
from CreationBDinstallation import CreationBDinstallation
from equipement import Equipement

allInstallation = ReadInstallation()
allInstallation.readInstallationMethod()

newBDinstallation = CreationBDinstallation()
newBDinstallation.creationTableInstallation()

i = 1
for inst in allInstallation.collectionInstallation:
	newBDinstallation.ajoutInstallation(inst)
	i = i + 1
	print(i)

newBDinstallation.commitBD()

print ("BD installation ok")



