import mysql.connector as sql #mysql.connector 1.1.6

class DAO:
    cursor = None # variable de classe
    conn = None # car cursor repose sur conn

    #Ouvre la connexion
    def connect () :
        try :
            DAO.conn = sql.connect(host="infoweb",user="E145910Y",password="E145910Y", database="E145910Y", port=3306)
            DAO.cursor = DAO.conn.cursor()
        except ValueError :
            print("Connect error")

    #Fermr la connexion
    def close () :
        try :
            DAO.cursor.close();
        except ValueError:
            print("Close error")

    #Permet de créer une table et de la remplir de données à partir d'un CSV
    def create_table (table_name, list, list_attribute) :
        DAO.connect()

        #On réinitialise la base de donnée
        request = "DROP TABLE IF EXISTS "+table_name+";"
        try :
            DAO.cursor.execute(request)
        except Error :
            print("Execute error")
            return

        #On créé la table
        request = "CREATE TABLE "+table_name+" ("

        for key, value in list_attribute.items() :
            request = request + (key + " " +  DAO.python_type_to_SQL(value) + ",")

        request = request[:-1]
        request = request + ");"

        try :
            DAO.cursor.execute(request)
        except Error :
            print("Execute error")
            return

        list_keys = []
        for key in list_attribute.keys() :
            list_keys.append(key)

        #On remplit la table à partir du fichier csv
        pre_request  = "INSERT INTO " +  table_name + " ("

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
                DAO.cursor.execute(request)
            except Error :
                print("Execute error")
                return
            print(request)

        DAO.conn.commit()
        DAO.close()

    def define_PK (table_name, constraint_name, PK) :
        DAO.connect()
        DAO.cursor.execute("ALTER TABLE "+table_name+" ADD CONSTRAINT "+constraint_name+" PRIMARY KEY("+PK+");")
        DAO.close()


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
