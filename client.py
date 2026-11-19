from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent
from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv
import asyncio
load_dotenv()
async def main():
    client=MultiServerMCPClient(
        {
            "math":{
                "command":"python",
                "args":["mathserver.py"],
                "transport":"stdio"
            },
            
            "weather":{
                "url":"http://localhost:8000/mcp",
                "transport":"streamable_http",
            }
        }
    )

    tools=await client.get_tools()
    model=ChatGroq(model="qwen/qwen3.8-27b")
    agent=create_react_agent(model,tools)

    math_response=await agent.ainvoke(
        {
            "messages":[{"role":"user","content":"whats's (3+5)*12"}]
        }
    )
    print("Math repsonse:",math_response['messages'][-1].content)

asyncio.run(main())

