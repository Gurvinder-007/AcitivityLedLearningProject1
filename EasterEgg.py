import discord
import random


from discord.ext import commands

client = commands.Bot(command_prefix="h!")

@client.event
async def on_ready():
    print('Moe has connected to Discord!')

@client.command(aliases=['list'])
async def _list(ctx):
    listEmbed = discord.Embed(title="Alcohol menu", description="Types of alcohol that I can offer you, depending on your choice I will show you cocktails with this type of alcohol in it! :cocktail: ", colour=discord.Colour.purple())
    listEmbed.add_field(name="**Selection:**", value='```Whiskey, Vodka, Gin, Rum, Tequila, Liqueur, Brandy, Bourbon.``` *To check the recipe for a cocktail, type h!<cocktail name> (you can type only the first letters e.g Is this even real? cocktail **h!iter**)', inline=True)
    listEmbed.add_field(name="Last updated", value="08.11.2020", inline=True)
    await ctx.send(embed=listEmbed)

@client.command(aliases=['flamingmoe','Flaming moe', 'Flaming Moe','FlamingMoe','fm'])
async def _flamingmoe(ctx):
    fmEmbed = discord.Embed(title="Flaming Moe", description="Stronger than dragon`s breath", colour=discord.Colour.red())
    fmEmbed.add_field(name="**Recipe: :pencil: **", value='To make this cocktail you have to combine every single other type of alcohol in a bucket, after that you must set the bucket on fire. After 5 five minutes get the liquid and combine it with watermellon juice, sugar , salt , antifreeze. Put it in the freezer for 12h. After the 12h the cocktail is ready.', inline=True)
    fmEmbed.add_field(name="Do not try it at home!", value="Please do not try it", inline=True)
    await ctx.send(embed=fmEmbed)

@client.command(aliases=['Inferno extreme','ie','Inferno Extreme','Infernoextreme','infernoextreme'])
async def _ie(ctx):
    ieEmbed = discord.Embed(title="Inferno Extreme", description="It is extreme and inferno at the same time, what else you need?", colour=discord.Colour.orange())
    ieEmbed.add_field(name="**Recipe: :pencil: **", value='To make this cocktail you have to add 4 bottles of vodka in a bucket, mix it with engine oil and add fuel. If you want to be even cooler, you can add and a glass of coffee.', inline=True)
    ieEmbed.add_field(name="Do not try it at home!", value="Please do not try it", inline=True)
    await ctx.send(embed=ieEmbed)

@client.command(aliases=['Multi Flavour Smash','mfs','MultiFlavourSmash','multiflavoursmash',])
async def _mfs(ctx):
    mfsEmbed = discord.Embed(title="Multi Flavour Smash", description="It has a lot of flavours, maybe smashed.", colour=discord.Colour.magenta())
    mfsEmbed.add_field(name="**Recipe: :pencil: **", value='There is not exact recipe, but I can help you create your own one. This cocktail is super easy to make. Firsly take every single fruit that u have, put them in a mixer add tequila, done. ', inline=True)
    mfsEmbed.add_field(name="Do not try it at home!", value="Please do not try it", inline=True)
    await ctx.send(embed=mfsEmbed)

@client.command(aliases=['balkanpower','Balkan Power','bp'])
async def _BalkanPower(ctx):
    bpEmbed = discord.Embed(title="Balkan Power", description="?@?$?@?$@?$?@", colour=discord.Colour.blurple())
    bpEmbed.add_field(name="**Recipe: :pencil: **", value='Get a bucket put every cocktail in it, go to the balkans. Done. Simple? Maybe.', inline=True)
    bpEmbed.add_field(name="Do not try it at home!", value="Please do not try it, like for real don't try it", inline=True)
    await ctx.send(embed=bpEmbed)

@client.command(aliases=['Honey moon','hm','Honeymoon'])
async def _HoneyMoon(ctx):
    hmEmbed = discord.Embed(title="Honey Moon", description="Neither has honey , neither moon", colour=discord.Colour.teal())
    hmEmbed.add_field(name="**Recipe: :pencil: **", value='Fill a container 1/5 with orange juice , 1/5 with coca cola, 1/5 illegal ingredients, 1/5 tobacco, 1/5 Liqueur. Mix for half an hour.', inline=True)
    hmEmbed.add_field(name="Do not try it at home!", value="Please do not try it", inline=True)
    await ctx.send(embed=hmEmbed)

@client.command(aliases=['AK-47','ak-47','ak47'])
async def _ak47(ctx):
    akEmbed = discord.Embed(title="AK-47", description="Strangly it is not a weapon", colour=discord.Colour.red())
    akEmbed.add_field(name="**Recipe: :pencil: **", value='Fill a container 1/5 with gin, 1/5 with brady, 1/5 with whisky, 1/5 with bourbon, 1/5 with ice :ice_cube: ...o no wait um, bot error I meant magma.', inline=True)
    akEmbed.add_field(name="Do not try it at home!", value="I mean you can try it who am I to stop you.", inline=True)
    await ctx.send(embed=akEmbed)

