class Grafo:
    def __init__(self):
        self.vertices = {}

    def insertar_vértice(self, ambiente):
        self.vertices[ambiente] = []

    def insertar_arista(self, origen, destino, peso):
        if origen in self.vertices and destino in self.vertices:
            arista = {'destino': destino, 'peso': peso}
            self.vertices[origen].append(arista)
            self.vertices[destino].append({'destino': origen, 'peso': peso})

    def obtener_arbol_expansion_minima(self):
        arbol_expansion_minima = Grafo()
        conjunto_conexo = {}

        for vertice in self.vertices:
            conjunto_conexo[vertice] = {vertice}

        aristas = []

        for vertice, lista_aristas in self.vertices.items():
            for arista in lista_aristas:
                aristas.append((arista['peso'], vertice, arista['destino']))

        aristas.sort()

        for peso, origen, destino in aristas:
            if destino not in conjunto_conexo[origen]:
                arbol_expansion_minima.insertar_vértice(origen)
                arbol_expansion_minima.insertar_vértice(destino)
                arbol_expansion_minima.insertar_arista(origen, destino, peso)

                conjunto_conexo[origen] |= conjunto_conexo[destino]

                for v in conjunto_conexo[destino]:
                    conjunto_conexo[v] = conjunto_conexo[origen]

        return arbol_expansion_minima

    def dijkstra(self, inicio, destino):
        distancias = {v: float('inf') for v in self.vertices}
        distancias[inicio] = 0
        visitados = set()

        while len(visitados) < len(self.vertices):
            vertice_actual = min((v for v in self.vertices if v not in visitados), key=lambda x: distancias[x])

            visitados.add(vertice_actual)

            for arista in self.vertices[vertice_actual]:
                nueva_distancia = distancias[vertice_actual] + arista['peso']

                if nueva_distancia < distancias[arista['destino']]:
                    distancias[arista['destino']] = nueva_distancia

        return distancias[destino]

# Crear grafo
casa = Grafo()

# a. Crear vértices
ambientes = ["cocina", "comedor", "cochera", "quincho", "baño1", "baño2", "habitación1", "habitación2", "sala_de_estar", "terraza", "patio"]
for ambiente in ambientes:
    casa.insertar_vértice(ambiente)

# b. Cargar aristas
casa.insertar_arista("cocina", "comedor", 3)
casa.insertar_arista("cocina", "habitación1", 5)
# Agregar más aristas según las necesidades

# c. Obtener árbol de expansión mínima
arbol_expansion_minima = casa.obtener_arbol_expansion_minima()

# Calcular la longitud total de cables necesarios
longitud_total_cables = sum(arista['peso'] for lista_aristas in arbol_expansion_minima.vertices.values() for arista in lista_aristas)

print(f"Árbol de expansión mínima: {arbol_expansion_minima.vertices}")
print(f"Longitud total de cables necesarios: {longitud_total_cables} metros")

# d. Determinar camino más corto
habitacion1_a_sala_de_estar = casa.dijkstra("habitación1", "sala_de_estar")

print(f"Camino más corto desde habitación 1 hasta sala de estar: {habitacion1_a_sala_de_estar} metros")