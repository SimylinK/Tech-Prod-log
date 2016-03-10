import mysql.connector as sql #mysql.connector 1.1.6
from lireCSV import CSV_read
from lireCSV import get_list_attribute

class BD:
    cursor = None # variable de classe
    conn = None # car cursor repose sur conn

    def connect () :
        try :
            BD.conn = sql.connect(host="infoweb",user="E145910Y",password="E145910Y", database="E145910Y", port=3306)
            BD.cursor = BD.conn.cursor()
        except ValueError :
            print("Connect error")
    
    def close () :
        try :
            BD.cursor.close();
        except ValueError:
            print("Close error")
    
    def create_table (CSV_file) :
        list = CSV_read(CSV_file)
        list_attribute = get_list_attribute(CSV_file)
        
        #On réinitialise la base de donnée
        request = "DROP TABLE "+BD.remove_dot_CSV(CSV_file)+";"
        try :
            BD.cursor.execute(request)
        except ValueError :
            print("Execute error")
    
        #On créé la table
        request = "CREATE TABLE "+BD.remove_dot_CSV(CSV_file)+" ("
        
        for key, value in list_attribute.items() :
            request = request + (key + " " +  BD.python_type_to_SQL(value) + ",")
        
        request = request[:-1]
        request = request + ");"
            
        try :
            BD.cursor.execute(request)
        except ValueError :
            print("Execute error")
        
        list_keys = []
        for key in list_attribute.keys() :
            list_keys.append(key)
        
        #On remplit la table à partir du fichier csv
        pre_request  = "INSERT INTO " +  BD.remove_dot_CSV(CSV_file) + " ("
            
        for key in list_keys :
            pre_request = pre_request + key + ","
        pre_request = pre_request[:-1] + ") VALUES ("
        
        
        for object in list :
            request = pre_request
            for key in list_keys :
                if isinstance(getattr(object, key), str):
                    tmp_string = str(getattr(object, key))
                    tmp_string = tmp_string.replace('"', '""')
                    request = request + "\"" + tmp_string + "\"" + ","
                else :
                    #Je crois qu'on ne rentre pas ici mais c'est pas grave
                    request = request + str(getattr(object, key)) + ","
            request = request[:-1] + ");"   
            
            try :
                BD.cursor.execute(request)
            except ValueError :
                print("Execute error")
            print(request)
            

    def define_PK (table_name, constraint_name, PK)         BD.cursor.execute("ALTER TABLE "+table_name+" ADD CONSTRAINT "+constraint_name+" PRIMARY KEY("+PK+");")

        
    def python_type_to_SQL(type) :
        if type is "int" :
            return "INTEGER DEFAULT NULL"
        elif type is "str" :
            return "VARCHAR(50) DEFAULT NULL"
        elif type is "bool" :
            return "BOOLEAN DEFAULT NULL"
        elif type is "float" :
            return "FLOAT DEFAULT NULL"
        else :
            print ("Problème de type")
    
    def remove_dot_CSV (CSV_file_name) :
        return CSV_file_name[:-4]
        

## Tests

BD.connect()
BD.create_table("installations.csv")
BD.create_table("equipements.csv")
BD.create_table("activites.csv")
#todo : définir clé primaire
BD.close()