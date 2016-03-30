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

    def select_all_table(db_table):
        #tname = type_objet[db_table];

        # select sur la base de données
        result = DAO.select_all(db_table)
        # nom des colonnes de la tables

        return BD.get_JSON(result)

    def select_from_activites(name_commune, number_equipment, activitie, practice, special) :
        # select sur la base de données

        #print("TEST2 : " + name_commune +", " + number_equipment +", " + activitie +", " + practice +", " + special)
        result = DAO.select_from_activites(name_commune, number_equipment, activitie, practice, special)
        # nom des colonnes de la tables

        #print(BD.get_JSON(result))
        return BD.get_JSON7(result)

    def select_from_equipements(activity_code) :
        # select sur la base de données
        resultEqu = DAO.select_from_equipements(activity_code)
        # nom des colonnes de la tables

        return BD.get_JSON(resultEqu)


    def select_from_installations(activity_code) :
        # select sur la base de données
        resultEqu = DAO.select_from_equipements(activity_code)
        # nom des colonnes de la tables

        tmp = str(resultEqu[1]).split(",")
        instal_number = tmp[7]

        resultIns = DAO.select_from_installations(instal_number)

        return BD.get_JSON(resultIns)


    def get_JSON(result) :
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

    def get_JSON7(result) :
        res = {}

        id1 = str(result[0][0]).replace("_", " ")
        id2 = str(result[0][1]).replace("_", " ")
        id3 = str(result[0][2]).replace("_", " ")
        id4 = str(result[0][3]).replace("_", " ")
        id5 = str(result[0][4]).replace("_", " ")
        id6 = str(result[0][5]).replace("_", " ")
        id7 = str(result[0][6]).replace("_", " ")

        # données de la table
        for row in result[1]:
            dict = {id1:row[0],
                    id2:row[1],
                    id3:row[2],
                    id4:row[3],
                    id5:row[4],
                    id6:row[5],
                    id7:row[6]}
            res[len(res)] = dict

        return res

    def remove_dot_CSV (CSV_file_name) :
        return CSV_file_name[:-4]

    def get_list_attribute (file_name) :
        return type_object[file_name].list_attribute


    def get_name_commune() :
        # select sur la base de données
        resultEqu = DAO.get_name_commune()
        # nom des colonnes de la tables


        res = {}
        id1 = str(resultEqu[0][0]).replace("_", " ")

        for row in resultEqu[1]:
            dict = {id1:row[0]}
            res[len(res)] = dict

        return (res)


    def get_name_activity() :
        # select sur la base de données
        resultEqu = DAO.get_name_activity()
        # nom des colonnes de la tables

        res = {}
        id1 = str(resultEqu[0][0]).replace("_", " ")

        for row in resultEqu[1]:
            dict = {id1:row[0]}
            res[len(res)] = dict

        return (res)


## Tests


#BD.create_tables()

#print(BD.select_from_activites("", -1, "", -1, -1))

#BD.get_name_commune()

#print(BD.select_from_installations(213704))
