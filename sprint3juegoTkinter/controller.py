from tkinter import simpledialog, messagebox

from PIL._tkinter_finder import tk

from model import GameModel
from view import MainMenu, GameView


class GameController:
    def __init__(self, root):
        self.root = root
        self.model = None
        self.difficulty = None
        self.selected = {}
        self.main_menu = MainMenu(root, self.start_game_callback, self.show_stats_callback, self.quit_callback)
        self.time_started = False
    def start_game_callback(self):
        self.show_difficulty_selection()
        if self.difficulty:
            self.player_name = self.ask_player_name()
            messagebox.showinfo("Información", f"Dificultad: {self.difficulty}, Jugador: {self.player_name}")

    def show_difficulty_selection(self):
        """
        Muestra una ventana emergente para que el usuario seleccione la dificultad
        del juego usando RadioButtons con IntVar y luego ingrese su nombre.
        """
        # Crear una ventana Toplevel para la selección de dificultad
        difficulty_window = tk.Toplevel(self.root)
        difficulty_window.title("Seleccionar Dificultad")
        difficulty_window.geometry("300x200")
        difficulty_window.transient(self.root)
        difficulty_window.grab_set()

        # Variable IntVar para almacenar la selección de dificultad
        dificultad_var = tk.IntVar(value=4)  # Por defecto 4 (Fácil)

        # Etiqueta de instrucción
        tk.Label(difficulty_window, text="Elige la dificultad:").pack(pady=10)

        # Crear RadioButtons para seleccionar la dificultad
        tk.Radiobutton(
            difficulty_window,
            text="Fácil (4x4)",
            variable=dificultad_var,
            value=4
        ).pack(anchor=tk.W)

        tk.Radiobutton(
            difficulty_window,
            text="Medio (6x6)",
            variable=dificultad_var,
            value=6
        ).pack(anchor=tk.W)

        tk.Radiobutton(
            difficulty_window,
            text="Difícil (8x8)",
            variable=dificultad_var,
            value=8
        ).pack(anchor=tk.W)
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
        answer = tk.messagebox.askyesno("Salir", "¿Estás seguro de que quieres salir?")
        if answer:
            self.root.quit()
            """
    def on_card_click(self):
    def update_move_count(self):
    def update_time(self):
            """