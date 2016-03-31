import os
import os.path
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../modele")))
import bottle
from bottle import route, run, template, static_file, post, get, response, redirect
import json
from bd import BD

#we need to use CORS to avoid Cross-Origin Request error
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


##Fill form fields
    ##commune field 
@app.route('/fill_form/commune', method=['OPTIONS', 'GET']) 
@enable_cors #don't forget to avoid CORS error
def fill_com() :
    response.headers['Content-type'] = 'application/json' #JSON expected
    res = json.dumps(BD.get_name_commune())
    return res
    ##activité (activity) field
@app.route('/fill_form/activity', method=['OPTIONS', 'GET'])
@enable_cors
def fill_act() :
    response.headers['Content-type'] = 'application/json'
    res = json.dumps(BD.get_name_activity())
    return res


##Tables import
@app.route('/create/<table_name>')
def import_table(table_name) :
    BD.create_table(table_name+".csv") #append CSV file format at the end
    return "<script>alert('Import terminé !'); history.go(-1);</script>" #print success message, then return on first page


##Tables display
@app.route('/display/<table_name>', method=['OPTIONS', 'GET'])
@enable_cors
def view_table(table_name):
    response.headers['Content-type'] = 'application/json'
    res = json.dumps(BD.select_all_table(table_name))
    return res


##Requests on tables

#Activites (activity) tables
@app.route('/request/activites/<name_commune>/<number_equipment>/<activitie>/<practice>/<special>', method=['OPTIONS', 'GET'])
@enable_cors
def request_table(name_commune, number_equipment, activitie, practice, special):
    activitie = activitie.replace(".", "/") #we replaced slashes before because they were interpreted in URL (bottle route)
    response.headers['Content-type'] = 'application/json'
    res = json.dumps(BD.select_from_activites(name_commune, number_equipment, activitie, practice, special))
    return res

#Equipement (equipment) table
@app.route('/request/equipements/<activity_code>', method=['OPTIONS', 'GET'])
@enable_cors
def request_table(activity_code):
    response.headers['Content-type'] = 'application/json'
    res = json.dumps(BD.select_from_equipements(activity_code))
    return res

#Installation table
@app.route('/request/installations/<activity_code>', method=['OPTIONS', 'GET'])
@enable_cors
def request_table(activity_code):
    response.headers['Content-type'] = 'application/json'
    res = json.dumps(BD.select_from_installations(activity_code))
    return res


##Get IP adress
f = os.popen('ifconfig eth0 | grep "inet\ addr" | cut -d: -f2 | cut -d" " -f1') #return device IP
ip=f.read()

##Server laucnhing
app.run(host=ip, port=8080, debug=True)
