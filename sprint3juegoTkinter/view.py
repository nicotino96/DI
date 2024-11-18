import tkinter as tk
from tkinter import simpledialog


class MainMenu:
    def __init__(self, root, start_game_callback, show_stats_callback, quit_callback):
        self.window = root
        self.window.title("Menú Principal - Juego de Memoria")
        self.window.geometry("300x200")
        self.window.resizable(False, False)

        # Botón "Jugar"
        btn_play = tk.Button(self.window, text="Jugar", command=start_game_callback, font=("Arial", 12))
        btn_play.pack(pady=10)

        # Botón "Estadísticas"
        btn_stats = tk.Button(self.window, text="Estadísticas", command=show_stats_callback, font=("Arial", 12))
        btn_stats.pack(pady=10)

        # Botón "Salir"
        btn_quit = tk.Button(self.window, text="Salir", command=quit_callback, font=("Arial", 12))
        btn_quit.pack(pady=10)

class GameView:
    def __init__(self, root, on_card_click_callback, update_move_count_callback, update_time_callback):
        self.root = root
        self.window = None
        self.labels = {}
        self.moves_label = None
        self.times_label = None
        self.on_card_click_callback = on_card_click_callback
        self.update_move_count_callback = update_move_count_callback
        self.update_time_callback = update_time_callback
        self.loading_window = None


    def ask_player_name(self):
        nombre = simpledialog.askstring("Nombre del Jugador", "Introduce tu nombre:")
        return nombre

    def show_difficulty_selection(self):
        # Crear una ventana Toplevel para la selección de dificultad
        difficulty_window = tk.Toplevel(self.window)
        difficulty_window.title("Seleccionar Dificultad")
        difficulty_window.geometry("300x200")
        difficulty_window.transient(self.window)
        difficulty_window.grab_set()

        # Variable IntVar para almacenar la selección de dificultad
        difficulty_var = tk.IntVar(value=4)  # Por defecto 4 (Fácil)

        # Etiqueta de instrucción
        tk.Label(difficulty_window, text="Elige la dificultad:").pack(pady=10)

        # Crear RadioButtons para seleccionar la dificultad
        tk.Radiobutton(
            difficulty_window,
            text="Fácil (4x4)",
            variable=difficulty_var,
            value=4
        ).pack(anchor=tk.W)

        tk.Radiobutton(
            difficulty_window,
            text="Medio (6x6)",
            variable=difficulty_var,
            value=6
        ).pack(anchor=tk.W)

        tk.Radiobutton(
            difficulty_window,
            text="Difícil (8x8)",
            variable=difficulty_var,
            value=8
        ).pack(anchor=tk.W)

        def choose_difficulty():
            # Cerrar el diálogo y retornar la dificultad seleccionada
            difficulty_window.destroy()

        # Botón para confirmar la selección de dificultad
        tk.Button(difficulty_window, text="Elegir", command=choose_difficulty).pack(pady=5)

        # Esperar hasta que la ventana se cierre y luego obtener el valor seleccionado
        self.root.wait_window(difficulty_window)
        return difficulty_var.get()

    def create_board(self, model):
        """
        Crea una ventana Toplevel para el tablero de juego utilizando el tamaño y contenido del modelo.
        """
        # Crear la ventana Toplevel
        self.window = tk.Toplevel(self.root)
        self.window.title("Juego de Memoria - Tablero")
        self.window.geometry(f"{model.difficulty * model.cell_size}x{model.difficulty * model.cell_size}")
        self.window.resizable(False, False)
        # Crear el tablero visualmente
        self.labels = {}  # Diccionario para almacenar los labels de cada carta
        k = 0
        j = 0
        for row in model.board:
            j = 0
            for i in row:
                label = tk.Label(self.window, text="", image=model.hidden_image)
                label.bind("<Button-1>", lambda event, pos=(j, k): self.on_card_click_callback(pos),
                           self.update_move_count_callback)
                label.grid(row=k, column=j)
                self.labels[(j, k)] = label
                j += 1
            k += 1
        self.moves_label = tk.Label(self.window, text=f"Movimientos: 0")
        self.moves_label.grid(row=k, column=(j // 2))
        self.times_label = tk.Label(self.window, text=f"Tiempo: 0")
        self.times_label.grid(row=k, column=(j // 2) + 1)

    def show_loading_window(self):
        self.loading_window = tk.Toplevel(self.root)
        self.loading_window.title("Cargando Imágenes...")
        loading_label = tk.Label(self.loading_window, text="Descargando imágenes, por favor espera...")
        loading_label.pack(padx=20, pady=20)
        self.root.update()

    def hide_loading_window(self):
        """Cierra la ventana de carga."""
        if self.loading_window is not None:
            self.loading_window.destroy()
            self.loading_window = None
