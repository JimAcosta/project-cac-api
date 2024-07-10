from flask import Blueprint,jsonify,request
from models.AlumnoModel import AlumnoModel
from models.entities.Alumno import Alumno


main = Blueprint('alumno_blueprint',__name__)

@main.route('/')
def get_alumnos():
    try:
        alumnos = AlumnoModel.get_alumnos()
        return jsonify(alumnos)
    
    except Exception as ex:
        return jsonify({'message': str(ex)})
    
@main.route('/get_alumno/<email>', methods=['GET'])
def get_alumno(email):
    try:
        alumno = AlumnoModel.get_by_email(email)
        if not alumno:
            return jsonify({'message': 'Alumno no encontrado'}), 404
        return jsonify(alumno.to_JSON())
    except Exception as ex:
        return jsonify({'message': str(ex), 'error': "No encontró xd"}), 500
    


@main.route('/add',methods=['POST'])
def add_alumno():
    try:
        nombre = request.json['nombre']
        apellido = request.json['apellido']
        telefono = request.json['telefono']
        email = request.json['email']
        alum = Alumno(nombre,apellido,telefono,email)

        AlumnoModel.add_alumno(alum)

        return jsonify({'message': 'Alumno Agregado'})
    except Exception as ex:
        return jsonify({'message': str(ex)})

@main.route('/delete/<email>', methods=['DELETE'])
def delete_alumno(email):
    try:
        alumno = AlumnoModel.get_by_email(email)
        print(alumno.to_JSON())
        if not alumno:
            raise ValueError("No se encontró ningún alumno con ese email")

        AlumnoModel.delete_alumno(alumno)
        return jsonify({'message': 'Alumno eliminado correctamente'}), 200

    except Exception as ex:
        return jsonify({'error': str(ex), 'message': "No se pudo eliminar el alumno"}),