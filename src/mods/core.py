import discord
from discord.ext import commands


class Core(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Bot logged in with ID {self.client.user}')

    @commands.command()
    async def load(self, ctx, module = 'null'):

        if module == 'null':

            embed = discord.Embed(title='Module Loading',
                                  description=f'Attempted to load module \'null\', are you missing the \'module\' parameter?',
                                  color=0x004080)
            await ctx.send(embed=embed)

        elif module != 'core':

            self.client.load_extension(f'mods.{module}')

            embed = discord.Embed(title='Module Loading',
                                  description=f'Loaded module {module}',
                                  color=0x004080)
            await ctx.send(embed=embed)

        else:

            embed = discord.Embed(title='Module Loading',
                                  description=f'Attempted to load module \'core\', core is already loaded, and should never be touched with commands!',
                                  color=0x004080)
            await ctx.send(embed=embed)

    @commands.command()
    async def unload(self, ctx, module = 'null'):

        if module == 'null':

            embed = discord.Embed(title='Module Unloading',
                                  description=f'Attempted to unload module \'null\', are you missing the \'module\' parameter?',
                                  color=0x004080)
            await ctx.send(embed=embed)

        elif module != 'core':

            self.client.unload_extension(f'mods.{module}')

            embed = discord.Embed(title='Module Unloading',
                                  description=f'Unloaded module {module}',
                                  color=0x004080)
            await ctx.send(embed=embed)

        else:

            embed = discord.Embed(title='Module Unloading',
                                  description=f'Attempted to unload module \'core\', core module can not be unloaded!',
                                  color=0x004080)
            await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Core(client))
