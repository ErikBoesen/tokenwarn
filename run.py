#!/usr/bin/env python3
# encoding: utf-8

import discord
import asyncio

from validate_tokens import valid_tokens

with open('message.md') as f:
    EMBED = discord.Embed(title='Warning!', type='rich', description=f.read())


class Bot(discord.Client):
    async def on_ready(self):
        """Run when the bot is ready."""

        print('connected as %s. ' % self.user.name, end='')

        for guild in self.guilds:
            print()
            for channel in guild.text_channels:
                await self.send_warning(channel)

        await self.logout()
        print('Logged out.')

    async def send_warning(self, channel):
        guild_channel = '{} #{}'.format(channel.guild.name, channel.name)
        try:
            await channel.send('', embed=EMBED)
        except:
            print("\t- Couldn't send message in", guild_channel)
        else:
            print('\t- Sent message in', guild_channel)


def main():
    loop = asyncio.get_event_loop()

    for token in valid_tokens():
        print('Logging in... ', end='')
        try:
            loop.run_until_complete(Bot().start(token))
        except KeyboardInterrupt:
            exit()
        except:
            pass


if __name__ == '__main__':
    main()
