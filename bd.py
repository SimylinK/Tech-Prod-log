import mysql.connector as sql #mysql.connector 1.1.6
from lireCSV import lecture_CSV

# se connecter à la base sur phpMyAdmin puis faire des create table à l'aide des données récup dans les CSV (utilisation de lireCSV.py)



def connect () :
    conn = sql.connect(host="infoweb",user="E145910Y",password="E145910Y", database="E145910Y", port=3306)
    cursor = conn.cursor()
    conn.close()

def create_table (CSV_file) :
    list = lecture_CSV(CSV_file)
    
    for row in list :
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS"""+""" CSV_file (
            """+create_field(row[0])+""",
            """+create_field(row[1])+""",
            """+create_field(row[2])+""",
            """+create_field(row[3])+""",
            """+create_field(row[4])+""",
            """+create_field(row[5])+""",
            """+create_field(row[6])+""",
            """+create_field(row[7])+""",
            """+create_field(row[8])+"""
        );
        """)

def define_PK (table_name, constraint_name, PK) :
    cursor.execute("ALTER TABLE "+table_name+" ADD CONSTRAINT "+contraint_name+" PRIMARY KEY("+PK+");")
    
def create_field(row) :
    


        id int(5) NOT NULL AUTO_INCREMENT,
        name varchar(50) DEFAULT NULL,
        age INTEGER DEFAULT NULL,

def remove_CSV_extension(string) :
    return string[:-4]

