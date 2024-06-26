
class Acumulador:
    
    def __init__(self, nombre_servicio,pos):
        self.nombre_acumulador = nombre_servicio
        self.posicion = pos
        self.tiempo_espera = 0
        self.cantidad_clientes_esperaron = 0
        self.tiempo_libre = 0
        

    def acumular_espera(self, tiempo_esperado):
        self.tiempo_espera += tiempo_esperado
        self.cantidad_clientes_esperaron += 1

        # se ejecuta 1: cuando llega un cliente y pone en estado siendo atendido
        # 2: cuando termina un servicio y se pasa a alguien en cola a siendo atendido



    def get_tiempo_espera(self):
        return round(self.tiempo_espera,2)
    
    def get_cantidad_clientes_esperaron(self):
        return self.cantidad_clientes_esperaron
    
    def get_nombre_acumulador(self):
        return self.nombre_acumulador
    
    def get_tiempo_ocio(self):
        return round(self.tiempo_libre,2)
    
    def get_posicion(self):
        return self.posicion

        