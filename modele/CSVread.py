import csv
import os
from bean.installations import Installation
from bean.equipements import Equipement
from bean.activites import Activite

#link classes with CSV files
type_object = {
    "installations.csv" : Installation,
    "equipements.csv" : Equipement,
    "activites.csv" : Activite
}

#read a CSV
def CSV_read (file_name) : 
    #get CSV file
    fname =  os.path.dirname(os.path.abspath(__file__))+"/data/"+file_name
    file = open(fname, "r") 
    list = []

    try :
        reader = csv.reader(file) 
        #for each row, we get columns we need 
        for row in reader :
            list.append(type_object[file_name](row))
    finally :
        file.close() #close the file

    list = list[1:]
    return list

#get table attributes list
def get_list_attribute (file_name) :
    return type_object[file_name].list_attribute
