class Personaje:
    def __init__(self, nombre, peliculas):
        self.nombre = nombre
        self.peliculas = peliculas

class PersonajesMarvel:
    def __init__(self):
        self.pila = []

    def esta_vacia(self):
        return len(self.pila) == 0

    def push(self, personaje):
        self.pila.append(personaje)

    def pop(self):
        if not self.esta_vacia():
            return self.pila.pop()
        else:
            raise IndexError("La pila está vacía")

    def peek(self):
        if not self.esta_vacia():
            return self.pila[-1]
        else:
            raise IndexError("La pila está vacía")

    def posicion_personajes(self, personaje1, personaje2):
        posicion = 0
        for i, personaje in enumerate(self.pila, 1):
            if personaje.nombre == personaje1 or personaje.nombre == personaje2:
                posicion = i
                break
        return posicion

    def personajes_con_mas_de_5_peliculas(self):
        personajes = []
        for personaje in self.pila:
            if personaje.peliculas > 5:
                personajes.append((personaje.nombre, personaje.peliculas))
        return personajes

    def peliculas_participadas_por_viuda_negra(self):
        for personaje in self.pila:
            if personaje.nombre == "Viuda Negra":
                return personaje.peliculas
        return 0

    def personajes_que_empiezan_con_c_d_g(self):
        personajes = []
        for personaje in self.pila:
            if personaje.nombre[0] in ['C', 'D', 'G']:
                personajes.append(personaje.nombre)
        return personajes



personajes_marvel = PersonajesMarvel()

personajes_marvel.push(Personaje("Hulk", 7))
personajes_marvel.push(Personaje("Thor", 6))
personajes_marvel.push(Personaje("Capitán América", 9))
personajes_marvel.push(Personaje("Rocket Raccoon", 5))
personajes_marvel.push(Personaje("Iron Man", 10))
personajes_marvel.push(Personaje("Viuda Negra", 8))
personajes_marvel.push(Personaje("Groot", 3))
personajes_marvel.push(Personaje("Doctor Strange", 4))

posicion_rocket = 0
posicion_groot = 0
for i, personaje in enumerate(personajes_marvel.pila, 1):
    if personaje.nombre == "Rocket Raccoon":
        posicion_rocket = i
    elif personaje.nombre == "Groot":
        posicion_groot = i

print("La posición de Rocket Raccoon es:", posicion_rocket)
print("La posición de Groot es:", posicion_groot)

personajes_mas_de_5_peliculas = personajes_marvel.personajes_con_mas_de_5_peliculas()
print("Personajes que participaron en más de 5 películas:")
for personaje in personajes_mas_de_5_peliculas:
    print("Nombre:", personaje[0], "- Películas:", personaje[1])

peliculas_viuda_negra = personajes_marvel.peliculas_participadas_por_viuda_negra()
print("La Viuda Negra participó en", peliculas_viuda_negra, "películas")