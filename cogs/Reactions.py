import nextcord
from nextcord.ext import commands

class Reactions(commands.Cog):
    
    def __init__(self, client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        channel = reaction.message.channel
        await channel.send(user.name + " added: " + str(reaction.emoji))
    
    @commands.Cog.listener()
    async def on_reaction_remove(self, reaction, user):
        channel = reaction.message.channel
        await channel.send(user.name + " removed: " + str(reaction.emoji))

    @commands.Cog.listener()
    async def on_message(self, message):
        
        if message.author == self.client.user:
            return

        if 'happy' in message.content:
            emoji = '😄'
            await message.add_reaction(emoji)

def setup(client):
    client.add_cog(Reactions(client))