from Equipo import *
from FechaHora import *

class Solicitud():
    def __init__(self, nombreInvestigador, tipo, estado):
        self.__nombreInvestigador = nombreInvestigador
        self.__tipo = tipo
        self.__equipo = Equipo
        self.__fechaSolicitud = FechaHora
        self.__estado = estado

    def setNombre(self, nombreInvestigador):
        self.__nombreInvestigador = nombreInvestigador
    
    def getNombre(self):
        return self.__nombreInvestigador
    
    def setTipo(self, tipo):
        self.__tipo = tipo
    
    def getTipo(self):
        return self.__tipo
    
    def setEquipo(self, Equipo):
        self.__equipo = Equipo
    
    def getEquipo(self):
        return self.__equipo
    
    def setFechaSolicitud(self, fechaSolicitud):
        self.__fechaSolicitud = fechaSolicitud
    
    def getFechaSolicitud(self):
        return self.__fechaSolicitud
    
    def setEstado(self, estado):
        self.__estado = estado
    
    def getEstado(self):
        return self.__estado
    
    def __str__(self):
        return str(self.getNombre()) + " " + str(self.getTipo()) + " " + str(self.getEquipo()) + " " + str(self.getFechaSolicitud()) + " " + str(self.getEstado())
        