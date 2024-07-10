from flask import Flask
from config import config
from routes import Alumno
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

def page_not_found(error):
    return '<h1>Not found page</h1>',404

if __name__== '__main__':

    app.config.from_object(config['development'])
    app.register_blueprint(Alumno.main, url_prefix = '/api/alumnos')
    app.register_error_handler(404,page_not_found)
    app.run()