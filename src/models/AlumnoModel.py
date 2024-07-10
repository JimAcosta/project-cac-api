from database.db import get_db,close_db
from .entities.Alumno import Alumno
from flask import jsonify


class AlumnoModel():

    @classmethod
    def get_alumnos(self):
        try:
            connection = get_db()
            alumnos = []
            with connection.cursor() as cursor:
                cursor.execute("SELECT nombre,apellido,telefono,email FROM alumnos ORDER by nombre ASC")
                resultset = cursor.fetchall()

                for row in resultset:
                    alumno = Alumno(row[0],row[1],row[2],row[3]) 
                    alumnos.append(alumno.to_JSON())
                return alumnos
            connection.close()

        except Exception as ex:
            raise Exception(ex)
        
    @staticmethod
    def get_by_email(email):
        try:
            db = get_db()
            cursor = db.cursor()
            cursor.execute("SELECT nombre, apellido, telefono, email FROM alumnos WHERE email = %s", (email,))
            row = cursor.fetchone()
            if row:
                return Alumno(row[0], row[1], row[2], row[3])
            return None
        except Exception as ex:
            raise Exception(ex)
        
        
    @classmethod
    def add_alumno(self,alumno):
        try:
            connection = get_db()
            with connection.cursor() as cursor:
                cursor.execute("""INSERT INTO alumnos (nombre,apellido,telefono,email)
                        VALUES(%s,%s,%s,%s)""",(alumno.nombre,alumno.apellido,alumno.telefono,alumno.email))
            connection.commit()
            connection.close()
        except Exception as ex:
            raise Exception(ex)
        
    @staticmethod
    def delete_alumno(alumno):
        try:
            db = get_db()
            cursor = db.cursor()
            cursor.execute("DELETE FROM alumnos WHERE email = %s", (alumno.email,))
            db.commit()
            cursor.close()
        except Exception as ex:
            raise Exception(ex)
        finally:
            db.close()