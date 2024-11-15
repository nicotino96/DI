from tkinter import simpledialog

from PIL._tkinter_finder import tk

from model import GameModel
from view import MainMenu, GameView


class GameController:
    def __init__(self, root):
        self.root = root
        self.model = None
        self.selected = {}
        self.main_menu = MainMenu(root, self.start_game_callback, self.show_stats_callback, self.quit_callback)
        self.time_started = False
    def start_game_callback(self):#
        """
        vista = GameView(self.on_card_click, self.update_move_count,
                 self.update_time)
        vista.window= tk.TopLevel(self.root)
        get_nombre = simpledialog.askstring("Introduce nombre","Introduce nombre: ")#generar tablero (con modelo)
        get_dificultad = simpledialog.askstring("Dificultad", "Selecciona la dificutad")#sacar dificultad
        self.model = GameModel(get_dificultad,get_nombre)
        """
        tk.messagebox.showinfo("Estadísticas", "Mostrando estadísticas (en desarrollo).")
    def show_stats_callback(self):
        """
        Función que se ejecuta al hacer clic en "Estadísticas".
        """
        tk.messagebox.showinfo("Estadísticas", "Mostrando estadísticas (en desarrollo).")
        # Aquí se mostrarían las estadísticas. Actualmente muestra un mensaje.

    def quit_callback(self):
        """
        Función que se ejecuta al hacer clic en "Salir".
        """
        respuesta = tk.messagebox.askyesno("Salir", "¿Estás seguro de que quieres salir?")
        if respuesta:
            self.root.quit()
            """
    def on_card_click(self):
    def update_move_count(self):
    def update_time(self):
            """