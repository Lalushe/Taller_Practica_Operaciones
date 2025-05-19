# main.py (tú)
from tkinter import *
from tkinter import messagebox
from operaciones import suma, resta, multiplicacion

def ejecutar_suma():
    resultado = suma(5, 3)  # valores de ejemplo
    messagebox.showinfo("Resultado", f"Suma: {resultado}")

def ejecutar_resta():
    resultado = resta(5, 3)
    messagebox.showinfo("Resultado", f"Resta: {resultado}")

def ejecutar_multiplicacion():
    resultado = multiplicacion(5, 3)
    messagebox.showinfo("Resultado", f"Multiplicación: {resultado}")

ventana = Tk()
ventana.title("Calculadora Colaborativa")
ventana.geometry("300x200")

Label(ventana, text="Selecciona una operación").pack(pady=10)
Button(ventana, text="Suma", command=ejecutar_suma).pack(pady=5)
Button(ventana, text="Resta", command=ejecutar_resta).pack(pady=5)
Button(ventana, text="Multiplicación", command=ejecutar_multiplicacion).pack(pady=5)

ventana.mainloop()
