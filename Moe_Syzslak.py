import discord
import wikipedia
import webbrowser
from discord.ext import commands
import asyncio
import os
import datetime
import random
from googlesearch import search
from random import choice
from discord.ext.commands import Bot

client = commands.Bot(command_prefix='')

TOKEN = 'NzcxMzE0MDk3MDg5MTUxMDA4.X5qUOw.vowBBQDX-ffRdOCo22ovFMjqwxo'

@client.event
async def on_ready():
	print(f'Bot connected') 
      
async def change():
    await client.wait_until_ready()

    statuslist = ['gaming','making cocktails','trying to make a cocktail','Help for help menu']

    while not client.is_closed():
        status = random.choice(statuslist)
        await client.change_presence(activity=discord.Game(name=status))

        await asyncio.sleep(5)

client.loop.create_task(change())

@client.event
async def on_member_join(member):
    embed=discord.Embed(title="Welcome to Moe's!", description=f"{member.mention} Make sure to try our cocktails!",colour=discord.Colour.blue())
    msg = await client.send_message(discord.Object(id="774991151081848844"),embed=embed)

def cocktail_summary(arg):
    cocktailDefinition = wikipedia.summary(arg, sentences=3, chars=1000,
    auto_suggest=True, redirect=True)
    return cocktailDefinition

Bartenders_Bible='https://static.wikia.nocookie.net/simpsons/images/1/1b/The_Bartender%27s_Bible.png/revision/latest/scale-to-width-down/350?cb=20130722194420'

#http://www.simpsoncrazy.com/lists/prank-calls

