This bot's token is publicly available on GitHub and was detected by this script. Using this token, anyone can take control of your bot and use it to perform malicious actions.

Please consider performing the following steps to assure the security of your bot and server:
* Regenerate your bot's token through the [App Configuration page](https://discordapp.com/developers/applications/me).
* Move token storage to a separate file (even something so simple as `token.txt`) and programatically reading from that file when starting your bot.
* Add the file with your token to the `.gitignore` file, so it isn't committed to GitHub again.
* If you're ambitious, rewrite your bot's Git history to remove the token using one of the techniques [here](https://help.github.com/articles/removing-sensitive-data-from-a-repository).

Your token was not used for anything except sending this message. However, the token is public on GitHub, and without steps to protect it, someone with destructive intent may make use of it.

_Warning by Erik Boesen. Check out the code on [GitHub](https://github.com/ErikBoesen/tokenwarn)._
