# main.py
from tkinter import *
from tkinter import messagebox
from operaciones import suma, resta, multiplicacion

def ejecutar_suma():
    try:
        a = int(entrada1.get())
        b = int(entrada2.get())
        resultado = suma(a, b)
        messagebox.showinfo("Resultado", f"Suma: {resultado}")
    except ValueError:
        messagebox.showerror("Error", "Por favor ingresa números válidos")

def ejecutar_resta():
    try:
        a = int(entrada1.get())
        b = int(entrada2.get())
        resultado = resta(a, b)
        messagebox.showinfo("Resultado", f"Resta: {resultado}")
    except ValueError:
        messagebox.showerror("Error", "Por favor ingresa números válidos")

def ejecutar_multiplicacion():
    try:
        a = int(entrada1.get())
        b = int(entrada2.get())
        resultado = multiplicacion(a, b)
        messagebox.showinfo("Resultado", f"Multiplicación: {resultado}")
    except ValueError:
        messagebox.showerror("Error", "Por favor ingresa números válidos")

# Interfaz
ventana = Tk()
ventana.title("Calculadora Colaborativa")
ventana.geometry("300x300")

Label(ventana, text="Número 1:").pack()
entrada1 = Entry(ventana)
entrada1.pack()

Label(ventana, text="Número 2:").pack()
entrada2 = Entry(ventana)
entrada2.pack()

Label(ventana, text="Seleccione una operación").pack(pady=10)
Button(ventana, text="Suma", command=ejecutar_suma).pack(pady=5)
Button(ventana, text="Resta", command=ejecutar_resta).pack(pady=5)
Button(ventana, text="Multiplicación", command=ejecutar_multiplicacion).pack(pady=5)

ventana.mainloop()
