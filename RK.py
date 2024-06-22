import tkinter as tk
from tkinter import *
from tkinter import ttk


def mostrar_datos(tabla):
    i = 0
    raiz = Tk()
    raiz.title("Grupo F - Ejercicio 4 - Montecarlo")

    ventana = Frame(raiz)
    ventana.pack()

    grilla = ttk.Treeview(ventana, columns=("col1", "col2", "col3", "col4", "col5", "col6", "col7"))
    barra = ttk.Scrollbar(raiz, orient="vertical", command=grilla.yview)
    barra.pack(side="right", fill="x")
    raiz.resizable(width=False, height=False)
    grilla.configure(xscrollcommand = barra.set)

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
    while i != len(tabla):
        grilla.insert("", END, text=tabla[i][0], values=(tabla[i][1], tabla[i][2], tabla[i][3], tabla[i][4],
                                                         tabla[i][5], tabla[i][6], tabla[i][7]))
        i = i + 1
    scroll_y = Scrollbar(ventana, orient="vertical", command=grilla.yview)
    scroll_y.pack(side="right", fill="y")
    grilla.configure(yscrollcommand=scroll_y.set)

    grilla.pack(fill="both", expand=True)

    raiz.mainloop()

def generar_Tabla(hora_corte):
    i = 0
    h=0.1
    C=hora_corte
    t = 0
    tabla = []

    while C>=0:

         if i == 0:
             Cprox = C
             tprox = t
             fila=["--", "--", "--", "--", "--", "--", str(Cprox), str(tprox)]

         else:
             C = Cprox
             t = tprox
             K1 = 0.025 * t - 0.5 * C - 12.85
             K2 = 0.025 * t - 0.5 * (C + (h/2)*K1) - 12.85
             K3 = 0.025 * t - 0.5 * (C + (h/2)*K2) - 12.85
             K4 = 0.025 * t - 0.5 * (C + h*K3) - 12.85
             Cprox = C + h/6*(K1 + 2*K2 + 2*K3 + K4)
             tprox = round(t + h, 2)
             fila = [str(t), str(C), str(K1), str(K2), str(K3), str(K4), str(Cprox), str(tprox)]

         tabla.append(fila)
         i = i + 1

    return tabla

