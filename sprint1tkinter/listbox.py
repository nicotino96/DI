import tkinter as tk
from tkinter.constants import MULTIPLE

def mostrar_seleccion():
    seleccion = listbox.curselection()
    fruta_seleccionada=[listbox.get(i) for i in seleccion]
    etiqueta.config(text=f"Fruta seleccionada: {", ".join(fruta_seleccionada)}")

root = tk.Tk()
root.title("Listbox")
root.geometry("300x300")

frutas = ["Manzana","Banana","Naranja"]

listbox=tk.Listbox(root, selectmode=MULTIPLE)
for fruta in frutas:
    listbox.insert(tk.END, fruta)
listbox.pack(pady=5)

boton=tk.Button(root, text="Mostrar frutas seleccionadas",command=mostrar_seleccion)
boton.pack(pady=5)

etiqueta=tk.Label(root, text="Frutas seleccionadas: Ninguna")
etiqueta.pack(pady=5)

root.mainloop()