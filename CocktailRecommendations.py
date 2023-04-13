@client.command(aliases=['recommendations', 'any recommendations for', 'you got something with']) # when user says something the bot checks for possible commands
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