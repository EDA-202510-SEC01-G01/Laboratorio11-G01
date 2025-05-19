#Importar estructuras necesarias, Se hizo un resumen pero hay detalles no documentados previos a la implementacion.
from DataStructures.Map import map_linear_probing as mp
from DataStructures.Graph import vertex as v
from DataStructures.Graph import edge as e

def new_graph(order): 
    rst={
        "vertices": mp.new_map(order, 0.5), 
        "num_edges": 0
        }
    return rst
    
def insert_vertex(my_graph, key_u, info_u): 
    value = v.new_vertex(key_u, info_u)
    mp.put(my_graph["vertices"], key_u, value)
    return my_graph

def update_vertex_info(my_graph, key_u, new_info_u):
    if contains_vertex(my_graph, key_u):
        vertex = mp.get(my_graph["vertices"], key_u)
        vertex["value"] = new_info_u
        return my_graph
    else:
        return None

def remove_vertex(my_graph, key_u):  
    if contains_vertex(my_graph, key_u):
        keys = mp.key_set(my_graph['vertices'])
        for k in keys:
            vertex = mp.get(my_graph['vertices'], k)
            if mp.contains(vertex['adjacents'], key_u):
                mp.remove(vertex['adjacents'], key_u)
                my_graph['num_edges'] -= 1
        vertex_removed = mp.get(my_graph["vertices"], key_u)
        my_graph['num_edges'] -= mp.size(vertex_removed['adjacents'])
        my_graph["vertices"] = mp.remove(my_graph["vertices"], key_u)
    return my_graph

def add_edge(my_graph, key_u, key_v, weight = 1.0):  
    if contains_vertex(my_graph, key_u) and contains_vertex(my_graph, key_v):
        vertex_u = mp.get(my_graph["vertices"], key_u)
        if mp.contains(vertex_u["adjacents"], key_v):
            edge = mp.get(vertex_u["adjacents"], key_v)
            edge["weight"] = weight
            mp.put(vertex_u["adjacents"], key_v, edge)
        else:
            new_edge = e.new_edge(key_v, weight)
            mp.put(vertex_u["adjacents"], key_v, new_edge)
            my_graph["num_edges"] += 1
        mp.put(my_graph["vertices"], key_u, vertex_u)
        return my_graph
    else:
        raise Exception("Uno o ambos vértices no existen")
    
def order(my_graph):
    return my_graph["vertices"]["size"]
    
def size(my_graph): 
    return my_graph["num_edges"]
    
def vertices(my_graph): 
    return mp.key_set(my_graph['vertices'])
    
def degree(my_graph, key_u):
    new_info=mp.get(my_graph["vertices"], key_u)
    return mp.size(new_info["adjacents"])
    
def get_edge(my_graph, key_u, key_v): 
    v1 = mp.get(my_graph['vertices'], key_u)
    if v1 is not None:
        v2 = mp.get(v1['adjacents'], key_v)
        if v2  is not None:
            return v2
    raise Exception ('El arco no existe entre ambos vertices')
def get_vertex_information(my_graph, key_u): #retorna key_u
    v1 = mp.get(my_graph['vertices'], key_u)
    if v1:
        return v1
    raise Exception("El vertice no existe")
def contains_vertex(my_graph, key_u): 
    v1 = mp.get(my_graph['vertices'], key_u)
    if v1:
        return True
    else:
        return False
def adjacents(my_graph, key_u):
    v1 = mp.get(my_graph['vertices'], key_u)
    if v1:
        return mp.key_set(v1['adjacents'])
    else: 
        raise Exception ('El vertice no existe')
def edges_vertex(my_graph, key_u): 
    v1 = mp.get(my_graph['vertices'], key_u)
    if v1:
        return mp.value_set(v1['adjacents'])
    else: 
        raise Exception ('El vertice no existe')
def get_vertex(my_graph, key_u): #retorna el valor(value) de key_u
    v1 = mp.get(my_graph['vertices'], key_u)
    if v1:
        return v1['value']
    else:
        raise Exception ('El vertice no existe')

