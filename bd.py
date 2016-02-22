import mysql.connector as sql #mysql.connector 1.1.6
from lireCSV import lecture_CSV

# se connecter à la base sur phpMyAdmin puis faire des create table à l'aide des données récup dans les CSV (utilisation de lireCSV.py)

conn = sql.connect(host="infoweb", user="E145910Y",password="E145910Y", database="E145910Y", port=3306)
cursor = conn.cursor()


conn.close()

def remove_CSV_extension(string) :
    return string[:-4]