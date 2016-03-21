import os.path
import sys
#pour revenir à un nvieau au-dessus dans le path (on fait un chemin absolu de celui où on est et on revient en plus un cran en arrière avec ..)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from bottle import route, run, template, static_file
from modele.bd import BD

#DOC : http://bottlepy.org/docs/dev/index.html
''' Exemple de la doc
@route('/hello/<name>')
def index(name):
    return template('<b>Hello {{name}}</b>!', name=name)
'''


@route('/<filepath:path>')
def index(filepath):
  return static_file(filepath,root=".")

@route('/import_install')
def import_install() :
    BD.connect()
    BD.create_table("installations.csv")
    BD.close()

run(host='localhost', port=8080) # après avoir lancé le script, aller à l'adresse http://localhost:8080/hello/world
