import discord
import json
import os
from discord.ext import commands
from dotenv import load_dotenv
import game.variables as vs


load_dotenv()
token=os.getenv('DISCORD_TOKEN')
prefix=os.getenv('PREFIX')


# def get_prefix(client,message):
#     with open('config.json','r') as f:
#         prefix=json.load(f)
#
#     return prefix[str(message.guild.id)]
# prefix=get_prefix
client = commands.Bot(prefix,description="Soccer Game",color=3447003,help_command=None)

@client.event
async def on_ready():
    print('Bot is ready.')

@client.command(name="prefix", pass_context=True)
async def _prefix(ctx, new_prefix):
    # Do any validations you want to do
    prefix[ctx.message.server.id] = new_prefix
    with open("config.json", "w") as f:
        json.dump(prefix, f)

# @client.event
# async def on_guild_join(guild):
#     with open('config.json','r') as f:
#        prefix=json.load(f)
#
#     prefix[str(guild.id)]='.'
#
#     with open('config.json','w') as f:
#         json.dump(prefix,f,indent=4)

@client.command()
async def play(ctx):
    # game.play.play(ctx)
    vs.p1=0
    vs.p2=0
    vs.stp=0
    await ctx.send(f"Here You are Playing with our bot")
    await ctx.send("Toss and start....")
    # for file in os.listdir('./cogs'):
    #     if file.endswith('.py'):
    #         client.load_extension(f'cogs.{file[:-3]}')
    client.load_extension(f'cogs.toss')
    # client.unload_extension(f'cogs.toss')
    # client.load_extension(f'cogs.startgame')

@client.event
async def on_Command_error(ctx):
    if ctx.author == client.user:
        return
    # if isinstance(err,commands.MissingRequiredArgument):
    else:
        await ctx.send('Please typed an invalid argument(check help for more)')

@client.command()
async def user(ctx):
    await ctx.send(f"""# of members: {ctx.guild.member_count}""")


@client.command()
async def help(ctx):
    embed=discord.Embed(title="Help", description="some useful commands", color=3447003)
    embed.add_field(name="play",value="Starts the game",inline=False)
    embed.add_field(name="rules",value="Displays the rules")
    embed.add_field(name="users",value="Displays total number of users",inline=False)
    embed.set_author(name=client.user.name,icon_url=client.user.avatar_url)
    embed.set_footer(text=ctx.author.name,icon_url=ctx.author.avatar_url)
    await ctx.channel.send(content=None,embed=embed)

@client.command()
async def rules(ctx):
    # await ctx.channel.send("Welome to Soccer game {0.author.mention} ".format(ctx))
    embed1=discord.Embed(title="Extremly official rules of Soccer game", description="Here two player will play the game. One Player will kick the ball and other is GoalKeeper which will be decided by the toss.The Player has to type number b/w 1 to 6, once the player will enter bot or other player will enter or (a random output generated if playing with bot)", color=3447003)
    embed1.add_field(name="1st.",value="If player1 number is greater than player2 player1 will get goal point or viseversa",inline=False)
    embed1.add_field(name="2nd.",value="the maximum point goal gainer wins the game at the end",inline=False)
    embed1.add_field(name="3rd.",value="All rules of Soccer apply",inline=False)
    # embed1.set_thumbnail(name=client.user.name,icon_url=client.user.avatar_url)
    embed1.set_footer(text=ctx.author.name,icon_url=ctx.author.avatar_url)
    await ctx.channel.send(content=None,embed=embed1)





client.run(token)

