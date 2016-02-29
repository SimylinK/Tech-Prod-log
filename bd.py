import mysql.connector as sql #mysql.connector 1.1.6
from lireCSV import CSV_read

def connect () :
    conn = sql.connect(host="infoweb",user="E145910Y",password="E145910Y", database="E145910Y", port=3306)
    cursor = conn.cursor()
    conn.close()

def create_table (CSV_file) :
    list = CSV_read(CSV_file)
    list_attribute = get_list_attribute(CSV_file)
    

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS"""+remove_dot_CSV(CSV_file)+""" ( """ + 
        for key, value in list_attribute :
            key + " " +  python_type_to_SQL(value)
        + """ ,); """)


    #print (list)



def define_PK (table_name, constraint_name, PK) :
    cursor.execute("ALTER TABLE "+table_name+" ADD CONSTRAINT "+constraint_name+" PRIMARY KEY("+PK+");")
    
def python_type_to_SQL(type) :
    if type is "int" :
        return "INTEGER DEFAULT NULL"
    elif type is "str" :
        return "VARCHAR(50) DEFAULT NULL"
    elif type is "bool" :
        return "BOOLEAN DEFAULT NULL"
    else :
        print ("Problème de type")

def remove_dot_CSV (CSV_file_name) :
    return CSV_file_name[:-4]



print (create_table("installations.csv"))
