from Fecha import *
from Hora import *

class FechaHora:
    def __init__(self, fecha: Fecha, hora: Hora):
        self.__fecha = fecha  # Instancia de la clase Fecha
        self.__hora = hora    # Instancia de la clase Hora

    def getFecha(self):
        return self.__fecha

    def getHora(self):
        return self.__hora

    def __str__(self):
        return f"{self.__fecha} {self.__hora}"