import os
from funciones import *

def menu_clientes():
    while True:
        os.system("cls")
        print("Elija una opcion")
        print("1. Crear cliente")
        print("2. Modificar cliente")
        print("3. Listar clientes")
        print("0. Volver al menu principal")
        print("\nOpcion: ", end = '')
        opc = int(input())

        if opc == 0: break
        else: 'Opcion incorrecta, intente nuevamente'