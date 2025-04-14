import os
import psycopg2
from flask import g
from dotenv import load_dotenv

load_dotenv()

DATABASE_CONFIG = {
    'user': os.getenv('DB_USERNAME'),
    'password': os.getenv('DB_PASSWORD'),
    'host': os.getenv('DB_HOST'),
    'database': os.getenv('DB_NAME'),
    'port': int(os.getenv('DB_PORT', 5432))  # Puerto de PostgreSQL
}

def get_db():
    if 'db' not in g:
        try:
            g.db = psycopg2.connect(**DATABASE_CONFIG)
        except Exception as e:
            print({
                'host': os.getenv('DB_HOST'),
                'user': os.getenv('DB_USERNAME'),
                'password': os.getenv('DB_PASSWORD'),
                'database': os.getenv('DB_NAME'),
                'port': int(os.getenv('DB_PORT', 5432))  # Puerto de PostgreSQL
            })
            print("❌ Error al conectar a la base de datos:", e)
            raise
    return g.db

def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()

def init_app(app):
    app.teardown_appcontext(close_db)
