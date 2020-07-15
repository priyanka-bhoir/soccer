# import discord
from discord.ext import commands
import random
from threading import Thread, Event
# from multiprocessing import Process
# import time
# import cogs.util
# import game.variables as vs

stop_event = Event()
# def do_actions():
#    """
#    Function that should timeout after 5 seconds. It simply prints a number and waits 1 second.
#    :return:
#    """
#    i = 0
#    while True:
#        i += 1
#        # print(i)
#        time.sleep(1)


class Startgame(commands.Cog):

    def __init__(self,client):
        self.client =client


    @commands.Cog.listener()
    async def on_ready(self):
        print("startgame.py")
        # await ctx.send('Game Starting in 3 seconds.')
        # action_process = Process()
        # action_process.start()
        # action_process.join(timeout=3)
        # action_process.terminate()

    @commands.command()
    async def throw(self,ctx):
        x=random.choice(['r','l'])
        if(x=='r'):
            print("t")

    @commands.command()
    async def catch(self,ctx):
        x=random.choice(['r','l'])
        if(x=='l'):
            print("C")





def setup(client):
    client.add_cog(Startgame(client))
