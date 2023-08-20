import nextcord
import json
from nextcord.ext import commands
from nextcord import Interaction

class DataManager(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    testServerId = 992451174110351420

    @nextcord.slash_command(name='set_game_time',description='Set a time for gaming!', guild_ids=[testServerId])
    async def set_game_time(self, interaction: Interaction, time: str):
        with open('json\gameTime.json','w') as data_file:
            json.dump({'gameTime': time}, data_file, indent=4)
            await interaction.response.send_message(f'Game Time has been set to: {time}')
    
    @nextcord.slash_command(name='get_game_time',description='Get the time for gaming!', guild_ids=[testServerId])
    async def get_game_time(self, interaction: Interaction):
        with open('json\gameTime.json','r') as data_file:
            data = json.load(data_file)
            gameTime = str(data['gameTime'])
            await interaction.response.send_message(f'The current time announced for gaming is {gameTime}')
    
    @nextcord.slash_command(name='clear_game_time',description='Clear gaming time!', guild_ids=[testServerId])
    async def clear_game_time(self, interaction: Interaction):
        with open('json\gameTime.json','w') as data_file:
            json.dump({'gameTime': None}, data_file, indent=4)
            await interaction.response.send_message('Game Time has been cleared!')

def setup(client):
    client.add_cog(DataManager(client))