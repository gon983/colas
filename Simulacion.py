import main
from Llegada import Llegada 
# Definición de la clase
class Simulacion:
    # El método __init__ es el constructor de la clase
    def __init__(self, llegada_caja , llegada_atencion_personalizada, llegada_tarjeta_credito, 
                llegada_plazo_fijo,  llegada_prestamos):
        self.llegada_caja = llegada_caja
        self.llegada_atencion_personalizada = llegada_atencion_personalizada
        self.llegada_tarjeta_credito = llegada_tarjeta_credito
        self.llegada_plazo_fijo = llegada_plazo_fijo
        self.llegada_prestamos = llegada_prestamos
    
    # Otros métodos de la clase
    
    
    def inicializacion(self, media_caja, media_atencion_personalizada, media_tarjeta_credito, media_plazo_fijo, media_prestamos):
        llegada_caja = Llegada(None)
        llegada_atencion_personalizada = Llegada(None)
        llegada_tarjeta_credito = Llegada(None)
        llegada_plazo_fijo = Llegada(None)
        llegada_prestamos = Llegada(None)

        llegada_caja.generar_prox_Llegada(media_caja,0)
        llegada_atencion_personalizada.generar_prox_Llegada(media_atencion_personalizada,0)
        llegada_tarjeta_credito.generar_prox_Llegada(media_tarjeta_credito,0)
        llegada_plazo_fijo.generar_prox_Llegada(media_plazo_fijo,0)
        llegada_prestamos.generar_prox_Llegada(media_prestamos,0)



