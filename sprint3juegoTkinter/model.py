import json
import os
import time
import random
import datetime
from tkinter import messagebox

from resources import descargar_imagen
import threading
class GameModel:
    def __init__(self, difficulty, player_name, cell_size=100):
        self.start_time = None
        self.difficulty = difficulty
        self.board = self._generate_board() #Según se instancia la clase se genera el tablero y se guarda en un atributo
        self.hidden_image = None
        self.images = {}
        self.images_loaded = False
        self.player_name = player_name
        self.cell_size = cell_size
        self._load_images()
        self.pares = 0
        self.pairs_found = 0
        self.moves = 0
    def _generate_board(self):
        #dependiendo de la dificultad el tablero es más pequeño o más grande
        num_cartas = self.difficulty ** 2
        #generamos una lista con los pares
        self.pares = list(range(1, (num_cartas // 2) + 1)) * 2
        #y los desordenamos cada vez que se inicie el juego
        random.shuffle(self.pares)
        board = []
        for i in range(0, num_cartas, self.difficulty):
            row = self.pares[i:i + self.difficulty]
            board.append(row)
        return board
    def _load_images(self):
        """
        Carga las imágenes de las cartas y la imagen oculta en un hilo separado.
        La carga se realiza en segundo plano para no bloquear la interfaz.
        """
        def load_images_thread():
            url_base = "https://raw.githubusercontent.com/nicotino96/DI/refs/heads/main/imagenes_juego/"  # URL base de las imágenes
            try:
                # Carga la imagen oculta
                hidden_image_url = f"{url_base}hidden.png"
                self.hidden_image = descargar_imagen(hidden_image_url, self.cell_size)
                # Carga imágenes para cada identificador de carta en el tablero
                unique_ids = set(id for row in self.board for id in row)  # Identificadores únicos de cartas
                for image_id in unique_ids:
                    image_url = f"{url_base}imagen{image_id}.jpg"
                    self.images[image_id] = descargar_imagen(image_url, self.cell_size)
            except IOError as e:
                messagebox.showerror("Error", "No se ha cargado la imagen")
            self.images_loaded=True  # Marca que las imágenes se han cargado
        # Inicia un hilo para cargar las imágenes sin bloquear la interfaz
        self.images_loaded = threading.Event()
        threading.Thread(target=load_images_thread, daemon=True).start()

    def images_are_loaded(self):
        return self.images_loaded

    def start_timer(self):
        if self.start_time is None:
            self.start_time = time.time()

    def get_time(self):
        """
        Devuelve el tiempo transcurrido desde que se inició el temporizador.
        Si el temporizador no ha sido iniciado, devuelve 0.
        """
        if self.start_time is None:
            return 0
        return round(time.time() - self.start_time, 2)
    def check_match(self, pos1, pos2):
        """
        Verifica si dos posiciones en el tablero tienen cartas coincidentes.
        """
        self.moves += 1
        x1, y1 = pos1
        x2, y2 = pos2
        if self.board[x1][y1] == self.board[x2][y2]:
            self.pairs_found += 1
            return True
        return False
    def is_game_completed(self):
        if self.pairs_found == self.pares:
            self.save_score()  # Guarda la puntuación al completar el juego
            return True
        return False
    def save_score(self):
        """
        Guarda la puntuación del jugador en un archivo ranking.json.
        """
        score = {
            "player_name": self.player_name,
            "difficulty": self.difficulty,
            "moves": self.moves,
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        ranking_file = "ranking.json"

        # Verificar si el archivo JSON existe, si no, crearlo con un diccionario vacío
        if not os.path.exists(ranking_file):
            with open(ranking_file, 'w') as file:
                json.dump({"4": [], "6": [], "8": []}, file)

        # Cargar las puntuaciones existentes desde el archivo JSON
        try:
            with open(ranking_file, "r") as file:
                rankings = json.load(file)

            # Asegurarse de que la dificultad esté en el diccionario
            difficulty_key = str(self.difficulty)
            if difficulty_key not in rankings:
                rankings[difficulty_key] = []

            # Agregar la nueva puntuación
            rankings[difficulty_key].append(score)

            # Ordenar las puntuaciones por el menor número de movimientos
            rankings[difficulty_key].sort(key=lambda x: x["moves"])

            # Mantener solo las 3 mejores puntuaciones
            rankings[difficulty_key] = rankings[difficulty_key][:3]

            # Guardar el ranking actualizado en el archivo JSON
            with open(ranking_file, "w") as file:
                json.dump(rankings, file, indent=4)

        except (IOError, json.JSONDecodeError) as e:
            print(f"Error al guardar el ranking: {e}")

    def load_scores(self):
        """
        Carga y devuelve las puntuaciones desde el archivo ranking.json.
        Si el archivo no existe, devuelve un diccionario vacío con listas
        para cada nivel de dificultad.
        """
        ranking_file = "ranking.json"

        # Verificar si el archivo existe, si no, devolver un diccionario vacío
        if not os.path.exists(ranking_file):
            return {"4": [], "6": [], "8": []}

        try:
            # Abrir y leer el archivo JSON
            with open(ranking_file, "r") as file:
                rankings = json.load(file)

            # Validar el formato del archivo JSON, asegurándose de que tenga las claves esperadas
            if not all(str(d) in rankings for d in [4, 6, 8]):
                # Si el formato no es correcto, inicializar con diccionarios vacíos
                rankings = {"4": [], "6": [], "8": []}

            return rankings

        except (IOError, json.JSONDecodeError) as e:
            print(f"Error al cargar el ranking: {e}")
            # En caso de error, devolver un diccionario vacío para evitar fallos en el programa
            return {"4": [], "6": [], "8": []}

