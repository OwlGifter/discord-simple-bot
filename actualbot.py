# this is the unimproved version of the project, made solely for testing
# as well as learning
# as such please disreguard issues and rewritten code in here
# again it was a prototype

import discord
import random

token = 'discord token'

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
    roles += 'GodFather \n'
    roles = mafiaKilling(roles)
    roles = mafiaSupport(roles)
    roles = randomMafia(roles)
    roles += 'Mercenary \n'
    roles += 'Governor \n'
    roles = randomNeutralEvil(roles)
    roles = randomNeutralKilling(roles)
    roles = randomAny(roles)


    return roles

def randomAny(roles) ->str:
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
    randomNum = random.randint(0,5)
    if(randomNum < 1):
        roles += 'Mercenary \n'
        return roles
    elif(randomNum < 2):
        roles += 'Avenger \n'
        return roles
    elif(randomNum < 3 and 'Mole' not in roles):
        roles += 'Berserker \n'
        return roles
    elif(randomNum < 4 and 'Councillor' not in roles):
        roles += 'BlackWidow \n'
        return roles
    elif(randomNum < 5):
        roles += 'Hunter \n'
        return roles
    elif(randomNum < 6):
        roles += 'Mad Scientist \n'
        return roles
    return 'randomNeutralKilling Did Not Work!!!!!!!! \n'

def randomNeutralEvil(roles) ->str:
    randomNum = random.randint(0,3)
    if(randomNum < 1):
        roles += 'Rebel Leader \n'
        return roles
    elif(randomNum < 2):
        roles += 'Freelancer \n'
        return roles
    elif(randomNum < 3):
        roles += 'Lunatic \n'
        return roles
    elif(randomNum < 4):
        roles += 'Logician \n'
        return roles
    return 'randomNeutralEvil Did Not Work!!!!!!!! \n'

def randomMafia(roles) ->str:
    randomNum = random.randint(0,1)
    if(randomNum < 1):
        roles = mafiaSupport(roles)
        return roles
    else:
        roles = mafiaKilling(roles)
        return roles

def mafiaSupport(roles) -> str:
    randomNum = random.randint(0,4)
    if(randomNum < 1):
        roles += 'Crooked Lawyer \n'
        return roles
    elif(randomNum < 2):
        roles += 'Consort \n'
        return roles
    elif(randomNum < 3 and 'Mole' not in roles):
        roles += 'Mole \n'
        return roles
    elif(randomNum < 4 and 'Councillor' not in roles):
        roles += 'Councillor \n'
        return roles
    elif(randomNum < 5):
        roles += 'Consigliere \n'
        return roles
    return 'mafiaSupport Did Not Work!!!!!!!! \n'

def mafiaKilling(roles) ->str:
    randomNum = random.randint(0,4)
    if(randomNum < 1):
        roles += 'Vanguard \n'
        return roles
    elif(randomNum < 2):
        roles += 'Sniper \n'
        return roles
    elif(randomNum < 3):
        roles += 'Caporegime \n'
        return roles
    elif(randomNum < 4):
        roles += 'Pyromaniac \n'
        return roles
    elif(randomNum < 5):
        roles += 'Demolitionist \n'
        return roles
    return 'mafiaKilling Did Not Work!!!!!!!! \n'

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
    randomNum = random.randint(0,1)
    if(randomNum < 1):
        roles += 'Vigilante \n'
        return roles
    elif(randomNum < 2 and 'Veteran' not in roles):
        roles += 'Veteran \n'
        return roles
    else:
        roles += 'Vigilante \n'
        return roles

def townSupport(roles) -> str:
    randomNum = random.randint(0,4)
    if(randomNum < 1 and 'Psychic' not in roles):
        roles += 'Psychic \n'
        return roles
    elif(randomNum < 2 and 'Consultant' not in roles):
        roles += 'Consultant \n'
        return roles
    elif(randomNum < 3):
        roles += 'SupplyMaster \n'
        return roles
    elif(randomNum < 4):
        roles += 'GraveDigger \n'
        return roles
    elif(randomNum < 5):
        roles += 'Escort \n'
        return roles
    return 'townSupport Did Not Work!!!!!!!! \n'

def townInvestigative(roles) -> str:
    randomNum = random.randint(0,3)
    if(randomNum < 1):
        roles += 'Detective \n'
        return roles
    elif(randomNum < 2):
        roles += 'Commissioner \n'
        return roles
    elif(randomNum < 3):
        roles += 'Watchman \n'
        return roles
    elif(randomNum < 4 and 'Spy' not in roles):
        roles += 'Spy \n'
        return roles
    else:
        roles += 'Watchman \n'
        return roles
    
    return 'townInvestigative Did Not Work!!!!!!!! \n'

def townProtective(roles) -> str:
    randomNum = random.randint(0,3)
    if(randomNum < 1):
        roles += 'Protector \n'
        return roles
    elif(randomNum < 2):
        roles += 'Zealot \n'
        return roles
    elif(randomNum < 3):
        roles += 'Constabulary \n'
        return roles
    elif(randomNum < 4):
        roles += 'Doctor \n'
        return roles

    return 'townProtective Did Not Work!!!!!!!!! \n'


def runBot():
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print({client.user}, 'is live')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        if message.content == '/rand':
            roles = rolesGenerator()
            await message.channel.send(roles)
            print('hmmm')
        
    

    client.run(token)