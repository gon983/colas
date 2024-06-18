
class Acumulador:
    
    def __init__(self, nombre_servicio):
        self.nombre_acumulador = nombre_servicio
        self.tiempo_espera = 0
        self.cantidad_clientes_esperaron = 0
        self.tiempo_libre = 0
        self.tiempo_ocupado = 0

    def acumular_espera(self, tiempo_esperado):
        self.tiempo_espera += tiempo_esperado
        self.cantidad_clientes_esperaron += 1

    def get_tiempo_espera(self):
        return round(self.tiempo_espera,2)
    
    def get_cantidad_clientes_esperaron(self):
        return self.cantidad_clientes_esperaron
    
    def get_nombre_acumulador(self):
        return self.nombre_acumulador
        


    
    
