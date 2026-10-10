import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(os.getenv("BASE_DIR")).resolve()

def obtener_ruta_segura(subruta: str = "") -> Path:
    # Combinar la ruta base con la subruta ingresada
    ruta_destino = (BASE_DIR / subruta.lstrip("/")).resolve()
    
    # Comprobar que la ruta final empiece con BASE_DIR
    if not str(ruta_destino).startswith(str(BASE_DIR)):
        raise ValueError(f"Acceso denegado: La ruta '{subruta}' está fuera de {BASE_DIR}")
        
    return ruta_destino