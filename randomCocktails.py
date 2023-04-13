# cocktail list from https://en.wikipedia.org/wiki/List_of_cocktails
# used discord.py documentation to convert it it into suitable for discord
# random.choice() from https://pynative.com/python-random-choice/
# written using python3
# 
#
#import random
#def randomCocktail():
#    abcd=['Vodka+redbull', 
#    'Pink gin+Ice+Schweppes+Lemon',
#    'Black and Tan',
#    'Black Velvet',
#    'Boilermaker',
#    'Hangmans Blood',
#    'Irish Car Bomb']
#       
#    rabcd=['and no refunds!',
#    'I hope you enjoy',
#    'might be your lucky day',
#    'well this might be your thing it might not be we will see',
#    'you know what its on the house for once, but do not you ever tell no one about this or I will slice your throat open' ]
#    svd=random.choice(abcd)
#    svd1=random.choice(rabcd)
#    return "Your random cocktail is "+random.choice(abcd)+" "+random.choice(rabcd)
#abc=input('user must write hey moe give me a random cocktail')
#if abc=="hey moe give me a random cocktail":
#    print (randomCocktail())
#else:
#    pass
# ### TESTED IN CODIO - WORKS###
# ###THIS IS EXACTLY WHAT MY CODE DOES, IT USES LISTS, PROOF CODE SHOWS LISTS###
# ### LINES ABOVE IS PROOF CODE THAT I CAN DO LISTS IN PYTHON, THE LIST NAMES OR FUNCTION NAMES MAY BE DIFFERENT AS IT IS A PROOF CODE###
# ### THIS PROOF CODE SHOULD BE ENOUGH AS PROOF CODE ###
#
#
# ###---THIS IS FEATURE CODE WHICH IS INTEGRATED TO THE DISCORD BOT BY MY COURSEMATE GURVINDER NAGRA---###
@client.command(aliases=['hey moe give me a random cocktail']) #@client.command from internet https://discordpy.readthedocs.io/en/latest/ext/commands/commands.html giving a command name according to documentation https://discordpy.readthedocs.io/en/latest/ext/commands/api.html?highlight=aliases#discord.ext.commands.Command.aliases
async def randomCocktail(ctx): # defining a function https://discordpy.readthedocs.io/en/latest/ext/commands/commands.html
    llist1=['Vodka+redbull', #making a list, learned in 4000cem
    'Pink gin+Ice+Schweppes+Lemon',
    'Black and Tan',
    'Black Velvet',
    'Boilermaker',
    'Hangmans Blood',
    'Irish Car Bomb',
    'Michelada',
    'Porchcrawler',
    'Queen Mary',
    'Sake Bomb',
    'Shandy',
    'Snakebite',
    'U-Boot',
    'B & B',
    'The Blenheim',
    'Blow my Skull Off',
    'Brandy Alexander',
    'Brandy Manhattan',
    'Brandy Sour (Cyprus)',
    'Brandy Sour/Brandy Daisy',
    'Chicago Cocktail',
    'Curacao Punch',
    'Diki-Diki',
    'Four Score',
    'French Connection',
    'Hennchata',
    'Horses Neck',
    'Incredible Hulk',
    'Jack Rose',
    'Panama',
    'Paradise',
    'Porto flip',
    'Savoy Affair',
    'Savoy Corpse Reviver',
    'Sazerac',
    'Sidecar',
    'Singapore Sling',
    'Stinger',
    '20th Century',
    'Alexander',
    'Angel Face',
    'Aviation',
    'Bees Knees',
    'Bijou',
    'Blackthorn',
    'Bloody Margaret',
    'Bramble',
    'Breakfast martini',
    'Bronx',
    'Casino',
    'Cloister',
    'Clover Club Cocktail',
    'Cooperstown Cocktail',
    'Corpse Reviver',
    'Damn the Weather',
    'Derby',
    'French',
    'Gibson',
    'Gimlet',
    'Gin and tonic',
    'Gin Fizz',
    'Gin pahit',
    'Gin sour',
    'Greyhound',
    'John Collins',
    'The Last Word',
    'Lime Rickey',
    'Long Island Iced Tea',
    'Lorraine',
    'Martini',
    'Mickey Slim',
    'Monkey Gland',
    'My Fair Lady',
    'Negroni',
    'Old Etonian',
    'Paradise',
    'Pegu',
    'Pimms Cup',
    'Pink Gin',
    'Cojito',
    'Cremat',
    'Cuba Libre',
    'Cuban Sunset',
    'Daiquiri',
    'Dark N Stormy',
    'El Presidente',
    'Fish House Punch',
    'Flaming Doctor Pepper',
    'Flaming volcano',
    'Fluffy Critter',
    'Grog',
    'Gunfire',
    'Hot buttered rum',
    'Hurricane',
    'Jagertee',
    'Jungle Bird',
    'Long Island Iced Tea',
    'Macuá',
    'Mai Tai',
    'Mojito',
    'Mr. Bali Hai',
    'Painkiller',
    'Piña colada',
    'Planters Punch',
    'Q.B. Cooler',
    'Royal Bermuda Cocktail',
    'Rum Swizzle',
    'Sumatra Kula',
    'Suffering Bastard' ]

    rList=['and no refunds!', #another list
    'I hope you enjoy',
    'might be your lucky day',
    'well this might be your thing it might not be we will see',
    'you know what its on the house for once, but do not you ever tell no one about this or I will slice your throat open' ]
    await ctx.send(f'Your random cocktail is: {random.choice(llist1)}, {random.choice(rList)}') #returns random choice of cocktail, and a random response just to make bot look like a hunman, refer to 3rd line