@client.event
async def on_message(message): 
    if message.author == client.user:
          return

    if message.content.startswith('Hey Moe I need information on the cocktail'):
      words = message.content.split("Hey Moe I need information on the ")
      important_words = words[1:]
      Cocktailsearch = discord.Embed(title='Well according to the bartender''s bible this is what your looking for and well, if you aint so sure what it aint, how about tellin'' us what it am?', description=cocktail_summary(important_words), colour=discord.Colour.blue())
      await message.channel.send(Bartenders_Bible)
      await message.channel.send(content=None, embed=Cocktailsearch)

    if message.content.startswith('Moe do you know where I can find information on the'):
        searchContent = ""
        text = str(message.content).split(' ')
        for importantWords in range(4, len(text)):
            searchContent = searchContent + text[importantWords]

        for searchResults in search(searchContent, tld="co.in", num=1, stop=1, pause=2):
            await message.channel.send(searchResults)
            await message.channel.send("Well according to my search history this is what your looking for")

    if message.content.startswith('Show me the prank call list'):
        await message.channel.send("Enjoy your journey")
        webbrowser.open('www.simpsoncrazy.com/lists/prank-calls')

  Drinks=["Duff","Duff-lite","Duff-Ultra","Mexican-Duff","Fudd"]

    if message.content == 'Hey Moe what is on your duff Menu today?':
      Drink=True
      if Drink == True:
        for Drink in Drinks:
          await message.channel.send("Drink Available: "+ Drink)

    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    if message.content == 'Hey Moe What is your weekly schedule?':
      for day in days:
          await message.channel.send("Okay so according to the duff calendar my schedule for " + day + " is")
          if day=="Monday":
              await message.channel.send("well, hmm that means that the guys are gonna be tired, sad and looking to refresh themselves with some of Uncle Moe's Medicine")
          if day=="Tuesday":
              await message.channel.send("well, nothing interesting ever happens today ")
          if day=="Wednesday":
              await message.channel.send("that tonight Moe is closed i got some important business at the ughhh duff brewery yeah, definitely not going to read to children in hospitals")
          if day=="Thursday":
              await message.channel.send("that tonight is alley night after we get some beers we can go score some strikes and maybe I can get lucky for once")
          if day=="Friday":
              await message.channel.send("today is the day the guys come in play some pool, get so drunk they dont even know how they got home. Its gonna be good business tonight")
          if day=="Saturday":
              await message.channel.send("that tonight will be poker night maybe I can win big and get out of crappy little bar")
          if day=="Sunday":
              await message.channel.send("well, it seems people gotta spend time with their families today meanwhile I got nothing but to, to ummm, I have to ughh.... Im just gonna call someone real quick")
 

    CantUnderstandResponses = [
      'Gonna be straight with you, I dont understand a word you just said',
      'Im gonna need you to repeat that and make sure I can understand it',
      'Your speaking jibberish, I hope you know that',
      'Is everyone just using a language I dont understand to make me feel even more lonely, cause it is working effectively',
      '*Points shotgun* Listen either you talk right or you get out after buying some beer which you wont be getting after you pay',
      'Woah woah woah, slow it down not everyone here speaks all sciency like you',
      'Listen here you little punk, if I ever hear from you again im gonna slice you up into little pieces'
    ]
    
    CorrectCommands = [
      'vodka',
      'gin',
      'Hello',
      'tequilla',
      'liqueur',
      'rum',
      'brady',
      'whiskey',
      'bourbon',
      'Hey Moe lets play truth or dare',
      'Moe I choose truth',
      'Moe I choose dare',
      'Truth-',
      'Dare-',
      'I did it Moe',
      'I did not do it Moe',
      'Rules?',
      'Help',
      'Random',
      'SpecialList',
      'LoveTester',
      'Hey Moe I need information on the cocktail'
      'Is Al there?',
      'Yeah, Al. Last name Caholic?',
      'Oliver Clothesoff.',
      'Is Mister Freely there?',
      'Freely, first initials I. P.',
      'Is Jaques there?',
      'Is Seymour there? Last name Butz.',
      'Hello, is Homer there?',
      'Homer... Sexual.',
      "Don't look at me!",
      'Blood Feud',
      'Uh, hello. Is Mike there? Last name, Rotch.',
      'Treehouse of Horror II',
      "Flaming Moe's",
      "Uh, yes, I'm looking for a friend of mine. Last name Jass. First name Hugh.",
      "Uh, I'm Hugh Jass.",
      'Bart Simpson.',
      "Uh, look, I'll level with you, Mister. This is a crank call that sort of backfired, and I'd like to bail out right now.",
      'Burns Verkaufen der Kraftwerk',
      "Uh, yes, I'm looking for a Mrs. O'Problem? First name, Bea.",
      'New Kid on the Block',
      'Maybe your standards are too high!',
      'My name is Jimbo Jones, and I live at 1094 Evergreen Terrace.',
      "I'm looking for a Mr. Smithers, first name Wayland",
      "Hello, I'd like to speak with a Mr. Snotball, first name Eura",
      "I'd like to speak to a Mr. Tabooger, first name Ollie.",
      'Yell out "Ill eat a booger"',
      'Just ask if anyone knows Ollie Tabooger.',
      'menu',
      'Rules?',
      'I did it Moe',
      'I did not do it Moe',
      'InfernoExtremeSBS',
      'FlamingMoeSBS',
      'MultiFlavourSmashSBS',
      'BalkanPowerSBS',
      'HoneyMoonSBS',
      'AK-47SBS',
      'ASongMaybeSBS',
      'CarMechanicCocktailSBS',
      'UnrealFeelingSBS',
      'Unreal feeling',
      'Unrealfeeling',
      'uf',
      'Car Mechanic Cocktail',
      'CarMechanicCocktail',
      'Carmechaniccocktail',
      'cmc',
      'A song maybe',
      'asm',
      'asongmaybe',
      'Is this even real?',
      'iter',
      'isthisevenreal',
      'is this even real?',
      'AK-47',
      'ak-47',
      'ak47',
      'Honey moon',
      'hm',
      'Honeymoon',
      'balkanpower',
      'Balkan Power',
      'bp',
      'Multi Flavour Smash',
      'mfs',
      'MultiFlavourSmash',
      'multiflavoursmash',
      'Inferno extreme',
      'ie',
      'Inferno Extreme',
      'Infernoextreme',
      'infernoextreme',
      'flamingmoe',
      'Flaming moe',
      'Flaming Moe',
      'FlamingMoe',
      'fm'
    ]

    if message.content in CorrectCommands:
      pass
    elif message.content.startswith('Hey Moe I need information on the cocktail'):
      pass
    elif message.content.startswith('Show me the prank call list'):
      pass
    elif message.content.startswith('Recommendations'):
      pass
    elif message.content.startswith('Moe do you know where I can find information on the'):
      pass
    elif message.content.startswith('Truth-'):
      pass
    elif message.content.startswith('Dare-'):
      pass
    else:    
      await message.channel.send(f'{random.choice(CantUnderstandResponses)}')
    

    has_vodka =  ['Inferno extreme','Flaming Moe','Balkan Power']
    has_tequila = ['Multi Flavour Smash','Flaming Moe','Balkan Power']
    has_liqueur = ['Flaming Moe','Honey moon','Balkan Power']
    has_rum = ['Real man`s cocktail','Flaming Moe','Balkan Power']
    has_gin = ['AK-47','Flaming Moe','Is this even real?','Balkan Power']
    has_brady = ['AK-47','Flaming Moe','Unreal feeling']
    has_whiskey = ['Car Mechanic Cocktail, AK-47','Flaming Moe','Balkan Power']
    has_bourbon = ['AK-47','Flaming Moe','A song maybe','Balkan Power']  
    
    if message.content == 'vodka':
        response = has_vodka
        await message.channel.send("Here have a"+random.choice(response))
    elif message.content == 'tequilla':
        response = has_tequila
        await message.channel.send("Here have a"+random.choice(response))
    elif message.content == 'liqueur':
        response = has_liqueur
        await message.channel.send("Here have a"+random.choice(response))
    elif message.content == 'rum':
        response = has_rum
        await message.channel.send("Here have a"+random.choice(response))
    elif message.content == 'gin':
        response = has_gin
        await message.channel.send("Here have a"+random.choice(response))
    elif message.content == 'brady':
        response = has_brady
        await message.channel.send("Here have a"+random.choice(response))
    elif message.content == 'whiskey':
        response = has_whiskey
        await message.channel.send("Here have a"+random.choice(response))
    elif message.content == 'bourbon':
        response = has_bourbon
        await message.channel.send("Here have a"+random.choice(response))      


    if message.content==('Is Al there?'):
      await message.channel.send(f'Al?')
    if message.content==('Yeah, Al. Last name Caholic?'):
      await message.channel.send(f"Hold on, Ill check. Phone call for Al... Al Caholic. Is there an Al Caholic here? Wait a minute... Listen, you little yellow-bellied rat jackass, if I ever find out who you are, I'm gonna kill you!")
    if message.content==('Oliver Clothesoff.'):
      await message.channel.send(f"Hold on, I'll check. (calls) Oliver Clothesoff! Call for Oliver Clothesoff!(Marge picks up the extension)Listen, you lousy bum, if I ever get a hold of you, I swear I'll cut your belly open!")
    if message.content==('Is Mister Freely there?'):
      await message.channel.send(f'Who?')
    if message.content==('Freely, first initials I. P.'):
      await message.channel.send(f"Hold on, I'll check. Uh, is I. P. Freely here? Hey everybody, I.P. Freely! (the customers laugh) Wait a minute... Listen to me you lousy bum. When I get a hold of you, you're dead. I swear I'm gonna slice your heart in half.")
    if message.content==('Is Jaques there?'):
      await message.channel.send(f'Who?')
    if message.content==('Jaques, last name Strap.'):
      await message.channel.send(f"Uh, hold on. Uh, Jock... Strap... Hey guys I'm looking for a Jock Strap. (laughs from all) Oh... wait a minute... Jock Strap... It's you isn't it ya cowardly little runt? When I get a hold of you, I'm gonna gut you like a fish and drink your blood.")
    if message.content==('Is Seymour there? Last name Butz.'):
      await message.channel.send(f"Just a sec. Hey, is there a Butz here? A Seymour Butz? Hey, everybody, I wanna Seymour Butz!(realizes) Wait a minute... Listen, you little scum-sucking pus-bucket! When I get my hands on you, I'm gonna pull out your eyeballs with a corkscrew!")
    if message.content==('Hello, is Homer there?'):
      await message.channel.send(f'Homer who?')
    if message.content==('Homer... Sexual.'):
      await message.channel.send(f'Wait one second, let me check. (calls) Uh, Homer Sexual? Hey, come on, come on, one of you guys has got to be Homer Sexual!')
    if message.content==("Don't look at me!"):
      await message.channel.send(f"You rotten liver pot! If I ever get a hold of you, I'll sink my teeth into your cheek and rip your face off!")
    if message.content==('Blood Feud'):
      await message.channel.send(f"(answers the phone) Moe's Tavern, where the elite meet to drink.")
    if message.content==('Uh, hello. Is Mike there? Last name, Rotch.'):
      await message.channel.send(f"Hold on, I'll check. (calls) Mike Rotch! Mike Rotch! Hey, has anybody seen Mike Rotch lately? (barflies laugh) Listen, you little puke. One of these days, I'm going to catch you, and I'm going to carve my name on your back with an ice pick.")
    if message.content==('Treehouse of Horror II'):
      await message.channel.send(f"(answers the phone) Moe's Tavern. ... Hold on, I'll check. Uh, hey, everybody! I'm a stupid moron with an ugly face and big butt and my butt smells and I like to kiss my own butt.")
    if message.content==("Flaming Moe's"):
      await message.channel.send(f"(answering the phone) Flaming Moe's.")
    if message.content==("Uh, yes, I'm looking for a friend of mine. Last name Jass. First name Hugh."):
      await message.channel.send(f"Uh, hold on, I'll check. (calling) Hugh Jass! Somebody check the men's room for a Hugh Jass!")
    if message.content==("Uh, I'm Hugh Jass."):
      await message.channel.send(f'Telephone. (hands over the receiver)... Hello, this is Hugh Jass.')
    if message.content==('Uh, hi.'):
      await message.channel.send(f"Who's this?")
    if message.content==('Bart Simpson.'):
      await message.channel.send(f'Well, what can I do for you, Bart?')
    if message.content==("Uh, look, I'll level with you, Mister. This is a crank call that sort of backfired, and I'd like to bail out right now."):
      await message.channel.send(f'All right. Better luck next time. (hangs up) What a nice young man.')
    if message.content==('Burns Verkaufen der Kraftwerk'):
      await message.channel.send(f"Moe's Tavern, Moe speaking.")
    if message.content==("Uh, yes, I'm looking for a Mrs. O'Problem? First name, Bea."):
      await message.channel.send(f"Uh, yeah, just a minute, I'll check. (calls) Uh, Bea O'Problem? Bea O'Problem! Come on guys, do I have a Bea O'Problem here? \n Oh... (to phone) It's you, isn't it! Listen, you. When I get a hold of you, I'm going to use your head for a bucket and paint my house with your brains!")
    if message.content==('New Kid on the Block'):
      await message.channel.send(f'(answers the phone) Yeah, just a sec; Ill check. (calls) Amanda Hugginkiss? Hey, Im lookin fer Amanda Hugginkiss. Why cant I find Amanda Hugginkiss?')
    if message.content==('Maybe your standards are too high!'):
      await message.channel.send(f'You little S.O.B. Why, when I find out who you are, Im going to shove a sausage down your throat and stick starving dogs in your butt!')
    if message.content==('My name is Jimbo Jones, and I live at 1094 Evergreen Terrace.'):
      await message.channel.send(f"I knew he's slip up sooner or later! He unsheathes a rusty knife and heads out of the tavern.")
    if message.content==("I'm looking for a Mr. Smithers, first name Wayland"):
      await message.channel.send(f"Oh, so, you're looking for a Mr. Smithers, eh? First name Wayland, is it? Listen to me, you; when I catch you, Im gonna pull out your eyes and stick 'em down your pants, so you can watch me kick the crap outta you, okay? Then Im gonna use your tongue to paint my boat!")
    if message.content==("Hello, I'd like to speak with a Mr. Snotball, first name Eura"):
      await message.channel.send(f'Eura Snotball?')
    if message.content==("I'd like to speak to a Mr. Tabooger, first name Ollie."):
      await message.channel.send(f'Ooh! My first prank call! What do I do?')
    if message.content==('Just ask if anyone knows Ollie Tabooger.'):
      await message.channel.send(f"I don't get it.")
    if message.content==('Yell out "Ill eat a booger"'):
      await message.channel.send(f"What's the gag?")  

    truthDatabase= ['Whats the most shameful thing you have done when drinking and drink 1 glass of whatever alcohol caused you to do that shameful thing and if its multiple alcohol then drink multiple alcohol',
                    'What is the most amount of alcohol you have ever drunk and try to beat that record *Do not forget the coaster*',
                    'What do you think is the worst alcohol? Also drink that alcohol',
                    'Who is your crush? Also drink enough alcohol until you can tell us with complete confidence',
                    'What do you truly think about your friends? Have whatever you think is the strongest alcohol a few times before giving the answer',
                   ]

    dareDatabase= ['I dare you to use the random command and drink 10 of whatever it gives you',
                   'I dare you to drink a cocktail from the specials menu and go flirt with your crush',
                   'I dare you to let your friends choose a random cocktail from any one of my databases and drink it 5 times',
                   'I dare you to mix 10 random cocktails from the random command and drink the end result',
                   'I dare you to spend all your money on a single type of cocktail and drink every one you order',
                   'I dare you to drink 10 cocktails of your choice and then spin and dance',
                   'I dare you to drink 1 of each cocktail from the specials list',
                   'I dare you to choose any cocktail you want and go sing on the roof top whilst drinking it',
                   ]


    if message.content==('Hey Moe lets play truth or dare'):
      await message.channel.send(f'Sure but since you drink less when you have fun this is gonna be  the Moe version of truth of dare and we got plenty of alcohol in my version. To get started just ask "Rules?"')
    if message.content==('Moe I choose truth'):
      await message.channel.send(random.choice(truthDatabase))
    elif message.content==('Moe I choose dare'):
      await message.channel.send(random.choice(dareDatabase))
    if message.content.startswith('Truth-'):
      await message.channel.send('Okay they chose truth if you wanna listen to the dirty little secrets now is your chance')
    elif message.content.startswith('Dare-'):
      await message.channel.send('Okay they chose dare, if you wanna watch them make fools of themselves now is your chance')
    if message.content==('I did it Moe'):
      await message.channel.send(f'Good work have a beer for £20')
    elif message.content==('I did not do it Moe'):
      await message.channel.send(Throw)  
    

    await client.process_commands(message)

