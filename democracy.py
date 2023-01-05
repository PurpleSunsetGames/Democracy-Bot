import os

import discord
from discord import app_commands
from dotenv import load_dotenv
from pathlib import Path

GUILD_ID = 1054879203637612544
load_dotenv(Path(str(os.getcwd()) + "\\token.env"))


class MyClient(discord.Client):
    async def on_ready(self):
        await tree.sync(guild=discord.Object(id=GUILD_ID))
        print("Ready!")


intents = discord.Intents.all()
client = MyClient(intents=intents)
tree = app_commands.CommandTree(client)


# Commands


@tree.command(name="ping", description="Test command to ping the bot", guild=discord.Object(id=GUILD_ID))
async def test(self: discord.Interaction):
    await self.response.send_message(f'Pong!')


# Command Structure
# ~~~~~~~~~~~~~~~~~~~
# motion
# |
# | - server
# |
# | - rule
# |
# | - channel
# |   |
# |   | - message
# |
# | - user
# |
# | - role
# |
# | - bot
# |
async def create_motion(category, action, data):
    motion_channel = client.get_channel(1054913273448890408)
    motion_string = f'Category: {category}\nAction: {action}\n'
    for i in data:
        motion_string += f'{i}: {data[i]}\n'

    motion_message = await motion_channel.send(motion_string)
    await motion_message.add_reaction("👍")
    await motion_message.add_reaction("👎")
    pass


motion_group = app_commands.Group(name="motion", description="Create a motion for a moderator action")
tree.add_command(motion_group, guild=discord.Object(id=GUILD_ID))

server_group = app_commands.Group(name="server", description="Commands relating to the server settings")
motion_group.add_command(server_group)


@server_group.command(name="test", description="test")
async def server_test(self: discord.Interaction):
    await create_motion("server", "test", {"Test": "test"})
    await self.response.send_message(f'Motion Created!')


@server_group.command(name="test2", description="test")
async def server_test2(self: discord.Interaction):
    await create_motion("server", "test2", {"Test": "test2"})
    await self.response.send_message(f'Motion Created!')


client.run(os.getenv('BOTTOKEN'))
