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
        
        simulacion = Simulacion(cantidad_cajeros)
        simulacion.inicializacion(caja_cph, at_personalizada_cph, tarj_credito_cph, plazo_fijo_cph, 
                                prestamos_cph, cantidad_cajeros)
        
        v_inicial = simulacion.fila("inicializacion","0",cantidad_cajeros )

        simulacion.mostrar_datos(cantidad_cajeros, v_inicial, 30)
        
#         simulacion_v_inicial = ["inicializacion","0", simulacion.llegada_caja.prox_llegada,
#                                     simulacion.llegada_atencion_personalizada.prox_llegada,
#                                     simulacion.llegada_tarjeta_credito.prox_llegada,
#                                     simulacion.llegada_plazo_fijo.prox_llegada,
#                                     simulacion.llegada_prestamos.prox_llegada]
        
#         simulacion_v_final =  [simulacion.fin_atencion_personalizada.v_prox_fin[0],
#                                     simulacion.fin_atencion_personalizada.v_prox_fin[1],
#                                     simulacion.fin_atencion_personalizada.v_prox_fin[2],
#                                     simulacion.fin_tarjeta_credito.v_prox_fin[0],
#                                     simulacion.fin_tarjeta_credito.v_prox_fin[1],
#                                     simulacion.fin_plazo_fijo.v_prox_fin[0],
#                                     simulacion.fin_prestamos.v_prox_fin[0],
#                                     simulacion.fin_prestamos.v_prox_fin[1]]
        
#         simulacion_v_3 = [simulacion.servidores_atencion_personalizada[0].getEstado(),
#                             simulacion.servidores_atencion_personalizada[0].cola,
#                                     simulacion.servidores_atencion_personalizada[1].getEstado(),
#                                     simulacion.servidores_atencion_personalizada[1].cola,
#                                     simulacion.servidores_atencion_personalizada[2].getEstado(),
#                                     simulacion.servidores_atencion_personalizada[2].cola,
#                                     simulacion.servidores_tarjeta_credito[0].getEstado(),
#                                     simulacion.servidores_tarjeta_credito[0].cola,
#                                     simulacion.servidores_tarjeta_credito[1].getEstado(),
#                                     simulacion.servidores_tarjeta_credito[1].cola,
#                                     simulacion.servidores_plazo_fijo[0].getEstado(),
#                                     simulacion.servidores_plazo_fijo[0].cola,
#                                     simulacion.servidores_prestamo[0].getEstado(),
#                                     simulacion.servidores_prestamo[0].cola,
#                                     simulacion.servidores_prestamo[1].getEstado(),
#                                     simulacion.servidores_prestamo[1].cola]
        

#         vec_arreglado = crear_vec_con_vectores(simulacion, simulacion_v_inicial, cantidad_cajeros, simulacion_v_final, simulacion_v_3)

#         simulacion.mostrar_datos(cantidad_cajeros, vec_arreglado)

# def crear_vec_con_vectores(simulacion, v_inicial, cantidad_cajeros, v_final, v_ultimo):
    
    
#     for i in range(cantidad_cajeros):
#         x = simulacion.fin_caja.v_prox_fin[i] 
#         v_inicial.append(x)

#     v_intermedio = v_inicial + v_final

#     for i in range(cantidad_cajeros):
#         x = simulacion.servidores_caja[i].getEstado()
#         y = simulacion.servidores_caja[i].cola
#         v_intermedio.append(x)
#         v_intermedio.append(y)
    
#     v_retornado = v_intermedio + v_ultimo

#     return v_retornado
