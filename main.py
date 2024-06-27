from tkinter import *
from tkinter import ttk
import random
import math

import RK
from Simulacion import *


def generarNumeroExponencial(media):

        #return truncate(-media*math.log(1-random.random()),2)
        return truncate(-(1/media)*math.log(1-random.random()),2)
        # Cuerpo del método


# def generarTiempoCorte(tabla1, tabla2, tiempo):
#     r = truncate(random.random(), 2)
#     t = 0
#     if tiempo == 0:
#         t = random.randint(10, 50)
#     else:
#         for i in tabla2:
#             if r < i:
#                 t = tabla1[tabla2.index(i)] * tiempo
#                 break
#     return t

def generarTiempoCorte(tabla1, tabla2):
    r = truncate(random.random(), 2)
    t = 0
    t_provisto = 0.3
    for i in tabla2:
        if r < i:
            t = tabla1[tabla2.index(i)] * t_provisto
            break
    return t


def truncate(number: float, max_decimals: int) -> float:
    int_part, dec_part = str(number).split(".")
    return float(".".join((int_part, dec_part[:max_decimals])))


def mostrarRK(tablota):
    i = 0
    raiz = Tk()
    raiz.title("Grupo F - TP5 - RK Colas")

    ventana = Frame(raiz)
    ventana.pack()
    barra = ttk.Scrollbar(raiz, orient="vertical")
    barra.pack(side="right", fill="y")
    for j in tablota:
        grilla = ttk.Treeview(ventana, columns=("col1", "col2", "col3", "col4", "col5", "col6", "col7"))
       # barra = ttk.Scrollbar(raiz, orient="vertical", command=grilla.yview)
       # barra.pack(side="right", fill="x")
       # grilla.configure(xscrollcommand=barra.set)
        raiz.resizable(width=False, height=False)


        grilla.column("#0", width=150)
        grilla.column("col1", width=150)
        grilla.column("col2", width=150)
        grilla.column("col3", width=150)
        grilla.column("col4", width=150)
        grilla.column("col5", width=150)
        grilla.column("col6", width=150)
        grilla.column("col7", width=150)

        grilla.heading("#0", text="t")
        grilla.heading("col1", text="C")
        grilla.heading("col2", text="K1")
        grilla.heading("col3", text="K2")
        grilla.heading("col4", text="K3")
        grilla.heading("col5", text="K4")
        grilla.heading("col6", text="C(t+1)")
        grilla.heading("col7", text="t+1")
        while i != len(j):
            grilla.insert("", END, text=j[i][0], values=(j[i][1], j[i][2], j[i][3], j[i][4],
                                                             j[i][5], j[i][6], j[i][7]))
            i = i + 1
        #scroll_y = Scrollbar(ventana, orient="vertical", command=grilla.yview)
        #scroll_y.pack(side="right", fill="y")
        #grilla.configure(yscrollcommand=scroll_y.set)

        grilla.pack(fill="both", expand=True)
    raiz.mainloop()


def iniciar_simulacion(caja_cph, at_personalizada_cph, tarj_credito_cph, plazo_fijo_cph, prestamos_cph, cantidad_cajeros, duracion_simulacion, linea_desde, linea_hasta, tasa_servicio_cajas, clientes):
    tablota = []
    simulacion = Simulacion(cantidad_cajeros)
    simulacion.inicializacion(caja_cph, at_personalizada_cph, tarj_credito_cph, plazo_fijo_cph, 
                            prestamos_cph, cantidad_cajeros,tasa_servicio_cajas)
    
    fila_a_mostrar = simulacion.fila("inicializacion",cantidad_cajeros )
            
    simulacion.generar_tabla(cantidad_cajeros,fila_a_mostrar, clientes)
    def actualizar_filas(tiempo_actual_simulacion):
    
        if tiempo_actual_simulacion <= duracion_simulacion:
            nombre_evento = ""
            (proximo_evento, tipo_servicio, nro_servidor) = simulacion.buscar_proximo_evento()

            #if simulacion.reloj > duracion_simulacion: return
            
            # si el nro de servidor es -1 implica que el proximo evento es una llegada. Caso contrario es un fin de atencion
            if nro_servidor == -1:
                if tipo_servicio == 6:
                    nombre_evento = "llegada_interrupcion"
                    t, tablita = RK.generar_Tabla(tiempo_actual_simulacion)
                    tablota.append(tablita)
                else:
                    nombre_evento = "llegada_cliente_" + proximo_evento.nombre
                simulacion.ejecutar_proxima_llegada(proximo_evento, tipo_servicio)

            else:
                if tipo_servicio == 6:
                    nombre_evento = "fin_interrupcion"
                else:
                    nombre_evento = "fin_atencion_" + proximo_evento.nombre + "_" + str(nro_servidor)
                simulacion.ejecutar_proximo_fin(proximo_evento, tipo_servicio, nro_servidor)


            # genera una nueva fila de datos
            fila_a_mostrar = simulacion.fila(nombre_evento, cantidad_cajeros)
            
            # agrega la fila generada a la grilla si cumple con la linea desde y hasta
            if linea_desde <= simulacion.cant_eventos_sucedidos <= linea_hasta:
                simulacion.agregar_fila(fila_a_mostrar)
                
            #if simulacion.cant_eventos_sucedidos == linea_hasta :
             #   resumen_acumuladores = simulacion.calcular_valores_acumuladores(cantidad_cajeros)
              #  simulacion.agregar_resumen_acumuladores(resumen_acumuladores)
               # mostrarRK(tablota)
                #return
            
            simulacion.raiz.after(0, actualizar_filas, simulacion.reloj) # el primer parametro es cada cuanto se llama la funcion
        else:
            if simulacion.cant_eventos_sucedidos < linea_hasta:
                # aca se podria avisar al usuario que la simulacion termino antes que mostrar la linea
                print("no se mostraron todas las lineas, la simulacion termino antes :)")
            resumen_acumuladores = simulacion.calcular_valores_acumuladores(cantidad_cajeros)
            simulacion.agregar_resumen_acumuladores(resumen_acumuladores)
            mostrarRK(tablota)




    actualizar_filas(0)
    simulacion.raiz.mainloop()

    