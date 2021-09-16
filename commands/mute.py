import discord
from discord.ext import commands


class MuteCommand(commands.Cog):
    def __init__(self, client):
        self.client = client
        client.remove_command("mute")

    @commands.command()
    @commands.has_role('Staff')
    async def mute(self, ctx, member: discord.Member, *, reason='No Reason'):
        user = ctx.message.author
        userAvatar = user.avatar_url
        mutedRole = discord.utils.get(ctx.guild.roles, id=703060570475069531)

        embed = discord.Embed(title=f'Mute', colour=discord.Colour.dark_red())
        embed.add_field(name='Info',
                        value=f'The User {member.mention} is now muted by {user.mention}.',
                        inline=False)
        embed.add_field(name=f'Reason', value=f'{reason}', inline=False)
        embed.set_footer(text=f'Requested by {user}', icon_url=f'{userAvatar}')
        await member.add_roles(mutedRole)
        await ctx.message.delete()
        await ctx.send(embed=embed, delete_after=5)

        log = self.client.get_channel(873997799203676232)
        
        embed1 = discord.Embed(title=f'**Mute Log**', colour=0xff1717,
                               timestamp=ctx.message.created_at)
        embed1.add_field(name=f'**User**', value=f'{member.mention}', inline=False)
        embed1.add_field(name=f'**Moderator**', value=f'{user.mention}', inline=False)
        embed1.add_field(name=f'**Reason**', value=f'{reason}', inline=False)
        embed1.set_footer(text=f'Requested by {user}', icon_url=f'{userAvatar}')
        await log.send(embed=embed1)

        embed2 = discord.Embed(colour=discord.Colour.dark_red(), timestamp=ctx.message.created_at)
        embed2.add_field(name=f'Actions have been taken',
                         value=f'You have been muted by the {ctx.guild.name} Server')
        embed2.set_footer(text=f'Action carried out by {user}', icon_url=f'{userAvatar}')
        await member.send(embed=embed2)

    @mute.error
    async def mute_error(self, ctx, error):
        if isinstance(error, commands.MissingRole):
            member = ctx.message.author
            userAvatar = member.avatar_url
            embed = discord.Embed(colour=discord.Colour.dark_red())
            embed.add_field(name=f'**ERROR**',
                            value=f'You cannot use the mute command, you need the staff role.', inline=False)
            embed.set_footer(text=f'Requested by {member}', icon_url=f'{userAvatar}')
            await ctx.send(embed=embed, delete_after=5)
            await ctx.message.delete()

        else:
            if isinstance(error, commands.MissingRequiredArgument):
                member = ctx.message.author
                userAvatar = member.avatar_url
                embed = discord.Embed(colour=discord.Colour.dark_red())
                embed.add_field(name=f'**ERROR**',
                                value=f'Usage: {self.client.prefix}mute @user#0000 <Reason>', inline=False)
                embed.set_footer(text=f'Requested by {member}', icon_url=f'{userAvatar}')
                await ctx.send(embed=embed, delete_after=5)
                await ctx.message.delete()


def setup(client):
    client.add_cog(MuteCommand(client))
