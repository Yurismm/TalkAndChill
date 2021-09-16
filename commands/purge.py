import discord

from discord.ext import commands


class Purge(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(pass_context=True)
    @commands.has_role('Staff')
    async def purge(self, ctx, amount: int):
        member = ctx.message.author
        userAvatar = member.avatar_url
        embed = discord.Embed(colour=0x6DF034)
        embed.add_field(name='Clear Info', value=f'Delete {amount} message(s)', inline=False)
        embed.set_footer(text=f'Requested by {member}', icon_url=f'{userAvatar}')
        await ctx.message.delete()
        await ctx.channel.purge(limit=amount)
        await ctx.send(embed=embed, delete_after=5)

    @purge.error
    async def purge_error(self, ctx, error):
        if isinstance(error, commands.MissingRole):
            member = ctx.message.author
            userAvatar = member.avatar_url
            embed = discord.Embed(colour=discord.Colour.dark_red())
            embed.add_field(name=f'**ERROR**', value=f'You cannot use the clear command, you need the staff role.',
                            inline=False)
            embed.set_footer(text=f'Requested by {member}', icon_url=f'{userAvatar}')
            await ctx.send(embed=embed, delete_after=5)
            await ctx.message.delete()

        else:
            if isinstance(error, commands.MissingRequiredArgument):
                member = ctx.message.author
                userAvatar = member.avatar_url
                embed = discord.Embed(colour=discord.Colour.dark_red())
                embed.add_field(name=f'**ERROR**',
                                value=f'Usage: {self.client.prefix}purge <number>', inline=False)
                embed.set_footer(text=f'Requested by {member}', icon_url=f'{userAvatar}')
                await ctx.send(embed=embed, delete_after=5)
                await ctx.message.delete()


def setup(client):
    client.add_cog(Purge(client))
