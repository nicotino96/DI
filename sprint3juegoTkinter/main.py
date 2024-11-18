import tkinter as tk
from controller import GameController



def main():
    root = tk.Tk()
    controller = GameController(root)
    root.mainloop()

if __name__ == "__main__":
    main()