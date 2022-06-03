from fnmatch import fnmatch
from os import walk
import logging


def find_cog_paths():
    file_pattern = '*.py'

    results = []
    for path, subdirectories, files in walk('./cogs'):
        for cog in files:
            if not fnmatch(cog, file_pattern):
                continue

            cog_path = path.replace('\\', '.').replace('./', '') + '.' + cog[:-3]
            results.append(cog_path)

    return results


def load_extensions(bot):
    cog_path_list = find_cog_paths()
    logger = logging.getLogger('discord')

    for cog_path in find_cog_paths():
        try:
            bot.load_extension(cog_path)
            logger.info(f"{cog_path[:-3]} has been successfully loaded.")
        except Exception as e:
            logger.warning(f"{cog_path[:-3]} couldn't be loaded! | {e}")

    if not len(cog_path_list):
        logger.info('No cogs were detected.')
