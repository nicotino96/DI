import tkinter as tk

def mostrar_mensaje():
    etiqueta.config(text="Botón presionado")
def cerrar_ventana():
    ventana.destroy()
ventana = tk.Tk()
ventana.title("Ejercicio 2: Botones")
etiqueta = tk.Label(ventana, text="")
etiqueta.pack(pady=10)
boton_mensaje = tk.Button(ventana, text="Mostrar Mensaje", command=mostrar_mensaje)
boton_mensaje.pack(pady=10)
boton_cerrar = tk.Button(ventana, text="Cerrar", command=cerrar_ventana)
boton_cerrar.pack(pady=10)
ventana.mainloop()