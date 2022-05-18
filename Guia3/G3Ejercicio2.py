class Lampara:
    def __init__(self):
        self.estado = False

    def cambiar_estado(self):
        self.estado = not self.estado

    def __str__(self):
        return "Estado de lampara es {}".format(self.estado)

lampara_nueva = Lampara()
lampara_nueva.cambiar_estado()
print(lampara_nueva)
lampara_nueva.cambiar_estado()
print(lampara_nueva)
