import csv
import os

class Equipement:

    """Class defining an Equipement with following attributes :
    - com_insee
    - com_lib
    - ins_numero_install
    - ins_nom
    - equipement_id
    - eq_nom
    - eq_nom_batiment
    - equipement_type_lib
    - equipement_fiche"""
    
    #the attributes list will permit to know the type of datas added in the db
    list_attribute = {'com_insee' : 'int', 'com_lib' : 'str', 'ins_numero_install' : 'int', 'ins_nom' : 'str', 'equipement_id' : 'int', 'eq_nom' : 'str', 'eq_nom_batiment' : 'str', 'equipement_type_lib' : 'str', 'equipement_fiche' : 'str'}
    
    #generic constructor
    def __init__(self, row) :

        self.com_insee = row[0]
        self.com_lib = row[1]
        self.ins_numero_install = row[2]
        self.ins_nom = row[3]
        self.equipement_id = row[4]
        self.eq_nom = row[5]
        self.eq_nom_batiment = row[6]
        self.equipement_type_lib = row[7]
        self.equipement_fiche = row[8]