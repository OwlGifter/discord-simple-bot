import discord
token = 'MTI4MDcxNDYyNzg2ODUyODY5Mw.Gqa35L.cudSmR_nG1P7St4cH606Bla2jqfJk7y9_XrcW4'

def handle_user_messages(msg, user, lst) -> str:
    message = msg.lower()
    if(message == '/jointos'):
        addPlayer(user, lst)
        return str(user) + ' added to the game'
    if(message == '/sendroles'):
        deletePlayers(lst)
        return "Roles Sent to DM's"
    if(message == 'hello'):
        return 'Hello user. Welcome'
    return 'fuck'



def addPlayer(user, people_in_game):
    people_in_game.append(user)
    print(people_in_game)

async def deletePlayers(people_in_game):
    await sendRoles(people_in_game)
    people_in_game.clear()


async def processMessage(message, user_message, lst):
    try:
        botfeedback = handle_user_messages(user_message, message.author, lst)
        if user_message.lower() == '/sendroles':
            await deletePlayers(lst)
        await message.channel.send(botfeedback)
    except Exception as error:
        print(error)

async def sendRoles(list):
        for player in list:
            try:
                if player.dm_channel is None:
                    await player.create_dm()
                await player.dm_channel.send('Testing roles')
            except discord.Forbidden:
                print(f"Cannot send message to {player.name}, permission denied.")
            except discord.HTTPException as error:
                print(f"Failed to send message to {player.name}: {error}")
            except Exception as error:
                print(f"An unexpected error occurred: {error}")


def runBot():
    people_in_game = []
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
        await processMessage(message, message.content, people_in_game)
    

    client.run(token)