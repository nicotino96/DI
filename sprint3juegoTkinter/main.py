import tkinter as tk
from model import GameModel
from controller import GameController
import tkinter as tk
from controller import GameController
from view import MainMenu


def main():
    root = tk.Tk()
    root.title("Juego de Memoria")

    controller = GameController(root)
    menu = MainMenu(root, controller)

    root.mainloop()

if __name__ == "__main__":
    main()