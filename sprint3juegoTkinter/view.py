import tkinter as tk

class MainMenu:
    def __init__(self, root, start_game_callback, show_stats_callback, quit_callback):
        self.window = root
        self.window.title("Juego memoria")#Título principal
        (tk.Button(self.window, text="Jugar", command=start_game_callback).pack(pady=10))#botones
        (tk.Button(self.window, text="Estadísticas", command=show_stats_callback).pack(pady=10))
        (tk.Button(self.window, text="Salir", command=quit_callback).pack(pady=10))

class GameView:
    def __init__(self, on_card_click_callback, update_move_count_callback,
                 update_time_callback):
        self.root = None
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
