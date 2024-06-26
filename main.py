from tkinter import *
from tkinter import ttk
import random
import math
from Simulacion import *


def generarNumeroExponencial(media):
        return truncate(-media*math.log(1-random.random()),2)
        # Cuerpo del método


def generarTiempoCorte(tabla1, tabla2, tiempo):
    r = truncate(random.random(), 2)
    t = 0
    if tiempo == 0:
        t = random.randint(10, 50)
    else:
        for i in tabla2:
            if r < i:
                t = tabla1[tabla2.index(i)] * tiempo
                break
    return t


def truncate(number: float, max_decimals: int) -> float:
    int_part, dec_part = str(number).split(".")
    return float(".".join((int_part, dec_part[:max_decimals])))


def iniciar_simulacion(caja_cph, at_personalizada_cph, tarj_credito_cph, plazo_fijo_cph, prestamos_cph, cantidad_cajeros, duracion_simulacion, linea_desde, linea_hasta, tasa_servicio_cajas, clientes):
    simulacion = Simulacion(cantidad_cajeros)
    simulacion.inicializacion(caja_cph, at_personalizada_cph, tarj_credito_cph, plazo_fijo_cph, 
                            prestamos_cph, cantidad_cajeros,tasa_servicio_cajas)
    
    fila_a_mostrar = simulacion.fila("inicializacion",cantidad_cajeros )
            
    simulacion.generar_tabla(cantidad_cajeros,fila_a_mostrar, clientes)
    def actualizar_filas(tiempo_actual_simulacion):
        if tiempo_actual_simulacion <= duracion_simulacion: #segun como lo hicimos en los acumuladores se ven los valores finales de la
            # duracion de las simulacion no los valores finales de las lineas q se muestran. ahi seria <= linea_hasta
            nombre_evento = ""
            (proximo_evento, tipo_servicio, nro_servidor) = simulacion.buscar_proximo_evento()

            if simulacion.reloj > duracion_simulacion: return
            
            
            # si el nro de servidor es -1 implica que el proximo evento es una llegada. Caso contrario es un fin de atencion
            if nro_servidor == -1:
                if tipo_servicio == 5:
                    nombre_evento = "llegada_interrupcion"
                else:
                    nombre_evento = "llegada_cliente_" + proximo_evento.nombre
                simulacion.ejecutar_proxima_llegada(proximo_evento, tipo_servicio)
            else:
                if tipo_servicio == 5:
                    nombre_evento = "fin_interrupcion"
                else:
                    nombre_evento = "fin_atencion_" + proximo_evento.nombre + "_" + str(nro_servidor)
                simulacion.ejecutar_proximo_fin(proximo_evento, tipo_servicio, nro_servidor)
            
            

            # genera una nueva fila de datos
            fila_a_mostrar = simulacion.fila(nombre_evento, cantidad_cajeros)
            
            # agrega la fila generada a la grilla si cumple con la linea desde y hasta
            if linea_desde <= simulacion.cant_eventos_sucedidos <= linea_hasta:
                simulacion.agregar_fila(fila_a_mostrar)
                
            simulacion.raiz.after(0, actualizar_filas, simulacion.reloj) # el primer parametro es cada cuanto se llama la funcion
        else:
            resumen_acumuladores = simulacion.calcular_valores_acumuladores(cantidad_cajeros)
            simulacion.agregar_resumen_acumuladores(resumen_acumuladores)



    actualizar_filas(0)
    simulacion.raiz.mainloop()

    