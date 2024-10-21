import tkinter as tk

from entry import boton
from usuario import Usuario

usuarios=[]

def actualizar_edad(edad):
    etiqueta_edad.config(text=f"Edad: {edad}")
def cambiar_genero():
    genero=genero_radio.get()
    if genero_radio==1:
        return "Masculino"
    else:
        return "Femenino"

def registro_usuario():
    usuario=Usuario(entrada_nombre.get(),barra_edad.get(),cambiar_genero())
    usuarios.append(usuario)
    listbox_usuarios.insert(tk.END, usuario.nombre)
def eliminar_usuario():
    seleccion = listbox_usuarios.curselection()  # Obtener la selección actual
    if seleccion:
        indice = seleccion[0]  # Obtener el índice del usuario seleccionado
        listbox_usuarios.delete(indice)  # Eliminar de la Listbox
        usuarios.pop(indice)  # Eliminar de la lista de usuarios



if __name__ == '__main__':
    root = tk.Tk()
    root.title("Registro de Usuarios")
    root.geometry("600x400")

    label=tk.Label(root,text="Escribe tu nombre: ")
    label.pack(pady=5)

    entrada_nombre = tk.Entry(root, width=30)
    entrada_nombre.pack(pady=5)

    barra_edad = tk.Scale(root, from_=0, to=100, orient="horizontal", command=actualizar_edad)
    barra_edad.pack(pady=20)
    etiqueta_edad=tk.Label(root, text="Edad: 0")
    etiqueta_edad.pack(pady=20)

    genero_radio=tk.IntVar()
    gen_masc=tk.Radiobutton(root, text="Masculino",variable=genero_radio, value=1, command=cambiar_genero)
    gen_masc.pack(pady=5)
    gen_fem=tk.Radiobutton(root, text="Femenino",variable=genero_radio, value=2, command=cambiar_genero)
    gen_fem.pack(pady=5)

    boton_registro=tk.Button(root, text="Registrar usuario",command=registro_usuario)
    boton_registro.pack(pady=5)

    etiqueta_label = tk.Label(root, text="Usuarios registrados.")
    etiqueta_label.pack(pady=5)
    frame_lista = tk.Frame(root)
    frame_lista.pack(pady=5)
    scrollbar = tk.Scrollbar(frame_lista)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    listbox_usuarios = tk.Listbox(frame_lista, selectmode=tk.SINGLE, bg="grey")
    listbox_usuarios.pack(pady=5)
    datos_usuario = tk.Label(root, text="")
    datos_usuario.pack(pady=5)

    def mostrar_usuarios():
        seleccion = listbox_usuarios.curselection()
        if seleccion:
            indice = seleccion[0]
            usuario_seleccionado = listbox_usuarios.get(indice)
            datos_usuario.config(text=f"Datos de {usuario_seleccionado}: Edad 30, Género Masculino")
    boton_mostrar = tk.Button(root, text="Mostrar datos usuario", command=mostrar_usuarios)
    boton_mostrar.pack(pady=5)
    boton_eliminar=tk.Button(root, text="Eliminar usuario", command=eliminar_usuario)
    boton_eliminar.pack(pady=5)


    root.mainloop()