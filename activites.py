import csv
import os

class Activite: # Définition de la classe Activite

    """Classe définissant une Activite caractérisée par :
    - code_INSEE
    - nom_commune
    - num_fiche_equipement
    - nb_equipements_identiques
    - activite_code
    - activite_libelle
    - activite_praticable
    - activite_pratiquee
    - dans_salle_spe"""
    self.list_attribute{'code_INSEE' : 'int', 'nom_commune' : 'str', 'num_fiche_equipement' : 'int', 
        'nb_equipements_identiques' : 'int', 'activite_code' : 'int', 'activite_libelle' : 'str', 
        'activite_praticable' : 'bool', 'activite_pratiquee' : 'bool', 'dans_salle_spe' : 'bool'}

    # constructeur
    def __init__(self, code_INSEE = -1, nom_commune = "default", num_fiche_equipement = -1, nb_equipements_identiques = -1, activite_code = -1, activite_libelle = "default", activite_praticable = False, activite_pratiquee = False, dans_salle_spe = False) :
        self.code_INSEE = code_INSEE
        self.nom_commune = nom_commune
        self.num_fiche_equipement = num_fiche_equipement
        self.nb_equipements_identiques = nb_equipements_identiques
        self.activite_code = activite_code
        self.activite_libelle = activite_libelle
        self.activite_praticable = activite_praticable
        self.activite_pratiquee = activite_pratiquee
        self.dans_salle_spe = dans_salle_spe    


## Lecture du CSV

def CSV_read_test () : 
    # on récupère le fichier CSV
    fname =  os.path.dirname(os.path.abspath(__file__))+"/data/activites.csv"
    file = open(fname, "r") #"r" pour "read" => indique ce qu'on fait avec le fichier

    list = []

    try :
        reader = csv.reader(file) 
        # pour chaque ligne, on récupère les colonnes qui nous intéressent pour créer des Activite
        for row in reader :
            list.append(Activite(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]))
    finally :
        file.close() # on ferme le fichier

    for row in list : 
        print (row.activite_libelle)


#CSV_read_test()