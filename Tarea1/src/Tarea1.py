# Topological sort

# Algoritmo Topological Sort para gráficas acíclicas dirigidas.
# Primero agregamos el vertice actual, a los vértices visitados
# después para todos los vecinos que no se han visitado; si el vecino no está dentro de visitado, lo visitamos 
# entonces, si todos los vecinos ya están visitados, agregamos el vértice actual a orden
# finalmente, si ninguno de los vertices ha sido visitado, seleccionamos uno nuevo para visitar.
# regresamos orden 

aristas = {"a": ["c", "d"], "b": ["e", "c"], "c": ["d"], "d": [], "e": ["a", "c"]}
vertices = ["a", "b", "c", "d", "e"]

def topological_sort(inicio, visitado, orden):
    actual = inicio
    visitado.append(actual)
    vecinos = aristas[actual]
    
    for vecino in vecinos:
        if vecino not in visitado:
            orden = topological_sort(vecino, visitado, orden)  
    orden.append(actual)
    if len(visitado) != len(vertices):
        for vertice in vertices:
            if vertice not in visitado:
                orden = topological_sort(vertice, visitado, orden)
    
    return orden


if __name__ == "__main__":
    orden = topological_sort("a", [], [])
    print(orden)