Card='https://25.media.tumblr.com/tumblr_ly3p12pRpw1qeweuno1_400.gif'

Throw='https://media3.giphy.com/media/l2Je3fAJ02BkvLYEE/giphy.gif'

Coaster='https://i.pinimg.com/originals/ef/ba/e9/efbae9b627b408e1406ff03c1e1b33ca.jpg'

@client.command(aliases=['Rules?'])
async def Rules(ctx):
    RulesEmbed= discord.Embed(title="Rules for Moe's Truth and Dare", description='Okay so here are the rules. Rule 1:"Hey Barney no drinking out of the tap when i have my back turned"', colour=discord.Colour.green())
    RulesEmbed.add_field(name="Rule 1:", value='If you want to do truth you say "Moe I choose truth"', inline=True)
    RulesEmbed.add_field(name="Rule 2:", value='If you want to do dare you say "Moe I choose dare"', inline=True)
    RulesEmbed.add_field(name="Rule 3:", value='No take backs your stuck with what you get for truth or dare', inline=True)
    RulesEmbed.add_field(name="Rule 4:", value='When choosing between the truth or dare put"Truth-[insert answer for the truth] or Dare-[insert answer for the dare]"', inline=True)
    RulesEmbed.add_field(name="Rule 5:", value='If you did the truth or dare say "I did it Moe", if you did not do it say "I did not do it Moe"', inline=True)
    RulesEmbed.add_field(name="Rule 6:", value="Since this is the Moe version it doesn't matter whether you choose truth or dare you will still be drinking", inline=True)
    await ctx.send(embed=RulesEmbed)
    await ctx.send(f'Also read the coaster cause if you drink too much its not my responsibility')
    await ctx.send(Coaster)
    
  
