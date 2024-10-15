import tkinter as tk

def obtener_saludo():
    nombre = entrada.get()
    label_resultado.config(text="Hola "+nombre)

root = tk.Tk()
root.title("Entrada")
root.geometry("300x300")

label=tk.Label(root,text="Escribe tu nombre: ")
label.pack(pady=5)

entrada= tk.Entry(root, width=30)
entrada.pack(pady=5)

boton = tk.Button(root,text="Saludo",command=obtener_saludo)
boton.pack(pady=5)

label_resultado= tk.Label(root, text="")
label_resultado.pack(pady=5)

root.mainloop()