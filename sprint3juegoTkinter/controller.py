from tkinter import simpledialog, messagebox
import tkinter as tk
from view import MainMenu, GameView


class GameController:
    def __init__(self, root):
        self.root = root
        self.model = None
        self.player_name=None
        self.difficulty = None
        self.selected = {}
        self.main_menu = MainMenu(
            root,
            self.start_game_callback,
            self.show_stats_callback,
            self.quit_callback
        )
        self.time_started = False
    def start_game_callback(self):
        self.difficulty=self.main_menu.show_difficulty_selection()
        if self.difficulty is not None:
            self.player_name = self.main_menu.ask_player_name()
            messagebox.showinfo("Información", f"Dificultad: {self.difficulty}, Jugador: {self.player_name}")

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