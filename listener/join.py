import discord

from discord.ext import commands
from discord.utils import get


class Join(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_member_join(self, member):
        welcomechannel = self.client.get_channel(703051794158452837)
        role = get(member.guild.roles, id=703699629052526642)
        embed = discord.Embed(color=discord.Color.green())
        embed.set_author(name=f'Welcome to {member.guild.name}', icon_url=f'{member.guild.icon_url}')
        embed.set_thumbnail(url=member.avatar_url)
        embed.add_field(name="Hey,",
                        value=f"{member.mention}We are happy that you're here. Enjoy your time! If you have any questions just let us know, we'll help you! Please take a look at our rules <#703057919763021914>",
                        inline=False)
        await welcomechannel.send(embed=embed)
        await member.add_roles(role)

def setup(client):
    client.add_cog(Join(client))
