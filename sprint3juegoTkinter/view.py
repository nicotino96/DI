import tkinter as tk

class GameView:
    def __init__(self, on_card_click_callback, update_move_count_callback,
                 update_time_callback):
        self.window = None
        self.labels = {}
        self.on_card_click_callback = on_card_click_callback
        self.update_move_count_callback = update_time_callback
        self.update_time_callback = update_time_callback
    def create_board(self, model):

class MainMenu:
    def __init__(self, root, start_game_callback, show_stats_callback, quit_callback):
        self.window = root
        self.window.title("Juego memoria")
        (tk.Button(self.window, text="Jugar", command=start_game_callback).pack(pady=10))
        (tk.Button(self.window, text="Estadísticas", command=show_stats_callback).pack(pady=10))
        (tk.Button(self.window, text="Salir", command=quit_callback).pack(pady=10))
