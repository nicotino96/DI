import tkinter as tk
from model import GameModel
from controller import GameController
import tkinter as tk
from controller import GameController
from view import MainMenu


def main():
    root = tk.Tk()
    controller = GameController(root)
    root.mainloop()

if __name__ == "__main__":
    main()