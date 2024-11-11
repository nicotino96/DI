import tkinter as tk


from usuario import Usuario

# Cada vez que un nuevo usuario sea registrado, se agregará a esta lista.
usuarios=[]
# Cada vez que se meve la barra_edad cambia la edad mostrada
def actualizar_edad(edad):
    etiqueta_edad.config(text=f"Edad: {edad}")
# Para definir el género del usuario registrado(solo permite masculino o femenino)
def cambiar_genero():
    genero=genero_radio.get()
    if genero==1:
        return "Masculino"
    else:
        return "Femenino"

def registro_usuario():
    usuario=Usuario(entrada_nombre.get(),barra_edad.get(),cambiar_genero())#instanciamos el usuario con los atributos escogidos
    usuarios.append(usuario)#lo metemos en la lista
    listbox_usuarios.insert(tk.END, usuario.nombre)#para mostrar en la listbox el nombre de los usuarios registrados
def eliminar_usuario():
    seleccion = listbox_usuarios.curselection()  #obbtener la selección actual
    if seleccion:
        indice = seleccion[0]  #obtenemos nuestra posición en la listbox
        listbox_usuarios.delete(indice)  # Eliminar de la Listbox
        usuarios.pop(indice)  # Eliminar de la lista de usuarios
def mostrar_usuarios():#similar a eliminar_usuarios
    seleccion = listbox_usuarios.curselection()
    if seleccion:
        indice = seleccion[0]
        usuario_seleccionado = listbox_usuarios.get(indice)#obtenemos el usuario del que queremos obetener los datos para mostrarlos
        datos_usuario.config(text=f"Datos de {usuario_seleccionado}: Edad 30, Género Masculino")


if __name__ == '__main__':
    #Ventana principal
    root = tk.Tk()
    root.title("Registro de Usuarios")
    root.geometry("600x400")
    #Primer campo (nombre) que escogemos con el entry debajo de esta etiqueta
    label=tk.Label(root,text="Escribe tu nombre: ")
    label.pack(pady=5)

    entrada_nombre = tk.Entry(root, width=30)
    entrada_nombre.pack(pady=5)
    #Barra (scale) para escoger la barra de edad
    barra_edad = tk.Scale(root, from_=0, to=100, orient="horizontal", command=actualizar_edad)#llama al método que cambia el atributo edad del usuario que se va a meter
    barra_edad.pack(pady=20)
    etiqueta_edad=tk.Label(root, text="Edad: 0")#va mostrando la edad que estamos seleccionando con la barra
    etiqueta_edad.pack(pady=20)
    #Radiobutton para escoge genero del usuario
    genero_radio=tk.IntVar()
    gen_masc=tk.Radiobutton(root, text="Masculino",variable=genero_radio, value=1, command=cambiar_genero)#llama al método que cambia el atributo genero del usuario que se va a meter
    gen_masc.pack(pady=5)
    gen_fem=tk.Radiobutton(root, text="Femenino",variable=genero_radio, value=2, command=cambiar_genero)
    gen_fem.pack(pady=5)
    #boton para efectuar el registro
    boton_registro=tk.Button(root, text="Registrar usuario",command=registro_usuario)
    boton_registro.pack(pady=5)

    etiqueta_label = tk.Label(root, text="Usuarios registrados.")
    etiqueta_label.pack(pady=5)
    #en este frame mostramos la listbos de nombre de lo usuarios registrados
    frame_lista = tk.Frame(root)
    frame_lista.pack(pady=5)
    #scroll para mostrar todos los usuarios que no caben en el frame
    scrollbar_frame = tk.Scrollbar(frame_lista)
    scrollbar_frame.pack(side=tk.RIGHT, fill=tk.Y)
    listbox_usuarios = tk.Listbox(frame_lista, selectmode=tk.SINGLE, bg="grey")
    listbox_usuarios.pack(pady=5)
    #creamos esta etiqueta vacía que se modificara cuando se le de la boton para mostrar los datos del usuario seleccionado
    datos_usuario = tk.Label(root, text="")
    datos_usuario.pack(pady=5)


    boton_mostrar = tk.Button(root, text="Mostrar datos usuario", command=mostrar_usuarios)
    boton_mostrar.pack(pady=5)
    boton_eliminar=tk.Button(root, text="Eliminar usuario", command=eliminar_usuario)
    boton_eliminar.pack(pady=5)


    root.mainloop()