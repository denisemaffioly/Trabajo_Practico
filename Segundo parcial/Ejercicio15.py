from lista_lista import Lista
from random import randint


class Entrenador:
    def __init__(self, nombre, ct_ganados=0, cb_perdidas=0, cb_ganadas=0):
        self.nombre = nombre
        self.ct_ganados = ct_ganados
        self.cb_perdidas = cb_perdidas
        self.cb_ganadas = cb_ganadas

    def __str__(self):
        return f"{self.nombre} --> ctg:{self.ct_ganados}-cbg{self.cb_ganadas}-cbp{self.cb_perdidas}"


class Pokemon:
    def __init__(self, nombre, tipo, nivel=1, subtipo=None):
        self.nombre = nombre
        self.nivel = nivel
        self.tipo = tipo
        self.subtipo = subtipo

    def __str__(self):
        return f"{self.nombre}-{self.nivel}-{self.tipo}-{self.subtipo}"


e1 = Entrenador(
    "Matias",
    ct_ganados=randint(1, 10),
    cb_ganadas=randint(1, 10),
    cb_perdidas=randint(1, 10),
)
e2 = Entrenador(
    "Francisco",
    ct_ganados=randint(1, 10),
    cb_ganadas=randint(1, 10),
    cb_perdidas=randint(1, 10),
)
e3 = Entrenador(
    "Maria",
    ct_ganados=randint(1, 10),
    cb_ganadas=randint(1, 10),
    cb_perdidas=randint(1, 10),
)
e4 = Entrenador(
    "Paula",
    ct_ganados=randint(1, 10),
    cb_ganadas=randint(1, 10),
    cb_perdidas=randint(1, 10),
)

entrenadores = [e1, e2, e3, e4]

lista_entrenadores = Lista()
for entrenador in entrenadores:
    lista_entrenadores.insert(entrenador, "nombre")

pokemons = [
    Pokemon("Pikachu", "Eléctrico", randint(1, 20)),
    Pokemon("Jolteon", "Eléctrico", randint(1, 20)),
    Pokemon("Vaporeon", "Agua", randint(1, 20)),
    Pokemon("Flareon", "Fuego", randint(1, 20)),
    Pokemon("Leafeon", "Planta", randint(1, 20)),
]

for pokemon in pokemons:
    numero_entrenador = randint(0, lista_entrenadores.size() - 1)
    entrenador = lista_entrenadores.get_element_by_index(numero_entrenador)
    entrenador[1].insert(pokemon, "nombre")

lista_entrenadores.barrido_entrenadores()


posicion = lista_entrenadores.search("Maria", "nombre")
if posicion is not None:
    entrenador, sublista = lista_entrenadores.get_element_by_index(posicion)
    cantidad_pokemons = sublista.size()
    print(f"{entrenador.nombre} tiene {cantidad_pokemons} pokemons")
else:
    print(f"no se encontro al entrenador")


for entrenador in entrenadores:
    if entrenador.ct_ganados > 3:
        print(f"entrenadores que ganaron mas de 3 torneos", entrenador)

mayor_entrenador = None
mayor_torneos_ganados = 0

for pos in range(lista_entrenadores.size()):
    entrenador, sublista = lista_entrenadores.get_element_by_index(pos)
    if entrenador.ct_ganados > mayor_torneos_ganados:
        mayor_torneos_ganados = entrenador.ct_ganados
        mayor_entrenador = entrenador

if mayor_entrenador is not None:
    mayor_pokemon = None
    mayor_nivel = 0

    for pos in range(sublista.size()):
        pokemon = sublista.get_element_by_index(pos)
        if pokemon.nivel > mayor_nivel:
            mayor_nivel = pokemon.nivel
            mayor_pokemon = pokemon

    if mayor_pokemon is not None:
        print(
            f"El Pokémon de mayor nivel del entrenador {mayor_entrenador.nombre} es {mayor_pokemon.nombre} {mayor_pokemon.nivel}"
        )
    else:
        print(f"El entrenador {mayor_entrenador.nombre} no tiene Pokémon en su lista.")
else:
    print("No se encontraron entrenadores con torneos ganados.")

nombre_entrenador = "Maria"  

pos = lista_entrenadores.search(nombre_entrenador, "nombre")
if pos is not None:
    entrenador, sublista = lista_entrenadores.get_element_by_index(pos)

    print(f"Datos del entrenador {entrenador.nombre}:")
    print(f"Cantidad de torneos ganados: {entrenador.ct_ganados}")
    print(f"Cantidad de batallas perdidas: {entrenador.cb_perdidas}")
    print(f"Cantidad de batallas ganadas: {entrenador.cb_ganadas}")

    print("Pokémon del entrenador:")
    for pos_pokemon in range(sublista.size()):
        pokemon = sublista.get_element_by_index(pos_pokemon)
        print(f"Nombre: {pokemon.nombre}")
        print(f"Nivel: {pokemon.nivel}")
        print(f"Tipo: {pokemon.tipo}")
        print(f"Subtipo: {pokemon.subtipo}")
        print()
else:
    print(f"No se encontró un entrenador con el nombre {nombre_entrenador}.")

for i in range(lista_entrenadores.size()):
    entrenador, sublista = lista_entrenadores.get_element_by_index(i)

    total_batallas = entrenador.cb_perdidas + entrenador.cb_ganadas

    if total_batallas > 0:
        porcentaje_ganados = (entrenador.cb_ganadas / total_batallas) * 100

        if porcentaje_ganados > 79:
            print(
                f"{entrenador.nombre} tiene un porcentaje de batallas ganadas del {porcentaje_ganados}%"
            )
    else:
        print(f"{entrenador.nombre} no ha tenido ninguna batalla.")


