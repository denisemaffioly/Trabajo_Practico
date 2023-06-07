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

    def atention(self):
        if self.size() > 0:
            return self._elementos.pop(0)

    def size(self):
        return len(self._elementos)

    def on_front(self):
        if self.size() > 0:
            return self._elementos[0]

    def move_to_end(self):
        if self.size() > 0:
            aux = self.atention()
            self.arrive(aux)
            return aux

    def eliminar_notificaciones_facebook(self):
        cola_aux = Cola()
        while self.size() > 0:
            notificacion = self.atention()
            if not notificacion["app"] == "Facebook":
                cola_aux.arrive(notificacion)
        self._elementos = cola_aux._elementos

    def mostrar_notificaciones(self):
        for notificacion in self._elementos:
            print(notificacion)

    def mostrar_notificaciones_twitter_python(self):
        print("Notificaciones de Twitter que incluyen la palabra 'Python':")
        for notificacion in self._elementos:
            if notificacion["app"] == "Twitter" and "Python" in notificacion["mensaje"]:
                print(notificacion)

    def contar_notificaciones_temporales(self):
        pila_temporal = Pila()
        contador = 0

        while self.size() > 0:
            notificacion = self.atention()
            if "11:43" <= notificacion["hora"] <= "15:57":
                pila_temporal.push(notificacion)
                contador += 1

        return contador


cola_notificaciones = Cola()
cola_notificaciones.arrive({"hora": "11:30", "app": "Facebook", "mensaje": "Notificacion de Facebook 1"})
cola_notificaciones.arrive({"hora": "12:20", "app": "Twitter", "mensaje": "Notificacion de Twitter 1 con Python"})
cola_notificaciones.arrive({"hora": "13:50", "app": "Twitter", "mensaje": "Notificacion de Twitter 2 Python"})
cola_notificaciones.arrive({"hora": "14:00", "app": "Facebook", "mensaje": "Notificacion de Facebook 2"})
cola_notificaciones.arrive({"hora": "15:20", "app": "Twitter", "mensaje": "Notificacion de Twitter 3 Python"})

cola_notificaciones.eliminar_notificaciones_facebook()
cola_notificaciones.mostrar_notificaciones()
print()

cola_notificaciones.mostrar_notificaciones_twitter_python()
print()

cantidad_temporales = cola_notificaciones.contar_notificaciones_temporales()
print ("Cantidad de notificaciones temporales:", cantidad_temporales)