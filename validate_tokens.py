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
        raise InvalidResponseError


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
        sys.stdout.flush()
    SESSION.close()


if __name__ == '__main__':
    main()
