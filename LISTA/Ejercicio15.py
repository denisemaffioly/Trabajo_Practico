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

# Crear lista secundaria de Pokémon
pokemons = [
    Pokemon("Pikachu", "Eléctrico", randint(1, 20)),
    Pokemon("Jolteon", "Eléctrico", randint(1, 20)),
    Pokemon("Vaporeon", "Agua", randint(1, 20)),
    Pokemon("Flareon", "Fuego", randint(1, 20)),
    Pokemon("Leafeon", "Planta", randint(1, 20)),
]

# Asignar aleatoriamente los Pokémon a los entrenadores
for pokemon in pokemons:
    numero_entrenador = randint(0, lista_entrenadores.size() - 1)
    entrenador = lista_entrenadores.get_element_by_index(numero_entrenador)
    entrenador[1].insert(pokemon, "nombre")

# Mostrar entrenadores y sus Pokémon
lista_entrenadores.barrido_entrenadores()

# a- cantidad de pokemon de los entrenadores

posicion = lista_entrenadores.search("Maria", "nombre")
if posicion is not None:
    entrenador, sublista = lista_entrenadores.get_element_by_index(posicion)
    cantidad_pokemons = sublista.size()
    print(f"{entrenador.nombre} tiene {cantidad_pokemons} pokemons")
else:
    print(f"no se encontro al entrenador")


# b-listar entrenadores que ganaron mas de tres torneos
for entrenador in entrenadores:
    if entrenador.ct_ganados > 3:
        print(f"entrenadores que ganaron mas de 3 torneos", entrenador)

# c. el Pokémon de mayor nivel del entrenador con mayor cantidad de torneos ganados;
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
# d!
nombre_entrenador = "Maria"  # Cambia esto al nombre del entrenador que desees mostrar

# Buscar al entrenador por su nombre
pos = lista_entrenadores.search(nombre_entrenador, "nombre")
if pos is not None:
    # Obtener los datos del entrenador y su lista de Pokémon
    entrenador, sublista = lista_entrenadores.get_element_by_index(pos)

    # Mostrar los datos del entrenador
    print(f"Datos del entrenador {entrenador.nombre}:")
    print(f"Cantidad de torneos ganados: {entrenador.ct_ganados}")
    print(f"Cantidad de batallas perdidas: {entrenador.cb_perdidas}")
    print(f"Cantidad de batallas ganadas: {entrenador.cb_ganadas}")

    # Mostrar los datos de sus Pokémon
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

# e. Mostrar los entrenadores cuyo porcentaje de batallas ganados sea mayor al 79 %
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


# f. los entrenadores que tengan Pokémons de tipo fuego y planta o agua/volador
tipos_a_verificar = ["fuego", "planta", "agua", "volador"]
# Lista para almacenar a los entrenadores que cumplen con los criterios
entrenadores_con_tipos = []
# Recorrer la lista de entrenadores
for pos in range(lista_entrenadores.size()):
    entrenador, sublista = lista_entrenadores.get_element_by_index(pos)
    tiene_tipos = False

    # Recorrer la lista de Pokémon del entrenador
    for pos_pokemon in range(sublista.size()):
        pokemon = sublista.get_element_by_index(pos_pokemon)
        # Verificar si el tipo o subtipo del Pokémon está en la lista de tipos a verificar
        if pokemon.tipo.lower() in tipos_a_verificar or (
            pokemon.subtipo and pokemon.subtipo.lower() in tipos_a_verificar
        ):
            tiene_tipos = True
            break  # Si un Pokémon cumple con los criterios, no es necesario verificar los demás

    # Si el entrenador tiene Pokémon con los tipos/subtipos especificados, agregarlo a la lista
    if tiene_tipos:
        entrenadores_con_tipos.append(entrenador)

# Mostrar los entrenadores que cumplen con los criterios
if len(entrenadores_con_tipos) > 0:
    print("Entrenadores con Pokémon de tipo fuego y planta o agua/volador:")
    for entrenador in entrenadores_con_tipos:
        print(entrenador.nombre)
else:
    print("Ningún entrenador cumple con los criterios.")

# g. el promedio de nivel de los Pokémons de un determinado entrenador;
nombre_entrenador = "Paula"

# Buscar al entrenador por su nombre
pos = lista_entrenadores.search(nombre_entrenador, "nombre")
if pos is not None:
    # Obtener los datos del entrenador y su lista de Pokémon
    entrenador, sublista = lista_entrenadores.get_element_by_index(pos)

    # Verificar si el entrenador tiene Pokémon en su lista
    if sublista.size() > 0:
        # Calcular el promedio de nivel de los Pokémon
        total_nivel = 0
        for pos_pokemon in range(sublista.size()):
            pokemon = sublista.get_element_by_index(pos_pokemon)
            total_nivel += pokemon.nivel

        promedio_nivel = total_nivel / sublista.size()

        # Mostrar el resultado
        print(
            f"El promedio de nivel de los Pokémon de {entrenador.nombre} es: {promedio_nivel:.2f}"
        )
    else:
        print(f"{entrenador.nombre} no tiene Pokémon en su lista.")
