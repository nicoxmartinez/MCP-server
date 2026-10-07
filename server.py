import asyncio
from mcp.server.mcpserver import MCPServer

mcp = MCPServer("Servidor MCP de prueba")

@mcp.tool()
async def saludar(nombre: str) -> str:
    """Saluda a una persona por su nombre."""
    return f"¡Hola, {nombre}! Bienvenido a tu primer servidor MCP."

if __name__ == "__main__":
    # Inicia el servidor usando el transporte estándar
    mcp.run(transport="stdio")