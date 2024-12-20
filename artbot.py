# this is the main class that gets run for the bot, 
# if you would like to know more info on the rules it
# follows, please read the readMe file

import discord
import random
import keys

token = keys.getKey()

def rolesGenerator() -> str:
    roles = 'Jailor \n'
    roles = townProtective(roles)
    roles = townInvestigative(roles)
    roles = townInvestigative(roles)
    roles = townSupport(roles)
    roles = townKilling(roles)
    roles = randomTown(roles)
    roles = randomTown(roles)
    roles = randomTown(roles)
    roles += '-\n'
    roles += 'GodFather \n'
    roles = mafiaKilling(roles)
    roles = mafiaSupport(roles)
    roles = randomMafia(roles)
    roles += '-\n'
    roles += 'Mercenary \n'
    roles += 'Governor \n'
    roles = randomNeutralEvil(roles)
    roles = randomNeutralKilling(roles)
    roles += '-\n'
    roles = randomAny(roles)


    return roles

def randomizerMethod(options_list, roles, unique_roles = None)-> str:
    # chooses a random role from the list of options given
    randomRole = random.choice(options_list)

    # checks if there are unique roles, if so, it checks if the 
    # role chosen is unique and if it already in the roles chosen
    if unique_roles and randomRole in unique_roles and randomRole in roles:
        # if role is unique and already in the roles chosen it reruns the code with the 
        # same options hoping for a different selection
        return randomizerMethod(options_list, roles, unique_roles)
    
    # adds role to selected roles and returns it
    roles += randomRole + ' \n'
    return roles





def randomAny(roles) ->str:
    # randomly chooses a role cetegory to choose the random character from
    FunctionList = [townProtective, townInvestigative, townSupport, townKilling, randomTown, mafiaKilling, mafiaSupport, randomMafia, randomNeutralEvil, randomNeutralKilling]
    random.shuffle(FunctionList)
    roles = FunctionList[0](roles)
    return roles

def randomNeutralKilling(roles) ->str:
    # selects options
    options = ['Waluigi', 'Avenger', 'Berserker', 'BlackWidow', 'Hunter', 'Mad Scientist']
    # selects uniques
    uniqueOptions = ['Waluigi']
    # runs role randomizer with chosen options
    roles = randomizerMethod(options, roles, uniqueOptions)
    # returns roles selected
    return roles

def randomNeutralEvil(roles) ->str:
    options = ['Rebel Leader', 'Freelancer', 'Lunatic', 'Logician']
    uniqueOptions = ['Rebel Leader']
    roles = randomizerMethod(options, roles, uniqueOptions)
    return roles

def randomMafia(roles) ->str:
    #randomizes functions in list and runs the first one on the list.
    functionList = [mafiaSupport, mafiaKilling]
    random.shuffle(functionList)
    roles = functionList[0](roles)
    return roles

def mafiaSupport(roles) -> str:
    options = ['Crooked Lawyer', 'Consort', 'Mole', 'Councillor', 'Consigliere']
    uniques = ['Mole', 'Councillor']
    roles = randomizerMethod(options, roles, uniques)
    return roles

def mafiaKilling(roles) ->str:
    options = ['Vanguard', 'Sniper', 'Caporegime', 'Pyromaniac', 'Demolitionist']
    roles = randomizerMethod(options, roles)
    return roles

def randomTown(roles) -> str:
    #randomized functions in list and runs the first one.
    functionList = [townProtective, townInvestigative, townSupport, townKilling]
    random.shuffle(functionList)
    roles = functionList[0](roles)
    return roles

def townKilling(roles) ->str:
    options = ['Vigilante', 'Veteran']
    uniques = ['Veteran']
    roles = randomizerMethod(options, roles, uniques)
    return roles

def townSupport(roles) -> str:
    options = ['Psychic', 'Consultant', 'SupplyMaster', 'GraveDigger', 'Escort']
    uniques = ['Psychic', 'Consultant']
    roles = randomizerMethod(options, roles, uniques)
    return roles

def townInvestigative(roles) -> str:
    options = ['Detective', 'Commissioner', 'Watchman', 'Spy']
    uniques = ['Spy']
    roles = randomizerMethod(options, roles, uniques)
    return roles

def townProtective(roles) -> str:
    options = ['Protector', 'Zealot', 'Constabulary', 'Doctor']
    uniques = ['Doctor']
    roles = randomizerMethod(options, roles, uniques)
    return roles


def runBot():
    # sets the client for discord
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    # lets us know the bot is up
    @client.event
    async def on_ready():
        print({client.user}, 'is live')

    # checks every message for specific command
    @client.event
    async def on_message(message):
        # ignores if the message is from the bot
        if message.author == client.user:
            return
        # if message is specified command, it runs our main command
        if message.content == '/rand':
            roles = rolesGenerator()
            await message.channel.send(roles)
    # runs the bot
    client.run(token)