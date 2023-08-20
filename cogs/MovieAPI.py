import nextcord
from nextcord.ext import commands
from nextcord import Interaction
import requests

class MovieAPI(commands.Cog):

    def __init__(self,client):
        self.client = client
    
    testServerId = 992451174110351420
    
    # @nextcord.slash_command(name='search_movie', description='Search for a movie', guild_ids=[testServerId])
    # async def movieinfo(self, interaction: Interaction, movie_name: str):
    #     url = f'https://moviesdatabase.p.rapidapi.com/titles/search/keyword/{movie_name.lower()}'

    #     headers = {
    #         "X-RapidAPI-Key": "791581e205msh7192be2564e1b2fp14aee9jsn8ac3d2d98788",
    #         "X-RapidAPI-Host": "moviesdatabase.p.rapidapi.com"
    #     }

    #     response = requests.get(url, headers=headers)
    #     json_response = response.json()

    #     embed = nextcord.Embed(title=json_response['results'][0]['titleText']['text'], color=0x00ff55)
    #     embed.set_image(url=json_response['results'][0]['primaryImage']['url'])

    #     await interaction.response.send_message(embed=embed)

def setup(client):
    client.add_cog(MovieAPI(client))