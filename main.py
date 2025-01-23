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
        for i in empleados:
            if tipos[0] == "investigador":
                listaDeTodo.addLast(Investigador.from_string(i))
                tipos.pop(0)
            else:
                listaDeTodo.addLast(Administrador.from_string(i))
                tipos.pop(0)
    
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
                    tipoEquipo = input("Ingrese el tipo de equipo: ")
                    numPlaca = int(input("Ingrese el numero de placa: "))
                    valor = int(input("Ingrese el valor del equipo: "))
                    empAsociado = nombre
                    
                   
                    

                    fechaSolicitud = Fecha(dia, mes, año)
                    horaSolicitud = Hora(hora, min, ss)
                    fechita = FechaHora(fechaSolicitud, horaSolicitud)
                    
                    equipoNuevo = Equipo(tipoEquipo, numPlaca, valor, empAsociado)
                    equipoNuevo.setFechaCompra(fechita)
                    
                     

                    nuevaSolicitud = Solicitud(nombre, tipo, estado)
                    nuevaSolicitud.setFechaSolicitud(fechita)
                    nuevaSolicitud.setEquipo(equipoNuevo)

                    listaSolicitudes.append(nuevaSolicitud)

                    print("La solicitud ha sido creada y agregada con exito. ")
                    with open("Textos/Solicitudes.txt", "a") as archivo:
                        if nuevaSolicitud == listaSolicitudes[0]:
                            archivo.write(str(nuevaSolicitud))
                        else:
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
                    
                    nuevaSolicitud = Solicitud(nombre, tipo, estado)
                    nuevaSolicitud.setFechaSolicitud(fechita)
                    
                    temp = listaDeTodo.first()
                    while temp != None and (temp != listaDeTodo.last() or temp == listaDeTodo.last()):
                        nombreEnLista = temp.getData().getNombre().lower()
                        if nombre == nombreEnLista:
                            inven = temp.getData().getInventario()
                        #print(inven)
                            for equip in inven:
                                if isinstance(equip, Equipo):
                                    if numPlaca == equip.getNumeroPlaca():
                                        nuevaSolicitud.setEquipo(equip)
                        if temp == None:
                            pass
                        else:
                            temp = temp.getNext()

                    listaSolicitudes.append(nuevaSolicitud)
                    #print(nuevaSolicitud)
                    print("La solicitud ha sido creada y agregada con exito. ")
                    with open("Textos/Solicitudes.txt", "a") as archivo:
                            archivo.write("\n" + str(nuevaSolicitud))
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
            elif op == 2:
                print("Esta opcion es para crear un nuevo usuario. ")
                respuesta = input("¿Desea continuar? Diga (si o no) ")
                if respuesta == "si":
                    nombre = input("Ingrese el nombre del nuevo usuario: ")
                    id = int(input("Ingrese el id del nuevo usuario: "))
                    contra = input("Ingrese la contraseña del nuevo usuario: ")
                    ciudadNacimiento = input("Ingrese la ciudad de nacimiento del nuevo usuario: ")
                    tel = int(input("Ingrese el telefono del nuevo usuario: "))
                    email = input("Ingrese el email del nuevo usuario: ")
                    
                    dd = int(input("Ingrese el dia de nacimiento: "))
                    mm= int(input("Ingrese el mes de nacimiento: "))
                    aa = int(input("Ingrese el año de nacimiento: "))
                    fechita = Fecha(dd, mm, aa)
                    
                    calle = input("Ingrese la calle de la direccion: ")
                    nomenclatura = input("Ingrese la nomenclatura de la direccion: ")
                    barrio = input("Ingrese el barrio de la direccion: ")
                    edificio = input("Ingrese el edificio de la direccion: ")
                    apto = input("Ingrese el apto de la direccion: ")
                    
                    nuevaDireccion = Direccion(calle, nomenclatura, barrio, ciudadNacimiento, edificio, apto)
                                   
                    tipo = input("Ingrese el tipo de usuario: ").lower()
                    if tipo == "investigador":
                        nuevoUsuario = Investigador(nombre, id, ciudadNacimiento, tel, email, contra, [])
                        nuevoUsuario.setFechaNacimiento(fechita)
                        nuevoUsuario.setDir(nuevaDireccion)
                        
                        with open("Textos/Password.txt", "a") as archivo:
                            archivo.write("\n"+str(id)+" "+contra+" "+tipo)
                            
                    else:
                        nuevoUsuario = Administrador(nombre, id, ciudadNacimiento, tel, email, contra, [])
                        nuevoUsuario.setFechaNacimiento(fechita)
                        nuevoUsuario.setDir(nuevaDireccion)
                        
                        with open("Textos/Password.txt", "a") as archivo:
                            archivo.write("\n"+str(id)+" "+contra+" "+tipo)
                        
                    listaDeTodo.addLast(nuevoUsuario)
                    print("El usuario ha sido creado con exito. ")
                    
                    with open("Textos/Empleados.txt", "a") as archivo:
                        if None == listaDeTodo.first().getData():
                            archivo.write(str(nuevoUsuario))
                        else:
                            archivo.write("\n"+str(nuevoUsuario))
                    menus()
                elif respuesta == "no":
                    print("Opcion equivocada")
                    menus()
                else:
                    sys.exit()
                    
            elif op == 3:
                print("Esta opcion es para eliminar un usuario. ")
                respuesta = input("¿Desea continuar? Diga (si o no) ")
                if respuesta == "si":
                    id = int(input("Ingrese el id del usuario a eliminar: "))
                    temp = listaDeTodo.first()
                    
                    empleados_data = []
                    
                    with open("Textos/Empleados.txt", "r") as arch:
                        empleados_data = arch.readlines()
                    
                    with open("Textos/Empleados.txt", "w") as arch:
                        for empleados in empleados_data:
                            g = empleados.split()
                            if int(g[1]) != id:
                                arch.write(empleados)
                                
                    with open("Textos/Password.txt", "w") as archivo:
                        temp = pss.First()
                        while temp is not None:
                            contras = temp.getData()
                            if int(contras[0]) != id:
                                archivo.write(" ".join(map(str, contras)) + "\n")
                            temp = temp.getNext()
                            
                                
                        
                    while temp != None and (temp != listaDeTodo.last() or temp == listaDeTodo.last()):
                        if id == temp.getData().getId():
                            listaDeTodo.remove(temp)
                            print("El usuario ha sido eliminado con exito. ")
                        if temp == None:
                            pass
                        else:
                            temp = temp.getNext()
                    menus()
                elif respuesta == "no":
                    print("Opcion equivocada")
                    menus()
                else:
                    sys.exit()
                
            elif op == 13:
                sys.exit()
            
            
    menus()

    #with open("Textos/Empleado.txt", "r") as archivo:
    #    for linea in archivo:
    #        listaNueva.append(Investigador.from_string(linea))
            

