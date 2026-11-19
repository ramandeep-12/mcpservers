from mcp.server.fastmcp import FastMCP
mcp=FastMCP()

@mcp.tool()
async def get_weather(location:str)->str:
    """
    Get tje weather location
    """

    return "It's always raining in toronto"

if __name__=="__main__":
    mcp.run(transport="streamable-http") 
