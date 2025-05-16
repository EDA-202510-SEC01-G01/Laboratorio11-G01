from DataStructures.List import array_list as ar

def new_queue():
    
    return ar.new_list()

def is_empty(my_list):
    if my_list["size"]==0:
        return True
    else:
        return False
def enqueue(my_list, new_element):
    return ar.add_last(my_list, new_element)

def dequeue(my_list):
    return ar.remove_first(my_list)
    
def peek(my_list):
    return ar.first_element(my_list)

def is_empty(my_list):
    return ar.is_empty(my_list)

def size(my_list):
    return ar.size(my_list)