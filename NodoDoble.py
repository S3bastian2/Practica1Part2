class NodoDoble:
    def __init__(self, data, next, prev):
        self.__data = data
        self.__next = next
        self.__prev = prev
        
    def nodoDoble(self):
        self.__init__(None, None, None)
    
    def nodoDoble(self, d):
        self.__init__(d, None, None)
        
    def setData(self, d):
        self.__data = d
    
    def setNext(self, n):
        self.__next = n 
    
    def setPrev(self, p):
        self.__prev = p
        
    def getData(self):
        return self.__data
    
    def getNext(self):
        return self.__next
    
    def getPrev(self):
        return self.__prev