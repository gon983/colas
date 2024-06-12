import main
import Servidor
# Definición de la clase
class Fin:
    # El método __init__ es el constructor de la clase
    def __init__(self, cantidad_servidores, rendimiento_medio):
        
        self.v_prox_fin = []
        self.rendimiento_medio = rendimiento_medio
        for i in range(cantidad_servidores):
            self.v_prox_fin.append(None)
        
    
    # Otros métodos de la clase
    
    
    def generar_prox_fin(self, media, horaActual, nroServidor):
        t_entre_fines = main.generarNumeroExponencial(media)
        self.v_prox_fin[nroServidor] = main.truncate(horaActual + t_entre_fines, 2)