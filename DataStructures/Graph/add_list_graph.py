#Importar estructuras necesarias, Se hizo un resumen pero hay detalles no documentados previos a la implementacion.
from DataStructures.Map import map_linear_probing as mp
from DataStructures.Graph import vertex as v
from DataStructures.Graph import edge as e
from DataStructures.Graph import dfo_structure as dfo_s
from DataStructures.List import array_list as ar
from DataStructures.Queue import queue
from DataStructures.Stack import stack
from DataStructures.Graph import prim_structure as prim_s
from DataStructures.Priority_queue import priority_queue as pq
from DataStructures.Graph import dfo_structure as dfo_s
from DataStructures.List import array_list as ar
from DataStructures.Queue import queue
from DataStructures.Stack import stack
from DataStructures.Graph import prim_structure as prim_s
from DataStructures.Priority_queue import priority_queue as pq

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

def dfs(my_graph, source):
    search = {'source': source, 'marked': None}
    search['marked'] = mp.new_map(order(my_graph), 0.5)
    mp.put(search['marked'], source, {'edge_from': None})
    dfs_vertex(my_graph, source, search)
    return search

def dfs_vertex(my_graph, vertex, visited_map):
    adj=adjacents(my_graph, vertex)
    for i in adj:
        if i in mp.key_set(visited_map["marked"]):
            mp.put(visited_map['marked'], i, {'edge_from': vertex})
            visited_map=dfs_vertex(my_graph, i, visited_map)
    return visited_map

def dfo(my_graph):
    aux_structure=dfo_s.new_dfo_structure(order(my_graph))
    lst_vtcs=vertices(my_graph)
    for i in range(ar.size(lst_vtcs)):
        vertex = ar.get_element(lst_vtcs, i)
        if mp.contains(aux_structure["marked"], vertex)==False:
            queue.enqueue(aux_structure["pre"], vertex)
            dfs_vertex(my_graph, vertex, aux_structure)
            queue.enqueue(aux_structure["post"], vertex)
            stack.push(aux_structure["reversepost"], vertex)
    return aux_structure


def bfs(my_graph, source):
    search = {'source': source, 'marked': None, 'post': ar.new_list()}
    search['marked'] = mp.new_map(order(my_graph), 0.5)
    mp.put(search['marked'], source, {'edge_from': None})
    search = bfs_vertex(my_graph, source, search)
    return search

def bfs_vertex(my_graph, source, visited_map):
    orden = queue.new_queue()
    queue.enqueue(orden, source['key'])
    pred = None
    while queue.is_empty(orden) != True:
        primero = get_vertex_information(my_graph, orden['first'])
        adyacentes = adjacents(my_graph, primero)
        queue.dequeue(orden)
        ar.add_last(visited_map['post'], primero['key'])
        pred = primero
        for vertice in adyacentes:
            if mp.get(visited_map['marked'], vertice) == None:
                mp.put(visited_map['marked'], vertice, {'edge_from': pred})
                queue.enqueue(orden, vertice)
    return visited_map

def prim_mst(my_graph, source):
    search = prim_s.new_prim_structure(source, size(my_graph))
    mp.put(search['marked'], source['key'], source)
    search = prim_vertex(my_graph, source, search)
    return search

def prim_vertex(my_graph, source, visited_map):
    pq.insert(visited_map['pq'], 0, source['key'])
    mp.put(visited_map['edge_from'], source['key'], None)
    mp.put(visited_map['dist_to'], source['key'], 0)
    pred = None
    while pq.is_empty(visited_map['pq']) != True:
        primero = get_vertex_information(my_graph, pq.get_first_priority(visited_map['pq']))
        adyacentes = adjacents(my_graph, primero)
        pq.remove(visited_map['pq'])
        pred = primero
        for vertice in adyacentes:
            edge = get_edge(my_graph, pred['key'], vertice)
            dist = edge['weight']
            if mp.get(visited_map['marked'], vertice) == None:
                mp.put(visited_map['marked'], vertice, True)
                mp.put(visited_map['edge_from'], vertice, pred)
                mp.put(visited_map['dist'], vertice, dist)
                pq.insert(visited_map['pq'], edge['peso'],vertice)
    return visited_map

def dijkstra(graph, source):
    dist_to = mp.new_map(order(graph), 0.5)
    edge_to = mp.new_map(order(graph), 0.5)
    visited = mp.new_map(order(graph), 0.5)
    pqu = pq.new_heap()  

    
    for v in vertices(graph):
        mp.put(dist_to, v, float('inf'))
    mp.put(dist_to, source, 0)

    
    pq.insert(pqu, (0, source))  

    while True:
        try:
            distancia_actual, v = pq.remove(pqu)
        except:
            break 

        
        if mp.get(visited, v) is not None:
            continue
        mp.put(visited, v, True)

        for w in adjacents(graph, v):
            edge = get_edge(graph, v, w)
            peso = edge['weight']
            nueva_dist = distancia_actual + peso

            if mp.get(dist_to, w)['value'] > nueva_dist:
                mp.put(dist_to, w, nueva_dist)
                mp.put(edge_to, w, v)
                pq.insert(pqu, (nueva_dist, w))  

    return dist_to, edge_to

def reconstruir_camino(dest, edge_to):
    camino = []
    actual = dest
    while True:
        camino.insert(0, actual)
        buscado = mp.get(edge_to, actual)
        if buscado is None:
            break
        actual = buscado['value']
    return camino

def dfs(my_graph, source):
    search = {'source': source, 'marked': None}
    search['marked'] = mp.new_map(order(my_graph), 0.5)
    mp.put(search['marked'], source, {'edge_from': None})
    dfs_vertex(my_graph, source, search)
    return search

def dfs_vertex(my_graph, vertex, visited_map):
    adj=adjacents(my_graph, vertex)
    for i in adj:
        if i in mp.key_set(visited_map["marked"]):
            mp.put(visited_map['marked'], i, {'edge_from': vertex})
            visited_map=dfs_vertex(my_graph, i, visited_map)
    return visited_map

def dfo(my_graph):
    aux_structure=dfo_s.new_dfo_structure(order(my_graph))
    lst_vtcs=vertices(my_graph)
    for i in range(ar.size(lst_vtcs)):
        vertex = ar.get_element(lst_vtcs, i)
        if mp.contains(aux_structure["marked"], vertex)==False:
            queue.enqueue(aux_structure["pre"], vertex)
            dfs_vertex(my_graph, vertex, aux_structure)
            queue.enqueue(aux_structure["post"], vertex)
            stack.push(aux_structure["reversepost"], vertex)
    return aux_structure
    
def prim_mst(my_graph, source):
    pass