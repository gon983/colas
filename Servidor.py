class Servidor:
    # El método __init__ es el constructor de la clase
    def __init__(self, nro ,estado):
        self.nro = nro
        self.estado = estado
        self.tiempo_ocio = 0
        self.ultimo_cambio_estado = 0
    

    def getEstado(self):
        return self.estado
    

    def setEstadoLibre(self, reloj_actual):
        self.estado = 'libre'
        self.ultimo_cambio_estado = reloj_actual
        

    def estoyLibre(self):
        if self.estado == "libre": 
            return True
        else: 
            return False

    def setEstadoOcupado(self, reloj_actual):
        if self.estado == 'libre':  # Si estaba libre, acumula el ocio hasta ahora
            self.tiempo_ocio += reloj_actual - self.ultimo_cambio_estado
            print(f'tiempo ocio {self.tiempo_ocio}, reloj actual= {reloj_actual}, ultimo cambio estado= {self.ultimo_cambio_estado}-')
        self.estado = 'ocupado'
        self.ultimo_cambio_estado = reloj_actual
    
    def estoyOcupado(self):
        if self.estado == "ocupado": return True
        else: return False

    def acumular_ocio(self, tiempo_actual):
        if self.estado == 'libre':
            self.tiempo_ocio += tiempo_actual - self.ultimo_cambio_estado
            self.ultimo_cambio_estado = tiempo_actual

    def get_tiempo_ocio(self):
        return self.tiempo_ocio

    def setEstadoInterrumpido(self):
        self.estado = 'interrumpido'

    def estoyInterrumpido(self):
        if self.estado == "interrumpido": return True
        else: return False

        