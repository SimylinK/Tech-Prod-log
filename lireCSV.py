import csv
import os
from installations import Installation
from equipements import Equipement
from activites import Activite

# On associe les classes aux bons fichiers CSV
type_objet = {
    "installations.csv" : Installation,
    "equipements.csv" : Equipement,
    "activites.csv" : Activite
}

def lecture_CSV (nomFichier) : 
    # on récupère le fichier CSV
    fname =  os.path.dirname(os.path.abspath(__file__))+"/data/"+nomFichier
    file = open(fname, "r") #"r" pour "read" => indique ce qu'on fait avec le fichier

    liste = []

    try :
        reader = csv.reader(file) 
        # pour chaque ligne, on récupère les colonnes qui nous intéressent 
        for row in reader :
            liste.append(type_objet[nomFichier](row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]))
    finally :
        file.close() # on ferme le fichier

    for row in liste : 
        print (row)


## Tests
#lecture_CSV("installations.csv")
#lecture_CSV("equipements.csv")
#lecture_CSV("activite.csv")
