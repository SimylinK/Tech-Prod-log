import os
import os.path
import sys
#pour revenir à un niveau au-dessus dans le path (on fait un chemin absolu de celui où on est et on revient en plus un cran en arrière puis dans modele avec ../modele)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../modele")))
import bottle
from bottle import route, run, template, static_file, post, get, response, redirect
import json
from bd import BD

#DOC : http://bottlepy.org/docs/dev/index.html
'''#Exemple de la doc
@route('/hello/<name>')
def index(name):
    return template('<b>Hello {{name}}</b>!', name=name)
'''

#on doit utiliser les CORS pour éviter une erreur de Cross-Origin Request
# the decorator
def enable_cors(fn):
    def _enable_cors(*args, **kwargs):
        # set CORS headers
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, OPTIONS'
        response.headers['Access-Control-Allow-Headers'] = 'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token'

        if bottle.request.method != 'OPTIONS':
            # actual request; reply with the actual response
            return fn(*args, **kwargs)

    return _enable_cors


app = bottle.app()


###Remplir les champs du formulaire
@app.route('/fill_form')
def fill() :
    



##Importation des tables
@app.route('/create/<table_name>')
def import_table(table_name) :
    BD.create_table(table_name+".csv")
    return "<script>alert('Import terminé !'); history.go(-1);</script>" #on affiche un message de succès puis on retourne à la page d'accueil


##Affichage des tables
@app.route('/display/<table_name>', method=['OPTIONS', 'GET'])
@enable_cors
def view_table(table_name):
    response.headers['Content-type'] = 'application/json'
    res = json.dumps(BD.select_all_table(table_name))
    return res


##Requêtes sur les tables

#Table activites
@app.route('/request/activites/<name_commune>/<number_equipment>/<activitie>/<practice>/<special>', method=['OPTIONS', 'GET'])
@enable_cors
def request_table(name_commune, number_equipment, activitie, practice, special):
    response.headers['Content-type'] = 'application/json'
    res = json.dumps(BD.select_from_activites(name_commune, number_equipment, activitie, practice, special))
    return res


#Table Equipement
@app.route('/request/equipements/<activity_code>', method=['OPTIONS', 'GET'])
@enable_cors
def request_table(activity_code):
    response.headers['Content-type'] = 'application/json'
    res = json.dumps(BD.select_from_equipements(number))
    return res

#Table Installation
@app.route('/request/installations/<activity_code>', method=['OPTIONS', 'GET'])
@enable_cors
def request_table(activity_code):
    response.headers['Content-type'] = 'application/json'
    res = json.dumps(BD.select_from_installations(number))
    return res



'''
#pour atteindre le fichier index.html dans le dossier vue. D'après nos tests, il faut toujours mettre cette route en dernier dans le code
@route('/<filepath:path>')
def index(filepath):
    return static_file(filepath,root="../vue")
'''


##Récupération de l'IP
f = os.popen('ifconfig eth0 | grep "inet\ addr" | cut -d: -f2 | cut -d" " -f1')
ip=f.read()

##Lancement du serveur
app.run(host=ip, port=8080, debug=True) # après avoir lancé le script, aller à l'adresse http://localhost:8080/index.html
