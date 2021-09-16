import discord
from discord.ext import commands


class VcUnmuteCommand(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_role('Staff')
    async def vcunmute(self, ctx, member: discord.Member):
        user = ctx.message.author
        userAvatar = user.avatar_url
        mutedRole = discord.utils.get(ctx.guild.roles, id=863569906326700062)

        embed = discord.Embed(title=f'Voice Mute', colour=discord.Colour.dark_green())
        embed.add_field(name='Info',
                        value=f'The User {member.mention} is now Voice muted by {user.mention}.',
                        inline=False)
        embed.set_footer(text=f'Requested by {user}', icon_url=f'{userAvatar}')
        await member.add_roles(mutedRole)
        await ctx.message.delete()
        await ctx.send(embed=embed, delete_after=5)

        log = self.client.get_channel(873997799203676232)
        embed1 = discord.Embed(title=f'**Voice Mute Log**', colour=0x0cf728,
                               timestamp=ctx.message.created_at)
        embed1.add_field(name=f'**User**', value=f'{member.mention}', inline=False)
        embed1.add_field(name=f'**Moderator**', value=f'{user.mention}', inline=False)
        embed1.set_footer(text=f'Requested by {user}', icon_url=f'{userAvatar}')
        await log.send(embed=embed1)

    @vcunmute.error
    async def vcunmute_error(self,ctx, error):
        if isinstance(error, commands.MissingRole):
            member = ctx.message.author
            userAvatar = member.avatar_url
            embed = discord.Embed(colour=discord.Colour.dark_red())
            embed.add_field(name=f'**ERROR**',
                            value=f'You cannot use the Voice Mute command, you need the staff role.', inline=False)
            embed.set_footer(text=f'Requested by {member}', icon_url=f'{userAvatar}')
            await ctx.send(embed=embed, delete_after=5)
            await ctx.message.delete()

        else:
            if isinstance(error, commands.MissingRequiredArgument):
                member = ctx.message.author
                userAvatar = member.avatar_url
                embed = discord.Embed(colour=discord.Colour.dark_red())
                embed.add_field(name=f'**ERROR**',
                                value=f'Usage: {self.client.prefix}vcunmute @user#0000', inline=False)
                embed.set_footer(text=f'Requested by {member}', icon_url=f'{userAvatar}')
                await ctx.send(embed=embed, delete_after=5)
                await ctx.message.delete()


def setup(client):
    client.add_cog(VcUnmuteCommand(client))
