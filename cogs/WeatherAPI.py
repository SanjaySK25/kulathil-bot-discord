import nextcord
from nextcord.ext import commands
from nextcord import Interaction
import requests

class WeatherAPI(commands.Cog):

    def __init__(self,client):
        self.client = client
    
    testServerId = 992451174110351420
    
    @nextcord.slash_command(name='weather', description='Get weather info based on a location name', guild_ids=[testServerId])
    async def weatherinfo(self, interaction: Interaction, location: str):
        url = f"https://open-weather13.p.rapidapi.com/city/{location}"
        headers = {
            "X-RapidAPI-Key": "791581e205msh7192be2564e1b2fp14aee9jsn8ac3d2d98788",
	        "X-RapidAPI-Host": "open-weather13.p.rapidapi.com"
        }

        response = requests.get(url=url, headers=headers).json()
        #embed = nextcord.Embed(title=f'Weather at {location}', description=response['weather'].main, color=0xff55)

        #for x in response.main:
            #embed.add_field(name=x, value=x)
        
        await interaction.response.send_message(response)
        print(response)

def setup(client):
    client.add_cog(WeatherAPI(client))