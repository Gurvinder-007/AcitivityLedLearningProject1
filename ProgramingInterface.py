#Pipinstall discord.py
#Pipinstall wikipidea
import discord
import wikipidea
from discord.ext import commands
import asyncio
import os
import datatime
import random
from random import randint
from discord.ext.commands import Bot

client = commands.Bot(commands_prefix = "!")

@client.event
async def on_ready():
    print("Moe is online!")

 @client.command(aliases=['Help'])
async def _HeyMoeIgotaproblem(ctx):
  myEmbed = discord.Embed(title="What's the matter?", description="Your help, enjoy it and dont expect me to be using any of that fancy grammar and puncuation I can't afford that no more", colour=discord.Colour.blue())
  myEmbed.add_field(name="Number 1:", value="This is 1", inline=True)
  myEmbed.add_field(name="!Random ", value="This command will cause me to just give you the first cocktail I lay eyes on and no refunds", inline=True)
  myEmbed.add_field(name="!Hey Moe I need information on the cocktail", value="Do this and ill consult the bartender's bible for a cocktail but if you don`t get something the first time dont expect a second time.", inline=True)
  myEmbed.add_field(name="!LoveTester", value="This command will let you use my love tester for 5 bucks and no refunds you cheapskate.", inline=True)
  myEmbed.add_field(name="Number 1:", value="This is 1", inline=True)


client.run("xOXY60vj8w8T5gb0tWH0bMVKiEJ2jwYY")