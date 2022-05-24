# Contains the basic bot commands such as ping, about, and help.

import discord
from discord.ext import commands


class Basics(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def ping(self, ctx):
        embed = discord.Embed(title='Discord API Latency', description=f'`{round(self.client.latency * 1000, 1)}ms` of measured latency to Discord API',
                              color=0x004080)
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Basics(client))
