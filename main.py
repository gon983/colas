from tkinter import *
from tkinter import ttk


def truncate(number: float, max_decimals: int) -> float:
    int_part, dec_part = str(number).split(".")
    return float(".".join((int_part, dec_part[:max_decimals])))


def tp_tkinter(pedido, simulacion, reposicion, costo_, precio_, vto_, stock_, recupero_):
    if simulacion == 0:
        mostrar_datos([], 0)
    else:
        tabla = [pedido, simulacion, reposicion, costo_, precio_, vto_, stock_, recupero_]
        print(tabla)
        

def mostrar_datos(tabla, promedio):
    i = 0
    raiz = Tk()
    raiz.title("Grupo F - Ejercicio 4 - Montecarlo")

    ventana = Frame(raiz)
    ventana.pack()

    grilla = ttk.Treeview(ventana, columns=("col1", "col2", "col3", "col4", "col5", "col6", "col7", "col8", "col9"))
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
    grilla.column("col8", width=150)

    grilla.heading("#0", text="Dias")
    grilla.heading("col1", text="RND Demanda")
    grilla.heading("col2", text="Demanda")
    grilla.heading("col3", text="Q(Stock)")
    grilla.heading("col4", text="Q Resultante")
    grilla.heading("col5", text="Q Recuperado")
    grilla.heading("col6", text="Venta")
    grilla.heading("col7", text="Costo Pedido")
    grilla.heading("col8", text="Total Dia")
    grilla.heading("col9", text="Acumulado")

    grilla.insert("", END, text="0", values=("N/A", "N/A", "0", "0", "0", "N/A", "N/A", "N/A", "N/A"))

    while i != len(tabla):
        grilla.insert("", END, text=str(tabla[i][0]), values=(tabla[i][1], tabla[i][2], tabla[i][3], tabla[i][4], tabla[i][5], tabla[i][6], tabla[i][7], tabla[i][8], tabla[i][9]))
        i = i + 1

    scroll_y = Scrollbar(ventana, orient = "vertical", command=grilla.yview)
    scroll_y.pack(side="right", fill="y")
    grilla.configure(yscrollcommand=scroll_y.set)

    nombrePromedio = Label(ventana, text="Ganancia promedio: $" + str(truncate(promedio, 2)))
    
    grilla.pack(fill="both", expand=True)
    nombrePromedio.pack()
    
    raiz.mainloop()
    return
