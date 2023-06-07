class Pila:
    def __init__(self):
        self._elementos = []

    def push(self, value):
        self._elementos.append(value)

    def pop(self):
        if self.size() > 0:
            return self._elementos.pop()

    def size(self):
        return len(self._elementos)

    def top(self):
        if self.size() > 0:
            return self._elementos[-1]


class Cola:
    def __init__(self):
        self._elementos = []

    def arrive(self, value):
        self._elementos.append(value)

    def attention(self):
        if self.size() > 0:
            return self._elementos.pop(0)

    def size(self):
        return len(self._elementos)

    def on_front(self):
        if self.size() > 0:
            return self._elementos[0]

    def move_to_end(self):
        if self.size() > 0:
            aux = self.attention()
            self.arrive(aux)
            return aux


# Crear una cola para almacenar los personajes
cola_personajes = Cola()

# Agregar los personajes a la cola
cola_personajes.arrive({"personaje": "Tony Stark", "superhéroe": "Iron Man", "género": "M"})
cola_personajes.arrive({"personaje": "Steve Rogers", "superhéroe": "Capitán América", "género": "M"})
cola_personajes.arrive({"personaje": "Natasha Romanoff", "superhéroe": "Black Widow", "género": "F"})
cola_personajes.arrive({"personaje": "Carol Danvers", "superhéroe": "Capitana Marvel", "género": "F"})
cola_personajes.arrive({"personaje": "Scott Lang", "superhéroe": "Ant-Man", "género": "M"})
cola_personajes.arrive({"personaje": "Peter Parker", "superhéroe": "Spider-Man", "género": "M"})
cola_personajes.arrive({"personaje": "Wanda Maximoff", "superhéroe": "Scarlet Witch", "género": "F"})

# a. Determinar el nombre del personaje de la superhéroe Capitana Marvel
nombre_personaje_capitana_marvel = ""
aux_cola = Cola()

while cola_personajes.size() > 0:
    personaje = cola_personajes.attention()
    aux_cola.arrive(personaje)
    if personaje["superhéroe"] == "Capitana Marvel":
        nombre_personaje_capitana_marvel = personaje["personaje"]

cola_personajes = aux_cola

# b. Mostrar los nombres de los superhéroes femeninos
nombres_superheroes_femeninos = []
aux_cola = Cola()

while cola_personajes.size() > 0:
    personaje = cola_personajes.attention()
    aux_cola.arrive(personaje)
    if personaje["género"] == "F":
        nombres_superheroes_femeninos.append(personaje["superhéroe"])

cola_personajes = aux_cola

# c. Mostrar los nombres de los personajes masculinos
nombres_personajes_masculinos = []
aux_cola = Cola()

while cola_personajes.size() > 0:
    personaje = cola_personajes.attention()
    aux_cola.arrive(personaje)
    if personaje["género"] == "M":
        nombres_personajes_masculinos.append(personaje["personaje"])

cola_personajes = aux_cola

# d. Determinar el nombre del superhéroe del personaje Scott Lang
nombre_superheroe_scott_lang = ""
aux_cola = Cola()

while cola_personajes.size() > 0:
    personaje = cola_personajes.attention()
    aux_cola.arrive(personaje)
    if personaje["personaje"] == "Scott Lang":
        nombre_superheroe_scott_lang = personaje["superhéroe"]

cola_personajes = aux_cola

# e. Mostrar todos los datos de los superhéroes o personajes cuyos nombres comienzan con la letra "S"
datos_personajes_letra_s = []
aux_cola = Cola()

while cola_personajes.size() > 0:
    personaje = cola_personajes.attention()
    aux_cola.arrive(personaje)
    if personaje["personaje"][0] == "S" or personaje["superhéroe"][0] == "S":
        datos_personajes_letra_s.append(personaje)

cola_personajes = aux_cola

# f. Determinar si el personaje Carol Danvers se encuentra en la cola e indicar su nombre de superhéroe
nombre_superheroe_carol_danvers = ""
encontrado = False

while cola_personajes.size() > 0:
    personaje = cola_personajes.attention()
    if personaje["personaje"] == "Carol Danvers":
        nombre_superheroe_carol_danvers = personaje["superhéroe"]
        encontrado = True

if encontrado:
    print("Carol Danvers se encuentra en la cola. Su nombre de superhéroe es:", nombre_superheroe_carol_danvers)
else:
    print("Carol Danvers no se encuentra en la cola.")

# Imprimir los resultados de las actividades a, b, c, d y e
print("Nombre del personaje de la superhéroe Capitana Marvel:", nombre_personaje_capitana_marvel)
print("Nombres de los superhéroes femeninos:", nombres_superheroes_femeninos)
print("Nombres de los personajes masculinos:", nombres_personajes_masculinos)
print("Nombre del superhéroe del personaje Scott Lang:", nombre_superheroe_scott_lang)
print("Datos de los superhéroes o personajes cuyos nombres comienzan con la letra S:")
for personaje in datos_personajes_letra_s:
    print(personaje)