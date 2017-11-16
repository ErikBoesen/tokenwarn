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
#!/usr/bin/env python3
# encoding: utf-8

import yaml
from github import Github
import base64
import re

TOKEN_RE = re.compile('M[A-Za-z0-9-_.]{58}')

def get_gh():
    with open('config.yml', 'r') as f:
        cfg = yaml.load(f)

    if 'gh_token' in cfg:
        gh = Github(cfg['gh_token'])
    else:
        gh = Github(cfg['gh_username'], cfg['gh_password'])
    return gh


def scrape(gh):
    for f in gh.search_code('discord Mz'):
        try:
            code = base64.b64decode(f.content).decode()
            token = re.search(TOKEN_RE, code).group(0)
        except KeyboardInterrupt:
            return
        except:
            print('Error parsing result.')
        else:
            write_token(token)


def write_token(token):
    global tokens
    global f

    if token not in tokens:
        tokens.add(token)
        f.write(token + '\n')
        print('Found new token', token)


def main():
    global tokens
    global f

    tokens = set()
    f = open('tokens.txt', 'w')

    scrape(get_gh())

    f.close()

if __name__ == '__main__':
    main()
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
    main()#!/usr/bin/env python3
# encoding: utf-8

import yaml
from github import Github
import base64
import re

TOKEN_RE = re.compile('M[A-Za-z0-9-_.]{58}')

def get_gh():
    with open('config.yml', 'r') as f:
        cfg = yaml.load(f)

    if 'gh_token' in cfg:
        gh = Github(cfg['gh_token'])
    else:
        gh = Github(cfg['gh_username'], cfg['gh_password'])
    return gh


def scrape(gh):
    for f in gh.search_code('discord Mz'):
        try:
            code = base64.b64decode(f.content).decode()
            token = re.search(TOKEN_RE, code).group(0)
        except KeyboardInterrupt:
            return
        except:
            print('Error parsing result.')
        else:
            write_token(token)


def write_token(token):
    global tokens
    global f

    if token not in tokens:
        tokens.add(token)
        f.write(token + '\n')
        print('Found new token', token)


def main():
    global tokens
    global f

    tokens = set()
    f = open('tokens.txt', 'w')

    scrape(get_gh())

    f.close()

if __name__ == '__main__':
    main()
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
    main()#!/usr/bin/env python3
# encoding: utf-8

import yaml
from github import Github
import base64
import re

TOKEN_RE = re.compile('M[A-Za-z0-9-_.]{58}')

def get_gh():
    with open('config.yml', 'r') as f:
        cfg = yaml.load(f)

    if 'gh_token' in cfg:
        gh = Github(cfg['gh_token'])
    else:
        gh = Github(cfg['gh_username'], cfg['gh_password'])
    return gh


def scrape(gh):
    for f in gh.search_code('discord Mz'):
        try:
            code = base64.b64decode(f.content).decode()
            token = re.search(TOKEN_RE, code).group(0)
        except KeyboardInterrupt:
            return
        except:
            print('Error parsing result.')
        else:
            write_token(token)


def write_token(token):
    global tokens
    global f

    if token not in tokens:
        tokens.add(token)
        f.write(token + '\n')
        print('Found new token', token)


def main():
    global tokens
    global f

    tokens = set()
    f = open('tokens.txt', 'w')

    scrape(get_gh())

    f.close()

if __name__ == '__main__':
    main()
#!/usr/bin/env python3
# encoding: utf-8

import sys

import asyncio
import aiohttp


SESSION = aiohttp.ClientSession()
LOOP = asyncio.get_event_loop()


async def valid_token(token):
    async with SESSION.get(
        'https://discordapp.com/api/v6/gateway/bot',
        headers={'Authorization': 'Bot ' + token},
    ) as resp:
        if resp.status == 200:
            return True
        elif resp.status == 401:
            return False
        raise InvalidResponseError('invalid token')


def valid_tokens():
    with open('tokens.txt') as input_file:
        tokens = {token.strip() for token in input_file if token}

    for token in tokens:
        if LOOP.run_until_complete(valid_token(token)):
            yield token


def log(*args, **kwargs):
    kwargs['file'] = sys.stderr
    print(*args, **kwargs)


class InvalidResponseError(Exception):
    """
    raised when the Discord API does not conclusively say
    whether a token is valid
    """

    pass


def main():
    for token in valid_tokens():
        print(token)


if __name__ == '__main__':
    main()
