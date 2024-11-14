import threading
import time
import random
import datetime
from tkinter import messagebox

from resources import descargar_imagen
import threading
class GameModel:
    def __init__(self, difficulty, player_name, cell_size=100):
        self.board = self._generate_board() #Según se instancia la clase se genera el tablero y se guarda en un atributo
        self.images = {}
        self.hidden = None
        self.images_loaded = threading.Event()
        self.difficulty = difficulty
        self.player_name = player_name
        self.cell_size = cell_size
    def _generate_board(self):
        #dependiendo de la dificultad el tablero es más pequeño o más grande
        if self.difficulty == 4:
            num_cartas = 4 * 4
        elif self.difficulty == 6:
            num_cartas = 6 * 6
        else:
            num_cartas = 8 * 8
        #generamos una lista con los pares
        pares = list(range(1, (num_cartas // 2) + 1)) * 2
        #y los desordenamos cada vez que se inicie el juego
        random.shuffle(pares)
        board = []
        for i in range(0, num_cartas, self.difficulty):
            row = pares[i:i + self.difficulty]
            board.append(row)
        return board
    def _load_images(self):
        """
        Carga las imágenes de las cartas y la imagen oculta en un hilo separado.
        La carga se realiza en segundo plano para no bloquear la interfaz.
        """
        def load_images_thread():
            url_base = ""  # URL base de las imágenes
            try:
                # Carga la imagen oculta
                hidden_image_url = f"{url_base}hidden.png"
                self.hidden = descargar_imagen(hidden_image_url, self.cell_size)
                # Carga imágenes para cada identificador de carta en el tablero
                unique_ids = set(id for row in self.board for id in row)  # Identificadores únicos de cartas
                for image_id in unique_ids:
                    image_url = f"{url_base}{image_id}.png"
                    self.images[image_id] = descargar_imagen(image_url, self.cell_size)
            except IOError as e:
                messagebox.showerror("Error", "No se ha cargado la imagen")
            self.images_loaded.set()  # Marca que las imágenes se han cargado
        # Inicia un hilo para cargar las imágenes sin bloquear la interfaz
        threading.Thread(target=load_images_thread, daemon=True).start()