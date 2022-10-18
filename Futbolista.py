from deportista import Deportista
from persona import Persona

class Futbolista(Deportista,Persona):

    futbolistas = []

    def __init__(self, nombre, edad, altura, sexo, añosPracticando, golesMarcados, tarjetasRojas, piernaHabil):
        Persona.__init__(self, nombre, edad, altura, sexo)
        Deportista.__init__(self, "Futbol", añosPracticando)
        self._golesMarcados = golesMarcados
        self._tarjetasRojas = tarjetasRojas
        self._piernaHabil = piernaHabil
        Futbolista.futbolistas.append(self)

    def getGolesMarcados(self):
        return self._golesMarcados

    def setGolesMarcados(self, nuevoGolesMarcados):
        self._golesMarcados = nuevoGolesMarcados

    def getTarjetasRojas(self):
        return self._tarjetasRojas

    def setTarjetasRojas(self, nuevaTarjetasRojas):
        self._tarjetasRojas = nuevaTarjetasRojas

    def getPiernaHabil(self):
        return self._piernaHabil

    def setPierHabil(self, nuevaPiernaHabil):
        self._piernaHabil = nuevaPiernaHabil

    def __str__(self):
        return f"Mi nombre es {self.getNombre()}" \
               f" soy profesional en el deporte {self.getDeporte()}" \
               f" Tengo {self.getEdad()}" \
               f" años de edad y llevo {self.getAñosPracticando()}" \
               f" años en el deporte"