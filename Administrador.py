from Usuario import *
from Equipo import *
from FechaHora import *
from Investigador import *

class Administrador(Usuario):
    def __init__(self, nombre, id, ciudad_nacimiento, tel, email, contraseña, inventario = None):
        super().__init__(nombre, id, ciudad_nacimiento, tel, email)
        self.__contraseña = contraseña
        self.__fechaNacimiento = Fecha
        self.__dir = Direccion
        self.__inventario = inventario if inventario is not None else []

    def setNombre(self, nombre):
        self.__nombre = nombre
    
    def getNombre(self):
        return self.__nombre
    
    def setId(self, id):
        self.__id = id
    
    def getId(self):
        return self.__id
    
    def getCiudadNacimiento(self):
        return super().getCiudadNacimiento()
    
    def setCiudadNacimiento(self, ciudadNacimiento):
        return super().setCiudadNacimiento(ciudadNacimiento)
    
    def setTelefono(self, tel):
        return super().setTelefono(tel)
    
    def getTelefono(self):
        return super().getTelefono()
    
    def setEmail(self, email):
        return super().setEmail(email)
    
    def getEmail(self):
        return super().getEmail()
    
    def setContraseña(self, contraseña):
        self.__contraseña = contraseña
    
    def getContraseña(self):
        return self.__contraseña
    
    def setFechaNacimiento(self, Fecha):
        self.__fechaNacimiento = Fecha
    
    def getFechaNacimiento(self):
        return self.__fechaNacimiento
    
    def setDir(self, Direccion):
        self.__dir = Direccion
    
    def getDir(self):
        return self.__dir
    
    def setInventario(self, inventario):
        self.__inventario = inventario
    
    def getInventario(self):
        return self.__inventario
    
    def __str__(self):
        listaStr = "|". join(map(str, self.__inventario))
        return self.getNombre() + "," + str(self.getId()) + "," + str(self.getFechaNacimiento()) + "," + self.getCiudadNacimiento() + "," + str(self.getTelefono()) + "," + self.getEmail() + "," + str(self.getDir()) + "," + self.getContraseña() + "," + listaStr
    
    @classmethod
    def from_string(cls, string):
        strSpliteado = string.strip().split(",")
        listaStr = strSpliteado[8]
        nombre = strSpliteado[0]
        id = int(strSpliteado[1])
        ciudadNacimiento = strSpliteado[3]
        tel = int(strSpliteado[4])
        email = strSpliteado[5]
        contraseña =strSpliteado[7]
        inventario = listaStr.split("|")
        for i in range(len(inventario)):
            inventario[i] = int(inventario[i])
            
        atrFecha = strSpliteado[2].split("/")
        fNacimiento = Fecha(atrFecha[0],atrFecha[1],atrFecha[2])
        cls.setFechaNacimiento(cls, fNacimiento)
        
        atrDireccion = strSpliteado[6].split("/")
        direccion = Direccion(atrDireccion[0],atrDireccion[1],atrDireccion[2],atrDireccion[3],atrDireccion[4],atrDireccion[5])
        cls.setDir(cls,direccion)

        return cls(nombre, id, ciudadNacimiento, tel, email, contraseña, inventario)