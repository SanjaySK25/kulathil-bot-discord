import nextcord
from nextcord.ext import commands
from nextcord import FFmpegPCMAudio
from nextcord import member
from nextcord.ext.commands import has_permissions, MissingPermissions
import os

TOKEN = 'MTExOTkzMjc0NDQ5NjA3MDY1Ng.GGGF9l.Ej8VZv3Ug_A95CaVlboNtnc_-U0kJzP1XfQ2l4'

queues = {}

def check_queue(ctx, id):
    if queues[id] != []:
        voice = ctx.guild.voice_client
        source = queues[id].pop(0)
        player = voice.play(source)

class Music(commands.Cog):
    
    def __init__(self, client):
        self.client = client

    @commands.command(pass_context=True, name='join')
    async def join(self,ctx):
        if(ctx.author.voice):
            channel = ctx.message.author.voice.channel
            voice = await channel.connect()
            await ctx.send("I joined the voice channel!")
        else:
            await ctx.send("You have to be in a voice channel to run this command!")

    @commands.command(pass_context=True)
    async def leave(self,ctx):
        if(ctx.voice_client):
            await ctx.guild.voice_client.disconnect()
            await ctx.send("I left the voice channel!")
        else:
            await ctx.send("I am not in a voice channel!")

    @commands.command(pass_context=True)
    async def pause(self,ctx):
        voice = nextcord.utils.get(self.client.voice_clients,guild=ctx.guild)
        if voice.is_playing():
            voice.pause()
        else:
            await ctx.send('At the moment, there is no audio playing in the voice channel!')

    @commands.command(pass_context=True)
    async def resume(self,ctx):
        voice = nextcord.utils.get(self.client.voice_clients,guild=ctx.guild)
        if voice.is_paused():
            voice.resume()
        else:
            await ctx.send("Nothing is paused at the moment!")

    @commands.command(pass_context=True)
    async def stop(self,ctx):
        voice = nextcord.utils.get(self.client.voice_clients,guild=ctx.guild)
        voice.stop()
        await ctx.send("I stopped the music!")

    @commands.command(pass_context=True)
    async def play(self,ctx, arg):
        voice = ctx.guild.voice_client
        source = FFmpegPCMAudio('./audio/' + arg)
        player = voice.play(source, after=lambda x=None: check_queue(ctx, ctx.message.guild.id))
        await ctx.send("Now playing " + arg)

    @commands.command(pass_context=True)
    async def queue(self,ctx,arg):
        voice = ctx.guild.voice_client
        source = FFmpegPCMAudio(arg)

        guild_id = ctx.message.guild.id

        if guild_id in queues:
            queues[guild_id].append(source)
        else:
            queues[guild_id] = [source];

        await ctx.send("Added " + arg + " to queue!")
    
    @commands.command(pass_context=True)
    async def BGMlist(self, ctx):
        excluded_files = ['.idea,venv,index.py']
        songs = os.listdir('E:\Programming Stuff\nextcord Bots\Bot\\audio')
        for song in songs:
            if song == '.idea':
                pass
            elif song == 'venv':
                pass
            elif song == 'index.py':
                pass
            else:
                await ctx.send(song)

def setup(client):
    client.add_cog(Music(client))