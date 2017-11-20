#!/usr/bin/env python3
# encoding: utf-8

import sys
import asyncio

import discord

from validate_tokens import valid_tokens


with open('message.md') as f:
    EMBED = discord.Embed(title='Warning!', type='rich', description=f.read())


class Bot(discord.Client):
    async def on_ready(self):
        """Run when the bot is ready."""

        log('connected as %s. ' % self.user.name, end='')
        await self.warn_owner()
        await self.warn_guilds()
        await self.logout()
        log('Logged out.')

    async def warn_owner(self):
        app_info = await self.application_info()
        owner = app_info.owner
        owner_name = '{0.name}#{0.discriminator}'.format(owner)

        try:
            await owner.send(embed=EMBED)
        except discord.errors.Forbidden:
            log('Failed to send message to', owner_name)
        else:
            log('Sent message to', owner_name)

    async def warn_guilds(self):
        for guild in self.guilds:
            await self.warn_guild(guild)

    async def warn_guild(self, guild):
        first_public_channel = discord.utils.find(
            lambda channel: self.should_warn_channel(channel),
            guild.channels
        )

        await self.warn_channel(first_public_channel)

    async def warn_channel(self, channel):
        guild_channel = '{} #{}'.format(channel.guild.name, channel.name)

        try:
            await channel.send(embed=EMBED)
        except:
            log("\t- Couldn't send message in", guild_channel)
        else:
            log('\t- Sent message in', guild_channel)

    def should_warn_channel(self, channel):
        return (
            isinstance(channel, discord.TextChannel)
            and self.everyone_can_read(channel)
            and self.can_send_messages(channel)
        )

    def everyone_can_read(self, channel: discord.TextChannel):
        everyone = channel.guild.default_role
        overwritten = channel.overwrites_for(everyone).read_messages

        if overwritten is None:
            return everyone.permissions.read_messages
        else:
            return overwritten

    def can_send_messages(self, channel: discord.TextChannel):
        """return whether the client has permissions to message this channel"""

        return channel.guild.me.permissions_in(channel).send_messages


def log(*args, **kwargs):
    kwargs['file'] = sys.stderr
    print(*args, **kwargs)


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
