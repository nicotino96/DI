import tkinter as tk

# Función para mostrar el contenido del Entry en la etiqueta
def mostrar_contenido():
    contenido = entry.get()
    label_resultado.config(text=contenido)

# Función para borrar el contenido del Entry
def borrar_contenido():
    entry.delete(0, tk.END)
    label_resultado.config(text="")  # Limpiar la etiqueta también


root = tk.Tk()
root.title("Interfaz con dos Frames")
root.geometry("400x200")

# Crear el Frame superior
frame_superior = tk.Frame(root, bg="lightgray", padx=10, pady=10)
frame_superior.pack(fill="x")

# Etiquetas y campo de entrada en el Frame superior
label1 = tk.Label(frame_superior, text="Etiqueta 1:", bg="lightgray")
label1.pack()
label2 = tk.Label(frame_superior, text="Etiqueta 2:", bg="lightgray")
label2.pack()
entry = tk.Entry(frame_superior, width=30)
entry.pack()

# Crear el Frame inferior
frame_inferior = tk.Frame(root, bg="lightblue", padx=10, pady=10)
frame_inferior.pack(fill="x")

# Etiqueta para mostrar el resultado
label_resultado = tk.Label(frame_inferior, text="", bg="lightblue")
label_resultado.pack(pady=5)

# Botones en el Frame inferior
boton_mostrar = tk.Button(frame_inferior, text="Mostrar", command=mostrar_contenido)
boton_mostrar.pack()

boton_borrar = tk.Button(frame_inferior, text="Borrar", command=borrar_contenido)
boton_borrar.pack()

root.mainloop()