import random
import math
import main
# Definición de la clase
class Llegada:
    # El método __init__ es el constructor de la clase
    def __init__(self, nombre, prox_llegada):
        self.nombre = nombre
        self.prox_llegada = prox_llegada
        
    
    # Otros métodos de la clase
    
    
    def generar_prox_Llegada(self, media, horaActual):
        t_entre_llegadas = main.generarNumeroExponencial(media)
        self.prox_llegada = main.truncate(horaActual + t_entre_llegadas, 2)
        


    
