class Hora():
    def __init__(self, hh, nn, ss):
        self.__hora = hh
        self.__minuto = nn
        self.__segundo = ss
    
    def getHora(self):
        return self.__hora
    
    def getMinuto(self):
        return self.__minuto
    
    def getSegundo(self):
        return self.__segundo
    
    def setHora(self, hh):
        self.__hora = hh
        
    def setMinuto(self, nn):
        self.__minuto = nn
        
    def setSegundo(self, ss):
        self.__segundo = ss
    
    def __str__(self):
        return str(self.__hora) + " " + str(self.__minuto) + " " + str(self.__segundo)