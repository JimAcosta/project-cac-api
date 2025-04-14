from flask import Flask
from src.config import config
from src.routes import Alumno
from flask_cors import CORS
from src.routes.test_connection import test_db
import os

app = Flask(__name__)
CORS(app)

def page_not_found(error):
    print("Entró al error 404")  # DEBUG
    return '<h1>No funciona mostro</h1>',404

if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.register_blueprint(Alumno.main, url_prefix='/')
    app.register_blueprint(test_db)
    app.register_error_handler(404, page_not_found)

    # ⚠️ SOLO este app.run()
    port = int(os.environ.get("PORT", 5000))  # Render lo pone como PORT
    app.run(host='0.0.0.0', port=port)
