import nextcord
from nextcord.ext import commands
from nextcord import Interaction
import random
import randfacts

class Poll(nextcord.ui.View):

    def __init__(self, author):
        super().__init__()
        self.positive = 0
        self.negative = 0
        self.should_stop = False
        self.submitted_users = []
        self.author = author
    
    @nextcord.ui.button(label='Option 1', style=nextcord.ButtonStyle.blurple)
    async def option_one(self, button: nextcord.ui.Button, interaction: Interaction):
        if interaction.user in self.submitted_users:
            await interaction.response.send_message(str(interaction.user.display_name) + ' already voted!')
            return
        if self.should_stop: self.stop()
        self.positive += 1
        await interaction.send("Thank you for choosing!")
        self.submitted_users.append(interaction.user)
    
    @nextcord.ui.button(label='Option 2', style=nextcord.ButtonStyle.red)
    async def option_two(self, button: nextcord.ui.Button, interaction: Interaction):
        if interaction.user in self.submitted_users:
            await interaction.response.send_message(str(interaction.user.display_name) + ' already voted!')
            return
        if self.should_stop: self.stop()
        self.negative += 1
        await interaction.send("Thank you for choosing!")
        self.submitted_users.append(interaction.user)
    
    @nextcord.ui.button(label='Show Results', style=nextcord.ButtonStyle.success)
    async def results(self, button: nextcord.ui.Button, interaction: Interaction):

        if interaction.user != self.author:
            await interaction.response.send_message('This button can only be used by the author of the poll!')
            return

        embed = nextcord.Embed(title="Poll Results", color=0x00ff55, description='The results of the poll')
        embed.set_author(name=interaction.user.display_name, icon_url=interaction.user.avatar)
        embed.add_field(name='Option 1 Votes:', value= str(self.positive))
        embed.add_field(name='Option 2 Votes:', value= str(self.negative))
        if self.positive == self.negative:
            embed.add_field(name='The poll ended in a', value='DRAW!')
        if self.positive > self.negative:
            embed.add_field(name='More votes for ', value='Option 1!')
        if self.positive < self.negative:
            embed.add_field(name='More votes for ', value='Option 2!', inline=False)
        await interaction.send(embed=embed)
        self.should_stop=True
        self.stop()

class Features(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    testServerId = 992451174110351420

    @nextcord.slash_command(name='roll_dice', description='Get a random value out of 1 to 6 including both endpoints', guild_ids=[testServerId])
    async def roll_dice(self, interaction: Interaction):
        embed = nextcord.Embed(title='Dice rolled', color=0xffffff, description=str(random.randint(1,6)))
        embed.set_author(name=interaction.user.display_name, icon_url=interaction.user.avatar)
        await interaction.response.send_message(embed=embed)
    
    @nextcord.slash_command(name='flip_coin', description='Flip a coin', guild_ids=[testServerId])
    async def flip_coin(self, interaction: Interaction):
        possible_outputs = ['Heads','Tails']
        embed = nextcord.Embed(title='Coin flipped', color=0xffffff, description=possible_outputs[random.randint(0,1)])
        embed.set_author(name=interaction.user.display_name, icon_url=interaction.user.avatar)
        await interaction.response.send_message(embed=embed)

    @commands.command()
    async def spam(self, ctx, spam_text:str, number:int):
        for x in range(int(number)):
            await ctx.send(str(spam_text))
        
    @nextcord.slash_command(name='fact', description='Gives a random fact', guild_ids=[testServerId])
    async def fact(self, interaction: Interaction):
        embed = nextcord.Embed(title='Random Fact', color=0x00ff55, description = randfacts.get_fact(filter_enabled=True))
        embed.set_author(name=interaction.user.display_name, icon_url=interaction.user.avatar)
        await interaction.response.send_message(embed=embed)
    
    @nextcord.slash_command(name='calculate', description='Calculate a given expression', guild_ids=[testServerId])
    async def calculate(self, interaction: Interaction, expression: str):
        embed = nextcord.Embed(title=f'Calculated {expression}', color=0x00ff55, description='Answer' + str(eval(expression)))
        embed.set_author(name=interaction.user.display_name, icon_url=interaction.user.avatar)
        await interaction.response.send_message(embed=embed)

    @nextcord.slash_command(name='message', description='Message someone to come to Annachi Squad', guild_ids=[testServerId])
    async def message(self, ctx, user:nextcord.Member, *, message=None):
        message='Come to Annachi Squad!'
        embed = nextcord.Embed(title=message, color=0xffffff, description='Someone from Annachi Squad wants you to come there')
        await user.send(embed=embed)
    
    @commands.command()
    async def embed(self, ctx, arg):
        embed = nextcord.Embed(title="This is a test embed!", url="https://google.com", description="Lets see if this works!", color=0xfff)
        embed.set_author(name=ctx.author.display_name, url="https://sanjaysk.itch.io", icon_url=ctx.author.avatar)
        embed.set_thumbnail(url=arg)
        embed.add_field(name="First Field", value="This is a test field", inline=True)
        embed.add_field(name="Second Field", value="This is a test field", inline=True)
        embed.set_footer(text="Information requested by: " + ctx.author.display_name)
        await ctx.send(embed=embed)
    
    @nextcord.slash_command(name='poll', description='Conduct a poll', guild_ids=[testServerId])
    async def poll(self, interaction: Interaction, title: str, description: str, option1: str, option2: str):
        embed = nextcord.Embed(title=title, color=0x00ff55, description=description)
        embed.set_author(name=interaction.user.display_name, icon_url=interaction.user.avatar)
        embed.add_field(name='Option 1', value=str(option1))
        embed.add_field(name='Option 2', value=str(option2))
        view = Poll(author=interaction.user)
        await interaction.response.send_message(embed=embed,view=view)
        await view.wait()

def setup(client):
    client.add_cog(Features(client))