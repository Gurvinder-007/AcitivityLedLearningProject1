# prank calls from http://www.simpsoncrazy.com/lists/prank-calls
# used discord.py documentation to convert it it into suitable for discord
#                       
# written using python3
# 
#def botrespond():
#    abb=input("you must message something to match the script as Bart from http://www.simpsoncrazy.com/lists/prank-calls")
#    if abb=="Is Al there?":
#        return "Al?"
#    elif abb=="Yeah, Al. Last name Caholic?":
#        return "Hold on, Ill check. Phone call for Al... Al Caholic. Is there an Al Caholic here? Wait a minute... Listen, you little yellow-bellied rat jackass, if I ever find out who you are, I'm gonna kill you!"
#    elif abb=="Is Oliver there?":
#        return "Who?"
#    elif abb=="Oliver Clothesoff.":
#        return "Hold on, I'll check. (calls) Oliver Clothesoff! Call for Oliver Clothesoff!(Marge picks up the extension)Listen, you lousy bum, if I ever get a hold of you, I swear I'll cut your belly open!"
#    else:
#       pass
#
# ###THERE MAY BE WRONG INDENTS AS THIS CODE IS IN COMMENTS AND IT IS WRITTEN IN VISUAL STUDIO###
# ###TESTED IN CODIO, EVERYTHING WORKS FOR ME###
#print(botrespond())
# ###THIS IS EXACTLY WHAT MY CODE DOES, INSTEAD OF ELIF ONLY USED IF STATEMENTS BECAUSE THE FEATURE IS ONE TIME USE###
# ### LINES ABOVE IS PROOF CODE THAT I CAN DO IF OR ELIF STATEMENTS, THE INTEGER abb OR botrespond() NAMES HAVE NOTHING TO DO WITH THE CODE, IT IS A PROOF CODE###
# ### THIS PROOF CODE SHOULD BE ENOUGH AS PROOF CODE ###
#
#
# ###---THIS IS FEATURE CODE WHICH IS INTEGRATED TO THE DISCORD BOT BY MY COURSEMATE GURVINDER NAGRA---###
@client.event #makes bot listen according to documentation https://discordpy.readthedocs.io/en/latest/ext/commands/api.html?highlight=client%20event
async def on_message(message): #consired not my line of code, defining function which takes a message https://discordpy.readthedocs.io/en/latest/quickstart.html
  if message.content==('Is Al there?'): #consired not my line of code,user messages the channel something as a Bart from the script mentioned in the first line of the file(URL is in the first line), example https://discordpy.readthedocs.io/en/latest/quickstart.html
    await message.channel.send(f'Al?')  #consired not my line of code,the bot returns this Al?, example https://discordpy.readthedocs.io/en/latest/quickstart.html
  if message.content==('Yeah, Al. Last name Caholic?'): #according by Simon, the rest of my code is written based on the tutorial https://discordpy.readthedocs.io/en/latest/quickstart.html
    await message.channel.send(f"Hold on, Ill check. Phone call for Al... Al Caholic. Is there an Al Caholic here? Wait a minute... Listen, you little yellow-bellied rat jackass, if I ever find out who you are, I'm gonna kill you!")
  if message.content==('Is Oliver there?'):
    await message.channel.send(f'Who?')
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