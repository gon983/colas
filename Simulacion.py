import main
from Llegada import Llegada 
from Fin import Fin
from Cliente import Cliente
from Servidor import *
from tkinter import *
from tkinter import ttk


# Definición de la clase
class Simulacion:
    # El método __init__ es el constructor de la clase
    def __init__(self, cantidad_cajeros):
        
        self.lista_llegadas = [None, None, None, None, None]
        self.lista_fines = [None, None, None, None, None]
        self.lista_servidores =[[],[],[],[],[]]
        self.v_clientes =[]
        #cada posicion representa una cola por servicio
        self.colas = [0, 0, 0, 0, 0]
        
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


    def fila(self, nombre, tiempo_actual, cantidad_cajeros):
        v_inicial = [nombre,tiempo_actual, self.lista_llegadas[0].prox_llegada,
                                    self.lista_llegadas[1].prox_llegada,
                                    self.lista_llegadas[2].prox_llegada,
                                    self.lista_llegadas[3].prox_llegada,
                                    self.lista_llegadas[4].prox_llegada]
        
        for i in range(cantidad_cajeros):
            x = self.lista_fines[0].v_prox_fin[i] 
            v_inicial.append(x)
        
        v_final =  [self.lista_fines[1].v_prox_fin[0],
                                    self.lista_fines[1].v_prox_fin[1],
                                    self.lista_fines[1].v_prox_fin[2],
                                    self.lista_fines[2].v_prox_fin[0],
                                    self.lista_fines[2].v_prox_fin[1],
                                    self.lista_fines[3].v_prox_fin[0],
                                    self.lista_fines[4].v_prox_fin[0],
                                    self.lista_fines[4].v_prox_fin[1]]
        
        for i in range(cantidad_cajeros):
            x = self.lista_servidores[0][i].getEstado()
            v_final.append(x)
            
        #como hay cola unica por servicio saque esto del for.
        v_final.append(self.colas[0])   
             
        v_3 = [ self.lista_servidores[1][0].getEstado(),
                self.lista_servidores[1][1].getEstado(),
                self.lista_servidores[1][2].getEstado(),
                self.colas[1],
                self.lista_servidores[2][0].getEstado(),
                self.lista_servidores[2][1].getEstado(),
                self.colas[2],
                self.lista_servidores[3][0].getEstado(),
                self.colas[3],
                self.lista_servidores[4][0].getEstado(),
                self.lista_servidores[4][1].getEstado(),
                self.colas[4]
            ]
            
        if len(self.v_clientes)>0:
            for i in range(len(self.v_clientes)):
                v_3.append(self.v_clientes[i].estado) # solo agrega el estado para simplificar en la interfaz
            
        
        v_retornar = v_inicial + v_final + v_3
        return v_retornar

    def inicializacion(self, media_caja, media_atencion_personalizada, media_tarjeta_credito, media_plazo_fijo, media_prestamos,
                    cantidad_cajas):
        
        nombre_llegada = ""
        media = 0
        for i in range(len(self.lista_llegadas)):
            if i == 0:
                media = media_caja
                nombre_llegada = "caja"
            elif i == 1:
                media = media_atencion_personalizada
                nombre_llegada = "atencion_personalizada"
            elif i == 2:
                media = media_tarjeta_credito
                nombre_llegada = "tarjeta_credito"
            elif i == 3:
                media = media_plazo_fijo
                nombre_llegada = "plazo_fijo"
            elif i == 4:
                media = media_prestamos
                nombre_llegada = "prestamos"
            
            self.lista_llegadas[i] =  Llegada(nombre_llegada, None)
            self.lista_llegadas[i].generar_prox_Llegada(media, 0)
            
        cant_serv = 0
        tasa_rendim = ""
        nombre_fin = ""
        for i in range(len(self.lista_fines)):
            if i == 0: 
                nombre_fin = "caja"
                cant_serv = cantidad_cajas
                tasa_rendim = 10
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
            
            self.lista_fines[i] =  Fin(nombre_fin, cant_serv, tasa_rendim)

    def agregar_linea_a_tabla(self,cantidad_cajeros, tupla_inicial, max_cli):
        pass
    
    def generar_tabla(self, cantidad_cajeros, tupla_inicial, max_cli):
        i = 0
        raiz = Tk()
        raiz.title("Grupo F - TP 4 - Linea de Colas")

        screen_width = raiz.winfo_screenwidth()
        screen_height = raiz.winfo_screenheight()
        raiz.geometry(f"{screen_width}x{screen_height}")

        ventana = Frame(raiz)
        ventana.pack(fill=BOTH, expand=True)
        
        
        columns = ["col1", "col2", "col3", "col4", "col5", "col6", "col7", "col8", "col9","col10","col11","col12","col13","col14","col15"]
        for i in range((cantidad_cajeros+ cantidad_cajeros*2+ 16+ max_cli)):
            columns.append(f'col{16+i}')    

        grilla = ttk.Treeview(ventana, columns=columns)
        
        # Crear y configurar la barra de desplazamiento vertical
        
        scroll_y = Scrollbar(ventana, orient=VERTICAL, command=grilla.yview)
        scroll_y.pack(side=RIGHT, fill=Y)
        grilla.configure(yscrollcommand=scroll_y.set)

        # Crear y configurar la barra de desplazamiento horizontal
        scroll_x = Scrollbar(ventana, orient=HORIZONTAL, command=grilla.xview)
        scroll_x.pack(side=BOTTOM, fill=X)
        grilla.configure(xscrollcommand=scroll_x.set)

        # grilla.column("#0", width=150)
        for col in columns:
            grilla.column(col, width=150)

        for i in range(cantidad_cajeros):
            grilla.column(f'col{16+i}', width=150)

        for i in range(cantidad_cajeros*2):
            grilla.column(f'col{16+cantidad_cajeros+i}', width=150)

        for i in range(max_cli):
            grilla.column(f'col{16+cantidad_cajeros+i+cantidad_cajeros*2}', width=150)

        

        # grilla.heading("#0", text="Dias")
        grilla.heading("col1", text="Eventos")
        grilla.heading("col2", text="Reloj(horas)")
        grilla.heading("col3", text="Proxima llegada caja")
        grilla.heading("col4", text="Proxima at personalizada")
        grilla.heading("col5", text="Proxima llegada tarjeta credito")
        grilla.heading("col6", text="Proxima llegada plazo fijo")
        grilla.heading("col7", text="Proxima llegada prestamos")
        
        for i in range(cantidad_cajeros):
            grilla.heading(f"col{8+i}", text=f"fin caja {i+1}")

        cant_encabez_agregados = (7 + cantidad_cajeros) #9

        grilla.heading(f"col{cant_encabez_agregados+1}", text="fin atencion personalizada 1")
        grilla.heading(f"col{cant_encabez_agregados+2}", text="fin atencion personalizada 2 ")
        grilla.heading(f"col{cant_encabez_agregados+3}", text="fin atencion personalizada 3 ")
        grilla.heading(f"col{cant_encabez_agregados+4}", text="fin tarjeta credito 1")
        grilla.heading(f"col{cant_encabez_agregados+5}", text="fin tarjeta credito 2")
        grilla.heading(f"col{cant_encabez_agregados+6}", text="fin plazo fijo")
        grilla.heading(f"col{cant_encabez_agregados+7}", text="fin prestamos 1")
        grilla.heading(f"col{cant_encabez_agregados+8}", text="fin prestamos 2")
        
        # en los fines primero va el fin de caja
        
        for i in range(cantidad_cajeros):
            grilla.heading(f"col{9+cant_encabez_agregados+i}", text=f"estado caja {i}")

        cant_encabez_agregados = cant_encabez_agregados + 8 + cantidad_cajeros  #20
        
        grilla.heading(f"col{cant_encabez_agregados+1}", text="cola caja")

        grilla.heading(f"col{cant_encabez_agregados+2}", text="estado atencion personalizada 1")
        grilla.heading(f"col{cant_encabez_agregados+3}", text="estado atencion personalizada 2 ")
        grilla.heading(f"col{cant_encabez_agregados+4}", text="estado atencion personalizada 3 ")
        grilla.heading(f"col{cant_encabez_agregados+5}", text="cola atencion personalizada")
        grilla.heading(f"col{cant_encabez_agregados+6}", text="estado tarjeta credito 1")
        grilla.heading(f"col{cant_encabez_agregados+7}", text="estado tarjeta credito 2")
        grilla.heading(f"col{cant_encabez_agregados+8}", text="cola tarjeta credito")
        grilla.heading(f"col{cant_encabez_agregados+9}", text="estado plazo fijo")
        grilla.heading(f"col{cant_encabez_agregados+10}", text="cola plazo fijo")
        grilla.heading(f"col{cant_encabez_agregados+11}", text="estado prestamos 1")
        grilla.heading(f"col{cant_encabez_agregados+12}", text="estado prestamos 2")
        grilla.heading(f"col{cant_encabez_agregados+13}", text="cola prestamos")

        cant_encabez_agregados = cant_encabez_agregados + 13 + 1

        for i in range(max_cli):
            grilla.heading(f"col{cant_encabez_agregados+i}", text=f"E Cliente{i}")
    
        
        grilla.pack(fill="both", expand=True)
        grilla.insert("", END, values=tupla_inicial)
        
        raiz.mainloop()
        return grilla
    
    
    def buscar_servidor_disponible(self, tipo_servicio):

        # accede a la posicion en la lista de servidores que corresponde al tipoo de servicio solicitado
        # recorre a todos lod servidores de ese servicio y devuelve al primer desocupado
        for servidor in self.lista_servidores[tipo_servicio]:
            if servidor.estoyLibre: return (servidor)
        return(None)
            
        return (False, None)
    
    def buscar_proximo_evento(self):
        
        (tipo_llegada, objeto_prox_lleg) = min(enumerate(self.lista_llegadas), key=lambda llegadaX: llegadaX[1].prox_llegada)
        #falta buscar el proximo fin y comparar si es menor a la proxima llegada
        return (objeto_prox_lleg, tipo_llegada, None)
 
    def ejecutar_proxima_llegada(self, objeto_llegada, tipo_servicio):
    
        servidor = self.buscar_servidor_disponible(tipo_servicio)
        if servidor:
            #ver que el segundo parametro tiene q ser el tiempo de llegada
            nuevo_cliente = Cliente(f"siendoAtendido_{objeto_llegada.nombre}", 0)
            servidor.setEstadoOcupado()
        else: 
            nuevo_cliente = Cliente(f"enCola_{objeto_llegada.nombre}", 0)
            self.colas[tipo_servicio] += 1
        self.v_clientes.append(nuevo_cliente)

