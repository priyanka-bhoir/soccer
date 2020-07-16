from discord.ext import commands
import random
import os
import game.variables as vs
from dotenv import load_dotenv
import game.variables as vs


load_dotenv()
prefix=os.getenv('PREFIX')
class Toss(commands.Cog):
    def __init__(self,client):
        self.client = client
        self.x =""


    @commands.Cog.listener()
    async def on_ready(self,ctx):
        print("toss.py")



    @commands.command()
    async def toss(self,ctx):

        await ctx.send("you need heads or tails....?")
        self.x = random.choice(['heads', 'tails'])
        print(self.x)
        print(prefix)

    @commands.command()
    async def heads(self,ctx):
        t = random.choice(['throw','catch'])
        a = f"{str(prefix)}heads"
        print(a)
        print(prefix+self.x)
        if str(prefix+self.x) == str(a):
            await ctx.send("you won the toss....")
            # self.won(ctx)
            print(f"{prefix}heads")
            await ctx.send("You want to throw or catch the goal....?(throw | catch)")
            self.client.load_extension(f'cogs.startgame')
        elif str(prefix+self.x) != str(a):
            await ctx.send("Ops... you lost the toss....")
            # self.lost(ctx,t)
            if t=="throw":
                vs.flag=1
            else:
                vs.flag=0
            await ctx.send(t)
            vs.stp=vs.stp+1
            vs.p1=vs.p1+1
            print(vs.p1)
            self.client.cogs_load(f'cogs.lrcmd')

    @commands.command()
    async def tails(self,ctx):
        # x = random.choice(['heads','tails'])
        t = random.choice(['throw','catch'])
        a = f"{str(prefix)}tails"
        if str(prefix+self.x) == str(a):
            await ctx.send("you won the toss....")
            # self.won(ctx)
            print(f"{prefix}heads")
            await ctx.send("You want to throw or catch the goal....?(throw | catch)")
            self.client.load_extension(f'cogs.startgame')
            # await ctx.send("you won the toss....")
            # await ctx.send("You want to throw or catch the goal....?(throw | catch)")
            # self.client.load_extension(f'cogs.startgame')

        elif str(prefix+self.x) != str(a):
            await ctx.send("Ops... you lost the toss....")
            # self.lost(ctx,t)
            if t=="throw":
                vs.flag=1
            else:
                vs.flag=0
            await ctx.send(t)
            vs.stp=vs.stp+1
            vs.p1=vs.p1+1
            print(vs.p1)
            self.client.load_extension(f'cogs.lrcmd')

            # await ctx.send("Ops... you lost the toss....")
            # if t=="throw":
            #     vs.flag=1
            # else:
            #     vs.flag=0
            # await ctx.send(t)
            # vs.stp=vs.stp+1
            # vs.p1=vs.p1+1
            # self.client.load_extension(f'cogs.commands')
            # print(vs.p1)


def setup(client):
    client.add_cog(Toss(client))
