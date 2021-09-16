import discord
from discord.ext import commands


class BanCommand(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_any_role('Owner', 'Head-Admin', 'Undercover Admin', 'Head-Moderator', 'Moderator')
    async def ban(self, ctx, member: discord.Member, *, reason='No Reason'):
        user = ctx.message.author
        userAvatar = user.avatar_url
        embed = discord.Embed(title=f'Ban', colour=discord.Colour.dark_red())
        embed.add_field(name='Info', value=f'The User {member.mention} has been Banned.', inline=False)
        embed.add_field(name=f'Reason', value=f'{reason}', inline=False)
        embed.set_footer(text=f'Requested by {user}', icon_url=f'{userAvatar}')
        await member.ban(reason=reason, delete_message_days=100)
        await ctx.message.delete()
        await ctx.send(embed=embed, delete_after=5)

        log = self.client.get_channel(873997799203676232)
        embed1 = discord.Embed(title=f'**Ban Log**', colour=0xff1717, timestamp=ctx.message.created_at)
        embed1.add_field(name=f'**User**', value=f'{member.mention}', inline=False)
        embed1.add_field(name=f'**Moderator**', value=f'{user.mention}', inline=False)
        embed1.add_field(name=f'**Reason**', value=f'{reason}', inline=False)
        embed1.set_footer(text=f'Requested by {user}', icon_url=f'{userAvatar}')
        await log.send(embed=embed1)

    @ban.error
    async def ban_error(self, ctx, error):
        if isinstance(error, commands.MissingRole):
            member = ctx.message.author
            userAvatar = member.avatar_url
            embed = discord.Embed(colour=discord.Colour.dark_red())
            embed.add_field(name=f'**ERROR**',
                            value=f'You need the moderator role or higher to use the command.', inline=False)
            embed.set_footer(text=f'Requested by {member}', icon_url=f'{userAvatar}')
            await ctx.send(embed=embed, delete_after=5)
            await ctx.message.delete()

        else:
            if isinstance(error, commands.MissingRequiredArgument):
                member = ctx.message.author
                userAvatar = member.avatar_url
                embed = discord.Embed(colour=discord.Colour.dark_red())
                embed.add_field(name=f'**ERROR**',
                                value=f'Usage: {self.client.prefix}ban @user#0000 <Reason>', inline=False)
                embed.set_footer(text=f'Requested by {member}', icon_url=f'{userAvatar}')
                await ctx.send(embed=embed, delete_after=5)
                await ctx.message.delete()


def setup(client):
    client.add_cog(BanCommand(client))
