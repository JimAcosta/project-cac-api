from flask import Flask
from src.config import config
from src.routes import Alumno
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

app.config.from_object(config['development'])
app.register_blueprint(Alumno.main, url_prefix='/')

def page_not_found(error):
    return '<h1>No funciona</h1>', 404

app.register_error_handler(404, page_not_found)

if __name__ == '__main__':

    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
