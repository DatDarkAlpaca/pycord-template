from discord.http import NotFound, HTTPException


# Reactions:
async def safe_add_reaction(message, reaction):
    try:
        await message.add_reaction(reaction)
    except NotFound:
        pass
    except HTTPException as e:
        print(e)


async def safe_remove_reaction(message, reaction, user):
    try:
        await message.remove_reaction(reaction, user)
    except NotFound:
        pass


# Message:
async def safe_delete_message(message):
    try:
        await message.delete()
    except (NotFound, AttributeError):
        pass


# Voice Channel:
async def safe_disconnect(ctx):
    if ctx.voice_client:
        await ctx.voice_client.disconnect()