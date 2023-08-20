import nextcord
from nextcord.ext import commands
from nextcord import Interaction
import requests
import os
import json

class Levels(commands.Cog):

    def __init__(self,client):
        self.client = client
    
    testServerId = 992451174110351420

    @commands.Cog.listener()
    async def on_message(self, message):

        if message.author == self.client.user or message.author.bot:
            return
        
        print(message.author.id)
        if os.path.exists(path=f'level_up_json\{message.author.id}.json'):
            new_data = None
            data = None
            exp = None
            level = None
            with open(f'level_up_json\{message.author.id}.json','r') as data_file:
                data = json.load(data_file)
                exp = data['exp'][0]
                exp += 1
                level = data['exp'][1]

                if exp >= data['exp'][1] * 150:
                    level += 1
            with open(f'level_up_json\{message.author.id}.json','w') as data_file:
                new_data = {'exp': [exp, level]}
                json.dump(new_data, data_file, indent=4)
            
                print(level)
        else:
            with open(f'level_up_json\{message.author.id}.json','w') as data_file:
                json.dump({'exp': [1, 0]}, data_file, indent=4)

def setup(client):
    client.add_cog(Levels(client))