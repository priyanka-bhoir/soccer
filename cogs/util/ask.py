import discord
from discord.ext import commands
def ask(client,askTo,channel,question,onAnswerCb):
    channel.send(f'<@{askTo.id}>{question}')

    # finalAnswerHandeler=
    # notAnswer=channel.send(f"<@{askTo}> You didn\'t answer in 15s, now your chance is gone.")
    # client.off('message',finalAn  swerHandeler)
    pass



