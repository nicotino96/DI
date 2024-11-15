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



    def ask_player_name(self):
        nombre = simpledialog.askstring("Nombre del Jugador", "Introduce tu nombre:", parent=self.window)
        return nombre

    def show_difficulty_selection(self):
        """
        Muestra una ventana emergente para que el usuario seleccione la dificultad
        del juego usando RadioButtons con IntVar y luego ingrese su nombre.
        """
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
            # una vez cerrada la venta nos quedamos con la dificultad seleccionada en ese momento
            difficulty_window.destroy()  # Cierra el diálogo
        tk.Button(difficulty_window, text="Elegir", command=choose_difficulty).pack(pady=5)  # Botón para confirmar la selección
        self.window.wait_window(difficulty_window)
        return difficulty_var.get()
class GameView:
    def __init__(self, on_card_click_callback, update_move_count_callback,
                 update_time_callback):
        self.window = None
        self.labels = {}
        self.on_card_click_callback = on_card_click_callback
        self.update_move_count_callback = update_time_callback
        self.update_time_callback = update_time_callback

    def create_board(self, root, model):
        """
        Crea una ventana Toplevel para el tablero de juego utilizando el tamaño y contenido del modelo.
        """
        # Crear la ventana Toplevel
        self.window = tk.Toplevel(root)
        self.window.title("Juego de Memoria - Tablero")
        self.window.geometry(f"{model.difficulty * model.cell_size}x{model.difficulty * model.cell_size}")
        self.window.resizable(False, False)
        # Crear el tablero visualmente
        board = model._generate_board()  # Generar el tablero usando el modelo
        self.labels = {}  # Diccionario para almacenar los labels de cada carta
        for row in range(model.difficulty):
            for col in range(model.difficulty):
                # Crear el label de la carta en el tablero
                label = tk.Label(self.window, text="❓", width=10, height=5, bg="lightblue",
                              font=("Arial", 14, "bold"))
                # Asociar un callback al hacer clic en una carta
                label.bind("<Button-1>", lambda event, r=row, c=col: self.on_card_click_callback(r, c))

                # Posicionar la carta en la ventana Toplevel
                label.grid(row=row, column=col, padx=5, pady=5)

                # Almacenar el label en el diccionario
                self.labels[(row, col)] = label
