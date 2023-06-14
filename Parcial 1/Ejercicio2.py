superheroes = [
    ('Capitán América', 'Steve Rogers', 'Guardianes de la Galaxia', 1941),
    ('Iron Man', 'Tony Stark', 'Guardianes de la Galaxia', 1963),
    ('Thor', 'Thor Odinson', 'Los Vengadores', 1962),
    ('Hulk', 'Bruce Banner', 'Guardianes de la Galaxia', 1962),
    ('Viuda Negra', 'Natasha Romanoff', 'Los Cuatro Fantásticos', 1964),
    ('Ojo de Halcón', 'Clint Barton', 'Los Cuatro Fantásticos', 1964),
    ('Pantera Negra', 'T\'Challa', 'Los Cuatro Fantásticos', 2016),
    ('Doctor Strange', 'Stephen Strange', 'Los Cuatro Fantásticos', 2016),
    ('Spider-Man', 'Peter Parker', 'Guardianes de la Galaxia', 2016),
    ('Capitana Marvel', 'Carol Danvers', 'Guardianes de la Galaxia', 2019),
    ('Ant-Man', 'Scott Lang', 'Guardianes de la Galaxia', 2015),
    ('La Avispa', 'Hope Van Dyne', 'Los Vengadores', 2015),
    ('Bruja Escarlata', 'Wanda Maximoff', 'Los Vengadores', 2015),
    ('Visión', 'Visión', 'Guardianes de la Galaxia', 2015),
    ('Falcon', 'Sam Wilson', 'Guardianes de la Galaxia', 2014),
    ('Soldado de Invierno', 'Bucky Barnes', 'Guardianes de la Galaxia', 2014),
    ('Máquina de Guerra', 'James Rhodes', 'Los Vengadores', 2010),
    ('Mantis', 'Mantis', 'Guardianes de la Galaxia', 2019),
    ('Pepper Potts', 'Pepper Potts', 'Los Vengadores', 1963),
    ('Nick Fury', 'Nick Fury', 'Los Vengadores', 1963),
]

for superheroe in superheroes:
    if superheroe[0] == 'Capitana Marvel':
        print('Capitana Marvel está en la lista, el nombre de su personaje es:', superheroe[1])

from collections import deque
class Cola:
    def __init__(self):
        self._elementos = deque()

    def arrive(self, value):
        self._elementos.append(value)

    def atention(self):
        if self.size() > 0:
            return self._elementos.popleft()

    def size(self):
        return len(self._elementos)

    def on_front(self):
        if self.size() > 0:
            return self._elementos[0]

guardianes_de_la_galaxia_cola = Cola()

for superheroe in superheroes:
    if superheroe[2] == 'Guardianes de la Galaxia':
        guardianes_de_la_galaxia_cola.arrive(superheroe)

cantidad_guardianes_de_la_galaxia = guardianes_de_la_galaxia_cola.size()

print("Cantidad de superhéroes de los Guardianes de la Galaxia:", cantidad_guardianes_de_la_galaxia)

superheroes_cuatro_fantasticos = []

for superheroe in superheroes:
    if superheroe[2] == "Los Cuatro Fantásticos":
        superheroes_cuatro_fantasticos.append(superheroe)

superheroes_cuatro_fantasticos.sort(key=lambda x: x[0], reverse=True)

print("Superhéroes de Los Cuatro Fantásticos en orden descendente:")
for superheroe in superheroes_cuatro_fantasticos:
    print(superheroe[0])
    
superheroes_guardianes = []

for superheroe in superheroes:
    if superheroe[2] == "Guardianes de la Galaxia":
        superheroes_guardianes.append(superheroe)

superheroes_guardianes.sort(key=lambda x: x[0], reverse=True)

print("Superhéroes de Guardianes de la Galaxia en orden descendente:")
for superheroe in superheroes_guardianes:
    print(superheroe[0])

superheroes_1960 = []

for superheroe in superheroes:
    if superheroe[3] > 1960:
        superheroes_1960.append(superheroe[0])

print("Superheroes que aparecieron despues del 1960",superheroes_1960)

for i in range(len(superheroes)):
    if superheroes[i][0] == "Vlanck Widow":
        superheroes[i] = ("Black Widow", superheroes[i][1], superheroes[i][2], superheroes[i][3])

personajes_auxiliares = ['Black Cat', 'Hulk', 'Rocket Racoonn', 'Loki']

for personaje in personajes_auxiliares:
    personaje_existente = False
    for superheroe in superheroes:
        if personaje == superheroe[0]:
            personaje_existente = True
            break
    if not personaje_existente:
        superheroes.append((personaje, '', '', 0))

print("Lista modificada:",superheroes)