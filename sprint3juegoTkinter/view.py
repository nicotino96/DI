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
        self.hidden_image = None
        self.move_counter = None
        self.root = root
        self.window = None
        self.timer = None
        self.move_counter = None
        self.labels = {}
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
        self.hidden_image = model.hidden_image
        self.window = tk.Toplevel(self.root)
        self.window.title("Juego de Memoria - Tablero")
        self.window.resizable(False, False)

        # Configurar un marco principal para organizar los widgets
        main_frame = tk.Frame(self.window)
        main_frame.grid(row=0, column=0)

        # Crear un marco para el tablero
        board_frame = tk.Frame(main_frame)
        board_frame.grid(row=1, column=0)

        # Crear el tablero visualmente
        self.labels = {}  # Diccionario para almacenar los labels de cada carta
        for row_index, row in enumerate(model.board):
            for col_index, _ in enumerate(row):
                label = tk.Label(board_frame, image=model.hidden_image)
                label.bind("<Button-1>", lambda event, pos=(row_index, col_index): self.on_card_click_callback(pos))
                label.grid(row=row_index, column=col_index)
                self.labels[(row_index, col_index)] = label

        # Crear un marco para los contadores (movimientos y temporizador)
        status_frame = tk.Frame(main_frame)
        status_frame.grid(row=0, column=0, pady=(10, 5))

        self.move_counter = tk.Label(
            status_frame,
            text="Movimientos: 0",
            font=("Arial", 14),
            bg="#4CAF50",
            fg="white",
            relief="raised",
            width=15,
        )
        self.move_counter.grid(row=0, column=0, padx=(10, 5))

        self.timer = tk.Label(
            status_frame,
            text="00:00",
            font=("Arial", 14),
            bg="#2196F3",
            fg="white",
            relief="raised",
            width=15,
        )
        self.timer.grid(row=0, column=1, padx=(5, 10))

        # Configurar la ventana para ajustar su tamaño
        board_size = model.difficulty * model.cell_size
        self.window.geometry(f"{board_size}x{board_size + 50}")

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

    def update_time(self, time):
        """
        Actualiza el temporizador en la interfaz para reflejar el tiempo transcurrido.

        :param time: El tiempo transcurrido que se mostrará en el temporizador.
        """
        self.timer.config(text=time)
    def update_move_count(self, moves):
        self.move_counter.config(text=f"Movimientos: {moves}")
    def reset_cards(self, pos1, pos2):
        """
        Restaura las imágenes de dos cartas a su estado oculto, útil cuando el jugador no encuentra
        una coincidencia entre dos cartas seleccionadas.

        :param pos1: La posición de la primera carta a restaurar.
        :param pos2: La posición de la segunda carta a restaurar.
        """
        self.labels.get(pos1).config(image=self.hidden_image)
        self.labels.get(pos2).config(image=self.hidden_image)
    def reveal_card(self, row, col, param):
        pass

    def update_board(self, row, col, image):
        """
        Actualiza la celda en la posición (row, col) con la imagen proporcionada.
        Si la celda aún no existe, la crea.
        """
        # Crea un identificador único para la celda basada en su fila y columna
        cell_id = (row, col)

        # Si la celda no existe aún, la creamos
        if cell_id not in self.labels:
            # Crea una etiqueta de tkinter para mostrar la imagen en esta celda
            label = tk.Label(self.root, image=image)
            label.grid(row=row, column=col)  # Ubica la etiqueta en el grid
            label.bind("<Button-1>", lambda event, r=row, c=col: self.on_card_click_callback(r, c))  # Vincula el clic
            self.labels[cell_id] = label  # Guarda la referencia a la etiqueta

        # Si la celda ya existe, solo actualizamos la imagen
        else:
            self.labels[cell_id].config(image=image)

    def lock_card(self, position):
        """
        Bloquea la carta en una posición específica, manteniéndola visible permanentemente.
        """
        label = self.labels.get(position)
        if label:
            label.unbind("<Button-1>")  # Desvincula el evento de clic para que no sea interactiva.

    def hide_card(self, row, col):
        """
        Oculta la carta en la posición especificada, mostrando nuevamente la imagen oculta.
        """
        label = self.labels.get((row, col))
        if label:
            label.config(image=self.hidden_image)  # Cambia la imagen de la carta a la oculta.