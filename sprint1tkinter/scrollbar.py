import tkinter as tk

def salir_ventana():
    root.quit()

root = tk.Tk()
root.title("Ventana con Scrollbar")
root.geometry("400x300")

# Crear un Frame para contener el Text y Scrollbar
frame = tk.Frame(root)
frame.pack(fill="both", expand=True)

# Crear el widget Text
texto = tk.Text(frame, wrap="word",width=51, height=10)
texto.pack(side="left", fill="both", expand=True)
texto.grid(row=0,column=0,sticky="nsew")

# Crear la barra de desplazamiento vertical
scrollbar = tk.Scrollbar(frame,orient="vertical", command=texto.yview)
scrollbar.grid(row=0, column=1, sticky="ns")
texto.config(yscrollcommand=scrollbar.set)

# Texto largo que aparecerá en el Text
contenido = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus odio tortor, laoreet nec
    vulputate viverra, tincidunt sit amet metus. Phasellus ut turpis nibh. Maecenas accumsan lacinia arcu sed
    tempus. Suspendisse nisi libero, condimentum vel tempus id, gravida eget ante. Nulla at consectetur neque,
    eu vulputate lorem. Integer fringilla orci non lacus malesuada, ac vehicula dolor ornare. Quisque feugiat lacus
    eget egestas porttitor. Sed eget urna sed velit rutrum ultricies. Ut ornare tellus sed aliquet tempus.
    Suspendisse at magna lectus. Vestibulum eu condimentum est, et lobortis erat. Nulla in tempus leo. Quisque
    dignissim, enim sed scelerisque fringilla, eros velit egestas lorem, in sollicitudin sapien ligula a ipsum.

    Nunc lorem ante, varius nec lobortis quis, faucibus eget orci. Duis eu lobortis odio. Phasellus ultrices
    ligula a imperdiet eleifend. Proin maximus sed nibh non auctor. Etiam nunc ipsum, hendrerit a scelerisque
    vitae, vestibulum sit amet dolor. Nam lobortis libero nibh, quis auctor justo semper quis. Phasellus lacus
    arcu, semper ut ante quis, feugiat viverra erat. In pellentesque vulputate augue. Phasellus vel metus orci.
    Sed egestas diam at malesuada dapibus. Sed euismod felis eu libero tempus, eu finibus enim pharetra.
    Nunc facilisis tincidunt risus. Praesent libero velit, vestibulum eu justo quis, scelerisque ullamcorper quam.

    Nunc ultrices sit amet est non blandit. Vestibulum ac erat non velit tincidunt finibus. Sed ligula arcu, laoreet
    a magna sit amet, pellentesque scelerisque lorem. Donec ullamcorper nisl nec sodales finibus. Vestibulum maximus
    lectus sollicitudin massa porta, sit amet elementum orci rhoncus. Aenean posuere congue nisl, in cursus urna
    scelerisque vel. In mollis nisl vel lacinia convallis. Etiam quis arcu et justo bibendum pharetra. Phasellus ornare
    leo ullamcorper, efficitur nunc sit amet, iaculis ipsum.

    Aliquam in lectus vitae nibh malesuada lobortis sit amet a quam. Mauris in scelerisque dui. Praesent bibendum,
    magna at sodales rutrum, tortor mi varius massa, eget mollis lorem quam in lectus. Vivamus efficitur, dolor a
    pulvinar fringilla, enim lorem semper lectus, et vulputate diam tortor et neque. Phasellus nibh diam, aliquam
    iaculis tempus ut, sollicitudin sodales mi. Etiam dui mi, rutrum sed elit at, lobortis laoreet augue. Donec
    ullamcorper, libero feugiat placerat finibus, dui orci ultricies turpis, luctus elementum ex mi mattis libero.
    Proin pretium aliquam augue, non fermentum dolor tincidunt sed. Curabitur et pretium velit. Donec rutrum venenatis
    lacus, non volutpat dolor gravida vitae. Proin vel auctor arcu. Etiam varius nulla arcu, vel rhoncus lectus
    sollicitudin eleifend. Ut pulvinar nibh enim. Duis nisl orci, molestie ac quam venenatis, tincidunt egestas odio.

    Mauris egestas finibus lacus sit amet auctor. Fusce ac urna ipsum. Phasellus efficitur tortor vel orci commodo,
    a laoreet mi sagittis. Morbi luctus, arcu sit amet scelerisque aliquam, nunc metus euismod mauris, ac finibus elit
    dui in ipsum. Donec tempus, enim vitae fringilla convallis, magna libero suscipit elit, vitae tempus odio ex eget
    massa. In et eleifend magna. Aliquam condimentum, mi vitae posuere sollicitudin, libero dolor iaculis nibh, in
    vulputate urna mauris et mi. Aliquam nec facilisis neque. Quisque sed enim sed velit efficitur finibus. Phasellus
    nunc quam, ullamcorper at quam sit amet, condimentum scelerisque quam.
"""
# Insertar el texto largo en el Text widget
texto.insert(tk.END, contenido)

root.mainloop()