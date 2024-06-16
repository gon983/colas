class Cliente:
    # El método __init__ es el constructor de la clase
    def __init__(self, estado, tiempo_inicio_espera):
        self.estado = estado
        self.tiempo_inicio_espera = tiempo_inicio_espera 
        self.tiempo_espera = None
    
    def setEstadoSiendoAtendido(self, hora_actual):
        self.estado = 'siendoAtendido'
        self.tiempo_espera = hora_actual - self.tiempo_inicio_espera

    def setEstadoEnCola(self):
        self.estado = 'enCola'

    

    


