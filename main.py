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
    simulacion = Simulacion(cantidad_cajeros)
    simulacion.inicializacion(caja_cph, at_personalizada_cph, tarj_credito_cph, plazo_fijo_cph, 
                            prestamos_cph, cantidad_cajeros)
    
    fila_a_mostrar = simulacion.fila("inicializacion",cantidad_cajeros )
            
    simulacion.generar_tabla(cantidad_cajeros,fila_a_mostrar,5)
    
    def actualizar_filas(i):
        if i < cant_lineas_mostrar:
            nombre_evento = ""
            (proximo_evento, tipo_servicio, nro_servidor) = simulacion.buscar_proximo_evento()
            
            # si el nro de servidor es -1 implica que el proximo evento es una llegada. Caso contrario es un fin de atencion
            if nro_servidor == -1:
                nombre_evento = "llegada_cliente_" + proximo_evento.nombre
                simulacion.ejecutar_proxima_llegada(proximo_evento, tipo_servicio)
            else:
                nombre_evento = "fin_atencion_" + proximo_evento.nombre + "_" + str(nro_servidor)
                simulacion.ejecutar_proximo_fin(proximo_evento, tipo_servicio, nro_servidor)
            
            #agrega una fila mas a la grilla
            fila_a_mostrar = simulacion.fila(nombre_evento, cantidad_cajeros)
            simulacion.agregar_fila(fila_a_mostrar)
            simulacion.raiz.after(1, actualizar_filas, i + 1) # el primer parametro es cada cuanto se llama la funcion

    actualizar_filas(0)
    simulacion.raiz.mainloop()

    