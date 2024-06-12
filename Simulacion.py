import main
from Llegada import Llegada 
from Fin import Fin
from Servidor import *
from tkinter import *
from tkinter import ttk


# Definición de la clase
class Simulacion:
    # El método __init__ es el constructor de la clase
    def __init__(self, cantidad_cajeros):
        self.llegada_caja = None
        self.llegada_atencion_personalizada = None
        self.llegada_tarjeta_credito = None
        self.llegada_plazo_fijo = None
        self.llegada_prestamos = None

        self.fin_caja = None
        self.fin_atencion_personalizada = None
        self.fin_tarjeta_credito = None
        self.fin_plazo_fijo = None
        self.fin_prestamos = None

        self.servidores_caja = []
        self.servidores_atencion_personalizada = []
        self.servidores_tarjeta_credito = []
        self.servidores_plazo_fijo = []
        self.servidores_prestamo = []

        for i in range(cantidad_cajeros):
            self.servidores_caja.append(Servidor('libre',0))
        
        for i in range(3):
            self.servidores_atencion_personalizada.append(Servidor('libre',0))

        for i in range(2):
            self.servidores_tarjeta_credito.append(Servidor('libre',0))

        for i in range(1):
            self.servidores_plazo_fijo.append(Servidor('libre',0))

        for i in range(2):
            self.servidores_prestamo.append(Servidor('libre',0))

        
        

    def fila(self, nombre, tiempo_actual, cantidad_cajeros):
        v_inicial = [nombre,tiempo_actual, self.llegada_caja.prox_llegada,
                                    self.llegada_atencion_personalizada.prox_llegada,
                                    self.llegada_tarjeta_credito.prox_llegada,
                                    self.llegada_plazo_fijo.prox_llegada,
                                    self.llegada_prestamos.prox_llegada]
        
        for i in range(cantidad_cajeros):
            x = self.fin_caja.v_prox_fin[i] 
            v_inicial.append(x)
        
        v_final =  [self.fin_atencion_personalizada.v_prox_fin[0],
                                    self.fin_atencion_personalizada.v_prox_fin[1],
                                    self.fin_atencion_personalizada.v_prox_fin[2],
                                    self.fin_tarjeta_credito.v_prox_fin[0],
                                    self.fin_tarjeta_credito.v_prox_fin[1],
                                    self.fin_plazo_fijo.v_prox_fin[0],
                                    self.fin_prestamos.v_prox_fin[0],
                                    self.fin_prestamos.v_prox_fin[1]]
        
        for i in range(cantidad_cajeros):
            x = self.servidores_caja[i].getEstado()
            y = self.servidores_caja[i].cola
            v_final.append(x)
            v_final.append(y)
        
        v_3 = [self.servidores_atencion_personalizada[0].getEstado(),
                            self.servidores_atencion_personalizada[0].cola,
                                    self.servidores_atencion_personalizada[1].getEstado(),
                                    self.servidores_atencion_personalizada[1].cola,
                                    self.servidores_atencion_personalizada[2].getEstado(),
                                    self.servidores_atencion_personalizada[2].cola,
                                    self.servidores_tarjeta_credito[0].getEstado(),
                                    self.servidores_tarjeta_credito[0].cola,
                                    self.servidores_tarjeta_credito[1].getEstado(),
                                    self.servidores_tarjeta_credito[1].cola,
                                    self.servidores_plazo_fijo[0].getEstado(),
                                    self.servidores_plazo_fijo[0].cola,
                                    self.servidores_prestamo[0].getEstado(),
                                    self.servidores_prestamo[0].cola,
                                    self.servidores_prestamo[1].getEstado(),
                                    self.servidores_prestamo[1].cola]
        
        v_retornar = v_inicial + v_final + v_3
        return v_retornar

    
    


    def inicializacion(self, media_caja, media_atencion_personalizada, media_tarjeta_credito, media_plazo_fijo, media_prestamos,
                    cantidad_cajas):
        self.llegada_caja = Llegada(None)
        self.llegada_atencion_personalizada = Llegada(None)
        self.llegada_tarjeta_credito = Llegada(None)
        self.llegada_plazo_fijo = Llegada(None)
        self.llegada_prestamos = Llegada(None)

        self.fin_caja = Fin(cantidad_cajas,10)
        self.fin_atencion_personalizada = Fin(3,5)
        self.fin_tarjeta_credito = Fin(2,3)
        self.fin_plazo_fijo = Fin(1,2)
        self.fin_prestamos = Fin(2,4)

        



        self.llegada_caja.generar_prox_Llegada(media_caja,0)
        self.llegada_atencion_personalizada.generar_prox_Llegada(media_atencion_personalizada,0)
        self.llegada_tarjeta_credito.generar_prox_Llegada(media_tarjeta_credito,0)
        self.llegada_plazo_fijo.generar_prox_Llegada(media_plazo_fijo,0)
        self.llegada_prestamos.generar_prox_Llegada(media_prestamos,0)


      



    def mostrar_datos(self,cantidad_cajeros, tupla_inicial):
        i = 0
        raiz = Tk()
        raiz.title("Grupo F - Ejercicio 4 - Linea de Colas")

        ventana = Frame(raiz)
        ventana.pack()
        columns = ["col1", "col2", "col3", "col4", "col5", "col6", "col7", "col8", "col9","col10","col11","col12","col13","col14","col15"]
        for i in range((cantidad_cajeros+ cantidad_cajeros*2+ 16)):
            columns.append(f'col{16+i}')    

        grilla = ttk.Treeview(ventana, columns=columns)
        barra = ttk.Scrollbar(raiz, orient="vertical", command=grilla.yview)
        barra.pack(side="right", fill="x")
        raiz.resizable(width=False, height=False)
        grilla.configure(xscrollcommand = barra.set)

        # grilla.column("#0", width=150)
        grilla.column("col1", width=150)
        grilla.column("col2", width=150)
        grilla.column("col3", width=150)
        grilla.column("col4", width=150)
        grilla.column("col5", width=150)
        grilla.column("col6", width=150)
        grilla.column("col7", width=150)
        grilla.column("col8", width=150)
        grilla.column("col9", width=150)
        grilla.column("col10", width=150)
        grilla.column("col11", width=150)
        grilla.column("col12", width=150)
        grilla.column("col13", width=150)
        grilla.column("col14", width=150)
        grilla.column("col15", width=150)

        for i in range(cantidad_cajeros):
            grilla.column(f'col{16+i}', width=150)

        for i in range(cantidad_cajeros*2):
            grilla.column(f'col{16+cantidad_cajeros+i}', width=150)

        # grilla.heading("#0", text="Dias")
        grilla.heading("col1", text="Eventos")
        grilla.heading("col2", text="Reloj(horas)")
        grilla.heading("col3", text="Proxima llegada caja")
        grilla.heading("col4", text="Proxima at personalizada")
        grilla.heading("col5", text="Proxima llegada tarjeta credito")
        grilla.heading("col6", text="Proxima llegada plazo fijo")
        grilla.heading("col7", text="Proxima llegada prestamos")
        


        for i in range(cantidad_cajeros):
            grilla.heading(f"col{8+i}", text=f"fin caja{i+1}")

        

        comenzamos = (7 + cantidad_cajeros)

        grilla.heading(f"col{comenzamos+1}", text="fin atencion personalizada 1")
        grilla.heading(f"col{comenzamos+2}", text="fin atencion personalizada 2 ")
        grilla.heading(f"col{comenzamos+3}", text="fin atencion personalizada 3 ")
        grilla.heading(f"col{comenzamos+4}", text="fin tarjeta credito 1")
        grilla.heading(f"col{comenzamos+5}", text="fin tarjeta credito 2")
        grilla.heading(f"col{comenzamos+6}", text="fin plazo fijo")
        grilla.heading(f"col{comenzamos+7}", text="fin prestamos 1")
        grilla.heading(f"col{comenzamos+8}", text="fin prestamos 2")
        
        # en los fines primero va el fin de caja
        
        for i in range(0,cantidad_cajeros*2,2 ):
            grilla.heading(f"col{9+comenzamos+i}", text=f"estado caja{i}")
            grilla.heading(f"col{9+comenzamos+i+1}", text=f"cola caja{i}")

        seguimos = 8+ comenzamos + cantidad_cajeros*2 

        grilla.heading(f"col{seguimos+1}", text="estado atencion personalizada 1")

        grilla.heading(f"col{seguimos+2}", text="cola atencion personalizada 1")
        grilla.heading(f"col{seguimos+3}", text="estado atencion personalizada 2 ")
        grilla.heading(f"col{seguimos+4}", text="cola atencion personalizada 2")
        grilla.heading(f"col{seguimos+5}", text="estado atencion personalizada 3 ")
        grilla.heading(f"col{seguimos+6}", text="cola atencion personalizada 3")

        grilla.heading(f"col{seguimos+7}", text="estado tarjeta credito 1")
        grilla.heading(f"col{seguimos+8}", text="cola tarjeta credito 1")
        grilla.heading(f"col{seguimos+9}", text="estado tarjeta credito 2")
        grilla.heading(f"col{seguimos+10}", text="cola tarjeta credito 2")
        grilla.heading(f"col{seguimos+11}", text="estado plazo fijo")
        grilla.heading(f"col{seguimos+12}", text="cola plazo fijo")
        grilla.heading(f"col{seguimos+13}", text="estado prestamos 1")
        grilla.heading(f"col{seguimos+14}", text="cola prestamos 1")
        grilla.heading(f"col{seguimos+15}", text="estado prestamos 2")
        grilla.heading(f"col{seguimos+16}", text="cola prestamos 2")



    

        grilla.insert("", END, values=tupla_inicial)

        # while i != len(tabla):
        #     grilla.insert("", END, text=str(tabla[i][0]), values=(tabla[i][1], tabla[i][2], tabla[i][3], tabla[i][4], tabla[i][5], tabla[i][6], tabla[i][7], tabla[i][8], tabla[i][9]))
        #     i = i + 1

        scroll_y = Scrollbar(ventana, orient = "vertical", command=grilla.yview)
        scroll_y.pack(side="right", fill="y")
        grilla.configure(yscrollcommand=scroll_y.set)

        
        
        grilla.pack(fill="both", expand=True)
        
        
        raiz.mainloop()
        return
    



