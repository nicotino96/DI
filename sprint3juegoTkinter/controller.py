from tkinter import simpledialog, messagebox
import tkinter as tk
from view import MainMenu, GameView
from model import GameModel


class GameController:
    def __init__(self, root):
        self.root = root
        self.click_blocked = False
        self.is_game_won = False
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

    def on_card_click(self, pos):
        """
        Maneja el evento de clic en una carta del tablero.
        - Inicia el temporizador si aún no ha comenzado.
        - Almacena la posición de la carta seleccionada.
        - Verifica coincidencias si se seleccionaron dos cartas.
        """
        # Verifica si el temporizador ya comenzó; si no, lo inicia.
        row, col = pos
        if not self.time_started:
            self.model.start_timer()
            self.time_started = True
            self.update_time()  # Método para actualizar el temporizador en la interfaz

        # Verifica si la carta ya ha sido seleccionada
        if (row, col) in self.selected:
            print(f"La carta en ({row}, {col}) ya está seleccionada.")
            return

        # Almacena la posición seleccionada
        self.selected[(row, col)] = self.model.board[row][col]
        card_value = self.selected[(row, col)]
        self.game_view.update_board(row, col, self.model.images[card_value])  # Muestra la imagen

        # Si hay dos cartas seleccionadas, verifica si coinciden
        if len(self.selected) == 2:
            self.root.after(500, self.handle_card_selection)  # Retrasa para mostrar las cartas seleccionadas

    def handle_card_selection(self):
        """
        Maneja la validación de las cartas seleccionadas.
        - Si coinciden, las mantiene visibles.
        - Si no coinciden, las oculta nuevamente.
        """
        # Obtiene las posiciones y valores de las dos cartas seleccionadas
        (pos1, card1), (pos2, card2) = list(self.selected.items())

        if self.model.check_match(pos1 , pos2):
            # Las cartas coinciden
            print(f"¡Pareja encontrada en {pos1} y {pos2}!")
            self.game_view.lock_card(pos1)  # Bloquea la carta en la vista
            self.game_view.lock_card(pos2)  # Bloquea la carta en la vista
        else:
            # Las cartas no coinciden
            print(f"No hay coincidencia: {pos1} ({card1}) y {pos2} ({card2})")
            self.game_view.hide_card(*pos1)  # Oculta la carta en la vista
            self.game_view.hide_card(*pos2)  # Oculta la carta en la vista

        # Limpia las cartas seleccionadas
        self.selected.clear()

        # Actualiza el contador de movimientos

        self.update_move_count(self.model.moves)

        # Verifica si el juego está completo
        if self.model.is_game_completed():
            self.handle_game_completion()

    def update_move_count(self, count):
        # Actualiza el contador de movimientos en la consola y en la interfaz gráfica
        print(f"Movimientos realizados: {count}")
        if self.game_view is not None:
            self.game_view.update_move_count(count)

    def update_time(self):
        if self.game_view is not None:
            self.game_view.update_time(self.model.get_time())

            if not self.is_game_won:
                self.root.after(1000, self.update_time)

    def revert_cards(self):
        # Revertir las cartas que no son una pareja
        self.game_view.labels[(self.cards_shown[0][0], self.cards_shown[0][1])].config(image=self.model.hidden_image)
        self.game_view.labels[(self.cards_shown[1][0], self.cards_shown[1][1])].config(image=self.model.hidden_image)
        # Limpiar la lista de cartas mostradas
        self.cards_shown.clear()

        # Desbloquear los clics para la siguiente selección
        self.click_blocked = False

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

    def handle_game_completion(self):
        time_taken = self.model.get_time()
        moves = self.model.moves
        messagebox.showinfo("¡Felicidades!", f"Juego completado en {time_taken} segundos y {moves} movimientos.")
        self.model.save_score()  # Guarda la puntuación
        self.return_to_main_menu()