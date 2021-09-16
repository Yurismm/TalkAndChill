from discord.ext import commands
from discord import Intents
from Loader import Loader
import os
import json

os.system("clear")
with open("config.json", "r") as jsonfile:
    data = json.load(jsonfile)
    prefix = data["prefix"]
    token = data["token"]
config = json.load(open("config.json"))
client = commands.Bot(command_prefix=prefix, intents=Intents.all())
client.prefix = prefix

loader = Loader(client)
loader.load("commands")
loader.load("event")
loader.load("listener")

client.run(token)
