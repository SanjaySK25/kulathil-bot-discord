import nextcord
from nextcord.ext import commands
from nextcord import Interaction

rules = ['Users must obey the nextcord community guidelines.',
         'No racism/homophobia/bullying/etc of any kind Bullying of any kind will end in a mute and possibly a ban.',
         'Everyone Can Report', 'No Server Raiding', 'No Chatting In welcome channel',
         'No robbing and bankrob is illegal', 'No impersonating']

class Greetings(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    testServerId = 992451174110351420
    
    @commands.Cog.listener()
    async def on_member_join(member):
        await member.send("Hi there, welcome to the server.")
        await member.send("These are the rules:")
        for x in range(len(rules)):
            await member.send('RULE ' + str(x+1) + ': ' + rules[x])

    @nextcord.slash_command(name='hi', description='Say hi!', guild_ids=[testServerId])
    async def hi(self,interaction: Interaction):
        await interaction.response.send_message("hi!")


def setup(client):
    client.add_cog(Greetings(client))