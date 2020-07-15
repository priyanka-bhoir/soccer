from game import variables as vs
from discord.ext import commands


class Scoreboard(commands.Cog):

    def __init__(self,client):
        self.client =client

    def score(self,a,b):
        s = f'''______________________________________\n" \
          "----------scoreboard-------------------\n" \
          "{a}={vs.p1}\n" \
          "{b}={vs.p2}\n" \
          "_________________________________________'''
        return s
    @commands.Cog.listener()
    async def on_ready(self,ctx):
        print("scoreboard.py")
        # ctx.unload(f'commands')
    @commands.command()
    async def score(self,ctx):
        await ctx.send(self.score())

def setup(client):
    client.add_cog(commands(client))
