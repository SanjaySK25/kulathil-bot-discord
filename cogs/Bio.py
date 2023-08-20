from nextcord import SlashOption
import nextcord
from nextcord.ext import commands
from nextcord import Interaction
import requests
import json
import os
from typing import Optional

class Bio(commands.Cog):

    def __init__(self,client):
        self.client = client
    
    testServerId = 992451174110351420

    @commands.Cog.listener()
    async def on_member_join(member, ctx):
        embed = nextcord.Embed(title='Welcome to the server!', description='Start by creating a bio for yourself using /add_bio', color=0x00ff55)
        member.send(embed=embed)
    
    @nextcord.slash_command(name='add_bio', description='Add a bio about yourself!', guild_ids=[testServerId])
    async def add_bio(self, interaction: Interaction, discord_user: nextcord.Member, real_name: str, age: int, birthday: str,description: str):
        new_data = {discord_user.id: [real_name, age, birthday, description]}
        path = f'json\{discord_user.id}.json'

        if os.path.exists(path=path):
            embed = nextcord.Embed(title='Error!', description=f"{discord_user.nick}'s bio already exists, use /update_bio to change it", color=0xff0000)
            await interaction.response.send_message(embed=embed)
        else:
            with open(path,'w') as data_file:
                json.dump(new_data, data_file, indent=4)
            
            embed = nextcord.Embed(title='Success!', description=f"{discord_user.nick}'s bio has been successfully created!", color=0x00ff55)
            await interaction.response.send_message(embed=embed)
    
    @nextcord.slash_command(name='show_bio', description="Check someone's bio", guild_ids=[testServerId])
    async def show_bio(self, interaction: Interaction, discord_user: nextcord.Member):
        if os.path.exists(path=f'json\{discord_user.id}.json'):    
            with open(f'json\{discord_user.id}.json','r') as data_file:
                data = json.load(data_file)
                discord_id = str(discord_user.id)
                
                embed = nextcord.Embed(title=discord_user.nick, color=0x00ff55)
                embed.set_image(url=discord_user.avatar.url)
                embed.add_field(name='Name:', value=data[discord_id][0], inline=False)
                embed.add_field(name='Age:', value=data[discord_id][1], inline=False)
                embed.add_field(name='Birthday:', value=data[discord_id][2], inline=False)
                embed.add_field(name='Description:', value=data[discord_id][3], inline=False)
                await interaction.response.send_message(embed=embed)
        else:
            embed = nextcord.Embed(title='Error!', description=f"{discord_user.nick} doesn't have a bio yet!", color=0xff0000)
            await interaction.response.send_message(embed=embed)
    
    @nextcord.slash_command(name='update_bio', description="Update your bio", guild_ids=[testServerId])
    async def update_bio(self, interaction: Interaction, discord_user: nextcord.Member, real_name: Optional[str] = SlashOption(required = False), age: Optional[int] = SlashOption(required = False), birthday: Optional[str] = SlashOption(required = False),description: Optional[str] = SlashOption(required = False)):
        if os.path.exists(path=f'json\{discord_user.id}.json'):
            data = None
            with open(f'json\{discord_user.id}.json','r') as data_file:
                data = json.load(data_file)

            with open(f'json\{discord_user.id}.json','w') as data_file:
                discord_id = str(discord_user.id)

                print(data)
                
                if real_name != None and real_name != '':
                    data[discord_id][0] = real_name
                if birthday != None and birthday != '':
                    data[discord_id][2] = birthday
                if description != None and description != '':
                    data[discord_id][3] = description
                if age != None and age > 5:
                    data[discord_id][1] = age
                
                new_data = {str(discord_user.id): [data[discord_id][0], data[discord_id][1], data[discord_id][2], data[discord_id][3]]}
                
                print(new_data)

                json.dump(new_data, data_file, indent=4)
                
                embed = nextcord.Embed(title=discord_user.nick, color=0x00ff55)
                embed.set_image(url=discord_user.avatar.url)
                embed.add_field(name='Name:', value=data[discord_id][0], inline=False)
                embed.add_field(name='Age:', value=data[discord_id][1], inline=False)
                embed.add_field(name='Birthday:', value=data[discord_id][2], inline=False)
                embed.add_field(name='Description:', value=data[discord_id][3], inline=False)
                await interaction.response.send_message(f"Successfully updated {discord_user.nick}'s bio!",embed=embed)
        else:
            embed = nextcord.Embed(title='Error!', description=f"{discord_user.nick} doesn't have a bio yet!", color=0xff0000)
            await interaction.response.send_message(embed=embed)

def setup(client):
    client.add_cog(Bio(client))