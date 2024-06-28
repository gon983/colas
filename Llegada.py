import random
import math
import main
# Definición de la clase
class Llegada:
    # El método __init__ es el constructor de la clase
    def __init__(self, media, nombre, prox_llegada, tabla1, tabla2):
        self.nombre = nombre
        self.prox_llegada = prox_llegada
        self.media = media
        self.tabla_tiempos = tabla1
        self.tabla_prob = tabla2
        
    
    # Otros métodos de la clase
    def generar_prox_Llegada(self, horaActual):
        if self.nombre != "interrupcion":
            t_entre_llegadas = main.generarNumeroExponencial(self.media)
        else:
            t_entre_llegadas = main.generarTiempoCorte(self.tabla_tiempos, self.tabla_prob, self.media)
        self.prox_llegada = round(horaActual + t_entre_llegadas, 2)

    