@client.command()
async def Hello(ctx):
  await ctx.send(f'Hi, how are you folks doing? Im Moe, or as the ladies like to call me, "hey, you behind the bushes." If you need any help just say Help and see if I do anything. Also here is my card')
  await ctx.send(Card)

@client.command(aliases=['Help'])
async def _HeyMoeIgotaproblem(ctx):
  myEmbed = discord.Embed(title="What's the matter?", description="Your help, enjoy it and dont expect me to be using any of that fancy grammar and puncuation I can't afford that no more", colour=discord.Colour.blue())
  myEmbed.add_field(name="Recommendations:", value="Write this then a flavour and ill give you a cocktail based on those flavours", inline=True)
  myEmbed.add_field(name="Random", value="This command will cause me to just give you the first cocktail I lay eyes on and no refunds", inline=True)
  myEmbed.add_field(name="Hey Moe I need information on the cocktail", value="Do this and ill consult the bartender's bible for a cocktail but if you don`t get something the first time dont expect a second time.", inline=True)
  myEmbed.add_field(name="LoveTester", value="This command will let you use my love tester for 5 bucks and no refunds you cheapskate.", inline=True)
  myEmbed.add_field(name="SpecialList", value="Type this and I will give you a list of ingriedients you can use for some very special cocktails", inline=True)
  myEmbed.add_field(name="Hey Moe lets play truth or dare", value="Just ask this if you want a goo ol game of truth or dare", inline=True)
  myEmbed.add_field(name="Show me the prank call list", value="Telling me to do this will cause me to send you on a alcohol fueled journey to a land of prank calls. If you speak the lines of the prank calls I will respond accordingly.", inline=True)
  myEmbed.add_field(name="Moe do you know where I can find information on the alcohol", value="Asking me this will make me consult my search history for the alcohol your looking for", inline=True)
  myEmbed.add_field(name="FlavourList", value="Type this and I will give you a list of flavours you can use for some cocktails", inline=True)

  await ctx.send(embed=myEmbed)

