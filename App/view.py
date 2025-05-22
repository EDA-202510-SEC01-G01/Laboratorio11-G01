"""
 * Copyright 2020, Departamento de sistemas y Computación
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 * Contribución de:
 *
 * Dario Correal
 *
 """


import sys
import threading
from App import logic

"""
La vista se encarga de la interacción con el usuario.
Presenta el menu de opciones  y  por cada seleccion
hace la solicitud al controlador para ejecutar la
operación seleccionada.
"""

# ___________________________________________________
#  Variables
# ___________________________________________________


servicefile = 'bus_routes_14000.csv'
initialStation = None

# ___________________________________________________
#  Menu principal
# ___________________________________________________


def print_menu():
    print("\n")
    print("*******************************************")
    print("Bienvenido")
    print("1- Inicializar Analizador")
    print("2- Cargar información de buses de singapur:")
    print("3- Calcular componentes conectados:")
    print("4- Establecer estacion base:")
    print("5- Hay camino entre base y estacion:")
    print("6- Ruta de costo minimo desde la estacion base y estacion:")
    print("7- Estacion que sirve a más rutas:Estacion que sirve a más rutas:")
    print("8- Existe un camino de bisqueda entre la estacion base y estacion destino:")
    print("9- Ruta de busqueda entre la estacion base y la estacion destino")
    print("0- Salir")
    print("*******************************************")


def option_two(cont):
    print("\nCargando información de transporte de singapur ....")
    logic.load_services(cont, servicefile)
    numedges = logic.total_connections(cont)
    numvertex = logic.total_stops(cont)
    print('Numero de vertices: ' + str(numvertex))
    print('Numero de arcos: ' + str(numedges))
    print('El limite de recursion actual: ' + str(sys.getrecursionlimit()))


"""Por falta de tiempo envia solo con la implementacion del grafo asegurando que la informacion carga correctamente dentro de la estructura"""
    


def option_three(cont):
    print('Calculando componentes conectados') #Con DFO calcular componentes conectados
    
def option_four(cont, base):
    print('Base instaurada correctamente')
    puede = logic.set_station(cont, base)
    if puede == True:
        global base_g
        base_g = base
    else:
        print('Pruebe nuevamente')
def option_five(cont, base):
    logic.camino_base_estacion() #Con dfs verificar si existe camino entre base y estacion 
def option_six(cont, base):
    logic.camino_costo_minimo() #Con dikjstra generar camino de costo minimo 

def option_seven(cont):
    logic.estacion_mas_rutas() #No sabemos bien como
    
def option_eight(cont):
    logic.search_path() #con algun algoritmo de recorrido modificar el retorno

def option_eight(cont):
    logic.search_path() #con algun algoritmo de recorrido modificar el retorno
"""
Menu principal
"""


def main():
    working = True
    while working:
        print_menu()
        inputs = input('Seleccione una opción para continuar\n>')

        if int(inputs[0]) == 1:
            print("\nInicializando....")
            # cont es el controlador que se usará de acá en adelante
            cont = logic.init()
        elif int(inputs[0]) == 2:
            option_two(cont)
        elif int(inputs[0]) == 3:
            option_three(cont)
        elif int(inputs[0]) == 4:
            option_four(cont)
        elif int(inputs[0]) == 5:
            option_five(cont, base_g)
        elif int(inputs[0]) == 6:
            option_six(cont)
        elif int(inputs[0]) == 7:
            option_seven(cont)
        elif int(inputs[0]) == 8:
            option_eight(cont)
        elif int(inputs[0]) == 9:
            option_nine(cont)
        else:
            working = False
            print("Saliendo...")
    sys.exit(0)


if __name__ == "__main__":
    threading.stack_size(67108864)  # 64MB stack
    sys.setrecursionlimit(2 ** 20)
    thread = threading.Thread(target=main)
    thread.start()
