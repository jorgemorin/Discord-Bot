import discord
from discord.ext import commands
from typing import Optional

class DiscordBot:
    def __init__(self, token: str):
        self.token = token
        self.bot = commands.Bot(
            command_prefix="!",
            intents=discord.Intents.default()
        )
        
        @self.bot.event
        async def on_ready():
            print(f"Bot connected as {self.bot.user}")

    async def send_message(self, channel_id: int, text: str):
        channel = self.bot.get_channel(channel_id)
        if channel:
            await channel.send(text)
            return True
        return False

    async def start(self):
        await self.bot.start(self.token)

    async def close(self):
        await self.bot.close()