@client.command(aliases=['Recommendations', 'any recommendations for', 'you got something with']) # when user says something the bot checks for possible commands
async def _HeyMoecanyourecommendccocktail(ctx, *, userInput):
    
    await ctx.send(runCocktailRecommendation(userInput))# goes through the runCocktailRecommendation Function until it outputs the recommended cocktail
    


def getFlavourList(userInput):# takes userInput and creates a list of flavours that the user requested (so long as it exists within the for loop)

    inputFromUser = userInput.lower()
    inputList = inputFromUser.split()
    userFlavour = []# starts the loop with a blank flavour list that is appended during the for loop process

    for flavour in inputList: # used to append the userFlavour list with flavours that the user input if they exist with in the for loop
        if flavour == "lemon" or flavour == "lemon,":
            userFlavour.append("lemon")
            print("lemon added to userFlavour Index")

        elif flavour == "mint" or flavour == "mint,":# accounts for the flaovur and if the user uses ',' to space them out in the string
            userFlavour.append("mint")# adds the associated flavour to the userFlavour List
            print("mint added to userFlavour index")# prints a message to the terminal for testing purposes.

        elif flavour == "lime" or flavour == "lime,":
            userFlavour.append("lime")
            print("lime added to userFlavour index")

        elif flavour == "cranberry" or flavour == "cranberry,":
            userFlavour.append("cranberry")
            print("cranberry added to userFlavour index")

        elif flavour == "orange" or flavour == "orange,":
            userFlavour.append("orange")
            print("orange added to userFlavour index")

    return (userFlavour)# brings the variable userFlavour over to the runCocktailRecommendation function to continue with the process


