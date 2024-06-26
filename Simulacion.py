import main
from Llegada import Llegada 
from Fin import Fin
from Cliente import Cliente
from Acumulador import Acumulador
from Servidor import *
from tkinter import *
from tkinter import ttk
import random 


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
        self.estados_serv_antes_corte = []
        self.servicio_con_cortes = 0 #el servicio de caja es el que tiene problemas de luz
        self.encabezados= None
        # 1 acumulador por servicio 
        self.v_acumuladores = [None,None,None,None,None,None]
        self.mayor_concurrencia = 0
        self.contador_clientes_idos = 0
        self.contador_clientes_que_se_fueron = 0
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
    def fila(self, nombre, cantidad_cajeros, van_a_deudas, termine_y_voy_a_deudas):
        horas = int(self.reloj)
        minutos = int((self.reloj - horas) * 60)
        segundos = int((self.reloj - horas - minutos / 60) * 3600)
        v_inicial = [self.cant_eventos_sucedidos, nombre, self.reloj, self.lista_llegadas[0].prox_llegada, self.lista_llegadas[1].prox_llegada, self.lista_llegadas[2].prox_llegada, self.lista_llegadas[3].prox_llegada, self.lista_llegadas[4].prox_llegada, van_a_deudas, self.lista_llegadas[6].prox_llegada]
        
        for i in range(cantidad_cajeros):
            x = self.lista_fines[0].v_prox_fin[i] 
            v_inicial.append(x)
        
        v_final =  [self.lista_fines[1].v_prox_fin[0], self.lista_fines[1].v_prox_fin[1], self.lista_fines[1].v_prox_fin[2], self.lista_fines[2].v_prox_fin[0], self.lista_fines[2].v_prox_fin[1], self.lista_fines[3].v_prox_fin[0], self.lista_fines[4].v_prox_fin[0], self.lista_fines[4].v_prox_fin[1], self.lista_fines[5].v_prox_fin[0], self.lista_fines[6].v_prox_fin[0]]
        v_final.append(termine_y_voy_a_deudas)
        
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

        self.mayor_concurrencia = max(len([ True for c in self.v_clientes if c.estado != "" ]), self.mayor_concurrencia)
        v_3.append(self.mayor_concurrencia)

        v_3.append(self.contador_clientes_que_se_fueron)

        if len(self.v_clientes)>0:
            for cliente in self.v_clientes:
                v_3.append(cliente.estado) # solo agrega el estado para simplificar en la interfaz
                
            
        v_retornar = v_inicial + v_final + v_3

        return v_retornar

    # crea todos los objetos que van a ser necesarios para la simulacion y le asigna valores de inicializacion
    def inicializacion(self, media_caja, media_atencion_personalizada, media_tarjeta_credito, media_plazo_fijo, media_prestamos,
                    cantidad_cajas, tasa_servicio_cajas):
        lista = [media_caja, media_atencion_personalizada, media_tarjeta_credito, media_plazo_fijo, media_prestamos]
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
            # elif i==5:  NO se le inicializa  llegada a deudas 
            # aunque si necesitamos un objeto fin
            #     media = media_prestamos
            #     nombre_llegada = "deudas"
            #     tabla_prob = []
            #     tabla_resultados = []

            elif i == 6:
                media = len(lista)/sum(lista)
                nombre_llegada = "interrupcion"
                tabla_prob = [0.2, 0.8, 1]
                tabla_resultados = [4, 6, 8]
            
            if i in (0,1,2,3,4,6):
                self.lista_llegadas[i] =  Llegada(media, nombre_llegada, None, tabla_resultados, tabla_prob)
                self.lista_llegadas[i].generar_prox_Llegada(0)
            if i == 5:
                self.lista_llegadas[i] = ''
            
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
                tasa_rendim = 50

            elif i == 6:
                nombre_fin = "interrupcion"
                cant_serv = 1
                tasa_rendim = len(lista)/sum(lista)

            
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
                pos=5

            self.v_acumuladores[i] = Acumulador(nombre_servicio, pos)



    
    # genera la grilla/tabla, especificando self.encabezados, scrolls y tamaños
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
        self.encabezados = [
            "Nro Evento", "Evento", "Reloj", "Proxima llegada caja", "Proxima at personalizada",
            "Proxima llegada tarjeta credito", "Proxima llegada plazo fijo", "Proxima llegada prestamos", "Me llamaron deudas",
            "Proxima llegada de corte"
        ]
        for i in range(cantidad_cajeros):
            self.encabezados.append(f"fin caja {i+1}")

        self.encabezados += [
            "fin atencion personalizada 1", "fin atencion personalizada 2", "fin atencion personalizada 3",
            "fin tarjeta credito 1", "fin tarjeta credito 2", "fin plazo fijo", "fin prestamos 1", "fin prestamos 2", "fin deudas",
            "fin interrupcion", "Termine y voy a deudas"
        ]

        for i in range(cantidad_cajeros):
            self.encabezados.append(f"estado caja {i}")

        self.encabezados += [
            "cola caja", "estado atencion personalizada 1", "estado atencion personalizada 2",
            "estado atencion personalizada 3", "cola atencion personalizada", "estado tarjeta credito 1",
            "estado tarjeta credito 2", "cola tarjeta credito", "estado plazo fijo", "cola plazo fijo",
            "estado prestamos 1", "estado prestamos 2", "cola prestamos", "estado deudas", "cola deudas"
        ]

        for i in range(len(self.v_acumuladores)):
            if i == 0: # caja
                self.encabezados += ['acum t '+ self.v_acumuladores[i].get_nombre_acumulador(), 'acum c ' + self.v_acumuladores[i].get_nombre_acumulador(), 'acum ocio '+ self.v_acumuladores[i].get_nombre_acumulador()]
            if i == 1: # at pers
                self.encabezados += ['acum t '+ self.v_acumuladores[i].get_nombre_acumulador(),'acum c ' + self.v_acumuladores[i].get_nombre_acumulador(), 'acum ocio '+ self.v_acumuladores[i].get_nombre_acumulador()]
            if i == 2: # tarj credito
                self.encabezados += ['acum t '+ self.v_acumuladores[i].get_nombre_acumulador(),'acum c ' + self.v_acumuladores[i].get_nombre_acumulador(), 'acum ocio '+ self.v_acumuladores[i].get_nombre_acumulador()]
            if i == 3: # plazo fijo
                self.encabezados += ['acum t '+ self.v_acumuladores[i].get_nombre_acumulador(),'acum c ' + self.v_acumuladores[i].get_nombre_acumulador(), 'acum ocio '+ self.v_acumuladores[i].get_nombre_acumulador()]
            if i == 4: # prestamos
                self.encabezados += ['acum t '+ self.v_acumuladores[i].get_nombre_acumulador(),'acum c ' + self.v_acumuladores[i].get_nombre_acumulador(), 'acum ocio '+ self.v_acumuladores[i].get_nombre_acumulador()]
            if i == 5: # deudas
                self.encabezados += ['acum t '+ self.v_acumuladores[i].get_nombre_acumulador(),'acum c ' + self.v_acumuladores[i].get_nombre_acumulador(), 'acum ocio '+ self.v_acumuladores[i].get_nombre_acumulador()]

        self.encabezados.append("Mayor concurrencia")
        self.encabezados += ['Contador Clientes Que Se Van']

        for i in range(max_cli):
            self.encabezados.append(f"E Cliente{i + 1}")

        for col, encabezado in zip(columns, self.encabezados):
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
        tipo_llegada, objeto_prox_lleg = min(
    ((idx, llegada) for idx, llegada in enumerate(self.lista_llegadas) if llegada != ''),
    key=lambda llegadaX: llegadaX[1].prox_llegada
)
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
        self.servicio_con_cortes = random.randint(0, 5)
        for serv in self.lista_servidores[self.servicio_con_cortes]:
            self.estados_serv_antes_corte.append(serv.getEstado())
            serv.setEstadoInterrumpido()
            
        # se genera la proxima interrupcion
        self.lista_fines[tipo_servicio].generar_prox_fin(self.reloj, tipo_servicio)
        # se establece el fin de la interrupcion actual
        self.finInt = self.lista_fines[tipo_servicio].v_prox_fin[0]
        
        tamaño = self.lista_fines[self.servicio_con_cortes].cantidad_servidores
        z = 0
        while z < tamaño:
            if self.lista_fines[self.servicio_con_cortes].v_prox_fin[z] is not None:
                self.lista_fines[self.servicio_con_cortes].v_prox_fin[z] = round(self.lista_fines[self.servicio_con_cortes].v_prox_fin[z] + \
                                                        (self.finInt - self.inicioInt), 2)
            else:
                pass
            z = z + 1

    # ejecuta todas las acciones que deben suceder al haber una llegada.
    def ejecutar_proxima_llegada(self, objeto_llegada, tipo_servicio):
        self.reloj = objeto_llegada.prox_llegada
        self.cant_eventos_sucedidos += 1
        van_a_deudas = False

        if tipo_servicio == 6:
            self.inicioInt = self.reloj
            self.ejecutarInterrupcion(tipo_servicio)
    
            
        else:
            
            if random.random() <= 0.18:
                van_a_deudas = True
            # Deudas hace exactamente lo mismo que cualquier otro servidor
            if van_a_deudas:
                servidor = self.buscar_servidor_disponible(5)
                if servidor is not None:
                    nuevo_cliente = Cliente(f"siendoAtendido_deudas", self.reloj)
                    self.v_acumuladores[5].acumular_espera(0)
                    nuevo_cliente.asignar_servidor(servidor)
                    servidor.setEstadoOcupado(self.reloj)
                    self.lista_fines[5].generar_prox_fin(self.reloj, servidor.nro)
                else:
                    nuevo_cliente = Cliente(f"enCola_deudas", self.reloj)
                    self.colas[5] += 1

                nuevo_cliente.tipo_servicio_demandado = 5
                nuevo_cliente.tipo_servicio_demandado_original = tipo_servicio
                self.v_clientes.append(nuevo_cliente)
            
            else:
                servidor = self.buscar_servidor_disponible(tipo_servicio)

                if servidor is not None:
                    # si hay un servidor disponible, se crea un cliente con estado Siendo atendido, y se le asigna el servidor que lo atiende.
                    # se establece como ocupado al servidor y se genera un proximo fin de atencion para el mismo.
                    nuevo_cliente = Cliente(f"siendoAtendido_{objeto_llegada.nombre}", self.reloj)
                    self.v_acumuladores[tipo_servicio].acumular_espera(0)
                    nuevo_cliente.asignar_servidor(servidor)
                    nuevo_cliente.estado += str(servidor.nro)
                    servidor.setEstadoOcupado(self.reloj)
                    self.lista_fines[tipo_servicio].generar_prox_fin(self.reloj, servidor.nro)

                else:
                    if tipo_servicio == 0 and self.get_cantidad_cola_caja() >= 5:
                        nuevo_cliente = Cliente("", self.reloj)
                        self.contar_cliente_que_se_va()
                    else:
                    # si no hay un servidor disponible, se crea un cliente con estado en cola, y se le suma uno mas a la cola del tipo de servicio.
                        nuevo_cliente = Cliente(f"enCola_{objeto_llegada.nombre}", self.reloj)
                        self.colas[tipo_servicio] += 1

                # se le asigna al cliente cual fue el tipo de servicio que demando.
                nuevo_cliente.tipo_servicio_demandado = tipo_servicio
                self.v_clientes.append(nuevo_cliente)
        # osea si es deudas no hay que generar una proxima llegada, pero nunca debiera haber una llegada de deudas si no se la inicializa
        objeto_llegada.generar_prox_Llegada(self.reloj)
        if van_a_deudas:
            return "SI"
        else:
            return "NO"

    def setearInterrumpido(self):
        for serv in self.lista_servidores[self.servicio_con_cortes]:
            serv.estado = self.estados_serv_antes_corte[serv.nro]


    # ejecuta todas las acciones que deben suceder al haber un fin de atencion.
    def ejecutar_proximo_fin(self, objeto_fin, tipo_servicio, nro_servidor):
        self.cant_eventos_sucedidos += 1
        self.reloj = objeto_fin.v_prox_fin[nro_servidor]
        termine_y_voy_a_deudas = False
        rta = ''
        if tipo_servicio == 6:
            self.setearInterrumpido()
            self.estados_serv_antes_corte = []
            objeto_fin.v_prox_fin[0] = None

        else:
            # "sacamos" al cliente del sistema y establecemos el tiempo en el que termino de ser atendido
            for cliente in self.v_clientes:
                # primero hay que validar que el cliente este siendo atendido, y luego que el servidor que lo esta atendiendo sea el mismo que el que termino su servicio.
                if cliente.servidor_asignado and cliente.tipo_servicio_demandado == tipo_servicio and cliente.servidor_asignado.nro == nro_servidor:
                    #print(f'1) Objeto Fin: {objeto_fin.nombre}, Tipo Servicio Dem: {cliente.tipo_servicio_demandado}, Estado: {cliente.estado}, servidor: {cliente.servidor_asignado.nro}')
          
                    if random.random() <= 0.33 and tipo_servicio != 5 and (not cliente.paso_por_deuda): #los clientes de deudas no recursan deudas
                        termine_y_voy_a_deudas = True
                    # se puede dar que quede el random false 
                    
                    if termine_y_voy_a_deudas:
                        servidor = self.buscar_servidor_disponible(5)
                        if servidor is not None:
                            cliente.setEstadoSiendoAtendido(self.reloj, 5)
                            self.v_acumuladores[5].acumular_espera(0)
                            cliente.asignar_servidor(servidor)
                            servidor.setEstadoOcupado(self.reloj)
                            self.lista_fines[5].generar_prox_fin(self.reloj, servidor.nro)

                        else:
                            cliente.servidor_asignado = None
                            cliente.setEstadoEnColaDeudas(self.reloj)
                            self.colas[5] += 1
                        cliente.tipo_servicio_demandado = 5
                        cliente.paso_por_deuda = True
                        rta = "SI"
                    else:
                        rta= "NO"
                        if tipo_servicio == 5 and (not cliente.paso_por_deuda):
                            servidor = self.buscar_servidor_disponible(cliente.tipo_servicio_demandado_original)

                            if servidor is not None:
                                cliente.setEstadoSiendoAtendido(self.reloj, cliente.tipo_servicio_demandado_original)
                                self.v_acumuladores[cliente.tipo_servicio_demandado_original].acumular_espera(0)
                                cliente.asignar_servidor(servidor)
                                cliente.estado += str(servidor.nro)
                                cliente.paso_por_deuda = True
                                servidor.setEstadoOcupado(self.reloj)
                                self.lista_fines[cliente.tipo_servicio_demandado_original].generar_prox_fin(self.reloj, servidor.nro)
                                cliente.tipo_servicio_demandado = cliente.tipo_servicio_demandado_original
                            else:
                                # si no hay un servidor disponible, se crea un cliente con estado en cola, y se le suma uno mas a la cola del tipo de servicio.
                                cliente.setEstadoEnCola(cliente.tipo_servicio_demandado_original)
                                self.colas[cliente.tipo_servicio_demandado_original] += 1
                                cliente.servidor_asignado = None
                            # se le asigna al cliente cual fue el tipo de servicio que demando.
                        else:                        
                            #print(f'Tipo Servicio Dem: {cliente.tipo_servicio_demandado}, Estado: {cliente.estado}, servidor: {cliente.servidor_asignado.nro}')
                            cliente.setTiempoFin(self.reloj)
                            cliente.quitarDelSistema()
                        break
                    
            # luego, verificamos la cola
            if self.colas[tipo_servicio] > 0:
                # si hay clientes en cola, se genera un proximo fin, se le cambia el estado al cliente y se disminuye en uno la cola
                objeto_fin.generar_prox_fin(self.reloj, nro_servidor)

                for cliente in self.v_clientes:
                    #primero hay que verificar si el cliente esta en cola y luego si el servicio demandado es el que se libero
                    if cliente.estaEnCola() and cliente.tipo_servicio_demandado == tipo_servicio:
                        cliente.setEstadoSiendoAtendido(self.reloj, cliente.tipo_servicio_demandado)
                        cliente.asignar_servidor(self.lista_servidores[tipo_servicio][nro_servidor])
                        tiempo_espera = cliente.get_tiempo_espera()
                        self.v_acumuladores[tipo_servicio].acumular_espera(tiempo_espera)
                        break

                self.colas[tipo_servicio] -= 1
            else:
                # si no hay clientes en cola, se limpia el valor de proximo fin y se establece al servidor en libre
                objeto_fin.v_prox_fin[nro_servidor] = None
                self.lista_servidores[tipo_servicio][nro_servidor].setEstadoLibre(self.reloj)
        return rta
        
                


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
            Label(frame_acumuladores, text=f"{nombre.upper()}:").pack(anchor='w')
            if cantidad_clientes > 0:
                Label(frame_acumuladores, text=f"- Tiempo de espera promedio: {round(tiempo_espera / cantidad_clientes, 2)}").pack(
                    anchor='w')
            if tiempo_ocio_promedio > 0:
                Label(frame_acumuladores,
                      text=f"- Porcentaje Ocupacion: {round(((self.reloj - tiempo_ocio_promedio) / self.reloj) * 100, 2)}").pack(
                    anchor='w')
        Label(frame_acumuladores, text=f"MAYOR CONCURRENCIA: {self.mayor_concurrencia}").pack(anchor='w')
        Label(frame_acumuladores, text="Cantidad clientes que se fueron del sistema:".upper()).pack(anchor='w')
        Label(frame_acumuladores, text=f"Contador: {self.get_contador_clientes_que_se_van()}").pack(anchor='w')


    def contarClientesIdos(self):
        self.contador_clientes_idos += 1
    def getContadorClientesIdos(self):
        return self.contador_clientes_idos

    def get_cantidad_cola_caja(self):
        return self.colas[0]

    def get_contador_clientes_que_se_van(self):
        return self.contador_clientes_que_se_fueron

    def contar_cliente_que_se_va(self):
        self.contador_clientes_que_se_fueron += 1