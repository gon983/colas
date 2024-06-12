from tkinter import *
from tkinter import ttk
import random
import math
from Simulacion import *

def generarNumeroExponencial(media):
        return truncate(-media*math.log(1-random.random()),2)
        # Cuerpo del método
        

def truncate(number: float, max_decimals: int) -> float:
    int_part, dec_part = str(number).split(".")
    return float(".".join((int_part, dec_part[:max_decimals])))


def iniciar_simulacion(caja_cph, at_personalizada_cph, tarj_credito_cph, plazo_fijo_cph, prestamos_cph, cantidad_cajeros, tiempo_simulacion, cant_lineas_mostrar):
    if tiempo_simulacion == 0:
        print([])
    else:
        # tiempo_simulacion
        # cant_lineas_mostrar 
        simulacion = Simulacion()
        simulacion.inicializacion(caja_cph, at_personalizada_cph, tarj_credito_cph, plazo_fijo_cph, 
                                prestamos_cph, cantidad_cajeros)
        
        
             

        simulacion_tupla_inicial = ("inicializacion","0", simulacion.llegada_caja.prox_llegada,
                                    simulacion.llegada_atencion_personalizada.prox_llegada,
                                    simulacion.llegada_tarjeta_credito.prox_llegada,
                                    simulacion.llegada_plazo_fijo.prox_llegada,
                                    simulacion.llegada_prestamos.prox_llegada,
                                    simulacion.fin_caja.v_prox_fin[0], # hay que ver como hacer para que se le puedan agregar mas fin_caja segun sea variable la cantidad de cajeros
                                    simulacion.fin_atencion_personalizada.v_prox_fin[0],
                                    simulacion.fin_atencion_personalizada.v_prox_fin[1],
                                    simulacion.fin_atencion_personalizada.v_prox_fin[2],
                                    simulacion.fin_tarjeta_credito.v_prox_fin[0],
                                    simulacion.fin_tarjeta_credito.v_prox_fin[1],
                                    simulacion.fin_plazo_fijo.v_prox_fin,
                                    simulacion.fin_prestamos.v_prox_fin[0],
                                    simulacion.fin_prestamos.v_prox_fin[1],
                                    )

        simulacion.mostrar_datos(cantidad_cajeros, simulacion_tupla_inicial)

        
        # simulacion. funciona()
        # simulacion .mostrar()
