import tkinter as tk
from tkinter import *
from tkinter import ttk



def generar_Tabla(hora_corte, prom):
    h=0.01
    C=hora_corte
    t = 0
    tabla = []
    Cprox = hora_corte
    tprox = 0
    T = prom
    fila = ["--", "--", "--", "--", "--", "--", str(Cprox), str(tprox)]
    tabla.append(fila)
    while C>=0:

         C = Cprox
         t = tprox
         K1 = 0.025 * T - 0.5 * C - 12.85
         K2 = 0.025 * T - 0.5 * (C + (h/2)*K1) - 12.85
         K3 = 0.025 * T - 0.5 * (C + (h/2)*K2) - 12.85
         K4 = 0.025 * T - 0.5 * (C + h*K3) - 12.85
         Cprox = C + h/6*(K1 + 2*K2 + 2*K3 + K4)
         tprox = round(t + h, 2)
         fila = [str(t), str(C), str(K1), str(K2), str(K3), str(K4), str(Cprox), str(tprox)]

         tabla.append(fila)


    return t, tabla

