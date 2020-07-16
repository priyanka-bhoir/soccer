# import discord
from discord.ext import commands
import random
import game.variables as vs
from threading import Thread, Event
# from multiprocessing import Process
# import time
# import cogs.util
# import game.variables as vs

stop_event = Event()
class Startgame(commands.Cog):

    def __init__(self,client):
        self.client =client


    @commands.Cog.listener()
    async def on_ready(self,ctx):
        print("startgame.py")
        # ctx.unload(f'cogs.toss')
        # await ctx.send('Game Starting in 3 seconds.')
        # action_process = Process()
        # action_process.start()
        # action_process.join(timeout=3)
        # action_process.terminate()

    @commands.command()
    async def throw(self,ctx):
        await ctx.send("wel... which direction(r (right) or l(left))")
        vs.flag=1
        self.client.load_extension(f'cogs.lrcmd')

    @commands.command()
    async def catch(self,ctx):
        await ctx.send("wel... which direction(r (right) or l(left))")
        vs.flag=0
        self.client.load_extension(f'cogs.lrcmd')




def setup(client):
    client.add_cog(Startgame(client))
