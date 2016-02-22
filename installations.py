import csv
import os

class Installation: # Définition de la classe Installation

    """Classe définissant une Installation caractérisée par :
    - nom
    - numero
    - nom_commune
    - code_INSEE
    - code_postal
    - nom_lieu_dit
    - numero_voie
    - nom_voie
    - location"""

    # constructeur
    def __init__(self, nom = "default", numero = -1, nom_commune = "default", code_INSEE = -1, code_postal = -1, nom_lieu_dit = "default", numero_voie = -1, nom_voie = "default", location = [-1][-1]) :

        self.nom = nom
        self.numero = numero
        self.nom_commune = nom_commune
        self.code_INSEE = code_INSEE
        self.code_postal = code_postal
        self.nom_lieu_dit = nom_lieu_dit
        self.numero_voie = numero_voie
        self.nom_voie = nom_voie
        self.location = location

"""

## Test du constructeur
        
test_install1 = Installation()
print(test_install1.nom)
print(str(test_install1.location)) #str : équivalent de toString() en Java

test_install2 = Installation("nom")
print(test_install2.nom)
   
"""     

## Lecture du CSV

def test_lecture_CSV () : 
    # on récupère le fichier CSV
    fname =  os.path.dirname(os.path.abspath(__file__))+"/data/installations.csv"
    file = open(fname, "r") #"r" pour "read" => indique ce qu'on fait avec le fichier

    liste = []

    try :
        reader = csv.reader(file) 
        # pour chaque ligne, on récupère les colonnes qui nous intéressent pour créer des Installation
        for row in reader :
            liste.append(Installation(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]))
    finally :
        file.close() # on ferme le fichier

    for row in liste : 
        print (row.nom)


#test_lecture_CSV()