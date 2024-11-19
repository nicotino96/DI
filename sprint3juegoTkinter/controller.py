from tkinter import simpledialog, messagebox
import tkinter as tk
from view import MainMenu, GameView
from model import GameModel


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
        self.game_view = GameView(
            self.root,
            on_card_click_callback=self.on_card_click,  # Método definido en tu controlador
            update_move_count_callback=self.update_move_count,  # Método para actualizar movimientos
            update_time_callback=self.update_time  # Método para actualizar tiempo
        )
        self.time_started = False

    def start_game_callback(self):
        self.difficulty = self.game_view.show_difficulty_selection()
        self.player_name = self.game_view.ask_player_name()
        messagebox.showinfo("Información", f"Dificultad: {self.difficulty}, Jugador: {self.player_name}")

        # Crear el modelo del juego
        self.model = GameModel(self.difficulty, self.player_name)

        # Mostrar la ventana de carga
        self.game_view.show_loading_window()

        # Comienza a verificar si las imágenes están cargadas
        self.check_images_loaded()

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

    def on_card_click(self, row, col):
        # Aquí manejas la lógica cuando se hace clic en una carta
        print(f"Carta clickeada en la posición: ({row}, {col})")

    def update_move_count(self, count):
        # Aquí manejas la actualización del contador de movimientos
        print(f"Movimientos realizados: {count}")

    def update_time(self, time):
        # Aquí manejas la actualización del tiempo transcurrido
        print(f"Tiempo transcurrido: {time}")

    def check_images_loaded(self):
        """Verifica periódicamente si las imágenes están cargadas antes de continuar."""
        if self.model.images_are_loaded().is_set():  # Verifica si el evento está activado
            print("Las imágenes se han cargado correctamente. Cerrando ventana de carga.")
            self.game_view.hide_loading_window()  # Cierra la ventana de carga
            self.initialize_game_view()  # Configura la interfaz del juego
        else:
            # Revisa nuevamente después de 100 ms
            self.root.after(100, self.check_images_loaded)

    def return_to_main_menu(self):
        # Mostrar la ventana principal nuevamente
        self.root.deiconify()  # Hace visible la ventana principal

        # Cerrar la ventana del juego (tablero)
        self.game_view.window.destroy()  # Cierra la ventana del juego

        # Reiniciar cualquier estado del juego si es necesario, o simplemente volver al menú principal
        self.game_view.window = None  # Limpiar la referencia a la ventana del juego

        # Si quieres reiniciar el modelo, puedes hacerlo aquí también:
        self.model = None  # Reinicia el modelo si es necesario, aunque podría no ser obligatorio

        # Mostrar nuevamente el menú principal (si lo ocultamos antes de iniciar el juego)
        self.main_menu.window.deiconify()  # Asegura que el menú principal sea visible

        # Aquí podrías resetear las variables o estados si lo necesitas, por ejemplo:
        self.difficulty = None  # O cualquier otra variable que quieras resetear
        self.player_name = None
        self.time_started = False

    def initialize_game_view(self):
        """Inicializa la vista del juego después de que las imágenes estén cargadas."""
        # Crea el tablero del juego
        self.game_view.create_board(self.model)
        # Actualiza cualquier otra parte de la interfaz si es necesario