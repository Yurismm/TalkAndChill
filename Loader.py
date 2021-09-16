import os

from discord.ext import commands
from datetime import date
from colorama import Fore
import time

current = date.today()


class Loader:
    def __init__(self, client: commands.Bot):
        self.client = client

    def load(self, dir: str) -> None:
        for file in os.listdir(dir):
            if file.endswith(".py"):
                try:
                    self.client.load_extension(f"{dir.replace('/', '.')}.{file[:-3]}")
                    print((current.strftime("%d.%m.%y - ")) + time.strftime("%H:%M:%S ") +
                          Fore.WHITE + "[" + Fore.LIGHTGREEN_EX + "EXTENSION" + Fore.WHITE + "] " + Fore.WHITE + f"{file} loaded successfully")
                except Exception as e:
                    print((current.strftime("%d.%m.%y - ")) + time.strftime("%H:%M:%S ") +
                          Fore.WHITE + "[" + Fore.LIGHTRED_EX + "EXTENSION" + Fore.WHITE + "] " + "Error detected at" + Fore.RED + f" {file}: {e}" + Fore.WHITE)
