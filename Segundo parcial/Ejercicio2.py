grafo = {
    "Luke Skywalker": {"Leia Organa": 5, "Han Solo": 3},
    "Leia Organa": {"Luke Skywalker": 5, "Han Solo": 5},
    "Han Solo": {"Luke Skywalker": 3, "Leia Organa": 5},
}
def kruskal_mst(grafo):
    aristas = []

    for personaje1, relaciones in grafo.items():
        for personaje2, episodios in relaciones.items():
            aristas.append((personaje1, personaje2, episodios))

    aristas.sort(key=lambda x: x[2])

    mst = {}
    conjuntos_disjuntos = {personaje: personaje for personaje in grafo}

    for arista in aristas:
        personaje1, personaje2, episodios = arista

        if conjuntos_disjuntos[personaje1] != conjuntos_disjuntos[personaje2]:
            mst[(personaje1, personaje2)] = episodios
            conjunto1 = conjuntos_disjuntos[personaje1]
            conjunto2 = conjuntos_disjuntos[personaje2]

            for personaje, conjunto in conjuntos_disjuntos.items():
                if conjunto == conjunto1:
                    conjuntos_disjuntos[personaje] = conjunto2

    return mst

mst = kruskal_mst(grafo)
print("Árbol de Expansión Mínimo:")
print(mst)

max_episodios = 0
personajes_max = []

for personaje1, relaciones in grafo.items():
    for personaje2, episodios in relaciones.items():
        if episodios > max_episodios:
            max_episodios = episodios
            personajes_max = [personaje1, personaje2]
        elif episodios == max_episodios:
            personajes_max.append(personaje1)
            personajes_max.append(personaje2)

print("Máximo de episodios compartidos:", max_episodios)
print("Personajes correspondientes:", personajes_max)


def kruskal_mst(grafo):
    grafo_ordenado = sorted(grafo, key=lambda x: x[2])  
    mst = []
    conjuntos_disjuntos = {}

    def encontrar_conjunto(personaje):
        if personaje not in conjuntos_disjuntos:
            return personaje
        return encontrar_conjunto(conjuntos_disjuntos[personaje])

    for arista in grafo_ordenado:
        personaje1, personaje2, peso = arista
        conjunto1 = encontrar_conjunto(personaje1)
        conjunto2 = encontrar_conjunto(personaje2)

        if conjunto1 != conjunto2:
            mst.append(arista)
            conjuntos_disjuntos[conjunto1] = conjunto2

    return mst

mst = kruskal_mst(grafo)

yoda_presente = any("Yoda" in arista for arista in mst)

if yoda_presente:
    print("El MST contiene a Yoda.")
else:
    print("El MST no contiene a Yoda.")


max_episodios_compartidos = 0
personaje1_max = None
personaje2_max = None

for arista in grafo:
    personaje1, personaje2, episodios = arista
    if episodios > max_episodios_compartidos:
        max_episodios_compartidos = episodios
        personaje1_max = personaje1
        personaje2_max = personaje2

if personaje1_max and personaje2_max:
    print(f"El número máximo de episodios compartidos es {max_episodios_compartidos}, entre {personaje1_max} y {personaje2_max}.")
else:
    print("No se encontraron personajes que compartan episodios en el grafo.")

for personaje, relaciones in grafo.items():
    print(f"{personaje}: {relaciones}")