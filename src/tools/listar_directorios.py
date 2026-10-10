import os
from src.mcp_server import mcp
from src.config import obtener_ruta_segura

@mcp.tool()
async def listar_directorio(subruta: str = "") -> str:
    """Lista los archivos y carpetas dentro del directorio."""
    try:
        ruta_objetivo = obtener_ruta_segura(subruta)
        
        if not ruta_objetivo.exists():
            return f"Error: El directorio '{ruta_objetivo}' no existe."
            
        if not ruta_objetivo.is_dir():
            return f"Error: La ruta '{ruta_objetivo}' no es un directorio."

        elementos = os.listdir(ruta_objetivo)
        if not elementos:
            return f"El directorio '{subruta or '.'}' está vacío."

        # Separar en carpetas y archivos para mostrarlo claro
        carpetas = []
        archivos = []
        for elem in sorted(elementos):
            item_path = ruta_objetivo / elem
            if item_path.is_dir():
                carpetas.append(f"{elem}/")
            else:
                archivos.append(f"{elem}")

        resultado = [f"Contenido de: {ruta_objetivo}"]
        resultado.extend(carpetas)
        resultado.extend(archivos)

        return "\n".join(resultado)

    except ValueError as err:
        return str(err)
    except Exception as err:
        return f"Error inesperado al listar el directorio: {str(err)}"