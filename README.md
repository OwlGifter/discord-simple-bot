this project was meant to randomize roles for a game, it follows set rules, and randomizes it

Below is the role and the options for the role, unique roles are marked with a *

    Town Protective:
    Protector
    Zealot 
    Constabulary
    Doctor*
    --------------
    Town Investigative:
    Detective
    Commissioner
    Watchman
    Spy*
    --------------
    Town Support:
    Psychic*
    Consultant*
    Supplymaster
    Gravedigger
    Escort
    --------------
    Town Killing:
    Vigilante
    Veteran*
    --------------
    Random Town:
    All of the Above (- any uniques) 
    Mafia Killing
    Vanguard
    Sniper
    Caporegime
    Pyromaniac
    Demolitionist
    --------------
    Mafia Support:
    Crooked Lawyer
    Consort
    Consigliere
    Mole*
    Councillor*
    --------------
    Random Mafia:
    All of the above (- any uniques) 
    Neutral Evil/Unvirtuous
    Rebel Leader
    Freelancer
    Lunatic
    Logician
    --------------
    Neutral Killing:
    Mercenary
    Avenger
    Berserker
    Black Widow
    Hunter
    Mad Scientist
    --------------
    Random Any: any role in the game, except for uniques

below this is the order the bot puts out the random roles:

    Jailor
    Town Protective
    Town Investigative
    Town Investigative
    Town Support
    Town Killing
    Random Town
    Random Town
    Random Town
    -
    Godfather
    Mafia Killing
    Mafia Support
    Random Mafia
    -
    Mercenary
    Governor
    Neutral Evil/Unvirtuous
    Neutral Killing
    -
    Random Any

The project includes two bots: "artbot" and "actualbot." Interestingly, the primary bot in use,
which is more efficient and fully implemented, is artbot. Actualbot, on the other hand, serves 
as a prototype developed to familiarize myself with the Discord library. This was my first 
experience creating a Discord bot, and I consider it a success. While there is room for further
improvement, the bot was specifically designed to meet a request. Given the limited and infrequent
usage anticipated, I believe the current implementation will sufficiently meet the requirements.
Below are examples of the bot in action:

![image](https://github.com/user-attachments/assets/1cba2875-b323-4ecf-9a94-b583c03bb4e4)

another example can be:

![image](https://github.com/user-attachments/assets/6dafdae7-b42d-49f8-8f71-346896b303f5)

last example:

![image](https://github.com/user-attachments/assets/8cdd97f7-3c89-4e26-8951-ec5dc3afe7cb)


!!! SET UP REQUIRED!!! :
to set up this project, you must create your own discord api through [discord developer](https://discord.com/developers/applications)   
and create a new bot, get the key for the bot and create a new python file named "keys.py"
in which you will have to set up a string with your key, and create a getKey() method that returns your discord key.
after doing that you will have to import the discord.py library to your python libraries, i recommend using
"pip install discord.py" that way you can create your own python environment and pip install it in there,
to not install directly onto the python your computer uses for everything.To create a python virtual environment
use the command "python -m venv nameOfEnv" use the command at your own risk.

main command used for the bot will be "/rand" which will run the randomizing order of the bot.