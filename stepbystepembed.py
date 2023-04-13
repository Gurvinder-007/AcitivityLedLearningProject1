#myself i never did embed in python so i just used https://stackoverflow.com/questions/44862112/how-can-i-send-an-embed-via-my-discord-bot-w-python to check the embed example
#also i use here similar technique from my prankcalls.py file for triggering the response from the bot. this one just uses aliases so i do not have to write a lot of if statements
#user must give the cocktail name in order for the feature to show the 
#
#firstlist=["Mojito", "Hot Shot"]
#secondlist=["MojitoSBS", "HotShotSBS"]
#def simplemenu(abcde):
#    fkgh=0
#    if abcde=="menu":
#        print("Our Menu")
#        while fkgh<len(firstlist):
#            print(firstlist[fkgh])
#            print("Type "+secondlist[fkgh]+" for step by step recipe")
#            fkgh=fkgh+1
#
#
#def stepbystep(abcde):
#    if abcde=="MojitoSBS":
#        print(firstlist[0])
#        print("      ")
#        print("Recipe")
#        print("1.Sprite")
#        print("2.Vodka")
#    if abcde=="HotShotSBS":
#        print(firstlist[1])
#        print("      ")
#        print("Recipe")
#        print("1.Tequilla")
#        print("2.Whiskey")
#        
#abcde=input("input either menu or a cocktail name adding SBS for step by step recipe from menu")
#if abcde=="menu":
#    simplemenu(abcde)
#else:
#    stepbystep(abcde)
#
# (this is what exactly the code does)
# ### TESTED IN CODIO - WORKS###
# ###THIS IS EXACTLY WHAT MY CODE DOES, IT USES LISTS, PROOF CODE SHOWS LISTS, IF STATEMENTS, BUT I USE IF STATEMENTS BECAUSE THATS HOW IT TRIGGERS THE FUNCTIONS IN MY PROOF CODE, IN DISCORD CODE IT USES ALIASES IN ORDER IT TO BE TRIGGERED###
# ### LINES ABOVE IS PROOF CODE THAT I CAN DO LISTS IN PYTHON, THE LIST NAMES OR FUNCTION NAMES MAY BE DIFFERENT AS IT IS A PROOF CODE###
# ### THIS PROOF CODE SHOULD BE ENOUGH AS PROOF CODE ###
#
#
# ###---THIS IS FEATURE CODE WHICH IS INTEGRATED TO THE DISCORD BOT BY MY COURSEMATE GURVINDER NAGRA---###
# cocktail names from Ivan Madzharov, recipes for them - came up with them by myself
myListX=["Inferno Extreme", "Flaming Moe", "Balkan Power", "Multi Flavour Smash", "Honey Moon", "AK-47", "Unreal Feeling", "Car Mechanic Cocktail", "A Song Maybe"]
myListZ=["InfernoExtremeSBS", "FlamingMoeSBS", "BalkanPowerSBS", "MultiFlavourSmashSBS", "HoneyMoonSBS", "AK-47SBS", "UnrealFeelingSBS", "CarMechanicCocktailSBS", "ASongMaybeSBS"]
@client.command(aliases=["menu"])#by me already learned this from randomcocktail.py
async def ourmenu(ctx):#by me
    akh=len(myListX)#by me
    akda=0#by me
    eembed=discord.Embed(title="Our menu for special cocktails:cocktail:", description="Just read the list below", colour=discord.Colour.blue()) #used tutorial, mentioned in 1st line
    while akda<akh: #by me
        eembed.add_field(name=myListX[akda], value="Message "+myListZ[akda]+" for the Step By Step recipe", inline=False) #used tutorial for the embed itself, mentioned in 1st line
        akda=akda+1 #by me
    await ctx.send(embed=eembed) #tutorial from 1st line
