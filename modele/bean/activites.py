import csv
import os

class Activite: 

    """Class defining an Activite with following attributes :
    - code_INSEE
    - nom_commune
    - num_fiche_equipement
    - nb_equipements_identiques
    - activite_code
    - activite_libelle
    - activite_praticable
    - activite_pratiquee
    - dans_salle_spe"""

    #the attributes list will permit to know the type of datas added in the db
    list_attribute = {'code_INSEE' : 'int', 'nom_commune' : 'str', 'num_fiche_equipement' : 'int',     'nb_equipements_identiques' : 'int', 'activite_code' : 'int', 'activite_libelle' : 'str', 'activite_praticable' : 'str', 'activite_pratiquee' : 'str', 'dans_salle_spe' : 'str'}

    #generic constructor
    def __init__(self, row) :
        self.code_INSEE = row[0]
        self.nom_commune = row[1]
        self.num_fiche_equipement = row[2]
        self.nb_equipements_identiques = row[3]
        self.activite_code = row[4]
        self.activite_libelle = row[5]
        self.activite_praticable = row[6]
        self.activite_pratiquee = row[7]
        self.dans_salle_spe = row[8]
