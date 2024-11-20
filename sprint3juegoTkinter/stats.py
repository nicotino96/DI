import os
import json

class StatsManager:
    @staticmethod
    def get_stats(file_path="ranking.json"):
        """
        Carga y organiza las estadísticas desde ranking.json.
        Devuelve un diccionario con las estadísticas por dificultad.
        """
        file_path = "ranking.json"
        if os.path.exists(file_path):
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    results = json.load(f)
                    # Aseguramos que las claves sean cadenas
                    results = {str(k): v for k, v in results.items()}
                    return results
            except json.JSONDecodeError:
                print("Error al leer el archivo JSON. El archivo puede estar corrupto.")
                return {"4": [], "6": [], "8": []}
        else:
            print("Archivo ranking.json no encontrado. Se creará uno nuevo.")
            return {"4": [], "6": [], "8": []}

    @staticmethod
    def save_score(file_path="ranking.json", difficulty=None, score=None):
        """
        Guarda una puntuación en el archivo ranking.json.
        """
        try:
            if not difficulty or not score:
                raise ValueError("La dificultad y la puntuación son obligatorias.")

            # Cargar datos existentes
            data = {}
            if os.path.exists(file_path):
                with open(file_path, "r", encoding="utf-8") as file:
                    data = json.load(file)

            # Asegurarse de que la dificultad existe en el archivo
            if difficulty not in data:
                data[difficulty] = []

            # Añadir la nueva puntuación
            data[difficulty].append(score)

            # Mantener solo las 3 mejores puntuaciones
            data[difficulty] = sorted(
                data[difficulty], key=lambda x: x["moves"]
            )[:3]

            # Guardar los datos actualizados
            with open(file_path, "w", encoding="utf-8") as file:
                json.dump(data, file, indent=4)

        except Exception as e:
            print(f"Error al guardar puntuación: {e}")