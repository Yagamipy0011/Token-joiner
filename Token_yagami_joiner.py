import discord
import asyncio
import time
import random

async def join_server(link, token):
    try:
        client = discord.Client()

        @client.event
        async def on_ready():
            print(f'Logged in as {client.user}')
            try:
                await client.fetch_invite(link)
                await client.accept_invite(link)
                print(f'Joined server with {token}')
            except Exception as e:
                print(f'Error joining server with {token}: {e}')

        await client.start(token)
        await client.close()
    except Exception as e:
        print(f'Error with {token}: {e}')

async def main():
    link = input('Enter server link: ')
    num_tokens = int(input('Enter number of tokens: '))

    with open('tokens.txt', 'r') as f:
        tokens = f.read().splitlines()

    for i in range(num_tokens):
        token = random.choice(tokens)
        await join_server(link, token)
        time.sleep(5)  # Wait 5 seconds between each join attempt

if __name__ == '__main__':
    asyncio.run(main())
