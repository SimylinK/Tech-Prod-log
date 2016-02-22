import csv
import os

class Equipement: # Définition de la classe Equipement

    """Classe définissant une Equipement caractérisée par :
    - com_insee
    - com_lib
    - ins_numero_install
    - ins_nom
    - equipement_id
    - eq_nom
    - eq_nom_batiment
    - equipement_type_lib
    - equipement_fiche"""

    # constructeur
    def __init__(self, com_insee = -1, com_lib = "default", ins_numero_install = -1, ins_nom = "default", equipement_id = -1, eq_nom = "default", eq_nom_batiment = "default", equipement_type_lib = "default", equipement_fiche = "default") :

        self.com_insee = com_insee
        self.com_lib = com_lib
        self.ins_numero_install = ins_numero_install
        self.ins_nom = ins_nom
        self.equipement_id = equipement_id
        self.eq_nom = eq_nom
        self.eq_nom_batiment = eq_nom_batiment
        self.equipement_type_lib = equipement_type_lib
        self.equipement_fiche = equipement_fiche


## Lecture du CSV

def test_lecture_CSV () : 
    # on récupère le fichier CSV
    fname =  os.path.dirname(os.path.abspath(__file__))+"/data/equipements.csv"
    file = open(fname, "r") #"r" pour "read" => indique ce qu'on fait avec le fichier

    liste = []

    try :
        reader = csv.reader(file) 
        # pour chaque ligne, on récupère les colonnes qui nous intéressent pour créer des Equipement
        for row in reader :
            liste.append(Equipement(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]))
    finally :
        file.close() # on ferme le fichier

    for row in liste : 
        print (row.eq_nom)


#test_lecture_CSV()