from Direccion import *
from Usuario import *
from Fecha import *
from Hora import *
from FechaHora import *

class Investigador(Usuario):
    def __init__(self, nombre, id, ciudad_nacimiento, tel, email, contraseña, inventario = None):
        super().__init__(nombre, id, ciudad_nacimiento, tel, email)
        self.__contraseña = contraseña
        self.__inventario = inventario if inventario is not None else []
        
    def setInventario(self, inventario):
        self.__inventario = inventario
        
    def getInventario(self):
        return self.__inventario
    
    def setDir(self, Direccion):
        return super().setDir(Direccion)
    
    def getDir(self):
        return super().getDir()
    
    def setNombre(self, nombre):
        return super().setNombre(nombre)
    
    def getNombre(self):
        return super().getNombre()
    
    def setId(self, id):
        return super().setId(id)
    
    def getId(self):
        return super().getId()
    
    def getCiudadNacimiento(self):
        return super().getCiudadNacimiento()
    
    def setCiudadNacimiento(self, ciudad_nacimiento):
        return super().setCiudadNacimiento(ciudad_nacimiento)
    
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
        return super().setFechaNacimiento(Fecha)
    
    def getFechaNacimiento(self):
        return super().getFechaNacimiento()
    
    def __str__(self):
        listaStr = "|". join(map(str, self.__inventario))
        return self.getNombre()+","+str(self.getId())+","+str(self.getFechaNacimiento())+","+self.getCiudadNacimiento()+","+str(self.getTelefono())+","+self.getEmail()+","+str(self.getDir())+","+self.getContraseña()+","+listaStr

IV = Investigador("Carlos", 1010, "medallo", 3131313, "asdas@fsdf.co", "Papulon",[1,2,3,4,5])
f1 = Fecha(15,12,2005)
d1 = Direccion("Kra84b","63-25","Robledo","Medellin",None,None)
IV.setFechaNacimiento(f1)
IV.setDir(d1)

IV2 = Investigador("Laura", 2020, "Bogotá", 3141414, "laura@example.com", "Biología",[6,7,8,9,10])
f2 = Fecha(22, 7, 1990)
d2 = Direccion("Carrera 15", "45-10", "Chapinero", "Bogotá", None, None)
IV2.setFechaNacimiento(f2)
IV2.setDir(d2)

IV3 = Investigador("Andrés", 3030, "Cali", 3151515, "andres@example.com", "Química",[11,12,13,14,15])
f3 = Fecha(9, 3, 1985)
d3 = Direccion("Calle 5", "25-50", "San Fernando", "Cali", None, None)
IV3.setFechaNacimiento(f3)
IV3.setDir(d3)

ListaTodos = [IV,IV2,IV3]

#Guardar
with open("C:/EjemplosPY/Empleados.txt", "w") as archivo:
    for emp in ListaTodos:
        if emp == ListaTodos[-1]:
            archivo.write(str(emp))
        else:
            archivo.write(str(emp)+ "\n")