def getCocktailList(userFlavour):
    cocktailList = []# list to be appened for to process the end result
    lemonCocktail = ["Long Island Ice Tea", "Martini", "Ramons Gin Fizz"] # list containing the cocktails associated with the flavour
    mintCocktail = ["Mojito", "Mint Julep", "Southside"]
    limeCocktail = ["Mojito", "Bramble", "Southside", "Sea Breeze", "Ramos Gin Fizz"]
    cranberryCocktail = ["Cosmopolitan", "Woo Woo", "Sea Breeze"]
    orangeCocktail = ["Old Fashioned", "Negroni", "El Presidente", "Ramos Gin Fizz"]

    for flavour in userFlavour:# a loop to iterate through the flavours collected previously to ass the cocktail lists to the potential cocktail recommendations
        if flavour == "lemon":
            
            cocktailList.extend(lemonCocktail)# extends the final cocktail list with the other lists of cocktails
            print("lemon list added to cocktailList")# writes to the terminal to confirm if the correct list was added.

        elif flavour == "mint":
            cocktailList.extend(mintCocktail)
            print("mint list added to  cocktailList")

        elif flavour == "lime":
            cocktailList.extend(limeCocktail)
            print("lime list added to  cocktailList")

        elif flavour == "cranberry":
            cocktailList.extend(cranberryCocktail)
            print("cranberry list added to  cocktailList")

        elif flavour == "orange":
            cocktailList.extend(orangeCocktail)
            print("orange list added to  cocktailList")

    return (cocktailList)# returns final cocktail list in order to provide the final output


