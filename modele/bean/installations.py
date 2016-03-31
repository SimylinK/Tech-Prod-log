import csv
import os

class Installation:

    """Class defining an Installation with following attributes :
    - nom
    - numero
    - nom_commune
    - code_INSEE
    - code_postal
    - nom_lieu_dit
    - numero_voie
    - nom_voie
    - location"""
    
    #the attributes list will permit to know the type of datas added in the db
    list_attribute = {'nom' : 'str', 'numero' : 'int', 'nom_commune' : 'str', 'code_INSEE' : 'int', 'code_postal' : 'int', 'nom_lieu_dit' : 'str', 'numero_voie' : 'int', 'nom_voie' : 'str', 'longitude' : 'float', 'latitude' : 'float'}

    #generic constructor
    def __init__(self, row) :

        self.nom = row[0]
        self.numero = row[1]
        self.nom_commune = row[2]
        self.code_INSEE = row[3]
        self.code_postal = row[4]
        self.nom_lieu_dit = row[5]
        self.numero_voie = row[6]
        self.nom_voie = row[7]
        self.longitude = row[9]
        self.latitude = row[10]