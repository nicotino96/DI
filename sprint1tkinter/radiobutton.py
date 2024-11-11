import tkinter as tk

def cambiar_color():
    color = var_radio.get()
    if color == 1:
        root.configure(bg="red")
    elif color == 2:
        root.configure(bg="green")
    elif color == 3:
        root.configure(bg="blue")

root = tk.Tk()
root.title("Radiobutton")
root.geometry("300x300")

var_radio=tk.IntVar()

rojo=tk.Radiobutton(root, text="Rojo",variable=var_radio, value=1, command=cambiar_color)
rojo.pack(pady=5)

verde=tk.Radiobutton(root, text="Verde",variable=var_radio, value=2, command=cambiar_color)
verde.pack(pady=5)

azul=tk.Radiobutton(root, text="Azul",variable=var_radio, value=3, command=cambiar_color)
azul.pack(pady=5)

root.mainloop()