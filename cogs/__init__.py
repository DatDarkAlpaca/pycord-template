from discord.ext import commands
from os import environ
import logging


class PycordBot(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def on_ready(self):
        logger = logging.getLogger('discord')
        logger.info(f"{environ.get('bot_name')} is ready.")


def setup(bot):
    bot.add_cog(PycordBot(bot))
