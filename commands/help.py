import discord

import json

from discord.ext import commands


class HelpCommand(commands.Cog):
    def __init__(self, client):
        self.client = client
        client.remove_command("help")

    @commands.command(pass_contex=True)
    async def help(self, ctx):
        member = ctx.message.author
        userAvatar = member.avatar_url
        embed = discord.Embed(title='List of all standard commands', colour=0xfc03f0)
        embed.add_field(name=f'{self.client.prefix}8ball',
                        value=f'Ask a question to the bot, it will give you an answer back.', inline=False)
        embed.add_field(name=f'{self.client.prefix}ping', 
                        value=f'Look at the ping of the bot', inline=False)
        embed.add_field(name=f'{self.client.prefix}ban', 
                        value=f'Ban users', inline=False),
        embed.add_field(name=f'{self.client.prefix}help', 
                        value=f'This command can show you how to use other commands, and gives you help on commands', inline=False),
        embed.add_field(name=f'{self.client.prefix}purge', 
                        value=f'Delete messages in mass', inline=False),
        embed.add_field(name=f'{self.client.prefix}unmute', 
                        value=f'Unmute a user.', inline=False),
        embed.add_field(name=f'{self.client.prefix}vcmute', 
                        value=f'Mute a user in VC', inline=False),
        embed.add_field(name=f'{self.client.prefix}vcunmute', 
                        value=f'Unmute a user in VC', inline=False),
        embed.add_field(name=f'{self.client.prefix}mute', 
                        value=f'Mute a user.', inline=False)
        embed.set_footer(text=f'Requested by {member}', icon_url=f'{userAvatar}')
        await ctx.message.delete()
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(HelpCommand(client))