def getUserCocktail(cocktailList):# takes the list of possible cocktails and randomly produces a cocktails for the output
    
    cocktailChoice = random.choice(cocktailList)# randomly selects a cocktail from the list for the output

    return (cocktailChoice)# returns the random cocktail
    

def runCocktailRecommendation(userInput):
    flavourList = getFlavourList(userInput) # runs the getFlavourList to acquire the necessary variable to continue with the process.
    cocktailList = getCocktailList(flavourList)# runs the getCocktailList to acquire the necessary variable to continue with the process.
    cocktail = str(getUserCocktail(cocktailList))# runs the getUserCocktail and convert it into a single string rather than a part of a list to finish the process.
    printResponse = "Okay this is your damn cocktail *hands over " + cocktail + "*, enjoy and remember *turns and points shotgun* No refunds" # creates response that is returned to the original discord command function.
    return (printResponse)# retuns the printResponse variable to be retuned to the user.

@client.command(aliases=['FlavourList'])
async def _normallist(ctx):
    nlistEmbed = discord.Embed(title="Flavours menu", description="Types of flavours that are in the cocktails, depending on your choice I will show you cocktails with that flavour in it! :cocktail: ", colour=discord.Colour.purple())
    nlistEmbed.add_field(name="**Selection:**", value='Mint, Lemon, Lime, Cranberry, Orange. When asking me for a recommended flavour make sure you say Recommendations and every flavour that comes after (PS no captial letters on the flavours)', inline=True)
    nlistEmbed.add_field(name="Last updated", value="21.11.2020", inline=True)
    await ctx.send(embed=nlistEmbed)

