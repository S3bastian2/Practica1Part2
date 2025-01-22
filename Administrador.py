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
        return super().setNombre(nombre)
    
    def getNombre(self):
        return super().getNombre()
    
    def setId(self, id):
        return super().setId(id)
    
    def getId(self):
        return super().getId()
    
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
            atrEquipo = inventario[i].split("*")
            eInv = Equipo(atrEquipo[0],atrEquipo[1],atrEquipo[3],atrEquipo[4])
            
            atrFEquipo = atrEquipo[2].split("/")
            fEquipo = Fecha(atrFEquipo[0],atrFEquipo[1],atrFEquipo[2])
            eInv.setFechaCompra(fEquipo)
            inventario[i] = eInv
            
        atrFecha = strSpliteado[2].split("/")
        fNacimiento = Fecha(atrFecha[0],atrFecha[1],atrFecha[2])
        cls.setFechaNacimiento(cls, fNacimiento)
        
        atrDireccion = strSpliteado[6].split("/")
        direccion = Direccion(atrDireccion[0],atrDireccion[1],atrDireccion[2],atrDireccion[3],atrDireccion[4],atrDireccion[5])
        cls.setDir(cls,direccion)

        return cls(nombre, id, ciudadNacimiento, tel, email, contraseña, inventario)
    
"""e1 = Equipo("HPproDesk", 98789876, 12000,1010)
fe = Fecha(15,12,2005)
e1.setFechaCompra(fe)

E1 = Equipo("PavilionZ10", 11223344, 1250,3030)
dia = 12
mes = 1
año = 2012
F1 = Fecha(dia, mes, año)
E1.setFechaCompra(F1)


IV = Administrador("Juancho", 1010, "medallo", 3131313, "asdas@fsdf.co", "Papulon",[E1])
f1 = Fecha(15,12,2005)
d1 = Direccion("Kra84b","63-25","Robledo","Medellin",None,None)
IV.setFechaNacimiento(f1)
IV.setDir(d1)

x = IV.getInventario()
x.append(e1)
IV.setInventario(x)

with open("Textos/Empleados.txt", "w") as archivo:
    archivo.write(str(IV))
    
listaNueva = []
with open("Textos/Empleados.txt", "r") as archivo:
    for linea in archivo:
        listaNueva.append(Administrador.from_string(linea))
        
for i in listaNueva:
    x = i.getInventario()
    print(str(x[0]), str(x[1]))"""