import tkinter as tk


def crear_rectangulo():
    canvas.delete("all")
    x1 = int(entry_x1.get())
    y1 = int(entry_y1.get())
    x2 = int(entry_x2.get())
    y2 = int(entry_y2.get())
    canvas.create_rectangle(x1,x2,y1,y2)
def crear_circulo():
    canvas.delete("all")
    x1 = int(entry_x1.get())
    y1 = int(entry_y1.get())
    x2 = int(entry_x2.get())
    y2 = int(entry_y2.get())
    canvas.create_oval(x1, x2, y1, y2)
root= tk.Tk()
root.title("Canvas")
root.geometry("400x400")

canvas = tk.Canvas(root, width=200, height=200,bg="white")
canvas.pack(pady=20)
#obtenemos coordenadas del rectángulo y/o óvalo
label_x1=tk.Label(root, text="X1:")
label_x1.pack()
entry_x1=tk.Entry(root, width=30)
entry_x1.pack()


label_x2=tk.Label(root, text="X2:")
label_x2.pack()
entry_x2=tk.Entry(root, width=30)
entry_x2.pack()


label_y1=tk.Label(root, text="Y1:")
label_y1.pack()
entry_y1=tk.Entry(root, width=30)
entry_y1.pack()


label_y2=tk.Label(root, text="Y2:")
label_y2.pack()
entry_y2=tk.Entry(root, width=30)
entry_y2.pack()




boton_rectangulo = tk.Button(root, text="Dibujar rectángulo", command=crear_rectangulo)
boton_rectangulo.pack(pady=10)
boton_circulo = tk.Button(root, text="Dibujar círculo", command=crear_circulo)
boton_circulo.pack(pady=10)
root.mainloop()