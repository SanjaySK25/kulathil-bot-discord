import nextcord
from nextcord.ext import commands
import os
from nextcord import Interaction

TOKEN = 'MTExOTkzMjc0NDQ5NjA3MDY1Ng.GGGF9l.Ej8VZv3Ug_A95CaVlboNtnc_-U0kJzP1XfQ2l4'

intents = nextcord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix='!', intents=intents)

@client.event
async def on_ready():
    await client.change_presence(status=nextcord.Status.online, activity=nextcord.Activity(type=nextcord.ActivityType.watching, name='A GOD'))
    print('We have Logged in as {0.user}'.format(client))

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("You didn't provide a required argument!")

initial_extensions = []

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        initial_extensions.append("cogs." + filename[:-3])

if __name__ == '__main__':
    for extension in initial_extensions:
        client.load_extension(extension)

client.run(TOKEN)