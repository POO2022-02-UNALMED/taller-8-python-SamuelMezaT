from persona import Persona
class Deportista:
    def __init__(self,deporte, añosPracticando):
        self._deporte = deporte
        self._añosPracticando = añosPracticando

    def getDeporte(self):
        return self._deporte

    def setDeporte(self, NuevoDeporte):
        self._deporte = NuevoDeporte

    def getAñosPracticando(self):
        return self._añosPracticando

    def setAñosPracticando(self,Anhos):
        self._añosPracticando = Anhos