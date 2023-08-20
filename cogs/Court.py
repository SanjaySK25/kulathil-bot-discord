import nextcord
from nextcord.ext import commands

shouldStaySilent = False
rules = ['Users must obey the nextcord community guidelines.',
         'No racism/homophobia/bullying/etc of any kind Bullying of any kind will end in a mute and possibly a ban.',
         'Everyone Can Report', 'No Server Raiding', 'No Chatting In welcome channel',
         'No robbing and bankrob is illegal', 'No impersonating']

questions = ['Who is the lord?','Who is the highest ranked person?', 'What is the best game in history?','Who is killadi of the India?']
answers = ['Lord is Sree.Kulathil Meen and Sree.SanjaySK!','Respected Neo sir has the highest rank!','Minecraft!','Sir.Neo']

class Court(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self,message):
        if '#' in str(message.author):
            username = str(message.author).split('#')[0]
            user_id = str(message.author).split('#')[1]
        else:
            username = str(message.author)
            user_id = str(message.author)
        content = str(message.content).lower()

        if message.author == self.client.user:
            return
        
        #Changing Values
        if user_id == 'sanjayskiqgod':
            username = 'Lord'

        if user_id == 'neo.007_':
            username = 'Judge'

        #Every channel
        if content == '/list rules':
            for x in range(len(rules)):
                await message.channel.send('RULE ' + str(x+1) + ': ' +rules[x])
        
        for x in range(len(questions)):
            if(content == questions[x].lower()):
                await message.channel.send(answers[x])


        #Court features

        if 'court' in message.channel.name:
            global shouldStaySilent

            if shouldStaySilent and username != 'Judge':
                await message.delete()

            #Code to silence the court

            if content == 'silence' and username == 'Judge':
                await message.channel.send('Silencing the court, your honour!')
                shouldStaySilent = True
            
            if content == 'unsilence' and username == 'Judge':
                await message.channel.send('Unsilencing the court, your honour!')
                shouldStaySilent = False

def setup(client):
    client.add_cog(Court(client))