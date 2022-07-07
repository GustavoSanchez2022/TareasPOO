class TableroDeBasquet:
    def __init__(self, local: str, visitante: str, puntos_local: int,
                 puntos_visitantes: int):
        self.local: str = local
        self.visitante: str = visitante
        self.puntos_local: int = puntos_local
        self.puntos_visitantes: int = puntos_visitantes

    def triple(self, equipo):
        if equipo == self.local:
            self.puntos_local =+ 3
            return self.puntos_local
        else:
            self.puntos_visitantes =+3
            return self.puntos_visitantes

    def doble(self, equipo):
        if equipo == self.local:
            self.puntos_local =+ 2
            return self.puntos_local
        else:
            self.puntos_visitantes =+2
            return self.puntos_visitantes

    def simple(self, equipo):
        if equipo == self.local:
            self.puntos_local =+ 1
            return self.puntos_local
        else:
            self.puntos_visitantes =+1
            return self.puntos_visitantes

    def __str__(self):
        return "El equipo local: {} va {}\n" \
               "El equipo visitante: {} va {}".format(self.local,self.puntos_local,
                                                      self.visitante,self.puntos_visitantes)

tablero = TableroDeBasquet("Boca","Tigre",0,0)
print(tablero)
print(tablero.triple("Tigre"))
tablero.simple("Boca")
print(tablero)

