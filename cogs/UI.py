import nextcord
from nextcord.ext import commands
from nextcord import Interaction

class Subscriptions(nextcord.ui.View):

    def __init__(self):
        super().__init__()
        self.value = None
    
    @nextcord.ui.button(label='Subscribe', style=nextcord.ButtonStyle.blurple)
    async def subscribe(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("Yeah my button works")
        self.value = True
        self.stop()
    
    @nextcord.ui.button(label='You should subscribe', style=nextcord.ButtonStyle.red)
    async def should_subscribe(self, button: nextcord.ui.Button, interaction: Interaction):
        await interaction.response.send_message("Yeah this works as well")
        self.value = False
        self.stop()

class Dropdown(nextcord.ui.Select):

    def __init__(self):
        select_options = [nextcord.SelectOption(label="Option 1", description="Just to see"),
                          nextcord.SelectOption(label="Option 2", description="Just to see"),
                          nextcord.SelectOption(label="Option 3", description="Just to see")]
        super().__init__(placeholder='Some options', min_values=1, max_values=2, options=select_options)


    async def callback(self, interaction: Interaction):

        if self.values[0] == 'Option 1':
            await interaction.response.send_message("You selected option 1!")
        elif self.values[0] == 'Option 2':
            await interaction.response.send_message("You selected Option 2!")
        else:
            await interaction.response.send_message("You selected Option 3!")

class DropdownView(nextcord.ui.View):

    def __init__(self):
        super().__init__()
        self.add_item(Dropdown())

class UI(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    testServerId = 992451174110351420

    @nextcord.slash_command(name='button', description='This is the command to test buttons', guild_ids=[testServerId])
    async def sub(self, interaction: Interaction):
        view = Subscriptions()
        await interaction.response.send_message("You have two options:" , view=view)
        await view.wait()

        if view.value is None:
            return
        elif view.value:
            print("Yay subscribed(You really didn't) :)!")
        else:
            print("Yeah u still want to sub!")
    
    @nextcord.slash_command(name='dropdown', description='Dropdown Test', guild_ids=[testServerId])
    async def drop(self, interaction: Interaction):
        view = DropdownView()
        await interaction.response.send_message("Let's test this out: ", view=view)

def setup(client):
    client.add_cog(UI(client))