else:
    print(f"No se encontró un entrenador con el nombre {nombre_entrenador}.")

# h. determinar cuántos entrenadores tienen a un determinado Pokémon;
nombre_pokemon = "Pikachu"  # Cambia esto al nombre del Pokémon que deseas buscar

# Contador para llevar el registro de entrenadores que tienen al Pokémon
cantidad_entrenadores_con_pokemon = 0

# Recorrer la lista de entrenadores
for pos_entrenador in range(lista_entrenadores.size()):
    entrenador, sublista = lista_entrenadores.get_element_by_index(pos_entrenador)
    # Verificar si el Pokémon está en la lista del entrenador
    for pos_pokemon in range(sublista.size()):
        pokemon = sublista.get_element_by_index(pos_pokemon)
        if pokemon.nombre == nombre_pokemon:
            cantidad_entrenadores_con_pokemon += 1

# Mostrar el resultado
print(
    f"{cantidad_entrenadores_con_pokemon} entrenadores tienen a {nombre_pokemon} en sus listas."
)
# i. mostrar los entrenadores que tienen Pokémons repetidos;
# Crear un diccionario para llevar un registro de los Pokémon y cuántas veces aparecen
pokemon_repetidos = {}

# Recorrer la lista de entrenadores
for pos_entrenador in range(lista_entrenadores.size()):
    entrenador, sublista = lista_entrenadores.get_element_by_index(pos_entrenador)

    # Recorrer la lista de Pokémon del entrenador
    for pos_pokemon in range(sublista.size()):
        pokemon = sublista.get_element_by_index(pos_pokemon)

        # Verificar si el Pokémon ya se encuentra en el diccionario
        if pokemon.nombre in pokemon_repetidos:
            # Incrementar la cuenta si ya existe en el diccionario
            pokemon_repetidos[pokemon.nombre] += 1
        else:
            # Agregar el Pokémon al diccionario si no existe
            pokemon_repetidos[pokemon.nombre] = 1

# Mostrar los entrenadores que tienen Pokémon repetidos
for pos_entrenador in range(lista_entrenadores.size()):
    entrenador, sublista = lista_entrenadores.get_element_by_index(pos_entrenador)
    tiene_pokemon_repetido = False

    # Verificar si alguno de los Pokémon del entrenador se repite
    for pos_pokemon in range(sublista.size()):
        pokemon = sublista.get_element_by_index(pos_pokemon)
        if pokemon_repetidos[pokemon.nombre] > 1:
            tiene_pokemon_repetido = True
            break

    # Mostrar el entrenador si tiene Pokémon repetidos
    if tiene_pokemon_repetido:
        print(f"{entrenador.nombre} tiene Pokémon repetidos en su lista.")
# j. determinar los entrenadores que tengan uno de los siguientes Pokémons: Tyrantrum, Te-rrakion o Wingull;

# Nombres de los Pokémon que deseas verificar
nombres_pokemon_verificar = ["Tyrantrum", "Terrakion", "Wingull"]

# Lista para almacenar los entrenadores que tienen uno de los Pokémon especificados
entrenadores_con_pokemon_especificado = []

# Recorrer la lista de entrenadores
for i in range(lista_entrenadores.size()):
    entrenador, sublista = lista_entrenadores.get_element_by_index(i)

    # Por ejemplo, para recorrer la lista de Pokémon del entrenador
    for pos_pokemon in range(sublista.size()):
        pokemon = sublista.get_element_by_index(pos_pokemon)
        # Verificar si el nombre del Pokémon está en la lista de nombres especificados
        if pokemon.nombre in nombres_pokemon_verificar:
            # Si se encuentra un Pokémon con nombre especificado, agregar el entrenador a la lista
            entrenadores_con_pokemon_especificado.append(entrenador)
            # Romper el bucle interno para evitar agregar al mismo entrenador varias veces

# Mostrar la lista de entrenadores que tienen uno de los Pokémon especificados
if entrenadores_con_pokemon_especificado:
    print("Entrenadores con uno de los siguientes Pokémon:")
    for entrenador in entrenadores_con_pokemon_especificado:
        print(entrenador.nombre)
else:
    print("Ningún entrenador tiene los Pokémon especificados.")

# k!

nombre_entrenador = "Maria"
nombre_pokemon = "Pikachu"

# Buscar al entrenador por su nombre
pos_entrenador = lista_entrenadores.search(nombre_entrenador, "nombre")

if pos_entrenador is not None:
    # Obtener los datos del entrenador y su lista de Pokémon
    entrenador, sublista_pokemon = lista_entrenadores.get_element_by_index(
        pos_entrenador
    )

    # Buscar al Pokémon en la lista de Pokémon del entrenador
    pos_pokemon = sublista_pokemon.search(nombre_pokemon, "nombre")

    if pos_pokemon is not None:
        # Si se encuentra el Pokémon en la lista del entrenador
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
