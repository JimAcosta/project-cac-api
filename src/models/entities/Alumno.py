
class Alumno:

    def __init__(self,nombre,apellido,telefono,email):
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.email = email


    def to_JSON(self):
        return {
            'nombre':self.nombre,
            'apellido':self.apellido,
            'telefono':self.telefono,
            'email':self.email,
        }
