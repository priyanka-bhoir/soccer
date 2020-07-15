import game.variables as vs
from discord.ext import commands
import random as r
import os
from dotenv import load_dotenv

load_dotenv()
prefix=os.getenv('PREFIX')

class Commands(commands.Cog):


    def __init__(self,client):
        self.client =client

    @commands.Cog.listener()
    async def on_ready(self,ctx):
        print("commands.py")
        ctx.unload(f'startgame')

    @commands.command()
    async def r(self,ctx):
        vs.stp=vs.stp+1
        if vs.stp>10:
            a=r.choice(['r','l'])
            await ctx.send(a)
            vs.stp=vs.stp+1
            if({prefix}+a=='r'):
                if(vs.flag==1):
                    vs.p2=vs.p2+1
                else:
                    vs.p1=vs.p1+1
            elif({prefix}+a!='r'):
                if(vs.flag==1):
                    vs.p1=vs.p1+1
                else:
                    vs.p2=vs.p2+1

        else:
            ctx.load(f'scoreboard')
        # a=sc.score(self.client,ctx.user)



    async def l(self,ctx):
        vs.stp=vs.stp+1
        if vs.stp>10:
            a=r.choice(['r','l'])
            await ctx.send(a)
            vs.stp=vs.stp+1
            if({prefix}+a=='l'):
                if(vs.flag==1):
                    vs.p2=vs.p2+1
                else:
                    vs.p1=vs.p2+1
            elif({prefix}+a!='l'):
                if(vs.flag==1):
                    vs.p1=vs.p1+1
                else:
                    vs.p2=vs.p2+1

        else:
            ctx.load(f'scoreboard')

def setup(client):
    client.add_cog(commands(client))
