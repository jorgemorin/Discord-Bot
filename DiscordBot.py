import discord
import asyncio
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

    async def start(self):
        await self.bot.start(self.token)
    async def close(self):
        await self.bot.close()

    async def send_message(self, channel_id: int, text: str):
        channel = self.bot.get_channel(channel_id)
        if channel:
            await channel.send(text)
            return True
        return False

    async def send_poll(self, channel_id: int, question: str, timeout: Optional[int] = None) -> Optional[bool]:
        channel = self.bot.get_channel(channel_id)
        
        # Emojis unicode for reaction
        true_emoji = '\U00002705'
        false_emoji = '\U0000274C'

        if channel:
            try:
                message = await channel.send(question)
                await message.add_reaction(true_emoji)
                await message.add_reaction(false_emoji)

                start_time = asyncio.get_event_loop().time()

                while True:
                    await asyncio.sleep(1)

                    message = await channel.fetch_message(message.id)

                    reactions = message.reactions
                    true_count = sum(reaction.count for reaction in reactions if str(reaction.emoji) == true_emoji)
                    false_count = sum(reaction.count for reaction in reactions if str(reaction.emoji) == false_emoji)
                    if true_count > false_count:
                        return True
                    elif false_count > true_count:
                        return False

                    if timeout:
                        elapsed = asyncio.get_event_loop().time() - start_time
                        if elapsed > timeout:
                            await message.reply("Poll timed out.")
                            return None
            except Exception as e:
                print(f"An error occurred: {e}")
                return None
