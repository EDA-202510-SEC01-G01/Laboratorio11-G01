#Importar estructuras necesarias, Se hizo un resumen pero hay detalles no documentados previos a la implementacion.
from DataStructures.Map import map_linear_probing as mp


def new_graph(order): # Crea un nuevo grafo; Salida: {vertices: Tabla Hash, num_edges: int}
    rst={
        "vertices": mp.new_map(order, 0.5), 
        "num_edges": 0
        }
    return rst
    
def insert_vertex(my_graph, key_u, info_u): #Usar funcion new_vertex de vertex.py y añadirlo a la tabla de hash "vertices"; Salida: Grafo dirigido
    value={"key": key_u, "value":info_u, "adjacents":mp.new_map(1, 0.5)}
    my_graph["vertices"]=mp.put(my_graph["vertices"], key_u, value)
    return my_graph

def update_vertex_info(my_graph, key_u, new_info_u): #Buscar llave, cambiar infor; Salida: Grafo dirigido
    if mp.contains(my_graph["vertices"], key_u) == True:
        return None
    else: 
        my_graph["vertices"]=mp.put(my_graph["vertices"],key_u, new_info_u)
        return my_graph

def remove_vertex(my_graph, key_u): #Busca la llave y la elimina de la tabla
    my_graph["vertices"]=mp.remove(my_graph["vertices"], key_u)
    return my_graph

def add_edge(my_graph, key_u, key_v, weight = 1.0):  #Genera un arco entre v1 y v2, si alguno de los vertices no existe se retorna una excepcion, si el arco existe se modifica su peso, 
    if (mp.contains(my_graph["vertices"], key_u) == True) and (mp.contains(my_graph["vertices"], key_v) == True):
        new_info=mp.get(my_graph["vertices"], key_u)
        value={"to": key_v, "weight": weight}
        mp.put(new_info["adjacents"], key_v, value)
        mp.put(my_graph["vertices"], key_u, new_info)
        my_graph["num_edges"]+=1
        return my_graph
    else:
        raise Exception("El vertice u no existe")
    
def order(grafo):#numero de vetices del grafo
    pass
def size(grafo): #numero de arcos del grafo
    pass
def vertices(grafo): #lista de llaves de todos los vertices
    pass
def degree(grafo, key): #grado de la llave key(numero de arcos adyacentes)
    pass
def get_edge(grafo, vertice1, vertice2): #Arco entre v1 y v2
    pass
def get_vertex_information(grafo, vertice): #info de v
    pass
def contains_vertex(grafo, vertice): #Determina si el vertice existe en el grafo
    pass
def adjacents(grafo, vertice): #lista de adyacentes de v
    pass
def edges_vertex(grafo, vertice): #lista de arcos asociados
    pass
def get_vertex(grafo, vertice): #retorna el valor del vertice
    pass

