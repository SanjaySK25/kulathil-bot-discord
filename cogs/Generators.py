import nextcord
from nextcord.ext import commands
from nextcord import Interaction
import requests
import json
import random

class Generators(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    testServerId = 992451174110351420
    
    @nextcord.slash_command(name='generate-img', description='Get a random image!', guild_ids=[testServerId])
    async def randomImg(self, interaction:Interaction, arg: str):
        embed = nextcord.Embed(title='Random Image of "' + arg + '"', url='https://source.unsplash.com/1600x900/?{}'.format(arg), description='Generated a random image of "' + arg + '"', color=0x00ff55)
        embed.set_author(name=interaction.user.display_name, icon_url=interaction.user.display_avatar)
        embed.set_image(url='https://source.unsplash.com/1600x900/?{}'.format(arg))
        await interaction.response.send_message(embed=embed)
    
    @nextcord.slash_command(name='generate-img-superhero', description='Get a random image of a hero!', guild_ids=[testServerId])
    async def random_superhero(self, interaction:Interaction):
        request_url = 'https://superheroapi.com/api/293343996575989/' + str(random.randint(1,631))
        response = requests.get(request_url).json()

        url = str(response['image']['url'])

        embed = nextcord.Embed(title=response['name'], url=url, description='Generated a random superhero!', color=0x00ff55)
        embed.set_author(name=interaction.user.display_name, icon_url=interaction.user.display_avatar)
        embed.set_image(url=url)
        await interaction.response.send_message(embed=embed)
    
    @nextcord.slash_command(name='generate_meme', description='Get a random meme!(200 per day)', guild_ids=[testServerId])
    async def generate_meme(self, interaction: Interaction):
        url = "https://meme-generator11.p.rapidapi.com/meme"

        headers = {
            "X-RapidAPI-Key": "791581e205msh7192be2564e1b2fp14aee9jsn8ac3d2d98788",
            "X-RapidAPI-Host": "meme-generator11.p.rapidapi.com"
        }

        response = requests.get(url, headers=headers).json()

        embed = nextcord.Embed(title=response['title'], color=0x00ff55)
        embed.set_image(url=response['url'])
        embed.set_footer(text=f'Requested by {interaction.user}', icon_url=interaction.user.display_avatar.url)

        await interaction.response.send_message(embed=embed)

        
    

def setup(client):
    client.add_cog(Generators(client))