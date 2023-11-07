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

arbolNombre = BinaryTree()
arbolNumero = BinaryTree()
arbolTipo = BinaryTree()

listaPokemon = [{'nombre': 'a', 'numero': 123, 'tipo': 'electrico'},
               {'nombre': 'b', 'numero': 4, 'tipo': 'oscuro'},
               {'nombre': 'c', 'numero': 5, 'tipo': 'roca'},
               {'nombre': 'd', 'numero': 8, 'tipo': 'veneno'},
               {'nombre': 'e', 'numero': 9, 'tipo': 'lucha'},
               {'nombre': 'f', 'numero': 12, 'tipo': 'bicho'},
               {'nombre': 'e', 'numero': 99, 'tipo': 'normal'},
               {'nombre': 'h', 'numero': 786, 'tipo': 'ada'},
               {'nombre': 'Jolteon', 'numero': 443, 'tipo': 'electrico'},
               {'nombre': 'Lycanroc', 'numero': 456, 'tipo': 'roca'},
               {'nombre': 'Tyrantrum', 'numero': 985, 'tipo': 'drago'},
               {'nombre': 'Lucario', 'numero': 9, 'tipo': 'lucha'}]

for pokemon in listaPokemon:
    arbolNombre.insert_node(pokemon['nombre'], (pokemon['numero'], pokemon['tipo']))
    arbolNumero.insert_node(pokemon['numero'], (pokemon['nombre'], pokemon['tipo']))
    arbolTipo.insert_node(pokemon['tipo'], (pokemon['numero'], pokemon['nombre']))

def search_pokemon_by_name(partial_name):
    result = []
    for name, (number, p_type) in arbolNombre.in_order_traversal():
        if partial_name.lower() in name.lower():
            result.append((name, number, p_type))
    return result

def get_pokemon_names_by_type(p_type):
    result = []
    for p_type_entry, (number, name) in arbolTipo.in_order_traversal():
        if p_type_entry.lower() == p_type.lower():
            result.append(name)
    return result

def list_pokemon_in_order():
    return arbolNumero.in_order_traversal()

def list_pokemon_by_name():
    return sorted(arbolNombre.in_order_traversal())

def get_pokemon_data(pokemon_name):
    return arbolNombre.search(pokemon_name)

def count_pokemon_by_type(p_type):
    count = 0
    for p_type_entry, _ in arbolTipo.in_order_traversal():
        if p_type_entry.lower() == p_type.lower():
            count += 1
    return count

print("Datos de Bulbasaur (por nombre):")
print(get_pokemon_data("Bulbasaur"))
print("\nDatos de Bulbasaur (por proximidad):")
print(search_pokemon_by_name("bul"))

print("\nNombres de Pokémon de tipo 'Agua':")
print(get_pokemon_names_by_type("Agua"))

print("\nListado en orden ascendente por número:")
for number, (name, p_type) in list_pokemon_in_order():
    print(f"{number}: {name} ({p_type})")

print("\nListado en orden ascendente por nombre:")
for name, (number, p_type) in list_pokemon_by_name():
    print(f"{name}: {number} ({p_type})")

pokemon_names = ["Jolteon", "Lycanroc", "Tyrantrum"]
print("\nDatos de Pokémon específicos:")
for name in pokemon_names:
    print(get_pokemon_data(name))

electric_count = count_pokemon_by_type("electrico")
steel_count = count_pokemon_by_type("acero")
print("\nCantidad de Pokémon de tipo Eléctrico:", electric_count)
print("Cantidad de Pokémon de tipo Acero:", steel_count)