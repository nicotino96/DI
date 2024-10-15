import tkinter as tk

def cambiar_texto():
    label3.config(text="¡El texto ha cambiado!")

ventana = tk.Tk()
ventana.title("La ventana")
ventana.geometry("300x150")


label1 = tk.Label(ventana, text="Bienvenido a la aplicación")
label1.pack(pady=5)

label2 = tk.Label(ventana, text="Nicolás")
label2.pack(pady=5)

label3 = tk.Label(ventana, text="Haz clic en el botón para cambiar este texto")
label3.pack(pady=5)

boton = tk.Button(ventana, text="Cambiar texto", command=cambiar_texto)
boton.pack(pady=5)

ventana.mainloop()

