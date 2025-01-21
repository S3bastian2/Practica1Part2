from NodoDoble import NodoDoble

class ListaDoble():
    def __init__(self,head, tail, size):
        self.__head = head
        self.__tail = tail
        self.__size = size
        
    def ListaDoble(self):
        self.__init__(None, None, 0)
        
    def size(self):
        return self.__size
    
    def isEmpty(self):
        if self.__size == 0:
            return True
        else:
            return False
    
    def first(self):
        return self.__head
    
    def last(self):
        return self.__tail
    
    def addFirst(self, e):
        n = NodoDoble(e,None,None)
        if self.isEmpty():
            self.__head = n
            self.__tail = n
        else:
            n.setNext(self.first())
            self.__head.setPrev(n)
            self.__head = n
        self.__size += 1
        
    def addLast(self, e):
        n = NodoDoble(e, None, None)
        if self.isEmpty():
            self.__head = n
            self.__tail = n
        else:
            self.__tail.setNext(n)
            n.setPrev(self.__tail)
            self.__tail = n
        self.__size += 1
            
    def removeFirst(self):
        if self.isEmpty():
            return None
        else:
            temp = self.first()
            self.__head = temp.getNext()
            temp.setNext(None)
            temp.setPrev(None)
            self.__size -= 1
            return temp.getData()
    
    def removeLast(self):
        if self.isEmpty():
            return None
        else:
            temp = self.last()
            self.__tail = temp.getPrev()
            temp.setNext(None)
            temp.setPrev(None)
            self.__size -= 1
            return temp.getData()

    def remove(self, n):
        if n == self.first():
            return self.removeFirst()
        elif n == self.last():
            return self.removeLast()
        else:
            e =n.getData()
            p = n.getPrev()
            nx = n.getNext()
            p.setNext(nx)
            nx.setPrev(p)
            n.setNext(None)
            n.setPrev(None)
            self.__size -= 1
            return e
        
    def addAfter(self, n, e):
        if n == self.last():
            self.addLast(e)
        else:
            m = NodoDoble(e,None,None)
            nx = n.getNext()
            n.setNext(m)
            m.setPrev(n)
            m.setNext(nx)
            nx.setPrev(m)
            self.__size += 1   
                      
    def addBefore(self, n, e):
        if n == self.first():
            self.addFirst(e)
        else:
            m = NodoDoble(e,None,None)
            p = n.getPrev()
            p.setNext(m)
            m.setPrev(p)
            m.setNext(n)
            n.setPrev(m)
            self.__size += 1