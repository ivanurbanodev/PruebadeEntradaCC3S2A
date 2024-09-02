import heapq

def dijkstra(grafo, inicio):
    # Inicializamos las distancias con infinito
    distancias = {nodo: float('inf') for nodo in grafo}
    distancias[inicio] = 0
    # Creamos una cola de prioridad para seleccionar la ruta más corta
    cola_prioridad = [(0, inicio)]





