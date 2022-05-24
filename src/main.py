#!/bin/env python3

# Salamander is a generic discord bot writen with the sole purpose of being entirely modular
# and a better, more robust alternative to other largely used bots such as Dyno or Carl.
# Salamander is meant to be self-hosted, because we believe putting the user in control of every
# aspect, including the actual source code, is not only beneficial to knowledgeable users,
# but also the end users they are serving.

# Salamander is written in Python 3.10 and licensed under the GPL v3. Please see LICENSE and
# README.md for more information

import discord
from discord.ext import commands
import os
import sys
from config import *

client = commands.Bot(command_prefix=prefix)

modules = []
for filename in os.listdir('./src/mods'):
    if filename.endswith('.py'):
        modules.append(f'{filename[:-3]}')
        print(f'Found module with filename {filename}! Module will not be loaded if not added to configuration!')

print(f'Registered modules into list {modules}')

if loadmods[0] != 'core':
    sys.exit('Core module not found, program exiting! Are you sure it\'s the first module in the config?')

for mod in modules:
    if mod in loadmods:
        print(f'Module present in config, loading {mod}!')
        client.load_extension(f'mods.{mod}')

client.run(token)
