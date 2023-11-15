from Ejercicio2 import Grafo
from random import randint

grafo = Grafo(dirigido=False)


personajesStwrs= ["Luke Skywalker", "Darth Vader", "Yoda", "Boba Fett", "C-3PO", "Leia", "Rey", "Kylo Ren", "Chewbacca", "Han Solo", "R2-D2", "BB-8"]:


for i in personajesStwrs:
    grafo.insert_vertice(i)

j=0


for i in personajesStwrs:
    posicion  = grafo.search_vertice(i)
    punto = grafo.get_element_by_index(posicion )
    if punto[1].size() < 4:
        k = 0
        while j == 0:
            if k >= len(personajesStwrs):
                j=1
            else:
                place = personajesStwrs[k]
                posicionb = grafo.search_vertice(place)
                puntob = grafo.get_element_by_index(posicionb)
                checker = grafo.is_adyacent(punto[0],puntob[0])
                if puntob[1].size() < 3 and punto[0] != puntob[0] and checker == False: 
                    value = randint(1, 20)
                    grafo.insert_arist(punto[0], puntob[0], value)
                    if punto[1].size() == 3:
                        j=1
                k += 1
        j=0

grafo.barrido()

i=0

tree_min = grafo.kruskal()

for tree in tree_min:
    print("Arbol Minimo")
    for nodo in tree.split(";"):
        value = nodo.split("-")
        print(nodo)
        if value[0]=="Yoda" or value[1]=="Yoda":
            i = 1
    if i ==1:
        print("Yoda existe en el arbol minimo")
        
def maximo_episodios(arbol_maximo):
    contador = 0
    puntero = arbol_maximo.raiz
    while puntero is not None:
        personajes = puntero.arista.split("-")
        numero_episodios = len(set(personajes[0].split(",")) & set(personajes[1].split(",")))
        if numero_episodios > contador:
            contador = numero_episodios
            personajes_maximos = personajes
        puntero = puntero.siguiente
    return contador, personajes_maximos

contador, personajes_maximos = maximo_episodios(tree_min)
print(f"El número máximo de episodios compartidos es {contador}. Los personajes que los comparten son {personajes_maximos}")
