from Usuario import *
from Fecha import *

class Equipo():
    def __init__(self, nombreEquipo, numeroPlaca, valorCompra, empleAsociado):
        self.__nombreEquipo = nombreEquipo
        self.__numeroPlaca = numeroPlaca
        self.__fechaCompra = Fecha
        self.__valorCompra = valorCompra
        self.__empleAsociado = empleAsociado

    def setNombreEquipo(self, nombreEquipo):
        self.__nombreEquipo = nombreEquipo

    def getNombreEquipo(self):
        return self.__nombreEquipo
    
    def setNumeroPlaca(self, numeroPlaca):
        self.__numeroPlaca = numeroPlaca
    
    def getNumeroPlaca(self):
        return self.__numeroPlaca
    
    def setFechaCompra(self, Fecha):
        self.__fechaCompra = Fecha
    
    def getFechaCompra(self):
        return self.__fechaCompra
    
    def setValorCompra(self, valorCompra):
        self.__valorCompra = valorCompra

    def getValorCompra(self):
        return self.__valorCompra
    
    def setEmpleAsociado(self, empleAsociado):
        self.__empleAsociado = empleAsociado
    
    def getEmpleAsociado(self):
        return self.__empleAsociado
    
    def __str__(self):
        return " " + self.getNombreEquipo() + "  " + str(self.getNumeroPlaca()) + "  " + str(self.getFechaCompra()) + "  " + str(self.getValorCompra()) + "  " 
    
#E1 = Equipo("PavilionZ10", 11223344, 1250)
#dia = 12
#mes = int(input("Ingrese el mes: "))
#año = 2012
#F1 = Fecha(dia, mes, año)
#E1.setFechaCompra(F1)
#E1.setEmpleAsociado(None)
#print(E1)
        