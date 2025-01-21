from Nodo import Nodo

class List():
    def __init__(self, head = Nodo, tail = Nodo, size = 0):
        self.__head = head
        self.__tail = tail
        self.__size = size
    
    def List(self):
        self.__init__()
    
    def isEmpty(self):
        if self.__size == 0:
            return True
        else:
            return False
    
    def setSize(self, s):
        self.__size = s
    
    def First(self):
        return self.__head
    
    def Last(self):
        return self.__tail
    
    def addFirst(self, e):
        n = Nodo(e, None) #Creamos un nodo con valor e.
        if self.isEmpty(): #Verificamos si la lista esta vacia.
            self.__head = n #Si la lista esta vacia entonces el valor apunta a la cabeza
            self.__tail = n #Si la lista este vacia entonces el mismo valor apunta a la cola
        else:
            n.setNext(self.__head) #Si no esta vacia
            self.__head = n #N apunta al sgte nodo que antes era la cabeza
        self.__size += 1 #Se aumenta el tamaño de la lista
    
    def addLast(self, e):
        n = Nodo(e, None) #Creamos un nuevo nodo que va a tener un valor e.
        if self.isEmpty(): #En el caso de la lista este vacia.
            self.__head = n #N va a ser la cabeza.
            self.__tail = n #N a su vez va a ser la cola.
        else: #Por el contrario si no esta vacia.
            self.__tail.setNext(n) #Hacemos que la cola apunte al nodo siguiente osea n.
            self.__tail = n #Actualizamos el valor de la cola para que esta sea n.
        self.__size += 1 #Aumentamos el tamaño de la lista.
    
    def removeFirst(self):
        if self.isEmpty(): #Verifica si la lista esta vacia.
            return None
        else:
            temp = self.__head #Hacemos una variable temporal que sirve de apuntador para la cabeza.
            self.__head = temp.getNext() #Actualizamos la cabeza para que sea igual a nodo siguiente.
            temp.setNext(None) #Cómo temp es la cabeza de nuestra lista ahora hacemos que apunte a nulo, osea es como si la eliminaramos.
            self.__size -= 1 #Disminuimos el tamaño de la lista.
            return temp.getData() #Pedimos el valor de temp osea la cabeza anterior.
    
    def removeLast(self):
        if self.__size == 1: #Dado que la lista tenga por lo menos un nodo, este sera la cabeza y la cola.
            return self.removeFirst() #Lo eliminamos y la lista quedaria vacia.
        else: #Si no.
            temp = self.__tail #Creamos una variable que apunte a la cola.
            anterior = self.__head #Creamos una variable que apunte a la cabeza.
            while(anterior.getNext() != self.__tail): #Iteramos sobre la lista con el fin de identificar que la cabeza y la cola y por ultimo encontrar el ultimo nodo de la lista.
                anterior = anterior.getNext() #Actualizamos el apuntador de la cabeza para que apunte al sgte nodo.
            anterior.setNext(None) #Ahora que anterior apunta al ultimo, desconectamos ese nodo de la lista.
            self.__tail = anterior #Ahora la cola va a ser igual al nodo que teniamos antes.
            self.__size -= 1 #Disminuimos el tamaño de la lista.
            return temp.getData() #Retornamos el valor de la nueva cola.