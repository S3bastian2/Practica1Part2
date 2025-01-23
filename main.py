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
    listaSolicitudes = []
    
    #cargue de solicitudes-----------------------------------------------------------
    with open("Textos/Solicitudes.txt", "r") as solis:
        for i in solis:
            strSpliteado = i.split()
            #Para equipo***********************************
            atrEquipo = strSpliteado[2].split("*")
            nombreEquipo = atrEquipo[0]
            placaEquipo = int(atrEquipo[1])
            valorCompra = int(atrEquipo[3])
            empAsociado = int(atrEquipo[4])
            #Fecha----------------------------
            atrFecha = atrEquipo[2].split("/")
            dd = int(atrFecha[0])
            mm = int(atrFecha[1])
            aa = int(atrFecha[2])
            faAsignar = Fecha(dd,mm,aa)
            EaAsignar = Equipo(nombreEquipo,placaEquipo,valorCompra,empAsociado)
            EaAsignar.setFechaCompra(faAsignar)
            #*************************************************
            
            #para Fecha y hora**********************************
            aTrFecha = strSpliteado[3]
            dd = int(atrFecha[0])
            mm = int(atrFecha[1])
            aa = int(atrFecha[2])
            faAsignar = Fecha(dd,mm,aa)
            
            aTrHora = strSpliteado[4].split("/")
            hh = int(aTrHora[0])
            mim = int(aTrHora[1])
            ss = int(aTrHora[2])
            haAsignar = Hora(hh,mim,ss)
            
            fhaAsignar = FechaHora(faAsignar, haAsignar)
            #******************************************************
            
            
            x = Solicitud.from_string(i)
            x.setEquipo(EaAsignar)
            x.setFechaSolicitud(fhaAsignar)
            listaSolicitudes.append(x)
            
        print(listaSolicitudes)
                    
    #Cargue de contraseñas -------------------------------------------------------
    pss = List(None,None,0)
    with open("Textos/Password.txt", "r") as contraseñas:
        for i in contraseñas:
            x = i.split()
            pss.addLast(x) 
    
    #cargue de los objetos a lista de todo ---------------------------------------
    tipos = []
    with open ("Textos/Password.txt", "r") as contraseñas:
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
        
        print(str(temp.getData().getNombre()))
        
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
            print("1. txt inventario")
            print("2. Agregar equipo")
            print("3. Eliminar equipo")
            print("4. txt Estado Solicitudes")
            print("5. salir")
            op = int(input())
            if op == 1:
                listaEnConsola = x.getInventario()
                for inven in listaEnConsola:
                    if isinstance(inven, Equipo):
                        print(inven)
                
                menus()
            elif op == 2:
                print("Esta opcion es para crear una solicitud de agregar equipo. ")
                respuesta = input("¿Desea continuar? Diga (si o no) ")
                if respuesta == "si":
                    nombre = input("Ingrese su nombre: ")
                    tipo = "agregar"
                    dia = int(input("Ingrese el dia en que esta haciendo la solicitud: "))
                    mes = int(input("Ingrese el mes en que esta haciendo la solicitud: "))
                    año = int(input("Ingrese el año de la solicitud: "))
                    hora = int(input("Ingrese la hora en que esta haciendo la solicitud: "))
                    min = int(input("Ingrese los minutos: "))
                    ss = int(input("Ingrese los segundos: "))
                    estado = "pendiente"

                    fechaSolicitud = Fecha(dia, mes, año)
                    horaSolicitud = Hora(hora, min, ss)
                    fechita = FechaHora(fechaSolicitud, horaSolicitud)

                    nombreEquipo = input("Ingrese el nombre del equipo: ")
                    numeroPlaca = int(input("Ingrese el numero de placa: "))
                    dd = int(input("Ingrese el dia de compra: "))
                    mm = int(input("Ingrese el mes de compra: "))
                    aa = int(input("Ingrese el año de compra: "))
                    fCompra = Fecha(dd,mm,aa)
                    valorCompra = int(input("Ingrese cuanto le costo: "))
                    empleAsociado = x.getId()
                    EáAsignar = Equipo(nombreEquipo,numeroPlaca,valorCompra,empleAsociado)
                    EáAsignar.setFechaCompra(fCompra)
                    
                    nuevaSolicitud = Solicitud(nombre, tipo, estado)
                    nuevaSolicitud.setFechaSolicitud(fechita)
                    nuevaSolicitud.setEquipo(EáAsignar)

                    listaSolicitudes.append(nuevaSolicitud)
                    """print(str(nuevaSolicitud)) #Probando si las solicitud se esta creando correctamente.
                    for soli in listaSolicitudes:
                        if isinstance(soli, Solicitud):
                            n = soli.getNombre()
                    print(n)"""
                    
                    print("La solicitud ha sido creada y agregada con exito. ")
                    with open("Textos/Solicitudes.txt", "a") as archivo:
                        archivo.write("\n"+str(nuevaSolicitud)) 

                    menus()
                elif respuesta == "no":
                    print("Opcion equivocada")
                    menus()
                else:
                    sys.exit()
            elif op == 3:
                print("Esta opcion es para crear una solicitud para eliminar un equipo de su inventario. ")
                respuesta = input("¿Desea continuar? Diga (si o no) ")
                if respuesta == "si":
                    nombre = input("Ingrese su nombre: ")
                    tipo = "eliminar"
                    numPlaca = int(input("Ingrese el numero de placa del equipo que desea eliminar: "))
                    dia = int(input("Ingrese el dia en que esta haciendo la solicitud: "))
                    mes = int(input("Ingrese el mes en que esta haciendo la solicitud: "))
                    año = int(input("Ingrese el año de la solicitud: "))
                    hora = int(input("Ingrese la hora en que esta haciendo la solicitud: "))
                    min = int(input("Ingrese los minutos: "))
                    ss = int(input("Ingrese los segundos: "))
                    estado = "pendiente"

                    fechaSolicitud = Fecha(dia, mes, año)
                    horaSolicitud = Hora(hora, min, ss)
                    fechita = FechaHora(fechaSolicitud, horaSolicitud)
                    
                    
                    listatodos = []
                    temp = listaDeTodo.first()
                    while temp != None and (temp != listaDeTodo.last() or temp == listaDeTodo.last()):
