import main
from Llegada import Llegada 
from Fin import Fin
from Cliente import Cliente
from Acumulador import Acumulador
from Servidor import *
from tkinter import *
from tkinter import ttk


# Definición de la clase
class Simulacion:
    # El método __init__ es el constructor de la clase
    def __init__(self, cantidad_cajeros):
        
        # simulacion es quien tiene el conocimiento del reloj y de todos los objetos del sistema
        self.cant_eventos_sucedidos = 0
        self.reloj = 0
        # cada posicion representa un tipo de servicio. 0: caja, 1: atencion personalizada, 2 tarjetas de credito, 3 plazo fijo, 4 prestamo, 5 Deudas, 6 Interrupciones.
        self.lista_llegadas = [None, None, None, None, None, None,None]
        self.lista_fines = [None, None, None, None, None, None,None]
        self.lista_servidores =[[],[],[],[],[],[]]
        self.v_clientes =[]
        #cada posicion representa una cola por servicio
        self.colas = [0, 0, 0, 0, 0,0]
        self.inicioInt = 0
        self.finInt = 0
        self.listaServidoresInt = []

        # 1 acumulador por servicio 
        self.v_acumuladores = [None,None,None,None,None,None]
        
        # se carga la lista de servidores segun la cantidad de servidores especificados
        
        for i in range(cantidad_cajeros):
            self.lista_servidores[0].append(Servidor(i,'libre'))
        
        for i in range(3):
            self.lista_servidores[1].append(Servidor(i,'libre'))

        for i in range(2):
            self.lista_servidores[2].append(Servidor(i,'libre'))

        for i in range(1):
            self.lista_servidores[3].append(Servidor(i,'libre'))

        for i in range(2):
            self.lista_servidores[4].append(Servidor(i,'libre'))
        
        for i in range(1):
            self.lista_servidores[5].append(Servidor(i, 'libre'))


    # crea una tupla con todos los valores a insertar en una nueva fila de la grilla
    def fila(self, nombre, cantidad_cajeros):
        v_inicial = [self.cant_eventos_sucedidos, nombre, self.reloj, self.lista_llegadas[0].prox_llegada, self.lista_llegadas[1].prox_llegada, self.lista_llegadas[2].prox_llegada, self.lista_llegadas[3].prox_llegada, self.lista_llegadas[4].prox_llegada, self.lista_llegadas[5].prox_llegada, self.lista_llegadas[6].prox_llegada]
        
        for i in range(cantidad_cajeros):
            x = self.lista_fines[0].v_prox_fin[i] 
            v_inicial.append(x)
        
        v_final =  [self.lista_fines[1].v_prox_fin[0], self.lista_fines[1].v_prox_fin[1], self.lista_fines[1].v_prox_fin[2], self.lista_fines[2].v_prox_fin[0], self.lista_fines[2].v_prox_fin[1], self.lista_fines[3].v_prox_fin[0], self.lista_fines[4].v_prox_fin[0], self.lista_fines[4].v_prox_fin[1], self.lista_fines[5].v_prox_fin[0], self.lista_fines[6].v_prox_fin[0]]
        
        for i in range(cantidad_cajeros):
            x = self.lista_servidores[0][i].getEstado()
            v_final.append(x)
            
        #como hay cola unica por servicio saque esto del for.
        v_final.append(self.colas[0])   
            
        v_3 = [ self.lista_servidores[1][0].getEstado(), self.lista_servidores[1][1].getEstado(), self.lista_servidores[1][2].getEstado(), self.colas[1], self.lista_servidores[2][0].getEstado(), self.lista_servidores[2][1].getEstado(), self.colas[2], self.lista_servidores[3][0].getEstado(), self.colas[3], self.lista_servidores[4][0].getEstado(), self.lista_servidores[4][1].getEstado(), self.colas[4], self.lista_servidores[5][0].getEstado(), self.colas[5] ]

        for i in range(len(self.v_acumuladores)):    
            v_3.append(self.v_acumuladores[i].get_tiempo_espera())
            v_3.append(self.v_acumuladores[i].get_cantidad_clientes_esperaron())
            v_3.append(round(sum(servidor.get_tiempo_ocio() for servidor in self.lista_servidores[i]),2))

        if len(self.v_clientes)>0:
            for i in range(len(self.v_clientes)):
                v_3.append(self.v_clientes[i].estado) # solo agrega el estado para simplificar en la interfaz
            
        v_retornar = v_inicial + v_final + v_3

        return v_retornar

    # crea todos los objetos que van a ser necesarios para la simulacion y le asigna valores de inicializacion
    def inicializacion(self, media_caja, media_atencion_personalizada, media_tarjeta_credito, media_plazo_fijo, media_prestamos,
                    cantidad_cajas, tasa_servicio_cajas):
        
        nombre_llegada = ""
        media = 0
        tabla_prob = []
        tabla_resultados = []
        for i in range(len(self.lista_llegadas)):
            if i == 0:
                media = media_caja
                nombre_llegada = "caja"
                tabla_prob = []
                tabla_resultados = []
            elif i == 1:
                media = media_atencion_personalizada
                nombre_llegada = "atencion_personalizada"
                tabla_prob = []
                tabla_resultados = []
            elif i == 2:
                media = media_tarjeta_credito
                nombre_llegada = "tarjeta_credito"
                tabla_prob = []
                tabla_resultados = []
            elif i == 3:
                media = media_plazo_fijo
                nombre_llegada = "plazo_fijo"
                tabla_prob = []
                tabla_resultados = []
            elif i == 4:
                media = media_prestamos
                nombre_llegada = "prestamos"
                tabla_prob = []
                tabla_resultados = []
            elif i==5:
                media = media_prestamos
                nombre_llegada = "deudas"
                tabla_prob = []
                tabla_resultados = []

            elif i == 6:
                media = 0
                nombre_llegada = "interrupcion"
                tabla_prob = [0.2, 0.8, 1]
                tabla_resultados = [4, 6, 8]
            
            self.lista_llegadas[i] =  Llegada(media, nombre_llegada, None, tabla_resultados, tabla_prob)
            self.lista_llegadas[i].generar_prox_Llegada(0)
            
        cant_serv = 0
        tasa_rendim = ""
        nombre_fin = ""
        for i in range(len(self.lista_fines)):
            if i == 0: 
                nombre_fin = "caja"
                cant_serv = cantidad_cajas
                tasa_rendim = tasa_servicio_cajas
            elif i == 1: 
                nombre_fin = "atencion_personalizada"
                cant_serv = 3
                tasa_rendim = 5
            elif i == 2: 
                nombre_fin = "tarjeta_credito"
                cant_serv = 2
                tasa_rendim = 3
            elif i == 3: 
                nombre_fin = "plazo_fijo"
                cant_serv = 1
                tasa_rendim = 2
            elif i == 4: 
                nombre_fin = "prestamos"
                cant_serv = 2
                tasa_rendim = 4
            elif i == 5:
                nombre_fin = "deudas"
                cant_serv = 1
                tasa_rendim = 3

            elif i == 6:
                nombre_fin = "interrupcion"
                cant_serv = 1
                tasa_rendim = 0
            
            self.lista_fines[i] =  Fin(nombre_fin, cant_serv, tasa_rendim)

        for i in range(len(self.v_acumuladores)):
            if i == 0:
            
                nombre_servicio = "caja"
                pos = 0
            elif i == 1:
                
                nombre_servicio = "atencion_personalizada"
                pos= 1

            elif i == 2:
                
                nombre_servicio = "tarjeta_credito"
                pos = 2
            elif i == 3:
                
                nombre_servicio = "plazo_fijo"
                pos=3
            elif i == 4:
                
                nombre_servicio = "prestamos"
                pos=4
            elif i == 5:
                
                nombre_servicio = "deudas"
                pos=4

            self.v_acumuladores[i] = Acumulador(nombre_servicio, pos)



    
    # genera la grilla/tabla, especificando encabezados, scrolls y tamaños
    def generar_tabla(self, cantidad_cajeros, tupla_inicial, max_cli): #max cli indica cuantas columnas podemos tener
        i = 0
        raiz = Tk()
        raiz.title("Grupo F - TP 4 - Linea de Colas")
        raiz.state('zoomed')  # Esta línea maximiza la ventana

        ventana = Frame(raiz)
        ventana.pack(fill=BOTH, expand=True)
        
        columns = ["col1", "col2", "col3", "col4", "col5", "col6", "col7", "col8", "col9","col10","col11","col12","col13","col14","col15", "col16", "col17", "col18"]
        for i in range((cantidad_cajeros+ cantidad_cajeros*2+ 17+ max_cli + 17)):
            columns.append(f'col{19+i}')

        grilla = ttk.Treeview(ventana, columns=columns, show="headings")
        
        # Crear y configurar la barra de desplazamiento vertical
        
        scroll_y = Scrollbar(ventana, orient=VERTICAL, command=grilla.yview)
        scroll_y.pack(side=RIGHT, fill=Y)
        grilla.configure(yscrollcommand=scroll_y.set)

        # Crear y configurar la barra de desplazamiento horizontal
        scroll_x = Scrollbar(ventana, orient=HORIZONTAL, command=grilla.xview)
        scroll_x.pack(side=BOTTOM, fill=X)
        grilla.configure(xscrollcommand=scroll_x.set)

        # Configurar las columnas de la grilla
        for col in columns:
            if col == "col2":  grilla.column(col, width=200)
            else: grilla.column(col, width=150)

        # Configurar encabezados de las columnas
        encabezados = [
            "Nro Evento", "Evento", "Reloj(horas)", "Proxima llegada caja", "Proxima at personalizada",
            "Proxima llegada tarjeta credito", "Proxima llegada plazo fijo", "Proxima llegada prestamos", "Proxima llegada deudas",
            "Proxima llegada de corte"
        ]
        for i in range(cantidad_cajeros):
            encabezados.append(f"fin caja {i+1}")

        encabezados += [
            "fin atencion personalizada 1", "fin atencion personalizada 2", "fin atencion personalizada 3",
            "fin tarjeta credito 1", "fin tarjeta credito 2", "fin plazo fijo", "fin prestamos 1", "fin prestamos 2", "fin deudas",
            "fin interrupcion"
        ]

        for i in range(cantidad_cajeros):
            encabezados.append(f"estado caja {i}")

        encabezados += [
            "cola caja", "estado atencion personalizada 1", "estado atencion personalizada 2",
            "estado atencion personalizada 3", "cola atencion personalizada", "estado tarjeta credito 1",
            "estado tarjeta credito 2", "cola tarjeta credito", "estado plazo fijo", "cola plazo fijo",
            "estado prestamos 1", "estado prestamos 2", "cola prestamos", "estado deudas", "cola deudas"
        ]

        for i in range(len(self.v_acumuladores)):
            if i == 0: # caja
                encabezados += ['acum t '+ self.v_acumuladores[i].get_nombre_acumulador(), 'acum c ' + self.v_acumuladores[i].get_nombre_acumulador(), 'acum ocio '+ self.v_acumuladores[i].get_nombre_acumulador()]
            if i == 1: # at pers
                encabezados += ['acum t '+ self.v_acumuladores[i].get_nombre_acumulador(),'acum c ' + self.v_acumuladores[i].get_nombre_acumulador(), 'acum ocio '+ self.v_acumuladores[i].get_nombre_acumulador()]
            if i == 2: # tarj credito
                encabezados += ['acum t '+ self.v_acumuladores[i].get_nombre_acumulador(),'acum c ' + self.v_acumuladores[i].get_nombre_acumulador(), 'acum ocio '+ self.v_acumuladores[i].get_nombre_acumulador()]
            if i == 3: # plazo fijo
                encabezados += ['acum t '+ self.v_acumuladores[i].get_nombre_acumulador(),'acum c ' + self.v_acumuladores[i].get_nombre_acumulador(), 'acum ocio '+ self.v_acumuladores[i].get_nombre_acumulador()]
            if i == 4: # prestamos
                encabezados += ['acum t '+ self.v_acumuladores[i].get_nombre_acumulador(),'acum c ' + self.v_acumuladores[i].get_nombre_acumulador(), 'acum ocio '+ self.v_acumuladores[i].get_nombre_acumulador()]
            if i == 5: # deudas
                encabezados += ['acum t '+ self.v_acumuladores[i].get_nombre_acumulador(),'acum c ' + self.v_acumuladores[i].get_nombre_acumulador(), 'acum ocio '+ self.v_acumuladores[i].get_nombre_acumulador()]


        for i in range(max_cli):
            encabezados.append(f"E Cliente{i + 1}")

        for col, encabezado in zip(columns, encabezados):
            grilla.heading(col, text=encabezado)
        
        grilla.pack(fill="both", expand=True)
        grilla.insert("", END, values=tupla_inicial)
        
        self.grilla = grilla
        self.raiz = raiz
    
    # agrega una fila en la grilla con los valores recibidos de fila.
    def agregar_fila (self, fila_a_agregar):
            fila_a_agregar = tuple("-" if x is None else x for x in fila_a_agregar)
            self.grilla.insert("", END, values=fila_a_agregar)

    # retorna el servidor que esta disponible para un determinado tipo de servicio 
    def buscar_servidor_disponible(self, tipo_servicio):

        # accede a la posicion en la lista de servidores que corresponde al tipoo de servicio solicitado
        # recorre a todos lod servidores de ese servicio y devuelve al primer desocupado
        for servidor in self.lista_servidores[tipo_servicio]:
            if servidor.estoyLibre(): return (servidor)
        return(None)

    # Retorna el evento que sucedera mas proximamente (llegada o fin) junto con el tipo de servicio y numero de servidor que finalizo la atencion. 
    def buscar_proximo_evento(self):

        # busca la proxima llegada
        (tipo_llegada, objeto_prox_lleg) = min(enumerate(self.lista_llegadas), key=lambda llegadaX: llegadaX[1].prox_llegada)
        # busca el proximo fin
        prox_fin = float('inf')
        tipo_fin = -1
        num_servidor = -1
        
        for i, fin in enumerate(self.lista_fines):
            for j, valor in enumerate(fin.v_prox_fin):
                if valor is not None:
                    if valor < prox_fin:
                        prox_fin = valor
                        tipo_fin = i
                        num_servidor = j
            
        # busca cual es mas proximo, si la llegada o el fin      
        if prox_fin < objeto_prox_lleg.prox_llegada: return (self.lista_fines[tipo_fin], tipo_fin, num_servidor)
        else: return (objeto_prox_lleg, tipo_llegada, -1)


    def ejecutarInterrupcion(self, tipo_servicio):
        for j in range(6):
            for i in self.lista_servidores[j]:
                self.listaServidoresInt.append(i.getEstado())
                i.setEstadoInterrumpido()

        self.lista_fines[tipo_servicio].generar_prox_fin(self.reloj, tipo_servicio)
        self.finInt = self.lista_fines[tipo_servicio].v_prox_fin[0]
        z = 0
        for k in range(6):
            tamaño = self.lista_fines[k].cantidad_servidores
            self.lista_llegadas[k].prox_llegada = round(self.lista_llegadas[k].prox_llegada + \
                                                        (self.finInt - self.inicioInt), 2)
            while z < tamaño:
                if self.lista_fines[k].v_prox_fin[z] is not None:
                    self.lista_fines[k].v_prox_fin[z] = round(self.lista_fines[k].v_prox_fin[z] + \
                                                            (self.finInt - self.inicioInt), 2)
                else:
                    pass
                z = z + 1
            z = 0

    # ejecuta todas las acciones que deben suceder al haber una llegada.
    def ejecutar_proxima_llegada(self, objeto_llegada, tipo_servicio):
        self.reloj = objeto_llegada.prox_llegada
        self.cant_eventos_sucedidos += 1
        if tipo_servicio == 6:
            self.inicioInt = self.reloj
            self.ejecutarInterrupcion(tipo_servicio)
        else:
            servidor = self.buscar_servidor_disponible(tipo_servicio)

            if servidor is not None:
                # si hay un servidor disponible, se crea un cliente con estado Siendo atendido, y se le asigna el servidor que lo atiende.
                # se establece como ocupado al servidor y se genera un proximo fin de atencion para el mismo.
                nuevo_cliente = Cliente(f"siendoAtendido_{objeto_llegada.nombre}", self.reloj)
                self.v_acumuladores[tipo_servicio].acumular_espera(0)
                nuevo_cliente.asignar_servidor(servidor)
                servidor.setEstadoOcupado(self.reloj)
                self.lista_fines[tipo_servicio].generar_prox_fin(self.reloj, servidor.nro)

            else:
                # si no hay un servidor disponible, se crea un cliente con estado en cola, y se le suma uno mas a la cola del tipo de servicio.
                nuevo_cliente = Cliente(f"enCola_{objeto_llegada.nombre}", self.reloj)
                self.colas[tipo_servicio] += 1

            # se le asigna al cliente cual fue el tipo de servicio que demando.
            nuevo_cliente.tipo_servicio_demandado = tipo_servicio
            self.v_clientes.append(nuevo_cliente)

        objeto_llegada.generar_prox_Llegada(self.reloj)

    def setearInterrumpido(self):
        h = 0
        for j in range(6):
            i = len(self.lista_servidores[j])
            for z in range(i):
                self.lista_servidores[j][z].estado = self.listaServidoresInt[h]
                h = h + 1

    # ejecuta todas las acciones que deben suceder al haber un fin de atencion.
    def ejecutar_proximo_fin(self, objeto_fin, tipo_servicio, nro_servidor):
        self.cant_eventos_sucedidos += 1
        self.reloj = objeto_fin.v_prox_fin[nro_servidor]
        if tipo_servicio == 6:
            self.setearInterrumpido()
            self.listaServidoresInt = []
            objeto_fin.v_prox_fin[0] = None

        else:
            self.reloj = objeto_fin.v_prox_fin[nro_servidor]
            if self.colas[tipo_servicio] > 0:
                # si hay clientes en cola, se genera un proximo fin, se le cambia el estado al cliente y se disminuye en uno la cola
                objeto_fin.generar_prox_fin(self.reloj, nro_servidor)
                for cliente in self.v_clientes:
                    if cliente.tipo_servicio_demandado == tipo_servicio:
                        cliente.setEstadoSiendoAtendido(self.reloj, cliente.tipo_servicio_demandado)
                        tiempo_espera = cliente.get_tiempo_espera()
                        self.v_acumuladores[tipo_servicio].acumular_espera(tiempo_espera)
                        break

                self.colas[tipo_servicio] -= 1
            else:
                # si no hay clientes en cola, se limpia el valor de proximo fin y se establece al servidor en libre
                objeto_fin.v_prox_fin[nro_servidor] = None
                self.lista_servidores[tipo_servicio][nro_servidor].setEstadoLibre(self.reloj)
                for cliente in self.v_clientes:
                    if cliente.tipo_servicio_demandado == tipo_servicio:
                        cliente.setEstadoNone()
                        cliente.tipo_servicio_demandado = -1
                        break





    # def acumular_ocio(self, tiempo_pasado): 
    #     for i in range(len(self.lista_servidores)):
    #         for servidor in self.lista_servidores[i]:
    #             if not(servidor.estoyOcupado()):
    #                 servidor.acumular_ocio(tiempo_pasado)

    def calcular_valores_acumuladores(self, cantidad_cajeros):
        resumen_acumuladores = []
        for i in range(len(self.v_acumuladores)):
            tiempo_espera = self.v_acumuladores[i].get_tiempo_espera()
            cantidad_clientes_esperaron = self.v_acumuladores[i].get_cantidad_clientes_esperaron()
            tiempo_ocio = sum(servidor.get_tiempo_ocio() for servidor in self.lista_servidores[i])
            if i == 0:
                cantidad_servidores = cantidad_cajeros
            elif i == 1:
                cantidad_servidores = 3
            elif i == 2:
                cantidad_servidores = 2
            elif i == 3:
                cantidad_servidores = 1
            elif i == 4:
                cantidad_servidores = 2
            elif i == 5:
                cantidad_servidores = 1
            resumen_acumuladores.append((self.v_acumuladores[i].get_nombre_acumulador(), tiempo_espera,
                                        cantidad_clientes_esperaron, (tiempo_ocio / cantidad_servidores)))
        return resumen_acumuladores

    def agregar_resumen_acumuladores(self, resumen_acumuladores):
        frame_acumuladores = Frame(self.raiz)
        frame_acumuladores.pack(pady=10, padx=10)
        for acumulador in resumen_acumuladores:
            nombre, tiempo_espera, cantidad_clientes, tiempo_ocio_promedio = acumulador
            Label(frame_acumuladores, text=f"{nombre}:").pack(anchor='w')
            if cantidad_clientes > 0:
                Label(frame_acumuladores, text=f"Tiempo de espera promedio: {round(tiempo_espera / cantidad_clientes, 2)}").pack(
                    anchor='w')
            if tiempo_ocio_promedio > 0:
                Label(frame_acumuladores,
                      text=f"Porcentaje Ocupacion: {round(((self.reloj - tiempo_ocio_promedio) / self.reloj) * 100, 2)}").pack(
                    anchor='w')