#everything below by me based on the tutorial, but i was not looking at the tutorial, i was writing code, except some error corrections, refer to comments on lines
@client.command(aliases=["InfernoExtremeSBS"]) #suggested by Gurvinder Nagra to remove space from Inferno Extreme to InfernoExtreme
async def iextreme(ctx):
    a1bed=discord.Embed(title="The Step By Step Recipe Book")
    a1bed.add_field(name=myListX[0], value="This one is definitely hot, all you need is", inline=False)
    a1bed.add_field(name="Vodka", value="Pour 150ml of Vodka into the bucket", inline=False)
    a1bed.add_field(name="Tequilla", value="Add 50ml of Tequilla", inline=False)
    a1bed.add_field(name="Brandy", value="Add 25ml of Brandy", inline=False)
    a1bed.add_field(name="Gin", value="Add 15ml of Gin", inline=False)
    a1bed.add_field(name="Cranberry Juice", value="Add 250ml of Cranberry juice", inline=False)
    a1bed.add_field(name=":fire:SET IT ON FIRE:fire:", value="Literally wait 5 minutes and then try to drink it using a straw", inline=False)
    await ctx.send(embed=a1bed)

@client.command(aliases=["FlamingMoeSBS"])
async def flamoe(ctx):
    a2bed=discord.Embed(title="The Step By Step Recipe Book")
    a2bed.add_field(name=myListX[1], value="This one will just eat your throat, why not", inline=False)
    a2bed.add_field(name="Vodka", value="Pour 15ml of Vodka into the shaker", inline=False)
    a2bed.add_field(name="Rum", value="Add 15ml of Rum", inline=False)
    a2bed.add_field(name="Absinthe", value="Add 50ml of Absinthe", inline=False)
    a2bed.add_field(name="Palm Wine", value="Add 20ml of Palm Wine", inline=False)
    a2bed.add_field(name="Tonic Water", value="Add 150ml of Tonic Water", inline=False)
    a2bed.add_field(name="Shake it, baby", value="Close the shaker, shake as hard as you can, then pour it into shot glasses", inline=False) #there was a1bed, should be a2bed, told by Gurvinder Nagra to fix it
    await ctx.send(embed=a2bed)

@client.command(aliases=["BalkanPowerSBS"])
async def balkpower(ctx):
    a3bed=discord.Embed(title="The Step By Step Recipe Book")
    a3bed.add_field(name=myListX[2], value="You will probably start speaking different languages after this one", inline=False)
    a3bed.add_field(name="Fruit Beer", value="Pour 25ml of Fruit Beer into the glass", inline=False)
    a3bed.add_field(name="Tequilla", value="Add 40ml of Tequilla", inline=False)
    a3bed.add_field(name="Sonti", value="Add 15ml of Sonti", inline=False)
    a3bed.add_field(name="Tepache", value="Add 25ml of Tepache", inline=False)
    a3bed.add_field(name="Cognac", value="Add 75ml of Cognac", inline=False)
    a3bed.add_field(name="CHUG IT STRAIGHT FROM THE GLASS", value="YOU UNDERSTOOD WHAT DOES IT SAY", inline=False)
    await ctx.send(embed=a3bed)

@client.command(aliases=["MultiFlavourSmashSBS"])
async def mulflasmash(ctx):
    a4bed=discord.Embed(title="The Step By Step Recipe Book")
    a4bed.add_field(name=myListX[3], value="Tasty one", inline=False)
    a4bed.add_field(name="Vodka", value="Pour 25ml of Vodka into the glass", inline=False)
    a4bed.add_field(name="Lemon Juice", value="Add 5ml of Lemon Juice", inline=False)
    a4bed.add_field(name="Orange Juice", value="Add 45ml of Orange Juice", inline=False)
    a4bed.add_field(name="Apple Juice", value="Add 50ml of Apple Juice", inline=False)
    a4bed.add_field(name="Just drink it", value="No need to shake it or set it on fire, just do what you have to - DRINK IT", inline=False)
    await ctx.send(embed=a4bed)

