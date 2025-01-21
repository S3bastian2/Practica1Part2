from Fecha import *
from Direccion import *

class Usuario():
    def __init__(self, nombre, id, ciudad_nacimiento, tel, email):
        self.__nombre = nombre
        self.__id = id
        self.__fechaNacimiento = Fecha
        self.__ciudadNacimiento = ciudad_nacimiento
        self.__telefono = tel
        self.__email = email
        self.__dir = Direccion

    def Usuario(self):
        self.__init__()
    
    def getNombre(self):
        return self.__nombre
    
    def setNombre(self, nombre):
        self.__nombre = nombre
    
    def getId(self):
        return self.__id
    
    def setId(self, id):
        self.__id = id
    
    def getFechaNacimiento(self):
        return self.__fechaNacimiento

    def setFechaNacimiento(self, Fecha):
        self.__fechaNacimiento = Fecha
    
    
    def getCiudadNacimiento(self):
        return self.__ciudadNacimiento

    def setCiudadNacimiento(self, ciudad_nacimiento):
        self.__ciudadNacimiento = ciudad_nacimiento
    
    def getTelefono(self):
        return self.__telefono
    
    def setTelefono(self, tel):
        self.__telefono = tel
    
    def getEmail(self):
        return self.__email
    
    def setEmail(self, email):
        self.__email = email
    
    def getDir(self):
        return self.__dir
    
    def setDir(self, Direccion):
        self.__dir = Direccion
    
    def __str__(self):
        return "El Nombre del usuario es: " + str(self.__nombre) + " identificado con el id: " + str(self.__id) + " nacido el dia: " + str(self.__fechaNacimiento) + " en la ciudad de: " + str(self.__ciudadNacimiento) + " su numero de telefono es: " + str(self.__telefono) + " su correo electronico es: " + str(self.__email) + " y su direccion es: " + str(self.__dir)