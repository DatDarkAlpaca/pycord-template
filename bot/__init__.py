from discord.ext import commands
from utils.logger import Logger


class Bot(commands.AutoShardedBot):
    def __init__(self, *args, **kwargs):
        super(Bot, self).__init__(*args, **kwargs)
        self.logger = Logger('bot')

    @commands.Cog.listener()
    async def on_ready(self):
        self.logger.info(f"{self.user} is online.")
        # await db.build()
