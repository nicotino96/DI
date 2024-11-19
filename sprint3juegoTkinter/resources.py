from PIL import Image, ImageTk
import requests
from io import BytesIO

def descargar_imagen(url, size):
    try:
        # Realizar la solicitud HTTP
        response = requests.get(url)
        response.raise_for_status()  # Verificar si hubo error en la solicitud
        print("Solicitud exitosa")
        # Abrir la imagen desde el contenido de la respuesta
        imagen = Image.open(BytesIO(response.content))
        # Redimensionar la imagen
        imagen_redimensionada = imagen.resize((size, size), Image.Resampling.LANCZOS)
        # Convertir la imagen a formato tkinter
        imagen_tk = ImageTk.PhotoImage(imagen_redimensionada)
        return imagen_tk
    except requests.exceptions.HTTPError as http_err:
        print(f"Error HTTP: {http_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"Error de solicitud: {req_err}")
    return None
