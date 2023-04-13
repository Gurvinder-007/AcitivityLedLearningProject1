import discord
import random
import asyncio


from discord.ext import commands

async def change():
    await client.wait_until_ready()

    statuslist = ['gaming','making cocktails','trying to make a cocktail','Help for help menu']

    while not client.is_closed():
        status = random.choice(statuslist)
        await client.change_presence(activity=discord.Game(name=status))

        await asyncio.sleep(5)

client.loop.create_task(change())

client.run()