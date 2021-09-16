import discord
import asyncio
from discord.ext import commands


class TempMute(commands.Cog):
    def __init__(self, client):
        self.client = client
        client.remove_command("tempmute")
    @commands.command()
    @commands.has_role("Staff")
    async def tempmute(ctx, member: discord.Member,*,time:int, d ,reason=None):
        guild = ctx.guild
        
        for role in guild.roles:
            if role.name == "Muted":
                await member.add_roles(role)
                embed = discord.Embed(title="Person has been muted", description=f"{member.mention} has been tempmuted",colour=discord.Colour.dark_red),
                embed.add_field(name="reason:", value=reason, inline=False),
                embed.add_field(name="Time left on mute:", value=f"{time}{d}", inline=False)
                await ctx.send(embed=embed)
                
                if d == "s":
                    await asyncio.sleep(time)
                    
                if d == "m":
                    await asyncio.sleep(time*60)
                    
                if d == "h":
                    await asyncio.sleep(time*60*60)
                    
                if d == "d":
                    await asyncio.sleep(time*60*60*24)
            
            await member.remove_roles(role)

            embed2 = discord.Embed(title="unmute (temp)",description=f"unmuted {member.mention}", colour=discord.Colour.dark_red)

            await ctx.send(embed=embed2)

            return
def setup(client):
    client.add_cog(TempMute(client))
