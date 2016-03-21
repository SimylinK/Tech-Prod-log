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
class Cors(object):
    name = 'cors'
    api = 2

    def apply(self, fn, context):
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


##Importation des tables
@app.route('/create/<table_name>')
def import_table(table_name) :
    BD.create_table(table_name+".csv")
    #il faudra essayer de récup url de la page précédente pour pouvoir rediriger dessus
    #redirect("http://localhost:8080/index.html") 
    

##Affichage des tables
@app.route('/display/<table_name>', method=['OPTIONS', 'GET'])
def view_table(table_name):
    response.headers['Content-type'] = 'application/json'
    res = json.dumps(BD.get_json_from_db(table_name))
    return res
    

'''
#pour atteindre le fichier index.html dans le dossier vue. D'après nos tests, il faut toujours mettre cette route en dernier dans le code
@route('/<filepath:path>')
def index(filepath):
    return static_file(filepath,root="../vue")
'''

##Installation des Cors
app.install(Cors())


##Récupération de l'IP
f = os.popen('ifconfig eth0 | grep "inet\ addr" | cut -d: -f2 | cut -d" " -f1')
ip=f.read()

##Lancement du serveur
run(host=ip, port=8080, debug=True) # après avoir lancé le script, aller à l'adresse http://localhost:8080/index.html
