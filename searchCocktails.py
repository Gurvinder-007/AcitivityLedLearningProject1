def cocktail_summary(arg):
    cocktailDefinition = wikipedia.summary(arg, sentences=3, chars=1000,
    auto_suggest=True, redirect=True)
    return cocktailDefinition

Bartenders_Bible='https://static.wikia.nocookie.net/simpsons/images/1/1b/The_Bartender%27s_Bible.png/revision/latest/scale-to-width-down/350?cb=20130722194420'

@client.event
async def on_message(message):
    words = message.content.split()
    important_words = words[1:]

    if message.content.startswith('!Hey Moe I need information on the cocktail'):
        words = message.content.split("!Hey Moe I need information on the ")
        important_words = words[1:]
        search = discord.Embed(title='Well according to the bartender''s bible this is what your looking for and well, if you aint so sure what it aint, how about tellin'' us what it am?', description=cocktail_summary(important_words), colour=discord.Colour.blue())
        await message.channel.send(Bartenders_Bible)
        await message.channel.send(content=None, embed=search)
        
    
    await client.process_commands(message)