from Investigador import *
from Equipo import *
from Investigador import *
from Administrador import *
from Solicitud import *
from List import *
from ListaDoble import *
from Nodo import *
from NodoDoble import *
from FechaHora import *

respuesta = " "
while respuesta != "salir":

    listaDeTodo = ListaDoble(None, None, 0)
        
    #Cargue de contraseñas -------------------------------------------------------
    pss = List(None,None,0)
    with open("Textos/Password.txt", "r") as contraseñas:
        for i in contraseñas:
            x = i.split()
            pss.addLast(x) 
    
    #cargue de los objetos a lista de todo ---------------------------------------
    tipos = []
    with open ("Textos/password.txt", "r") as contraseñas:
        for i in contraseñas:
            x = i.split()
            tipos.append(x[-1])
    
    
    with open("Textos/Empleados.txt", "r") as empleados:
        LEmpleados =[]
        for linea in empleados:
            LEmpleados.append(linea)
    
        iteracion = 0
        while iteracion != len(tipos):
            if tipos[iteracion] == "investigador":
                listaDeTodo.addLast(Investigador.from_string(LEmpleados[iteracion]))
            else:
                listaDeTodo.addLast(Administrador.from_string(LEmpleados[iteracion]))
            iteracion += 1
    
    #login ------------------------------------------------------------------------------------------------
    print("*** Bienvenido al sistema ***")
    NumId = input("ID: ")
    contra = input("Contraseña: ")

    def login():

        vf = False
        temp = pss.First()
        while temp != None and (temp != pss.Last() or temp == pss.Last()):
            
            if temp.getData()[0] == NumId and temp.getData()[1] == contra:
                
                vf = True
                #ciclo dentro de lista de todo para apuntarlo aca-----------------------------------------
                temp1 = listaDeTodo.first()
                while temp1 != None and (temp1 != listaDeTodo.last() or temp1 == listaDeTodo.last()):
                    
                    
                    if int(NumId) == temp1.getData().getId():
                        ASesionIniciada = temp1.getData()
                        return ASesionIniciada
                    #iterador while anidado*********************
                    if temp1 == None:
                        pass
                    else:
                        temp1 = temp1.getNext()  
                        
            #iterador primer while*******************          
            if temp == None:
                pass
            else:
                temp = temp.getNext()
        if vf == False:
            return print("Id o contrasela incorrectos")
        
        
    x = login()
    print(x)
                                
    
    respuesta = "salir"
    
"""    with open("Textos/Empleado.txt", "r") as archivo:
        for linea in archivo:
            listaNueva.append(Investigador.from_string(linea))"""
            

