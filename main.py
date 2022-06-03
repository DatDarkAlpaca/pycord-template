from bot.cogs import load_extensions
from discord import Bot, Intents
from os import environ
import logging


def main():
    logging.basicConfig(level=logging.INFO)
    intents = Intents.default()

    bot = Bot(command_prefix=environ.get('command_prefix'), intents=intents,
              command_attrs=dict(hidden=True))

    load_extensions(bot)

    bot.run(environ.get('token'))


if __name__ == '__main__':
    main()
