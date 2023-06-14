class Pila:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)


def planetas_visitados(bitacora):
    pila_auxiliar = Pila()
    while not bitacora.is_empty():
        mision = bitacora.pop()
        print(mision[0])
        pila_auxiliar.push(mision)
    while not pila_auxiliar.is_empty():
        bitacora.push(pila_auxiliar.pop())


def creditos(bitacora):
    total_creditos = 0
    pila_auxiliar = Pila()
    while not bitacora.is_empty():
        mision = bitacora.pop()
        total_creditos += mision[2]
        pila_auxiliar.push(mision)
    while not pila_auxiliar.is_empty():
        bitacora.push(pila_auxiliar.pop())
    return total_creditos

def mision_han_solo(bitacora):
    pila_auxiliar = Pila()
    num_mision = 1
    while not bitacora.is_empty():
        mision = bitacora.pop()
        if mision[1] == 'Han Solo':
            print(f"Han Solo fue capturado en la misión {num_mision} en el planeta {mision[0]}")
        pila_auxiliar.push(mision)
        num_mision += 1
    while not pila_auxiliar.is_empty():
        bitacora.push(pila_auxiliar.pop())

bitacora_pila = Pila()

bitacora_pila.push(('Tatooine', 'Han Solo', 100000))
bitacora_pila.push(('Naboo', 'Jabba the Hutt', 50000))
bitacora_pila.push(('Alderaan', 'Leia Organa', 25000))
bitacora_pila.push(('Yavin IV', 'Luke Skywalker', 10000))

print("Planetas visitados en el orden de las misiones:")
planetas_visitados(bitacora_pila)

total_creditos = creditos(bitacora_pila)
print(f"Total de créditos galácticos recaudados: {total_creditos}")

mision_han_solo(bitacora_pila)