"""
bot.py

This is where we define our bot object and setup_hook (replacement for on_ready)

Dependencies: Constants, Metadata

"""
# import libraries
import asyncio
import re

# import discord
import discord
import logging
from discord import Forbidden
from discord.ext import commands

# import constants
from ptn.colorbot._metadata import __version__
from ptn.colorbot.constants import bot_guild, channel_botdev, channel_botspam, EMBED_COLOUR_OK




"""
Bot object
"""


# define bot object
class ColorBot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.none()
        intents.guilds = True
        intents.members = True
        intents.messages = True

        super().__init__(command_prefix=commands.when_mentioned_or('🌈'), intents=intents, chunk_guilds_at_startup=False)

    async def on_ready(self):
        try:
            # TODO: this should be moved to an on_setup hook
            logging.info(f'{bot.user.name} version: {__version__} has connected to Discord!')
            # TODO: I don't know why "devchannel = await get_channel(channel_botdev())" doesn't work here, but
            #  it don't and this does.
            guild = await bot.fetch_guild(bot_guild())
            devchannel = await guild.fetch_channel(channel_botdev())

            embed = discord.Embed(
                title="🌈 COLORBOT ONLINE (on_ready)",
                description=f"🌈<@{bot.user.id}> connected, version **{__version__}**.",
                color=EMBED_COLOUR_OK
            )
            await devchannel.send(embed=embed)

        except Exception as e:
            logging.exception(e)

    async def on_disconnect(self):
        logging.warning(f'🔌colorbot has disconnected from discord server, version: {__version__}.')


bot = ColorBot()