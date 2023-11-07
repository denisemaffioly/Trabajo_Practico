class Node:
    def __init__(self, key, value):
        self.left = None
        self.right = None
        self.key = key
        self.value = value

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert_node(self, key, value):
        self.root = self._insert(self.root, key, value)

    def _insert(self, root, key, value):
        if root is None:
            return Node(key, value)
        if key < root.key:
            root.left = self._insert(root.left, key, value)
        elif key > root.key:
            root.right = self._insert(root.right, key, value)
        return root

    def in_order_traversal(self):
        result = []
        self._in_order(self.root, result)
        return result

    def _in_order(self, node, result):
        if node:
            self._in_order(node.left, result)
            result.append((node.key, node.value))
            self._in_order(node.right, result)

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, node, key):
        if node is None:
            return None
        if key == node.key:
            return node.value
        if key < node.key:
            return self._search(node.left, key)
        return self._search(node.right, key)

arbolNombre = BinaryTree()
arbolNumero = BinaryTree()
arbolTipo = BinaryTree()

listaPokemon = [
    {'nombre': 'a', 'numero': 123, 'tipo': 'electrico'},
    {'nombre': 'b', 'numero': 4, 'tipo': 'oscuro'},
    {'nombre': 'c', 'numero': 5, 'tipo': 'roca'},
    {'nombre': 'd', 'numero': 8, 'tipo': 'veneno'},
    {'nombre': 'e', 'numero': 9, 'tipo': 'lucha'},
    {'nombre': 'f', 'numero': 12, 'tipo': 'acero'},
    {'nombre': 'e', 'numero': 99, 'tipo': 'normal'},
    {'nombre': 'h', 'numero': 786, 'tipo': 'ada'},
    {'nombre': 'Jolteon', 'numero': 443, 'tipo': 'electrico'},
    {'nombre': 'Lycanroc', 'numero': 456, 'tipo': 'roca'},
    {'nombre': 'Tyrantrum', 'numero': 985, 'tipo': 'drago'},
    {'nombre': 'Lucario', 'numero': 9, 'tipo': 'lucha'}
]

# Buscar pokemon por su nombre
def search_pokemon_by_name(pokemon_name):
    results = []
    for pokemon in listaPokemon:
        if pokemon['nombre'].lower() == pokemon_name.lower():
            results.append((pokemon['nombre'], pokemon['numero'], pokemon['tipo']))
    return results

pokemon_nombre = 'lucario'
search_results = search_pokemon_by_name(pokemon_nombre)

if search_results:
    print(f"Pokemon: '{pokemon_nombre}':")
    for name, number, p_type in search_results:
        print(f"Nombre: {name}, Número: {number}, Tipo: {p_type}")
else:
    print(f"No se encontraron pokemones con ese nombre '{pokemon_nombre}'.")

# Buscar el Pokémon por número
def search_pokemon(pokemon_list, pokemon_number):
    results = []
    for pokemon in pokemon_list:
        if pokemon['numero'] == pokemon_number:
            results.append((pokemon['nombre'], pokemon['numero'], pokemon['tipo']))
    return results

pokemon_number = 123
search_results = search_pokemon(listaPokemon, pokemon_number)

if search_results:
    for result in search_results:
        print(f"Nombre: {result[0]}, Número: {result[1]}, Tipo: {result[2]}")
else:
    print(f"No hay pokemon con ese numero {pokemon_number}.")

# Mostrar todos los nombres de todos los Pokémons de un determinado tipo
def get_pokemon_names_by_type(pokemon_list, p_type):
    results = []
    for pokemon in pokemon_list:
        if pokemon['tipo'].lower() == p_type.lower():
            results.append(pokemon['nombre'])
    return results

p_type = 'electrico'
pokemon_names = get_pokemon_names_by_type(listaPokemon, p_type)

if pokemon_names:
    print(f"Nombres de Pokémon de tipo '{p_type}':")
    for name in pokemon_names:
        print(name)
else:
    print(f"No se encontraron Pokémon de ese tipo '{p_type}'.")

    # Ordenar los pokemones por números ascendentes
def list_pokemon_by_number(pokemon_list):
    return sorted(pokemon_list, key=lambda x: x['numero'])

pokemon_by_number = list_pokemon_by_number(listaPokemon)

print("Listado en orden ascendente por número de Pokémon:")
for pokemon in pokemon_by_number:
    print(f"Número: {pokemon['numero']}, Nombre: {pokemon['nombre']}, Tipo: {pokemon['tipo']}")

# Mostrar el listado en orden ascendente por nombre de Pokémon
def list_pokemon_by_name(pokemon_list):
    return sorted(pokemon_list, key=lambda x: x['nombre'])

pokemon_by_name = list_pokemon_by_name(listaPokemon)

print("Listado en orden ascendente por nombre de Pokémon:")
for pokemon in pokemon_by_name:
    print(f"Nombre: {pokemon['nombre']}, Número: {pokemon['numero']}, Tipo: {pokemon['tipo']}")

# Mostrar todos los datos de los Pokémon "Jolteon", "Lycanroc", "Tyrantrum"
def get_pokemon_data(pokemon_list, name):
    for pokemon in pokemon_list:
        if pokemon['nombre'].lower() == name.lower():
            return (pokemon['numero'], pokemon['tipo'])
    return None

pokemon_names = ["Jolteon", "Lycanroc", "Tyrantrum"]

for name in pokemon_names:
    pokemon_data = get_pokemon_data(listaPokemon, name)
    if pokemon_data is not None:
        number, p_type = pokemon_data
        print(f"Nombre: {name}, Número: {number}, Tipo: {p_type}")
    else:
        print(f"No se encontraron datos para el Pokémon {name}.")

# Determinar cantidad de Pokémon de tipo "eléctrico" y "acero"
def count_pokemon_by_type(pokemon_list, p_type):
    count = 0
    for pokemon in pokemon_list:
        if pokemon['tipo'].lower() == p_type.lower():
            count += 1
    return count

electric_type = "electrico"
steel_type = "acero"

count_electric = count_pokemon_by_type(listaPokemon, electric_type)
count_steel = count_pokemon_by_type(listaPokemon, steel_type)

print(f"Cantidad de Pokémon de tipo '{electric_type}': {count_electric}")
print(f"Cantidad de Pokémon de tipo '{steel_type}': {count_steel}")