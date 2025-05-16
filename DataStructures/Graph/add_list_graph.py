#Importar estructuras necesarias, Se hizo un resumen pero hay detalles no documentados previos a la implementacion.



def new_graph(): # Crea un nuevo grafo; Salida: {vertices: Tabla Hash, num_edges: int}
    """{
    'vertices': {
        'prime': 109345121,
        'capacity': 3,
        'scale': 1,
        'shift': 0,
        'table': {
            'elements': [
                {
                    'key': None,
                    'value': None
                },
                {
                    'key': None,
                    'value': None
                },
                {
                    'key': None,
                    'value': None
                }
            ],
            'size': 3
        },
        'current_factor': 0,
        'limit_factor': 0.5,
        'size': 0
    },
    'num_edges': 0
}"""
    pass
def insert_vertex(grafo, key, info): #Usar funcion new_vertex de vertex.py y añadirlo a la tabla de hash "vertices"; Salida: Grafo dirigido
    pass
def update_vertex_info(grafo, key, nueva_info): #Buscar llave, cambiar infor; Salida: Grafo dirigido
    pass
def remove_vertex(grafo, key): #Busca la llave y la elimina de la tabla
    pass
def add_edge(grafo, vertice1, vertice2, weight = 1.0):  #Genera un arco entre v1 y v2, si alguno de los vertices no existe se retorna una excepcion, si el arco existe se modifica su peso, 
    pass
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

