from flask import Flask
from src.config import config
from src.routes import Alumno
from flask_cors import CORS





app = Flask(__name__)
CORS(app)

def page_not_found(error):
    print("Entró al error 404")  # DEBUG
    return '<h1>No funciona mostro</h1>',404

if __name__== '__main__':

    app.config.from_object(config['development'])
    app.register_blueprint(Alumno.main, url_prefix = '/')
    app.register_error_handler(404,page_not_found)
    app.run()