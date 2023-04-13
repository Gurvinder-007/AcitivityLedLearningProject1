@client.command(aliases=['normallist'])
async def _normallist(ctx):
    nlistEmbed = discord.Embed(title="Flavours menu", description="Types of flavours that are in the cocktails, depending on your choice I will show you cocktails with that flavour in it! :cocktail: ", colour=discord.Colour.purple())
    nlistEmbed.add_field(name="**Selection:**", value='Mint, Lemon, Lime, Cranberry, Orange', inline=True)
    nlistEmbed.add_field(name="Last updated", value="21.11.2020", inline=True)
    await ctx.send(embed=nlistEmbed)