@client.command(aliases=['Random'])
async def randomCocktail(ctx):
    Randomlist=['Vodka+redbull', 
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

    ResponseList = [
    'and no refunds',
    'I hope you enjoy',
    'and I would not recommend charging someone else for it, Barney ended up in a ditch when he tried that',
    'well this might be your thing it might not be we will see',
    'you know what its on the house for once, but dont you ever tell no one about this or ill slice your throat open']

    await ctx.send(f'Okay so the cocktail that you will be receiving today is {random.choice(Randomlist)}, {random.choice(ResponseList)}')

@client.command(aliases=['SpecialList'])
async def _list(ctx):
    listEmbed = discord.Embed(title="Alcohol menu", description="Types of alcohol that I can offer you, depending on your choice I will show you cocktails with this type of alcohol in it! :cocktail: ", colour=discord.Colour.purple())
    listEmbed.add_field(name="**Selection:**", value='```Whiskey, Vodka, Gin, Rum, Tequila, Liqueur, Brady, Bourbon.``` *To check the recipe for a cocktail, type the <cocktail name> (you can type only the first letters e.g Is this even real? cocktail **iter**)', inline=True)
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
    ieEmbed.add_field(name="**Recipe: :pencil: **", value='To make this cocktail you have to add 4 bottles of vodka in a bucket, mix it with engine oil and add fuel. If you want to be even cooler, you can add and a glass of coffe.', inline=True)
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
    ufEmbed.add_field(name="**Recipe: :pencil: **", value='1/2 Brady, 0,5/2 Lemon juice, 0,3543635/2 sugar, 0.324522353432432/2 coffe mixed with milk, 3/2 ice ice baby, 1/2 onions', inline=True)
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

myListX=["Inferno Extreme", 
         "Flaming Moe", 
         "Balkan Power", 
         "Multi Flavour Smash", 
         "Honey Moon", 
         "AK-47", 
         "Unreal Feeling", 
         "CarMechanic Cocktail",
         "A Song Maybe"]
 
myListZ=["InfernoExtremeSBS", 
         "FlamingMoeSBS", 
         "BalkanPowerSBS", 
         "MultiFlavourSmashSBS", 
         "HoneyMoonSBS", 
         "AK-47SBS", 
         "UnrealFeelingSBS",
         "CarMechanicCocktailSBS", 
         "ASongMaybeSBS"]

@client.command(aliases=["menu"])
async def ourmenu(ctx):
    akh=len(myListX)
    akda=0
    eembed=discord.Embed(title="Our menu for special cocktails:cocktail:", description="Just read the list below, when you want a step by step recipie just write the cocktail name without spaces and use capitals for separate words and put SBS at the end of it", colour=discord.Colour.blue())
    while akda<akh:
        eembed.add_field(name=myListX[akda], value="Message "+myListZ[akda]+" for the Step By Step recipe", inline=False)
        akda=akda+1
    await ctx.send(embed=eembed)

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
    a2bed.add_field(name="Shake it, baby", value="Close the shaker, shake as hard as you can, then pour it into shot glasses", inline=False)
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
    await ctx.send(embed=a5bed)

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
    a9bed.add_field(name="Beer", value="Fill up the rest of the glass with beer", inline=False)
    a9bed.add_field(name="Now you are ready to request a song to play", value="I prefer you to choose What A Wonderful World by Louis Armstrong, but it is up to you", inline=False)
    await ctx.send(embed=a9bed)

@client.command(aliases=['LoveTester'])
async def _Lovetester(ctx):
    loveResponses = ['casanova, well well looks like we got a elite lover in the bar. Oh how I hate your pretty boys...... Oh god why am I so lonely',
                     'hot tamale, dammit why cant I ever catch break like you just for that im gonna be spitting in every one of your drinks',
                     'luke warm Luke, average is still more above than me so get out there and make something of yourself',
                     'lovelorn, ah well you can just talk to uncle Moe and drink all your problems away',
                     'cold fish, welp join the club pal']
    await ctx.send(f'According to the love tester your love level is {random.choice(loveResponses)}')

client.run(TOKEN)