<<<<<<< Updated upstream
                        listatodos.append(temp.getData())
=======
                        nombreEnLista = temp.getData().getNombre().lower()
                        if nombre == nombreEnLista:
                            inven = temp.getData().getInventario()
                        #print(inven)
                            for equip in inven:
                                if numPlaca == equip.getNumeroPlaca():
                                    nuevaSolicitud.setEquipo(equip)
                                    
>>>>>>> Stashed changes
                        if temp == None:
                            pass
                        else:
                            temp = temp.getNext()
                    
                    IEspecifico = []
                    EaAsignar = None
                    for i in range(len(listatodos)):
                        n = str(listatodos[i].getNombre())
                        p = listatodos[i].getInventario()
                        if nombre == n:
                            for y in p:
                                IEspecifico.append(y)
                    for i in range(len(IEspecifico)):                    
                        if numPlaca == int(IEspecifico[i].getNumeroPlaca()):
                            EaAsignar = IEspecifico[i]
                    

                    nuevaSolicitud = Solicitud(nombre, tipo, estado)
                    nuevaSolicitud.setFechaSolicitud(fechita)
                    nuevaSolicitud.setEquipo(EaAsignar)
                    
                    listaSolicitudes.append(nuevaSolicitud)
                    print("La solicitud ha sido creada y agregada con exito. ")
                    with open("Textos/Solicitudes.txt", "a") as archivo:
<<<<<<< Updated upstream
                            if nuevaSolicitud == listaSolicitudes[0]:
                                archivo.write(str(nuevaSolicitud))    
                            else:
                                archivo.write("\n" + str(nuevaSolicitud))
                            
=======
                        if nuevaSolicitud == listaSolicitudes[0]:
                            archivo.write(str(nuevaSolicitud))
                            e1 = nuevaSolicitud.getEquipo()
                            print(str(e1))
                        else:
                            archivo.write("\n"+str(nuevaSolicitud)) 
>>>>>>> Stashed changes
                    menus()
                elif respuesta == "no":
                    print("Opcion equivocada")
                    menus()
                else:
                    sys.exit()
                    
                    
            elif op == 4:
                print(listaSolicitudes)


            elif op == 5:
                sys.exit()
                
                
         
        else:
            print("***********MENU***********")
            print("0. Buscar usuario registrado")
            print("1. txt inventario")
            print("2. Agregar usuario")
            print("3. Eliminar usuario")
            print("4. Cambiar contraseña")
            print("5. Solicitudes Agregar equipo")
            print("6. Solicitudes Eliminar equipo")
            print("7. Inventario segun investigador(txt)")
            print("8. Inventario general(txt)")
            print("9. Control de cambios(txt)")
            print("10. Solicitudes agregar(txt)")
            print("11. Solicitudes eliminar(txt)")
            print("12. Agregar Equipo Administrador")
            print("13. Salir")
            op = int(input())
            if op == 0:                        
                pass
                menus()
            elif op == 1:
                listaEnConsola = x.getInventario()
                for inven in listaEnConsola:
                    if isinstance(inven, Equipo):
                        print(inven)
                
                menus()
            elif op == 13:
                sys.exit()
            
            
    menus()

    #with open("Textos/Empleado.txt", "r") as archivo:
    #    for linea in archivo:
    #        listaNueva.append(Investigador.from_string(linea))
            

