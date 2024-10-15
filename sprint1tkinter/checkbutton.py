import tkinter as tk


def actualizar_aficiones():
    seleccionadas = []
    if leer_var.get():
        seleccionadas.append("Leer")
    if deporte_var.get():
        seleccionadas.append("Deporte")
    if musica_var.get():
        seleccionadas.append("Música")

    label_resultado.config(text="Aficiones : " + ", ".join(seleccionadas))


root = tk.Tk()
root.title("Aficiones")
root.geometry("300x200")

leer_var = tk.BooleanVar()
deporte_var = tk.BooleanVar()
musica_var = tk.BooleanVar()


check_leer = tk.Checkbutton(root, text="Leer", variable=leer_var, command=actualizar_aficiones)
check_leer.pack(anchor='w')

check_deporte = tk.Checkbutton(root, text="Deporte", variable=deporte_var, command=actualizar_aficiones)
check_deporte.pack(anchor='w')

check_musica = tk.Checkbutton(root, text="Música", variable=musica_var, command=actualizar_aficiones)
check_musica.pack(anchor='w')


label_resultado = tk.Label(root, text="Aficiones seleccionadas: ")
label_resultado.pack(pady=10)

root.mainloop()