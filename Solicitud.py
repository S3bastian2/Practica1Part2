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
    
    def setEquipo(self, equipo):
        self.__equipo = equipo
    
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
        return self.getNombre() + " " + self.getTipo() + " " + str(self.getEquipo()) + " " + str(self.getFechaSolicitud()) + " " + self.getEstado()
    
    @classmethod
    def from_string(cls, string):
        strSpliteado = string.strip().split()
        nombreInvestigador = strSpliteado[0]
        tipo = strSpliteado[1]
        estado = strSpliteado[5]
        
        atrEquipo = strSpliteado[2].split("*")
        equipAgre = Equipo(atrEquipo[0], atrEquipo[1], atrEquipo[3], atrEquipo[4])
        #Fecha del equipo----------------------------------------------------------
        atrFechaCompra = atrEquipo[2].split("/")
        FaAsignar = Fecha(atrFechaCompra[0],atrFechaCompra[1],atrFechaCompra[2])
        equipAgre.setFechaCompra(FaAsignar)
        
        cls.setEquipo(cls, equipAgre)
        
        feSoliDia = strSpliteado[3].split("/")
        fSolicitud = Fecha(feSoliDia[0], feSoliDia[1], feSoliDia[2])
        feSoliHora = strSpliteado[4].split("/")
        hSolicitud = Hora(feSoliHora[0], feSoliHora[1], feSoliHora[2])
        fecSoli = FechaHora(fSolicitud, hSolicitud)
        cls.setFechaSolicitud(cls, fecSoli)
        
        return cls(nombreInvestigador, tipo, estado)

        