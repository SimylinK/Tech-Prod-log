from bottle import route, run, template

@route('/hello/<name>')
def index(name):
    return template('<b>Hello {{name}}</b>!', name=name)

run(host='localhost', port=8080) # après avoir lancé le script, aller à l'adresse http://localhost:8080/hello/world



#DOC : http://bottlepy.org/docs/dev/index.html