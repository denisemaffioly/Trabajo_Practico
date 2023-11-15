from Ejercicio1 import BinaryTree

class Pokemon:
    def __init__(self, nombre, numero, tipos):
        self.nombre = nombre
        self.numero = numero
        self.tipos = tipos

    def __str__(self):
        tipo_str = "/".join(self.tipos)
        return f"nombre: {self.nombre}\nNúmero en la Pokédex: #{self.numero}\nTipo/Tipos: {tipo_str}"
    
arbol_nombre= BinaryTree()
arbol_numero=BinaryTree()
arbol_tipo= BinaryTree()
pokemones = [
    {'nombre': "Ivysaur", 'numero': 2, 'tipo': "Planta-Veneno"},
    {'nombre': "Charmeleon", 'numero': 5, 'tipo': "Fuego"},
    {'nombre': "Wartortle", 'numero': 8, 'tipo': "Agua"},
    {'nombre': "Raichu", 'numero': 26, 'tipo': "Eléctrico"},
    {'nombre': "Wigglytuff", 'numero': 40, 'tipo': "Normal-Hada"},
    {'nombre': "Haunter", 'numero': 93, 'tipo': "Fantasma-Veneno"},
    {'nombre': "Lapras", 'numero': 131, 'tipo': "Agua-Hielo"},
    {'nombre': "Mew", 'numero': 151, 'tipo': "Psíquico"},
    {'nombre': "Lapras", 'numero': 130, 'tipo': "Agua-Volador"},
    {'nombre': "Flareon", 'numero': 136, 'tipo': "Fuego"},
    {'nombre': "Midday Lycanroc", 'numero': 745, 'tipo': "Roca"},
    {'nombre': "Tyrantrum", 'numero': 697, 'tipo': "Roca-Dragón"},
    {'nombre': "Machoke", 'numero': 67, 'tipo': "Lucha"}
]
for i in pokemones:
    arbol_nombre.insert_node(i['nombre'],[i['numero'],i['tipo']])
    arbol_numero.insert_node(i['numero'],[i['nombre'],i['tipo']])
    arbol_tipo.insert_node(i['tipo'],[i['numero'],i['nombre']])

print('')
arbol_nombre.inorden()
arbol_numero.inorden()
arbol_tipo.inorden() 

print('DATOS DE UN POKEMON A PARTIR DE SU NUMERO Y NOMBRE: ')
arbol_numero.search_pokemon_por_numero(25)

arbol_nombre.search_pokemon_por_nombre("Mewtwo")

print('POKEMON A PARTIR DE UN TIPO: ')
arbol_tipo.inorden_tipos()

print('LISTADO ASCENDENTE POR NUMERO:')
arbol_numero.inorden_numero()
print('LISTADO ASCENDENTE POR NOMBRE:')
arbol_nombre.inorden_nombre()
print('LISTADO ASCENDENTE POR NIVEL POR NOMBRE:')
arbol_nombre.by_level_nombre()

print('INFORMACION DE JOLTEON, LYCANROC Y TYRANTRUM:')
arbol_nombre.search_pokemon_por_nombre("Jolteon")
arbol_nombre.search_pokemon_por_nombre("Lycanroc")
arbol_nombre.search_pokemon_por_nombre("Tyrantrum")

contador_electricos=arbol_tipo.contador_pokemon_electricos()
print(f'CANTIDAD DE POKEMONES ELÉCTRICOS:{contador_electricos} ')
contador_acero= arbol_tipo.contador_pokemon_acero()
print(f'CANTIDAD DE POKEMONES ACERO:{contador_acero}')