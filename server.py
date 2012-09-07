from bottle import *
import json

# Import Settings Into a Dictionary
settings = json.load(open('settings.json'))

# Main Page
@get('/')
def index():  
    return template("templates/index.html", settings)

# Error 404
@error(404)
def error404(error):
    return "Sorry, can't find that page!"

# Static Routes
@get('/<filename:re:.*\.js>')
def javascripts(filename):
    return static_file(filename, root='static/js')

@get('/<filename:re:.*\.css>')
def stylesheets(filename):
    return static_file(filename, root='static/css')

@get('/<filename:re:.*\.(jpg|png|gif|ico)>')
def images(filename):
    return static_file(filename, root='static/img')

@get('/<filename:re:.*\.(eot|ttf|woff|svg)>')
def fonts(filename):
    return static_file(filename, root='static/fonts')
  

debug(True)
run(host='localhost', port=9000, reloader=True)