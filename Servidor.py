class Servidor:
    # El método __init__ es el constructor de la clase
    def __init__(self, estado, cola):
        self.estado = estado
        self.cola = cola
    

    def getEstado(self):
        return self.estado
    
    def getCola(self):
        return self.cola
    

    def setEstadoLibre(self):
        self.estado = 'libre'

    def setEstadoOcupado(self):
        self.estado = 'ocupado'

    def agregar_a_cola(self):
        self.cola += 1

    def quitar_de_cola(self):
        self.cola -=1
    


        