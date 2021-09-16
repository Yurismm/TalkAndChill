import json
import os

import discord

from discord.ext import commands


class Ping(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def ping(self, ctx):
        member = ctx.message.author
        userAvatar = member.avatar_url
        embed = discord.Embed(color=0x11DC41)
        embed.add_field(name="Ping", value=f'My Ping is {round(self.client.latency * 1000)} MS')
        embed.set_footer(text=f'Requested by {member}', icon_url=f'{userAvatar}')
        await ctx.message.delete()
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Ping(client))
