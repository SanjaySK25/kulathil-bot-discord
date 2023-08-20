import nextcord
from nextcord.ext import commands
from nextcord import Interaction

class TTT(nextcord.ui.View):

    def __init__(self, values):
        super().__init__()
        self.values = values

    @nextcord.ui.button(label='None', style=nextcord.ButtonStyle.blurple)
    async def option_one(self, button: nextcord.ui.Button, interaction: Interaction):
        self.values[0] = interaction.user
    
    @nextcord.ui.button(label='None1', style=nextcord.ButtonStyle.blurple)
    async def option_two(self, button: nextcord.ui.Button, interaction: Interaction):
        self.values[1] = interaction.user

    @nextcord.ui.button(label='None2', style=nextcord.ButtonStyle.blurple)
    async def option_three(self, button: nextcord.ui.Button, interaction: Interaction):
        self.values[2] = interaction.user

    @nextcord.ui.button(label='None3', style=nextcord.ButtonStyle.blurple)
    async def option_four(self, button: nextcord.ui.Button, interaction: Interaction):
        self.values[3] = interaction.user

    @nextcord.ui.button(label='None4', style=nextcord.ButtonStyle.blurple)
    async def option_five(self, button: nextcord.ui.Button, interaction: Interaction):
        self.values[4] = interaction.user

    @nextcord.ui.button(label='None5', style=nextcord.ButtonStyle.blurple)
    async def option_six(self, button: nextcord.ui.Button, interaction: Interaction):
        self.values[5] = interaction.user
    
    @nextcord.ui.button(label='None6', style=nextcord.ButtonStyle.blurple)
    async def option_seven(self, button: nextcord.ui.Button, interaction: Interaction):
        self.values[6] = interaction.user
    
    @nextcord.ui.button(label='None7', style=nextcord.ButtonStyle.blurple)
    async def option_one(self, button: nextcord.ui.Button, interaction: Interaction):
        self.values[7] = interaction.user
    
    @nextcord.ui.button(label='None8', style=nextcord.ButtonStyle.blurple)
    async def option_eight(self, button: nextcord.ui.Button, interaction: Interaction):
        self.values[8] = interaction.user


class TicTacToe(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    testServerId = 992451174110351420
    
    @nextcord.slash_command(name='tic-tac-toe', description='Play a round of tic-tac-toe with me', guild_ids=[testServerId])
    async def startTTT(self, interaction: Interaction):
        embed = nextcord.Embed(title='Tic-Tac-Toe', description='Play a game of tic-tac-toe',color=0xff55)
        view = TTT(values=[0,0,0,
                           0,0,0,
                           0,0,0])
        await interaction.response.send_message(embed=embed,view=view)
        await view.wait()

def setup(client):
    client.add_cog(TicTacToe(client))