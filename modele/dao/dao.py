import mysql.connector as sql #mysql.connector 1.1.6

class DAO:
    cursor = None #class attribute
    conn = None #cursor is supported by conn

    #Open db connexion
    def connect () :
        try :
            DAO.conn = sql.connect(host="infoweb",user="E145910Y",password="E145910Y", database="E145910Y", port=3306)
            DAO.cursor = DAO.conn.cursor()
        except ValueError :
            print("Connect error")

    #Close db connexion
    def close () :
        try :
            DAO.cursor.close();
        except ValueError:
            print("Close error")

    #create a table and fill it from a CSV file
    def create_table (table_name, list, list_attribute) :
        DAO.connect()

        #reinit the db
        request = "DROP TABLE IF EXISTS "+table_name+";"
        try :
            DAO.cursor.execute(request)
        except Error :
            print("Execute error")
            return

        #create the table
        request = "CREATE TABLE "+table_name+" ("

        #create a request with attributes and their types
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

        #fill the table
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
                    request = request + str(getattr(object, key)) + ","
            request = request[:-1] + ");"

            try :
                DAO.cursor.execute(request)
            except Error :
                print("Execute error")
                return

        DAO.conn.commit()
        DAO.close()

    #method to define a primary key in db table
    def define_PK (table_name, constraint_name, PK) :
        DAO.connect()
        DAO.cursor.execute("ALTER TABLE "+table_name+" ADD CONSTRAINT "+constraint_name+" PRIMARY KEY("+PK+");")
        DAO.close()

    #select query on all the table
    def select_all(table_name) :
        DAO.connect()

        request = "SELECT * FROM "+table_name+";"
        try :
            DAO.cursor.execute(request)
        except Error :
            print("Execute error")
            return

        field_names = [i[0] for i in DAO.cursor.description]

        rows = DAO.cursor.fetchall()

        result = [field_names]
        result.append(rows)

        DAO.close()
        return result

    #select query on activites (activities) table
    def select_from_activites(name_commune, number_equipment, activitie, practice, special) :
        DAO.connect()

        tmp = int(number_equipment)

        request = "SELECT activite_libelle, nom_commune, nb_equipements_identiques, dans_salle_spe, activite_pratiquee, activite_praticable, num_fiche_equipement FROM activites where "

        if name_commune is not "_" :
            request += "nom_commune = '" + name_commune + "' AND  "
        if tmp != -1 :
            request += "nb_equipements_identiques = " + number_equipment + " AND  "
        if activitie is not "_" :
            request += "activite_libelle = '" + activitie + "' AND  "
        if practice is not "_" :
            request += "activite_pratiquee = '" +  practice +"' AND  "
        if special is not "_" :
            request += "dans_salle_spe = '" + special + "' AND  "

        request = request[:-6] +";"

        try :
            DAO.cursor.execute(request)
        except Error :
            print("Execute error")
            return

        field_names = [i[0] for i in DAO.cursor.description]

        rows = DAO.cursor.fetchall()

        result = [field_names]
        result.append(rows)

        DAO.close()
        return result

    #select query on equipements (equipment) table
    def select_from_equipements(activity_code) :
        DAO.connect()

        request = "SELECT com_insee, com_lib, equipement_fiche, equipement_type_lib, eq_nom, ins_numero_install FROM equipements where equipement_id = " + str(activity_code) + ";"

        try :
            DAO.cursor.execute(request)
        except Error :
            print("Execute error")
            return

        field_names = [i[0] for i in DAO.cursor.description]

        rows = DAO.cursor.fetchall()

        result = [field_names]
        result.append(rows)

        DAO.close()
        return result

    #select query on installations table
    def select_from_installations(instal_number) :
        DAO.connect()

        request = "SELECT nom_commune, code_postal, nom_voie, numero_voie, longitude, latitude FROM installations where numero = " + str(instal_number) + ";"

        try :
            DAO.cursor.execute(request)
        except Error :
            print("Execute error")
            return

        field_names = [i[0] for i in DAO.cursor.description]

        rows = DAO.cursor.fetchall()

        result = [field_names]
        result.append(rows)

        DAO.close()
        return result

    #do the link between python types and SQL types
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

    #remove file format from a CSV name (so remove the .csv)
    def remove_dot_CSV (CSV_file_name) :
        return CSV_file_name[:-4]

    #get list of all communes in db
    def get_name_commune() :
        DAO.connect()

        request = "SELECT DISTINCT 	nom_commune FROM activites;"
        try :
            DAO.cursor.execute(request)
        except Error :
            print("Execute error")
            return

        field_names = [i[0] for i in DAO.cursor.description]

        rows = DAO.cursor.fetchall()

        result = [field_names]
        result.append(rows)

        DAO.close()
        return result

    #get list of all activites (activities) in db
    def get_name_activity() :
        DAO.connect()

        request = "SELECT DISTINCT 	activite_libelle FROM activites;"
        try :
            DAO.cursor.execute(request)
        except Error :
            print("Execute error")
            return

        field_names = [i[0] for i in DAO.cursor.description]

        rows = DAO.cursor.fetchall()

        result = [field_names]
        result.append(rows)

        DAO.close()
        return result
