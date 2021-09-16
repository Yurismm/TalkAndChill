import discord
from discord.ext import commands
import random


class _8ball(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["8ball"])
    async def _8ball(self, ctx, *, frage):
        antworten = ['Yes',
                     'No',
                     'Possibly',
                     'Maybe',
                     'Just ask the question again',
                     "I can't judge, because I'm not a person, but I think so"]
        embed = discord.Embed(color=0xC1C0C0)
        embed.add_field(name=f'Question:', value=f'{frage}', inline=False)
        embed.add_field(name=f'Answer:', value=f'{random.choice(antworten)}', inline=False)
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(_8ball(client))
