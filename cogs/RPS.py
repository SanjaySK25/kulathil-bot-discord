import nextcord
from nextcord.ext import commands
from nextcord import Interaction
import random

class RPS(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.playingRPS = False
        self.rps_round_length = 3
        self.rps_opponent = None
        self.rps_player_points = 0
        self.rps_bot_points = 0
        self.did_player_score = False
        self.did_bot_score = False
        self.rock_paper_scissor_options = ['rock', 'paper', 'scissors']
        self.bot_choice = ''
        self.user_choice = ''
    
    testServerId = 992451174110351420
    
    @nextcord.slash_command(name='rock_paper_scissors', description='Play Rock Paper Scissors with me', guild_ids=[testServerId])
    async def RPS(self, interaction:Interaction, round_length:int):
        self.playingRPS = True
        self.rps_round_length = round_length
        self.rps_opponent = interaction.user
        await interaction.response.send_message("New Rock Paper Scissors Game Started!")
    
    @nextcord.slash_command(name='rock_paper_scissors_score', description='Shows the result of the game rps game that ended', guild_ids=[testServerId])
    async def display_score(self, interaction: Interaction):
        if self.playingRPS and self.rps_round_length == 0:
            if(self.rps_player_points > self.rps_bot_points):
                embed = nextcord.Embed(title='RPS results', description=str(self.rps_opponent) + " won " + str(self.rps_player_points) + " - " + str(self.rps_bot_points) + "!", color=0x00ff55)
                await interaction.response.send_message(embed=embed)
            if(self.rps_player_points > self.rps_bot_points):
                embed = nextcord.Embed(title='RPS results', description=str(self.rps_opponent) + " lost " + str(self.rps_player_points) + " - " + str(self.rps_bot_points) + "!", color=0x00ff55)
                await interaction.response.send_message(embed=embed)
            if(self.rps_player_points == self.rps_bot_points):
                embed = nextcord.Embed(title='RPS results', description="The game ended in a draw with " + str(self.rps_player_points) + " each!", color=0x00ff55)
                await interaction.response.send_message(embed=embed)

            self.playingRPS = False
            self.rps_round_length = 3
            self.rps_opponent = None
            self.rps_player_points = 0
            self.rps_bot_points = 0


    @commands.Cog.listener()
    async def on_message(self,message):

        if self.playingRPS and message.author == self.rps_opponent:

            if message.content == 'rock' or message.content == 'scissors' or message.content == 'paper':
                pass
            else:
                return

            if self.rps_round_length != 0:
                choice_int = random.randint(0,2)
                choice_str = self.rock_paper_scissor_options[choice_int]

                await message.channel.send(choice_str)

                self.bot_choice = choice_str
                self.user_choice = message.content.lower()

            if(self.bot_choice == 'rock' and self.user_choice == 'paper'):
                self.rps_player_points += 1
                self.did_player_score = True
            if(self.bot_choice == 'paper' and self.user_choice == 'scissors'):
                self.rps_player_points += 1
                self.did_player_score = True
            if(self.bot_choice == 'scissors' and self.user_choice == 'rock'):
                self.rps_player_points += 1
                self.did_player_score = True

            if(self.user_choice == 'rock' and self.bot_choice == 'paper'):
                self.rps_bot_points += 1
                self.did_bot_score = True
            if(self.user_choice == 'paper' and self.bot_choice == 'scissors'):
                self.rps_bot_points += 1
                self.did_bot_score = True
            if(self.user_choice == 'scissors' and self.bot_choice == 'rock'):
                self.rps_bot_points += 1
                self.did_bot_score = True

            if(self.user_choice == self.bot_choice):
                self.did_player_score = False
                self.did_bot_score = False

            if(self.did_player_score):
                await message.channel.send('You scored one point, your current score is: ' + str(self.rps_player_points))
            elif(self.did_bot_score):
                await message.channel.send('I scored one point, my current score is: ' + str(self.rps_bot_points))
            else:
                await message.channel.send('No one scored!')

            self.did_player_score = False
            self.did_bot_score = False
            self.rps_round_length -= 1

            if(self.rps_round_length == 0):
                embed = nextcord.Embed(title='Game Ended', description='Use /rock_paper_scissors_score to get the results', color=0x00ff55)
                await message.channel.send(embed=embed)

def setup(client):
    client.add_cog(RPS(client))