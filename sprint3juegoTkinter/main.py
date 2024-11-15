import tkinter as tk
from model import GameModel
from controller import GameController
import tkinter as tk
from controller import GameController

if __name__ == "__main__":
    # Crear ventana principal de Tkinter
    root = tk.Tk()

    # Inicializar el controlador
    controller = GameController(root)

    # Iniciar el loop de la aplicación
    root.mainloop()