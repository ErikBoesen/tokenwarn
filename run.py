import discord
import asyncio
import sys

with open('message.md') as f:
    EMBED = discord.Embed(title='Warning!', type='rich', description=f.read())


class Bot(discord.Client):
    def __init__(self):
        super().__init__()
        print('Logging in... ', end='')

    async def on_ready(self):
        """Run when the bot is ready."""
        print('connected as %s.' % self.user.name)
        for server in self.servers:
            await self.send_message(server.default_channel, '', embed=EMBED)
            print('- Sent message in %s#%s.' % (server.name, server.default_channel.name))
        await self.logout()
        print('Logged out.')


if __name__ == '__main__':
    with open('tokens.txt') as f:
        tokens = [token for token in f.read().split('\n') if token]

    loop = asyncio.get_event_loop()
    for token in tokens:
        bot = Bot()
        loop.run_until_complete(bot.start(token))
