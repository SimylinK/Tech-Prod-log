import os.path
import sys
#pour revenir à un niveau au-dessus dans le path (on fait un chemin absolu de celui où on est et on revient en plus un cran en arrière puis dans modele avec ../modele)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../modele")))
from bottle import route, run, template, static_file, post, get, response
import json
from bd import BD

#DOC : http://bottlepy.org/docs/dev/index.html
'''#Exemple de la doc
@route('/hello/<name>')
def index(name):
    return template('<b>Hello {{name}}</b>!', name=name)
'''

#pour atteindre le fichier index.html dans le dossier vue
@route('/<filepath:path>')
def index(filepath):
    return static_file(filepath,root="../vue")

##Import des tables

'''
@route('/create/<table_name>')
def import_table(table_name) :
    BD.create_table(table_name+".csv")
'''  
    
@route('/create/installations')
def import_table() :
    #BD.create_table("installations.csv")
    return template('<b>Hello</b>!')
    


@route('/display/<table_name>')
def view_table(table_name):
    #response.headers['Content-type'] = 'application/json'
    res = json.dumps(BD.get_json_from_db(table_name))
    return res


run(host='localhost', port=8080) # après avoir lancé le script, aller à l'adresse http://localhost:8080/index.html
