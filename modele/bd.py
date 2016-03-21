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

    def create_table (table) :

        list = CSV_read(table)
        list_attribute = BD.get_list_attribute(table)
        name = BD.remove_dot_CSV(table)
        DAO.create_table(name, list, list_attribute)

    def get_json_from_db(db_table):
        #tname = type_objet[db_table];

        # select sur la base de données
        result = DAO.db_select(db_table)
        # nom des colonnes de la tables
        res = {}

        id1 = str(result[0][0]).replace("_", " ")
        id2 = str(result[0][1]).replace("_", " ")
        id3 = str(result[0][2]).replace("_", " ")
        id4 = str(result[0][3]).replace("_", " ")
        id5 = str(result[0][4]).replace("_", " ")
        id6 = str(result[0][5]).replace("_", " ")

        # données de la table
        for row in result[1]:
            dict = {id1:row[0],
                    id2:row[1],
                    id3:row[2],
                    id4:row[3],
                    id5:row[4],
                    id6:row[5]}
            res[len(res)] = dict

        return res

    def remove_dot_CSV (CSV_file_name) :
        return CSV_file_name[:-4]

    def get_list_attribute (file_name) :
        return type_object[file_name].list_attribute


## Tests


#BD.create_tables()
