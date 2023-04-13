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
