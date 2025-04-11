from src.database.db import get_db
from .entities.Alumno import Alumno

class AlumnoModel:

    @classmethod
    def get_alumnos(cls):
        try:
            connection = get_db()
            alumnos = []
            with connection.cursor() as cursor:
                cursor.execute("SELECT nombre, apellido, telefono, email FROM alumnos ORDER BY nombre ASC")
                resultset = cursor.fetchall()
                for row in resultset:
                    alumno = Alumno(row[0], row[1], row[2], row[3])
                    alumnos.append(alumno.to_JSON())
            return alumnos
        except Exception as ex:
            raise Exception(f"Error al obtener alumnos: {ex}")

    @staticmethod
    def get_by_email(email):
        try:
            db = get_db()
            with db.cursor() as cursor:
                cursor.execute("SELECT nombre, apellido, telefono, email FROM alumnos WHERE email = %s", (email,))
                row = cursor.fetchone()
                if row:
                    return Alumno(row[0], row[1], row[2], row[3])
                return None
        except Exception as ex:
            raise Exception(f"Error al buscar alumno por email: {ex}")

    @classmethod
    def add_alumno(cls, alumno):
        try:
            connection = get_db()
            with connection.cursor() as cursor:
                cursor.execute("""
                    INSERT INTO alumnos (nombre, apellido, telefono, email)
                    VALUES (%s, %s, %s, %s)
                """, (alumno.nombre, alumno.apellido, alumno.telefono, alumno.email))
            connection.commit()
        except Exception as ex:
            raise Exception(f"Error al agregar alumno: {ex}")

    @staticmethod
    def delete_alumno(alumno):
        try:
            db = get_db()
            with db.cursor() as cursor:
                cursor.execute("DELETE FROM alumnos WHERE email = %s", (alumno.email,))
            db.commit()
        except Exception as ex:
            raise Exception(f"Error al eliminar alumno: {ex}")
