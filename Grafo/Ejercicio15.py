class Maravilla:
    def __init__(self, nombre, pais, tipo):
        self.nombre = nombre
        self.pais = pais
        self.tipo = tipo

class GrafoMaravillas:
    def __init__(self):
        self.maravillas = {}

    def agregar_maravilla(self, nombre, pais, tipo):
        maravilla = Maravilla(nombre, pais, tipo)
        self.maravillas[nombre] = maravilla

    def relacionar_maravillas(self, nombre1, nombre2, distancia):
        maravilla1 = self.maravillas.get(nombre1)
        maravilla2 = self.maravillas.get(nombre2)

        if maravilla1 and maravilla2:
            if maravilla1.tipo == maravilla2.tipo:
                maravilla1.relaciones[nombre2] = distancia
                maravilla2.relaciones[nombre1] = distancia

    def arbol_expansion_minima_tipo(self, tipo):
        pass

    def paises_con_maravillas(self):
        pass

    def paises_con_mas_de_una_maravilla_del_mismo_tipo(self):
        pass

grafo_maravillas = GrafoMaravillas()

grafo_maravillas.agregar_maravilla("Machu Picchu", "Perú", "arquitectónica")
grafo_maravillas.agregar_maravilla("Chichén Itzá", "México", "arquitectónica")

grafo_maravillas.relacionar_maravillas("Machu Picchu", "Chichén Itzá", 100)

arbol_expansion_minima_arq = grafo_maravillas.arbol_expansion_minima_tipo("arquitectónica")
arbol_expansion_minima_nat = grafo_maravillas.arbol_expansion_minima_tipo("natural")

paises_con_maravillas = grafo_maravillas.paises_con_maravillas()

paises_con_mas_de_una_maravilla = grafo_maravillas.paises_con_mas_de_una_maravilla_del_mismo_tipo()
