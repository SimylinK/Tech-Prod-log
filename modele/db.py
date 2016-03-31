import mysql.connector as sql #mysql.connector 1.1.6

from CSVread import CSV_read
from CSVread import get_list_attribute
from CSVread import type_object
from dao.dao import DAO

from bean.activites import Activite
from bean.installations import Installation
from bean.equipements import Equipement

class DB:

    #create all tables from CSV files
    def create_tables () :
        tables = ["installations.csv", "equipements.csv", "activites.csv"] #get CSV files
        for table in tables :
            list = CSV_read(table)
            list_attribute = DB.get_list_attribute(table) #link with tables attributes lists
            name = DB.remove_dot_CSV(table) #removing .csv
            DAO.create_table(name, list, list_attribute)


    #create a table from a CSV file
    def create_table (table) :
        list = CSV_read(table)
        list_attribute = DB.get_list_attribute(table) #link with table attributes list
        name = DB.remove_dot_CSV(table) #removing .csv
        DAO.create_table(name, list, list_attribute)


    #select query on all table, depending on the table name
    def select_all_table(db_table):
        result = DAO.select_all(db_table)
        return DB.get_JSON(result)


    #select query on the activites table
    def select_from_activites(name_commune, number_equipment, activitie, practice, special) :
        result = DAO.select_from_activites(name_commune, number_equipment, activitie, practice, special)
        return DB.get_JSON7(result)


    #select query on the equipements table
    def select_from_equipements(activity_code) :
        #get the equipment thanks to the activity_code given by activites table
        resultEqu = DAO.select_from_equipements(activity_code)
        return DB.get_JSON(resultEqu)


    #select query on the installations table
    def select_from_installations(activity_code) :
        #get equipement table
        resultEqu = DAO.select_from_equipements(activity_code)

        #get instal_number (num_install in db) from equipement table to get the installation
        tmp = str(resultEqu[1]).split(",")
        instal_number = tmp[5]
        instal_number = str(instal_number)[:-2]

        resultIns = DAO.select_from_installations(instal_number)
        return DB.get_JSON(resultIns)


    #return a string that can be used with json.dumps in order to create a good JSON file
    def get_JSON(result) :
        res = {}

        id1 = str(result[0][0]).replace("_", " ")
        id2 = str(result[0][1]).replace("_", " ")
        id3 = str(result[0][2]).replace("_", " ")
        id4 = str(result[0][3]).replace("_", " ")
        id5 = str(result[0][4]).replace("_", " ")
        id6 = str(result[0][5]).replace("_", " ")

        #get tables data
        for row in result[1]:
            dict = {id1:row[0],
                    id2:row[1],
                    id3:row[2],
                    id4:row[3],
                    id5:row[4],
                    id6:row[5]}
            res[len(res)] = dict

        return res


    #same method but only used for select_from_activites that have 7 objects to display
    def get_JSON7(result) :
        res = {}

        id1 = str(result[0][0]).replace("_", " ")
        id2 = str(result[0][1]).replace("_", " ")
        id3 = str(result[0][2]).replace("_", " ")
        id4 = str(result[0][3]).replace("_", " ")
        id5 = str(result[0][4]).replace("_", " ")
        id6 = str(result[0][5]).replace("_", " ")
        id7 = str(result[0][6]).replace("_", " ")

        #get tables data
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

    #remove file format from a CSV name (so remove the .csv)
    def remove_dot_CSV (CSV_file_name) :
        return CSV_file_name[:-4]


    #getter of a list attributes table
    def get_list_attribute (file_name) :
        return type_object[file_name].list_attribute


    #get list of all communes in db
    def get_name_commune() :
        resultEqu = DAO.get_name_commune()

        res = {}
        #replacing underscores by space for a better displaying
        id1 = str(resultEqu[0][0]).replace("_", " ")

        #fill the list with db datas
        for row in resultEqu[1]:
            dict = {id1:row[0]}
            res[len(res)] = dict

        return (res)


    #get list of all activites (activities) in db
    def get_name_activity() :
        resultEqu = DAO.get_name_activity()

        res = {}
        #replacing underscores by space for a better displaying
        id1 = str(resultEqu[0][0]).replace("_", " ")

        #fill the list with db datas
        for row in resultEqu[1]:
            dict = {id1:row[0]}
            res[len(res)] = dict

        return (res)