tipos_a_verificar = ["fuego", "planta", "agua", "volador"]
entrenadores_con_tipos = []
for pos in range(lista_entrenadores.size()):
    entrenador, sublista = lista_entrenadores.get_element_by_index(pos)
    tiene_tipos = False

    for pos_pokemon in range(sublista.size()):
        pokemon = sublista.get_element_by_index(pos_pokemon)
        if pokemon.tipo.lower() in tipos_a_verificar or (
            pokemon.subtipo and pokemon.subtipo.lower() in tipos_a_verificar
        ):
            tiene_tipos = True
            break 

    if tiene_tipos:
        entrenadores_con_tipos.append(entrenador)

if len(entrenadores_con_tipos) > 0:
    print("Entrenadores con Pokémon de tipo fuego y planta o agua/volador:")
    for entrenador in entrenadores_con_tipos:
        print(entrenador.nombre)
else:
    print("Ningún entrenador cumple con los criterios.")

nombre_entrenador = "Paula"

pos = lista_entrenadores.search(nombre_entrenador, "nombre")
if pos is not None:
    entrenador, sublista = lista_entrenadores.get_element_by_index(pos)

    if sublista.size() > 0:
        total_nivel = 0
        for pos_pokemon in range(sublista.size()):
            pokemon = sublista.get_element_by_index(pos_pokemon)
            total_nivel += pokemon.nivel

        promedio_nivel = total_nivel / sublista.size()

        print(
            f"El promedio de nivel de los Pokémon de {entrenador.nombre} es: {promedio_nivel:.2f}"
        )
    else:
        print(f"{entrenador.nombre} no tiene Pokémon en su lista.")
else:
    print(f"No se encontró un entrenador con el nombre {nombre_entrenador}.")

nombre_pokemon = "Pikachu" 

cantidad_entrenadores_con_pokemon = 0

for pos_entrenador in range(lista_entrenadores.size()):
    entrenador, sublista = lista_entrenadores.get_element_by_index(pos_entrenador)
    for pos_pokemon in range(sublista.size()):
        pokemon = sublista.get_element_by_index(pos_pokemon)
        if pokemon.nombre == nombre_pokemon:
            cantidad_entrenadores_con_pokemon += 1

print(
    f"{cantidad_entrenadores_con_pokemon} entrenadores tienen a {nombre_pokemon} en sus listas."
)

pokemon_repetidos = {}

for pos_entrenador in range(lista_entrenadores.size()):
    entrenador, sublista = lista_entrenadores.get_element_by_index(pos_entrenador)

    for pos_pokemon in range(sublista.size()):
        pokemon = sublista.get_element_by_index(pos_pokemon)

        if pokemon.nombre in pokemon_repetidos:
            pokemon_repetidos[pokemon.nombre] += 1
        else:
            pokemon_repetidos[pokemon.nombre] = 1

for pos_entrenador in range(lista_entrenadores.size()):
    entrenador, sublista = lista_entrenadores.get_element_by_index(pos_entrenador)
    tiene_pokemon_repetido = False

    for pos_pokemon in range(sublista.size()):
        pokemon = sublista.get_element_by_index(pos_pokemon)
        if pokemon_repetidos[pokemon.nombre] > 1:
            tiene_pokemon_repetido = True
            break

    if tiene_pokemon_repetido:
        print(f"{entrenador.nombre} tiene Pokémon repetidos en su lista.")

nombres_pokemon_verificar = ["Tyrantrum", "Terrakion", "Wingull"]

entrenadores_con_pokemon_especificado = []

for i in range(lista_entrenadores.size()):
    entrenador, sublista = lista_entrenadores.get_element_by_index(i)

    for pos_pokemon in range(sublista.size()):
        pokemon = sublista.get_element_by_index(pos_pokemon)
        if pokemon.nombre in nombres_pokemon_verificar:
            entrenadores_con_pokemon_especificado.append(entrenador)

if entrenadores_con_pokemon_especificado:
    print("Entrenadores con uno de los siguientes Pokémon:")
    for entrenador in entrenadores_con_pokemon_especificado:
        print(entrenador.nombre)
else:
    print("Ningún entrenador tiene los Pokémon especificados.")


nombre_entrenador = "Maria"
nombre_pokemon = "Pikachu"

pos_entrenador = lista_entrenadores.search(nombre_entrenador, "nombre")

if pos_entrenador is not None:
    entrenador, sublista_pokemon = lista_entrenadores.get_element_by_index(
        pos_entrenador
    )

    pos_pokemon = sublista_pokemon.search(nombre_pokemon, "nombre")

    if pos_pokemon is not None:
        pokemon = sublista_pokemon.get_element_by_index(pos_pokemon)
        print(f"Entrenador {entrenador.nombre} tiene al Pokémon {pokemon.nombre}:")
        print(f"Datos del entrenador:")
        print(f"Cantidad de torneos ganados: {entrenador.ct_ganados}")
        print(f"Cantidad de batallas perdidas: {entrenador.cb_perdidas}")
        print(f"Cantidad de batallas ganadas: {entrenador.cb_ganadas}")
        print(f"Datos del Pokémon:")
        print(f"Nivel: {pokemon.nivel}")
        print(f"Tipo: {pokemon.tipo}")
        print(f"Subtipo: {pokemon.subtipo}")
    else:
        print(
            f"El entrenador {entrenador.nombre} no tiene al Pokémon {nombre_pokemon}."
        )
else:
    print(f"No se encontró un entrenador con el nombre {nombre_entrenador}.")