@client.command(aliases=['Is this even real?','iter','isthisevenreal','is this even real?'])
async def _istr(ctx):
    irEmbed = discord.Embed(title="Is this even real?", description="If you are reading this you found an easteregg", colour=discord.Colour.red())
    irEmbed.add_field(name="**Recipe: :pencil: **", value='Is this even real?Is this even real?Is this even real?Is this even real?Is this even real?Is this even real?Is this even real?Is this even real?Is this even real?', inline=True)
    irEmbed.add_field(name="Do not Is this even real?", value="Is this even real?.", inline=True)
    await ctx.send(embed=irEmbed)

@client.command(aliases=['Unreal feeling','Unrealfeeling','uf'])
async def _uf(ctx):
    ufEmbed = discord.Embed(title="Unreal feeling", description="How do you actually feel it if it is unreal?", colour=discord.Colour.purple())
    ufEmbed.add_field(name="**Recipe: :pencil: **", value='1/2 Brandy, 0,5/2 Lemon juice, 0,3543635/2 sugar, 0.324522353432432/2 coffe mixed with milk, 3/2 ice ice baby, 1/2 onions', inline=True)
    ufEmbed.add_field(name="It keeps the girls away", value="wait... no no the oposite...what if?", inline=True)
    await ctx.send(embed=ufEmbed)

@client.command(aliases=['Car Mechanic Cocktail','CarMechanicCocktail','Carmechaniccocktail','cmc'])
async def _cmc(ctx):
    cmcEmbed = discord.Embed(title="Car Mechanic Cocktail", description="I am not completely sure why are you asking a Discord-Bot to give you a recipe for a cocktail that is called Car Mechanic Cocktail... but here we go I will come up with soemthing!", colour=discord.Colour.purple())
    cmcEmbed.add_field(name="**Recipe: :pencil: **", value='Whiskey like um? a Bottle? maybe a tire, oil? gas? lets end it here it should be good like this.', inline=True)
    cmcEmbed.add_field(name="Do not try it please", value="*Try it*", inline=True)
    await ctx.send(embed=cmcEmbed)

@client.command(aliases=['A song maybe','asm','asongmaybe'])
async def _asm(ctx):
    asmEmbed = discord.Embed(title="A song maybe", description="The discription was not added because me(The bot) can not sing.", colour=discord.Colour.purple())
    asmEmbed.add_field(name="**Recipe: :pencil: **", value='This is quite easy to make, you need bourbon just like in the lyrics of that famous rap song, guitar strings, bake it for 30 minuntes, not 29:59 not 30:01 not 29:61 but 30minutes. Mix it with a button from a keyboard and I believe it should be good. p.s I am only a discord bot not a barman', inline=True)
    asmEmbed.add_field(name="Try it", value="*no do not*", inline=True)
    await ctx.send(embed=asmEmbed)


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    has_vodka =  ['Inferno extreme','Flaming Moe','Balkan Power']
    has_tequila = ['Multi Flavour Smash','Flaming Moe','Balkan Power']
    has_liqueur = ['Flaming Moe','Honey moon','Balkan Power']
    has_rum = ['Real man`s cocktail','Flaming Moe','Balkan Power']
    has_gin = ['AK-47','Flaming Moe','Is this even real?','Balkan Power']
    has_brandy = ['AK-47','Flaming Moe','Unreal feeling']
    has_whiskey = ['Car Mechanic Cocktail, AK-47','Flaming Moe','Balkan Power']
    has_bourbon = ['AK-47','Flaming Moe','A song maybe','Balkan Power']

        
    
    if message.content == 'h!vodka':
        response = has_vodka
        await message.channel.send(random.choice(response))
    elif message.content == 'h!tequilla':
        response = has_tequila
        await message.channel.send(random.choice(response))
    elif message.content == 'h!liqueur':
        response = has_liqueur
        await message.channel.send(random.choice(response))
    elif message.content == 'h!rum':
        response = has_rum
        await message.channel.send(random.choice(response))
    elif message.content == 'h!gin':
        response = has_gin
        await message.channel.send(random.choice(response))
    elif message.content == 'h!brandy':
        response = has_brandy
        await message.channel.send(random.choice(response))
    elif message.content == 'h!whiskey':
        response = has_whiskey
        await message.channel.send(random.choice(response))
    elif message.content == 'h!bourbon':
        response = has_bourbon
        await message.channel.send(random.choice(response))                            
      

    await client.process_commands(message)

client.run("TOKEN")
