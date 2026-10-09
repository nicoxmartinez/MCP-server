from src.mcp_server import mcp

@mcp.tool()
async def saludar(nombre: str) -> str:
    """Saluda a una persona por su nombre."""
    return f"¡Hola, {nombre}! Bienvenido a tu primer servidor MCP."