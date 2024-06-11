from tkinter import *
from tkinter import ttk
from main import *


def Mensaje_Error(mensaje, titulo, resultado):
    raiz2 = Tk()
    raiz2.title(titulo)
    raiz2.geometry("400x50")

    raiz2.resizable(width=False, height=False)
    if resultado == True:
        back2 = "green3"
    else:
        back2 = "red2"
    raiz2.configure(background=back2)
    nombreMensaje=Label(raiz2, text=mensaje, font=("Arial bold", 13), background=back2)
    nombreMensaje.pack()

def llamar_TP():
    pedido = cuadroPedido.get()
    simulacion = cuadroSimulacion.get()
    reposicion = cuadroReposicion.get()
    costo = cuadroCosto.get()
    precio = cuadroPrecio.get()
    vto = cuadroVto.get()
    recupero = cuadroRecupero.get()
    stock = cuadroStock.get()
    while True:
        if int(pedido) >= 0 \
                and int(simulacion) > 0 \
                and int(reposicion) > 0 \
                and int(costo) >= 0 \
                and int(precio) >= 0 \
                and int(vto) > 0 \
                and int(recupero) >= 0 \
                and int(stock) >= 0:
            Mensaje_Error("Ingreso satisfactorio", "¡¡Bien Hecho!!", True)
            tp_tkinter(int(pedido), int(simulacion), int(reposicion),
                       int(costo), int(precio), int(vto), int(stock), int(recupero)) # Aca llama al tp_tkinter
            break
        else:
            Mensaje_Error("INGRESO INCORRECTO", "¡¡ERROR!!", False)
            return


raiz = Tk()
raiz.title("Grupo F - Ejercicio 4 - Montecarlo")
raiz.geometry("900x600")
ventana = Frame(raiz)
ventana.pack()
raiz.configure(background="#F7D358")
raiz.resizable(width=False, height=False)
back = "#FE9A2E"
ventana.configure(background=back)

cuadroReposicion=Entry(ventana, font=("Arial bold", 13))
cuadroReposicion.grid(row=1,column=1)
nombreReposicion=Label(ventana, text="Ingrese cada cuanto dias se hace la reposicion", font=("Arial bold", 13), background=back)
nombreReposicion.grid(row=1, column=0)


cuadroPedido=Entry(ventana, font=("Arial bold", 13))
cuadroPedido.grid(row=2,column=1)
nombrePedido=Label(ventana, text="Ingrese el tamaño del pedido de reposicion", font=("Arial bold", 13), background=back)
nombrePedido.grid(row=2, column=0)


cuadroSimulacion=Entry(ventana, font=("Arial bold", 13))
cuadroSimulacion.grid(row=3,column=1)
nombreSimulacion=Label(ventana, text="Ingrese la cantidad de dias a simular", font=("Arial bold", 13), background=back)
nombreSimulacion.grid(row=3, column=0)


cuadroVto=Entry(ventana, font=("Arial bold", 13))
cuadroVto.grid(row=4,column=1)
nombreVto=Label(ventana, text="Ingrese la cantidad de dias para descomposición", font=("Arial bold", 13), background=back)
nombreVto.grid(row=4, column=0)


cuadroCosto=Entry(ventana, font=("Arial bold", 13))
cuadroCosto.grid(row=5,column=1)
nombreCosto=Label(ventana, text="Ingrese el costo de compra del producto", font=("Arial bold", 13), background=back)
nombreCosto.grid(row=5, column=0)


cuadroPrecio=Entry(ventana, font=("Arial bold", 13))
cuadroPrecio.grid(row=6,column=1)
nombrePrecio=Label(ventana, text="Ingrese el precio de venta del producto", font=("Arial bold", 13), background=back)
nombrePrecio.grid(row=6, column=0)

cuadroStock=Entry(ventana, font=("Arial bold", 13))
cuadroStock.grid(row=7, column=1)
nombreStock=Label(ventana, text="Ingrese el stock inicial", font=("Arial bold", 13), background=back)
nombreStock.grid(row=7, column=0)

cuadroRecupero=Entry(ventana, font=("Arial bold", 13))
cuadroRecupero.grid(row=8,column=1)
nombreRecupero=Label(ventana, text="Ingrese el valor de recupero (si es cero se asume vencido)", font=("Arial bold", 13), background=back)
nombreRecupero.grid(row=8, column=0)

boton = Button(ventana, text="Aceptar", font=6, command=llamar_TP, width=8, background="#F5DA81")
boton.grid(row=9, column=1)


raiz.mainloop()