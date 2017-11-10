import discord
import asyncio

with open('message.md') as f:
    EMBED = discord.Embed(title='Warning!', type='rich', description=f.read())

class Bot(discord.Client):
    def __init__(self):
        super().__init__()
        print('Starting roll...')

    async def on_ready(self):
        """Run when the bot is ready."""
        print('Logged in as ' + self.user.name + ' (ID ' + self.user.id + ').')
        for server in self.servers:
            await self.send_message(server.default_channel, '', embed=EMBED)
            print('Sent message in %s#%s.' % (server.name, server.default_channel.name))
        await self.logout()


if __name__ == '__main__':
    with open('tokens.txt') as f:
        tokens = [token for token in f.read().split('\n') if token]

    for token in tokens:
        bot = Bot()
        bot.run(token)
        bot.close()