@client.command(aliases=["HoneyMoonSBS"])
async def honmoon(ctx):
    a5bed=discord.Embed(title="The Step By Step Recipe Book")
    a5bed.add_field(name=myListX[4], value="You may puke from this one, but you will truly see the moon", inline=False)
    a5bed.add_field(name="Absinthe", value="Pour 150ml of Absinthe into the glass", inline=False)
    a5bed.add_field(name="Vodka", value="Add 50ml of Vodka", inline=False)
    a5bed.add_field(name="Potato", value="Add one slice of Potato", inline=False)
    a5bed.add_field(name="Pure Honey", value="Add one teaspoon of Pure Honey", inline=False)
    a5bed.add_field(name="Cranberry Juice", value="Add 250ml of Cranberry juice", inline=False)
    a5bed.add_field(name="STIR IT AND THEN DRINK IT", value="You need to stir it with the spoon in order the honey to spread around the glass, then just drink it. See you in the moon sir.", inline=False)
    await ctx.send(embed=a5bed) #there was a bad indent, suggested by Gurvinder Nagra

@client.command(aliases=["AK-47SBS"])
async def ak47C(ctx):
    a6bed=discord.Embed(title="The Step By Step Recipe Book")
    a6bed.add_field(name=myListX[5], value="PEW PEW PEW", inline=False)
    a6bed.add_field(name="Vodka", value="Pour 15ml of Vodka into the glass", inline=False)
    a6bed.add_field(name="Tequilla", value="Add 50ml of Tequilla", inline=False)
    a6bed.add_field(name="Mamajuana", value="Add 15ml of Mamajuana", inline=False)
    a6bed.add_field(name="Orange Juice", value="Add 100ml of Orange Juice", inline=False)
    a6bed.add_field(name="DRINK IT", value="This one is not a weapon, this cocktail is meant to be consumed", inline=False)
    await ctx.send(embed=a6bed)

@client.command(aliases=["UnrealFeelingSBS"])
async def unrfeeling(ctx):
    a7bed=discord.Embed(title="The Step By Step Recipe Book")
    a7bed.add_field(name=myListX[6], value="The unreal feeling is that you don't feel the alchohol at all", inline=False)
    a7bed.add_field(name="Pink Gin", value="Pour 25ml of Pink Gin into the glass", inline=False)
    a7bed.add_field(name="Sparkling Mineral Water", value="Add 75ml of Sparkling Mineral Water", inline=False)
    a7bed.add_field(name="Raspberry juice", value="Add 150ml of Raspberry juice", inline=False)
    a7bed.add_field(name="You deserve it", value="Enjoy the sweet taste of raspberry, you could drink 7 of these", inline=False)
    await ctx.send(embed=a7bed)

@client.command(aliases=["CarMechanicCocktailSBS"])
async def cmcocktailZ(ctx):
    a8bed=discord.Embed(title="The Step By Step Recipe Book")
    a8bed.add_field(name=myListX[7], value="Hard work is done, time to get wasted", inline=False)
    a8bed.add_field(name="Awamori", value="Pour 20ml of Awamori into the glass", inline=False)
    a8bed.add_field(name="London Dry Gin", value="Add 20ml of London Dry Gin", inline=False)
    a8bed.add_field(name="Palinka", value="Add 5ml of Palinka", inline=False)
    a8bed.add_field(name="Samohon", value="Add 5ml of Samohon", inline=False)
    a8bed.add_field(name="Arrack", value="Add 5ml of Arrack", inline=False)
    a8bed.add_field(name="Ice", value="Add 2 cubes of Ice", inline=False)
    a8bed.add_field(name="Apple Juice", value="Fill up the rest of glass with Apple Juice", inline=False)
    a8bed.add_field(name="Forget your problems", value="But you still have 3 cars to fix in your garage", inline=False)
    await ctx.send(embed=a8bed)

@client.command(aliases=["ASongMaybeSBS"])
async def asongmayz(ctx):
    a9bed=discord.Embed(title="The Step By Step Recipe Book")
    a9bed.add_field(name=myListX[8], value="This one is very light", inline=False)
    a9bed.add_field(name="Vodka", value="Pour 15ml of Vodka into the glass", inline=False)
    a9bed.add_field(name="Beer", value="Fill up the rest of the glass with glass", inline=False)
    a9bed.add_field(name="Now you are ready to request a song to play", value="I prefer you to choose What A Wonderful World by Louis Armstrong, but it is up to you", inline=False)
    await ctx.send(embed=a9bed)
