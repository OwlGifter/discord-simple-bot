# this project was meant to randomize roles for a game, it follows set rules, and randomizes it
# Below is the role and the options for the role
#     Town Protective:
#     Protector
#     Zealot 
#     Constabulary
#     Doctor*

#     Town Investigative:
#     Detective
#     Commissioner
#     Watchman
#     Spy*

#     Town Support:
#     Psychic*
#     Consultant*
#     Supplymaster
#     Gravedigger
#     Escort

#     Town Killing:
#     Vigilante
#     Veteran*

#     Random Town:
#     All of the Above (- any uniques) 
#     Mafia Killing
#     Vanguard
#     Sniper
#     Caporegime
#     Pyromaniac
#     Demolitionist

#     Mafia Support:
#     Crooked Lawyer
#     Consort
#     Consigliere
#     Mole*
#     Councillor*

#     Random Mafia:
#     All of the above (- any uniques) 
#     Neutral Evil/Unvirtuous
#     Rebel Leader
#     Freelancer
#     Lunatic
#     Logician

#     Neutral Killing:
#     Mercenary
#     Avenger
#     Berserker
#     Black Widow
#     Hunter
#     Mad Scientist

#     Random Any: any role in the game, except for uniques

# below this is the order the bot puts out the random roles
#     Jailor
#     Town Protective
#     Town Investigative
#     Town Investigative
#     Town Support
#     Town Killing
#     Random Town
#     Random Town
#     Random Town
#     -
#     Godfather
#     Mafia Killing
#     Mafia Support
#     Random Mafia
#     -
#     Mercenary
#     Governor
#     Neutral Evil/Unvirtuous
#     Neutral Killing
#     -
#     Random Any

import discord
import random

token = 'discord token here'

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
    randomNum = random.randint(0,9)
    if(randomNum < 1):
        roles = townProtective(roles)
        return roles
    elif(randomNum < 2):
        roles = townInvestigative(roles)
        return roles
    elif(randomNum < 3):
        roles = townSupport(roles)
        return roles
    elif(randomNum < 4):
        roles = townKilling(roles)
        return roles
    elif(randomNum < 5):
        roles = randomTown(roles)
        return roles
    elif(randomNum < 6):
        roles = mafiaKilling(roles)
        return roles
    elif(randomNum < 7):
        roles = mafiaSupport(roles)
        return roles
    elif(randomNum < 8):
        roles = randomMafia(roles)
        return roles
    elif(randomNum < 9):
        roles = randomNeutralEvil(roles)
        return roles
    elif(randomNum < 10):
        roles = randomNeutralKilling(roles)
        return roles
    return 'randomAny Did Not Work!!!!!!!!!!!!!!!! \n'

def randomNeutralKilling(roles) ->str:
    # selects options
    options = ['Waluigi', 'Avenger', 'Berserker', 'BlackWidow', 'Hunter', 'Mad Scientist']
    # selects uniques
    uniques = ['Waluigi']
    # runs role randomizer with chosen options
    roles = randomizerMethod(options, roles, uniques)
    # returns roles selected
    return roles

def randomNeutralEvil(roles) ->str:
    options = ['Rebel Leader', 'Freelancer', 'Lunatic', 'Logician']
    uniques = ['Rebel Leader']
    roles = randomizerMethod(options, roles, uniques)
    return roles

def randomMafia(roles) ->str:
    randomNum = random.randint(0,1)
    if(randomNum < 1):
        roles = mafiaSupport(roles)
        return roles
    else:
        roles = mafiaKilling(roles)
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
    randomNum = random.randint(0, 3)
    if(randomNum < 1):
        roles = townProtective(roles)
        return roles
    elif(randomNum < 2):
        roles = townInvestigative(roles)
        return roles
    elif(randomNum < 3):
        roles = townSupport(roles)
        return roles
    elif(randomNum < 4):
        roles = townKilling(roles)
        return roles
    else:
        return 'randTown Did Not Work!!!!!! \n'

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
        if message.content == '/rand':
            roles = rolesGenerator()
            await message.channel.send(roles)
    # runs the bot
    client.run(token)