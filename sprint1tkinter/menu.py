import tkinter as tk
from tkinter import messagebox


def salir_ventana():
    root.quit()
def mensaje_informativo():
    messagebox.showinfo("Acerca de","Este es lo que aparece cuando le das a este botón")
root = tk.Tk()
root.title("La ventana")
root.geometry("300x150")

menu_principal = tk.Menu(root)
root.config(menu=menu_principal)

menu_archivo = tk.Menu(menu_principal, tearoff=0)
menu_principal.add_cascade(label="Archivo", menu=menu_archivo)
menu_archivo.add_command(label="Abrir")
menu_archivo.add_command(label="Salir",command=salir_ventana)


menu_ayuda = tk.Menu(menu_principal, tearoff=0)
menu_principal.add_cascade(label="Ayuda", menu=menu_ayuda)
menu_ayuda.add_command(label="Acerda de",command=mensaje_informativo)

root.mainloop()