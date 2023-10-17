Ejercicio5.py

from lista import Lista


class Superheroe:
    def __init__(self, nombre, anio_aparicion, casa_comic, biografia):
        self.nombre = nombre
        self.anio_aparicion = anio_aparicion
        self.casa_comic = casa_comic
        self.biografia = biografia

    def __str__(self):
        return f" {self.nombre }---> {self.anio_aparicion }>>>>{self.casa_comic}>>>> {self.biografia}"


# Crear una instancia de la clase Lista para almacenar los superhéroes
superheroes_lista = Lista()

# Agregar los objetos Superheroe a la lista con un criterio específico (por ejemplo, 'nombre')
superheroes_lista.delete(
    Superheroe("Linterna Verde", "1940", "DC", "Biografía de Linterna Verde"),
    "nombre",
)
superheroes_lista.insert(
    Superheroe("Wolverine", "1974", "Marvel", "Biografía de Wolverine"),
    "nombre",
)
superheroes_lista.insert(
    Superheroe(
        "Dr. Strange", "1963", "DC", "Biografía de Dr. Strange con traje mágico"
    ),
    "nombre",
)
superheroes_lista.insert(
    Superheroe("Iron Man", "1963", "Marvel", "Biografía de Iron Man con armadura"),
    "nombre",
)
superheroes_lista.insert(
    Superheroe("Capitana Marvel", "1967", "Marvel", "Biografía de Capitana Marvel"),
    "nombre",
)
superheroes_lista.insert(
    Superheroe("Mujer Maravilla", "1941", "DC", "Biografía de Mujer Maravilla"),
    "nombre",
)
superheroes_lista.insert(
    Superheroe("Flash", "1956", "DC", "Biografía de Flash"),
    "nombre",
)
superheroes_lista.insert(
    Superheroe("Star-Lord", "1976", "Marvel", "Biografía de Star-Lord"),
    "nombre",
)
superheroes_lista.insert(
    Superheroe("Batman", "1939", "DC", "Biografía de Batman"),
    "nombre",
)
superheroes_lista.insert(
    Superheroe("Superman", "1938", "DC", "Biografía de Superman"),
    "nombre",
)
superheroes_lista.insert(
    Superheroe("Spider-Man", "1962", "Marvel", "Biografía de Spider-Man"),
    "nombre",
)

# Mostrar la información de los superhéroes
superheroes_lista.barrido()

# a. Eliminar el nodo que contiene la información de Linterna Verde
superheroes_lista.delete("Linterna Verde", "nombre")

# b. Mostrar el año de aparición de Wolverine
for index in range(superheroes_lista.size()):
    heroe = superheroes_lista.get_element_by_index(index)
    if heroe.nombre == "Wolverine":
        print(f"Año de aparicion de wolverine:{heroe.anio_aparicion}")


# c. Cambiar la casa de Dr. Strange a Marvel
for index in range(superheroes_lista.size()):
    heroe = superheroes_lista.get_element_by_index(index)
    if heroe.nombre == "Dr. Strange":
        heroe.casa = "Marvel"
        print(f"la casa de dr strange se cambio ha {heroe.casa}")


# d. Mostrar el nombre de aquellos superhéroes que en su biografía mencionan la palabra "traje" o "armadura"
for index in range(superheroes_lista.size()):
    heroe = superheroes_lista.get_element_by_index(index)
    if "traje" in heroe.biografia.lower() or "armadura" in heroe.biografia.lower():
        print(f"Los super heroes con armadura o traje son:{heroe.nombre}")

# e. Mostrar el nombre y la casa de los superhéroes cuya fecha de aparición sea anterior a 1963

for index in range(superheroes_lista.size()):
    heroe = superheroes_lista.get_element_by_index(index)
    if int(heroe.anio_aparicion) < 1963:
        print(
            f"anio de aparicion anterior que 1963 Nombre: {heroe.nombre}, Casa de cómic: {heroe.casa_comic}"
        )

# f. Mostrar la casa a la que pertenece Capitana Marvel y Mujer Maravilla
for index in range(superheroes_lista.size()):
    heroe = superheroes_lista.get_element_by_index(index)
    if heroe.nombre == "Capitana Marvel" or heroe.nombre == "Mujer Maravilla":
        print(f"{heroe.nombre} pertenece a la casa de cómic: {heroe.casa_comic}")

# g. Mostrar toda la información de Flash y Star-Lord

for index in range(superheroes_lista.size()):
    heroe = superheroes_lista.get_element_by_index(index)
    if heroe.nombre == "Flash" or heroe.nombre == "Star-Lord":
        print(f"Nombre: {heroe.nombre}")
        print(f"Año de aparición: {heroe.anio_aparicion}")
        print(f"Casa de cómic: {heroe.casa_comic}")
        print(f"Biografía: {heroe.biografia}")

# h. Listar los superhéroes que comienzan con la letra B, M y S
for index in range(superheroes_lista.size()):
    heroe = superheroes_lista.get_element_by_index(index)
    if heroe.nombre[0] in ["B", "M", "S"]:
        print(
            f"nombre de los superheroes que comiensan con la letra B,M Y S:{heroe.nombre}"
        )


# i. Determinar cuántos superhéroes hay de cada casa de cómic
marvel_count = 0
dc_count = 0
for index in range(superheroes_lista.size()):
    heroe = superheroes_lista.get_element_by_index(index)
    if heroe.casa_comic == "Marvel":
        marvel_count += 1
    elif heroe.casa_comic == "DC":
        dc_count += 1


print(f"Superhéroes de Marvel: {marvel_count}")
print(f"Superhéroes de DC: {dc_count}")


