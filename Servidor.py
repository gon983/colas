class Servidor:
    # El método __init__ es el constructor de la clase
    def __init__(self, nro ,estado):
        self.nro = nro
        self.estado = estado
    

    def getEstado(self):
        return self.estado
    

    def setEstadoLibre(self):
        self.estado = 'libre'
    def estoyLibre(self):
        if self.estado == "libre": return True
        else: return False

    def setEstadoOcupado(self):
        self.estado = 'ocupado'
    
    def estoyOcupado(self):
        if self.estado == "ocupado": return True
        else: return False

    


        