from typing import Final
import os
from dotenv import load_dotenv
from discord import Intents, Client, Message
from responses import get_response

#Load our token from somewhere safe
load_dotenv()
TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')
GUILD: Final[str] = os.getenv('DISCORD_GUILD')

#Bot Setup
intents: Intents = Intents.default()
intents.message_content = True
client: Client = Client(intents=intents)


#Message Functionality
async def send_message(message: Message, user_message: str) -> None:
    if not user_message:
        print('(Message was empty because Intents were not enabled probably)')
        return
    
    if is_private := user_message[0] == '?':
        user_message = user_message[1:]
        
    try:
        response: str = get_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)

    
#handle startup
@client.event
async def on_ready() -> None:
    for guild in client.guilds:
        if guild.name == GUILD:
            break
        
    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )


#handle incoming message
@client.event
async def on_message(message: Message) -> None:
    user_message = message.content.lower()
    if message.author == client.user:
        return
    if not user_message.startswith(('!suggest-prompt','!get-prompt')):
        print('message did not start with trigger')
        return

    username : str = str(message.author)
    user_message: str = message.content
    channel: str = str(message.channel)
    
    print(f'[{channel}] {username}: "{user_message}"')
    await send_message(message, user_message)
    
#main entry point
def main() -> None:
    client.run(token=TOKEN)
        
        
if __name__ == '__main__':
    main()