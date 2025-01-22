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

    with open("Textos/Empleado.txt", "r") as archivo:
        
