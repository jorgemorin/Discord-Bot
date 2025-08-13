# Discord Bot (v1.0)

A Python-based Discord bot manager that simplifies bot creation and management with easy-to-use methods for common Discord operations.

## Features

- Simple message sending
- Rich embed messages
- Interactive polls with timeout
- Easy bot initialization and management
- Asynchronous operation support

## Installation

1. Install Python 3.8 or higher
2. Install required packages:
   ```
   pip install discord.py asyncio
   ```
   
## Usage
```
import asyncio
from DiscordBot import DiscordBot

TOKEN = "your_bot_token_here"
CHANNEL_ID = 1234567890123456  # Your channel ID here

async def main():
  bot = DiscordBot(TOKEN)

  bot_task = asyncio.create_task(bot.start())
  await asyncio.sleep(5)  # Wait for connection

  # Example usage
  await bot.send_message(CHANNEL_ID, "Hello, Discord!")
  await bot.send_embed(CHANNEL_ID, "Embed Title", "Embed Description")
  await bot.send_poll(CHANNEL_ID, "Poll Title", "Poll Description", timeout=30)

if __name__ == "__main__":
  asyncio.run(main())
```
* Getting your Bot Token
  1. Go to Discord Developer Portal: https://discord.com/developers/applications
  2. Click "New Application" and name your Bot
  3. Go to "Bot" in the left sidebar
  4. Click "Add Bot" > "Yes, do it!"
  5. Under "TOKEN", click "Copy" (THIS IS YOUR BOT TOKEN - KEEP IT SECRET)
* Getting the Channel Id
  1. Open Discord and go to your server
  2. Right-Click the text channel you want the bot to use
  3. Select "Copy Channel ID" (If you don't see this option):
     - Go to User Settings > Appearance
     - Enable "Developer Mode"
     - Try right-clicking the channel again
* Inviting your Bot to your Server
  1. In Developer Portal, got to "OAuth2" > "URL Generator"
  2. Select these scopes:
     - bot
     - applications.commands
  3. Select these bot permissions:
     - Send Messages
     - Embed Links
     - Add Reactions
     - Read Message History
  4. Copy the generated URL and open it in your browser
  5. Select your server and click "Authorize"

# Requirements
- Python 3.8+
- discord.py
- asyncio

# License
This project is open source and available under the MIT License
