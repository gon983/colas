from tkinter import *
from tkinter import ttk
import random
import math
from Simulacion import Simulacion

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
        # simulacion. funciona()
        # simulacion .mostrar()
