import tkinter as tk
from model import GameModel
from controller import GameController

def main():
    root = tk.Tk()
    modelo = GameModel(medio, Nico)
    vista = View(root)
    controlador = GameController(modelo, vista)
    root.mainloop()

if __name__ == "__main__":
    main()