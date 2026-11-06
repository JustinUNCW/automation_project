from mcp.server.mcpserver import MCPServer
import requests
from pprint import pprint as pp

mcp = MCPServer("Genesys Cloud MCP")


class genesys_request_client:

    def __init__(self):
        self.url = "https://api.usw2.pure.cloud"

        req = requests.post(
                url="https://login.usw2.pure.cloud/oauth/token",
                headers={"content-type": "application/x-www-form-urlencoded"}, 
                params={"grant_type": "client_credentials"},
                auth=("eccc5a30-82f8-4a7e-9e15-3cb62902ae3a", "G88C__7oRKOtTcwxCWhhy0sanBmG_rKxV0gRLurvDGuWFRlMU9nJM6IZpBbo")
            ).json()

        self.headers = {
            "Authorization": f"bearer {req["access_token"]}", 
            "content_type": "application/json"
            }



req = genesys_request_client()

@mcp.tool()
def get_queues():
    '''Function to get all queue names from an org'''

    queue_names = ""

    r = requests.get(
        url=f"{req.url}/api/v2/routing/queues",
        headers=req.headers
    ).json()

    for queue_name in r["entities"]:
        queue_names += f"{queue_name["name"]}: {queue_name["id"]}\n"

    return queue_names


if __name__ == "main":
    get_queues()
