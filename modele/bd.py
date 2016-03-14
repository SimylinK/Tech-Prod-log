import mysql.connector as sql #mysql.connector 1.1.6

from lireCSV import CSV_read
from lireCSV import get_list_attribute
from lireCSV import type_object
from dao.dao import DAO

from bean.activites import Activite
from bean.installations import Installation
from bean.equipements import Equipement



class BD:
    
    def create_tables () :
        
        tables = ["installations.csv", "equipements.csv", "activites.csv"]
        
        for table in tables :
            list = CSV_read(table)
            list_attribute = BD.get_list_attribute(table)
            name = BD.remove_dot_CSV(table)
            DAO.create_table(name, list, list_attribute)

    
    def remove_dot_CSV (CSV_file_name) :
        return CSV_file_name[:-4]
    
    def get_list_attribute (file_name) :
        return type_object[file_name].list_attribute
        

## Tests


#BD.create_tables()