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
import sys

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
    
    
    #Prueba de contenido lista de todo :)
    """temp = listaDeTodo.first()
    while temp != None and (temp != listaDeTodo.last() or temp == listaDeTodo.last()):
        
        print(str(temp.getData()))
        
        if temp == None:
            pass
        else:
            temp = temp.getNext()"""
    
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
            print("Id o contrasela incorrectos")
            sys.exit()
            
    x = login()
    
    # Menu de opciones -------------------------------------------------------------------------
    
    def menus():
        
        if type(x) == Investigador:
            print("***********MENU***********")
            print("1.txt inventario")
            print("2. Agregar equipo")
            print("3. Eliminar equipo")
            print("4.txt Estado Solicitudes")
            print("5. salir")
            op = int(input())
            if op == 1:
                listaEnConsola = x.getInventario()
                for inven in listaEnConsola:
                    if isinstance(inven, Equipo):
                        print(inven)
                
                menus()
            elif op == 5:
                sys.exit()
                
                
         
        else:
            print("***********MENU***********")
            print("0.Buscar usuario registrado")
            print("1.txt inventario")
            print("2.Agregar usuario")
            print("3.Eliminar usuario")
            print("4.Cambiar contraseña")
            print("5.Solicitudes Agregar equipo")
            print("6.Solicitudes Eliminar equipo")
            print("7.Inventario segun investigador(txt)")
            print("8.Inventario general(txt)")
            print("9.Control de cambios(txt)")
            print("10.Solicitudes agregar(txt)")
            print("11.Solicitudes eliminar(txt)")
            print("12. Agregar Equipo Administrador")
            print("13. Salir")
            op = int(input())
            if op == 0:                        
                pass
                menus()
            elif op == 13:
                sys.exit()
            
            
    menus()

    with open("Textos/Empleado.txt", "r") as archivo:
        for linea in archivo:
            listaNueva.append(Investigador.from_string(linea))
            

