class Direccion:
    def __init__(self, calle, nomenclatura, barrio, ciudad, edificio, apto):
        self.__calle = calle
        self.__nomenclatura = nomenclatura
        self.__barrio = barrio
        self.__ciudad = ciudad
        self.__edificio = edificio
        self.__apto = apto
    
    def Direccion(self):
        self.__init__
        
    def setCalle(self, c):
        self.__calle = c
        
    def getCalle(self):
        return self.__calle
    
    def setCiudad(self, ci):
        self.__ciudad = ci
        
    def getCiudad(self):
        return self.__ciudad
    
    def setNomenclatura(self,n):
        self.__nomenclatura = n
        
    def getNomenclatura(self):
        return self.__nomenclatura
    
    def setBarrio(self,b):
        self.__barrio = b
        
    def getBarrio(self):
        return self.__barrio
    
    def setEdificio(self, e):
        self.__edificio = e
        
    def getEdificio(self):
        return self.__edificio
    
    def setApto(self, a):
        self.__apto = a
        
    def getApto(self):
        return self.__apto
    
    def __str__(self):
        return str(self.__calle) + " " + str(self.__nomenclatura) + " " +  str(self.__barrio) + " " + str(self.__ciudad) + " " + str(self.__edificio) + " " + str(self.__apto)