import tkinter as tk
from tkinter import messagebox


ventana = tk.Tk()
ventana.title("Menú de Operaciones")
ventana.geometry("300x200")


def suma():
    messagebox.showinfo("Suma")

def resta():
    messagebox.showinfo("Resta")

def multiplicacion():
    messagebox.showinfo("Multiplicación")


titulo = tk.Label(ventana, text="Seleccione una operación", font=("Arial", 14))
titulo.pack(pady=10)


btn_suma = tk.Button(ventana, text="Suma", width=20, command=suma)
btn_suma.pack(pady=5)

btn_resta = tk.Button(ventana, text="Resta", width=20, command=resta)
btn_resta.pack(pady=5)

btn_multi = tk.Button(ventana, text="Multiplicación", width=20, command=multiplicacion)
btn_multi.pack(pady=5)


ventana.mainloop()
