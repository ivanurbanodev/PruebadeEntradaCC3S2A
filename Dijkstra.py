import heapq

def dijkstra(grafo, inicio):
    # iniciamos las distancias los nodos como infinito, menos el inicial 
    distancias = {nodo: float('inf') for nodo in grafo}
    distancias[inicio] = 0
    
    # creamos una cola de prioridad que tendra las distancias actuales y el nodo correspondiente
    cola_prioridad = [(0, inicio)]  # (distancia, nodo)

    while cola_prioridad:
        # quitamos el nodo con la menor distancia
        distancia_actual, nodo_actual = heapq.heappop(cola_prioridad)

        # si la distancia quitada es mayor que la registrada entonces ignoramos esta ruta
        if distancia_actual > distancias[nodo_actual]:
            continue

        # recorremos los vecinos del nodo 
        for vecino, peso in grafo[nodo_actual].items():
            # calculamos la distancia desde el nodo actual hasta el vecino
            distancia = distancia_actual + peso

            # sii esta distancia es menor que la distancia conocida enotnces la actualizamos
            if distancia < distancias[vecino]:
                distancias[vecino] = distancia
                # añadimos el vecino a la cola de prioridad para otras busquedas
                heapq.heappush(cola_prioridad, (distancia, vecino))

    # Retornamos el diccionario que contiene la distancia mínima desde el nodo inicial a los otros nodo
    return distancias
