from flask import Blueprint, jsonify
from src.database.db import get_db

test_db = Blueprint('test_db', __name__)

@test_db.route('/testdb')
def test_db_connection():
    try:
        db = get_db()
        cursor = db.cursor()
        cursor.execute('SELECT 1;')
        result = cursor.fetchone()
        return jsonify({"message": "✅ Conexión exitosa", "result": result})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
