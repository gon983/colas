import tkinter as tk
from tkinter import *
from tkinter import ttk



def generar_Tabla(hora_corte):
    i = 0
    h=0.01
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

    return t, tabla

