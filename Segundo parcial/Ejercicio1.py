pokemons = [
    {'nombre': 'Bulbasaur', 'numero': 1, 'tipo': ['Planta', 'Veneno']},
    {'nombre': 'Ivysaur', 'numero': 2, 'tipo': ['Planta', 'Veneno']},
    {'nombre': 'Venusaur', 'numero': 3, 'tipo': ['Planta', 'Veneno']},
    {'nombre': 'Charmander', 'numero': 4, 'tipo': ['Fuego']},
    {'nombre': 'Charmeleon', 'numero': 5, 'tipo': ['Fuego']},
    {'nombre': 'Charizard', 'numero': 6, 'tipo': ['Fuego', 'Volador']},
]

import bisect

arbol_nombre = {}
arbol_numero = {}
arbol_tipo = {}

for pokemon in pokemons:
    nombre = pokemon['nombre']
    numero = pokemon['numero']
    tipo = pokemon['tipo']

    if nombre not in arbol_nombre:
        arbol_nombre[nombre] = []

    if numero not in arbol_numero:
        arbol_numero[numero] = []

    for t in tipo:
        if t not in arbol_tipo:
            arbol_tipo[t] = []

        bisect.insort(arbol_nombre[nombre], pokemon)
        bisect.insort(arbol_numero[numero], pokemon)
        bisect.insort(arbol_tipo[t], pokemon)

def buscar_pokemon(nombre, numero):
    resultados = []
    if nombre in arbol_nombre:
        resultados.extend(arbol_nombre[nombre])
    if numero in arbol_numero:
        resultados.extend(arbol_numero[numero])
    return resultados

    def listado_pokemon():
    return [pokemon for num in sorted(arbol_numero.keys()) for pokemon in arbol_numero[num]]

def listado_por_nivel():
    pokemon_por_nivel = {}
    for num in sorted(arbol_numero.keys()):
        for pokemon in arbol_numero[num]:
            nivel = pokemon['nivel']
            if nivel not in pokemon_por_nivel:
                pokemon_por_nivel[nivel] = []
            pokemon_por_nivel[nivel].append(pokemon)
    return pokemon_por_nivel

def buscar_generacion():
    pokemon_generacion = []
    for num in sorted(arbol_numero.keys()):
        for pokemon in arbol_numero[num]:
            if (pokemon['nombre'] == 'Jolteon' and pokemon['generacion'] == 3) or \
               (pokemon['nombre'] == 'Lycanroc' and pokemon['generacion'] == 5) or \
               (pokemon['nombre'] == 'Machamp' and pokemon['generacion'] == 6):
                pokemon_generacion.append(pokemon)
    return pokemon_generacion