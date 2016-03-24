import csv
import os
from bean.installations import Installation
from bean.equipements import Equipement
from bean.activites import Activite

# On associe les classes aux bons fichiers CSV
type_object = {
    "installations.csv" : Installation,
    "equipements.csv" : Equipement,
    "activites.csv" : Activite
}

def CSV_read (file_name) : 
    # on récupère le fichier CSV
    fname =  os.path.dirname(os.path.abspath(__file__))+"/data/"+file_name
    file = open(fname, "r") #"r" pour "read" => indique ce qu'on fait avec le fichier

    list = []

    try :
        reader = csv.reader(file) 
        # pour chaque ligne, on récupère les colonnes qui nous intéressent 
        for row in reader :
            list.append(type_object[file_name](row))
    finally :
        file.close() # on ferme le fichier

    # afficher le type de row :
    #print(type(row))
    
    """
    for row in list : 
        print (row.nom)
    """
    
    list = list[1:]
    return list


def get_list_attribute (file_name) :
    return type_object[file_name].list_attribute
    
    
    
    
## Tests
#CSV_read("installations.csv")
#CSV_read("equipements.csv")
#CSV_read("activite.csv")
