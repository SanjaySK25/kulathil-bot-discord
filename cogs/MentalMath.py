import nextcord
from nextcord.ext import commands
from nextcord import Interaction
import random

class Minigames(commands.Cog):

    testServerId = 992451174110351420

    def __init__(self, client):
        self.client = client
        self.playing_math = False
        self.digit_count = None
        self.math_rounds = None
        self.current_math_round = None
        self.math_type = None
        self.question_asked = None
        self.question = None
        self.answered_people = []
        self.answered_people_points = []
        self.second_number_of_digits = None
    
    @nextcord.slash_command(name='math', description='Contest a mental math competition', guild_ids=[testServerId])
    async def mental_math(self, interaction: Interaction, number_of_digits: int, second_number_of_digits:int, rounds: int, type: str):
        self.playing_math = True
        self.digit_count = number_of_digits
        self.math_rounds = rounds
        self.math_type = type
        self.current_math_round = 1
        self.question_asked = False
        self.second_number_of_digits = second_number_of_digits
        embed = nextcord.Embed(title='Starting mental math round', description='A new game of mental math will start', color=0x00ff55)
        embed.set_author(name=interaction.user.display_name, icon_url=interaction.user.avatar)
        await interaction.response.send_message(embed=embed)
    
    @commands.Cog.listener()
    async def on_message(self, message):
        current_message_author = message.author.display_name
        current_message = message.content

        if message.author == self.client.user:
            return

        operation = ''

        if self.playing_math:

            if self.math_type == 'add':
                operation = '+'
            elif self.math_type == 'subtract':
                operation = '-'
            elif self.math_type == 'multiply':
                operation = '*'
            elif self.math_type == 'divide':
                operation = '/'

            if self.math_rounds == self.current_math_round:
                
                self.answered_people_points[self.answered_people.index(current_message_author)] += 1

                embed = nextcord.Embed(title='Results', description='Check who won!', color=0xff0000)

                for x in self.answered_people:
                    embed.add_field(name=str(x), value=str(self.answered_people_points[self.answered_people.index(x)]), inline=True)
                
                await message.channel.send(embed=embed)

                self.playing_math = False
                self.digit_count = None
                self.math_rounds = None
                self.current_math_round = None
                self.math_type = None
                self.question_asked = None
                self.question = None
                self.answered_people = []
                self.answered_people_points = []

            if not self.question_asked:

                math_limit = ''
                math_limit2 = ''
                math_limit_small1 = '1'
                math_limit_small2 = '1'

                for x in range(self.digit_count):
                    math_limit = math_limit + '9'
                    math_limit_small1 = math_limit_small1 + '0'
                
                for x in range(self.second_number_of_digits):
                    math_limit2 = math_limit2 + '9'
                    math_limit_small2 = math_limit_small2 + '0'
                
                self.question = str(random.randint(0,int(math_limit))) + operation + str(random.randint(int(math_limit2),int(math_limit2)))

                embed = nextcord.Embed(title='Question ' + str(self.current_math_round), description=self.question, color=0x00ff55)
                await message.channel.send(embed=embed)
                self.question_asked = True
            
            elif self.question_asked and str(current_message).isdigit():

                if int(current_message) == eval(self.question):

                    if current_message_author in self.answered_people:
                        self.answered_people_points[self.answered_people.index(current_message_author)] += 1
                    else:
                        self.answered_people.append(current_message_author)
                        self.answered_people_points.append(1)

                    embed = nextcord.Embed(title=f'Answered by {str(current_message_author)}', description=str(current_message_author) + ' got one point!', color=0x00ff55)
                    await message.channel.send(embed=embed)

                    self.current_math_round += 1
                    self.question_asked = False

                    math_limit = ''
                    math_limit2 = ''
                    math_limit_small1 = '1'
                    math_limit_small2 = '1'

                    for x in range(self.digit_count):
                        math_limit = math_limit + '9'
                        math_limit_small1 = math_limit_small1 + '0'
                    
                    for x in range(self.second_number_of_digits):
                        math_limit2 = math_limit2 + '9'
                        math_limit_small2 = math_limit_small2 + '0'
                    
                    self.question = str(random.randint(0,int(math_limit))) + operation + str(random.randint(0,int(math_limit2)))

                    embed = nextcord.Embed(title='Question ' + str(self.current_math_round), description=self.question, color=0x00ff55)
                    await message.channel.send(embed=embed)
                    self.question_asked = True

def setup(client):
    client.add_cog(Minigames(client))