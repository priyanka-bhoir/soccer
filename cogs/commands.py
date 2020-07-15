import game.variables as vs
import game.scoreboard as sc
from discord.ext import commands
import random as r

class Commands(commands.Cog):


    def __init__(self,client):
        self.client =client

    @commands.Cog.listener()
    async def on_ready(self):
        print("commands.py")

    @commands.command()
    async def r(self,ctx):
        # for i in range(5):
        a=r.choice(['r','l'])
        if(a=='r'):
            vs.p1=vs.p1+1
        else:
            vs.p2=vs.p2+1
        # a=sc.score(self.client,ctx.user)



    async def l(self,ctx):
        # for i in range(5):
        a=r.choice(['r','l'])
        if(a=='l'):
            vs.p1=vs.p1+1
        else:
            vs.p2=vs.p2+1
        # a=sc.score(self.client,ctx.user)

def setup(client):
    client.add_cog(commands(client))
