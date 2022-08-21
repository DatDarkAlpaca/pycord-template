from discord.errors import ExtensionNotLoaded, ExtensionAlreadyLoaded, ExtensionError
from discord.commands import SlashCommandGroup, Option
from discord import ApplicationContext
from discord.ext import commands
from utils.logger import Logger

import sys
import os


class Admin(commands.Cog):
    admin = SlashCommandGroup('admin', 'Useful commands for bot admins.', checks=[commands.is_owner().predicate])

    def __init__(self, bot):
        self.logger = Logger('cog-admin')
        self.bot = bot

    @admin.command(description='Loads a bot cog', aliases=['unload_cog'])
    @commands.is_owner()
    async def load_extension(self, ctx: ApplicationContext,
                             cog: Option(str, 'Select cog to load.', required=True)):
        try:
            self.bot.load_extension(f"cogs.{cog}")
        except ExtensionAlreadyLoaded:
            return await ctx.respond(f"The cog '{cog}' is already loaded.", delete_after=10)

        await ctx.respond(f"Loaded extension: `{cog}`")
        self.logger.info(f"Loaded extension: {cog}")

    @admin.command(description='Unloads a bot cog', aliases=['unload_cog'])
    @commands.is_owner()
    async def unload_extension(self, ctx: ApplicationContext,
                               cog: Option(str, 'Select cog to load.', required=True)):
        try:
            self.bot.unload_extension(f"cogs.{cog}")
        except ExtensionNotLoaded:
            return await ctx.respond(f"The cog '{cog}' has not been loaded.", delete_after=10)

        await ctx.respond(f"Unloaded extension: `{cog}`")
        self.logger.info(f"Unloaded extension: {cog}")

    @admin.command(description='Reloads a bot cog', aliases=['unload_cog'])
    @commands.is_owner()
    async def reload_extension(self, ctx: ApplicationContext,
                               cog: Option(str, 'Select cog to load.', required=True)):
        try:
            self.bot.unload_extension(f"cogs.{cog}")
            self.bot.load_extension(f"cogs.{cog}")
        except ExtensionError:
            return await ctx.respond(f"An error has occurred while reloading '{cog}'.", delete_after=10)

        await ctx.respond(f"Unloaded extension: `{cog}`")
        self.logger.info(f"Unloaded extension: {cog}")

    @admin.command(description='Shuts me down...')
    @commands.is_owner()
    async def shutdown(self, ctx: ApplicationContext):
        await ctx.respond('Shutting down... Bye bye!')
        self.logger.info('Shutting down.')
        await self.bot.close()

    @admin.command(description='Restarts me!')
    @commands.is_owner()
    async def restart(self, ctx: ApplicationContext):
        await ctx.respond("I'll restart in a moment.")
        self.logger.info('Restarting bot.')
        await self.bot.close()
        os.execl(sys.executable, sys.executable, *sys.argv)


def setup(bot):
    bot.add_cog(Admin(bot))
