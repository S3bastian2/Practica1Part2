class Nodo():
    def __init__(self, data, next):
        self.__data = data
        self.__next = next
    
    def Nodo(self):
        self.__init__(None, None)
    
    def Nodo(self, e):
        self.__init__(e, None)
    
    def setData(self, e):
        self.__data = e
    
    def setNext(self, n):
        self.__next = n
    
    def getData(self):
        return self.__data
    
    def getNext(self):
        return self.__next