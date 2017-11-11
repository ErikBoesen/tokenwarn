This bot's token is publicly available on GitHub and was detected by this script. Using this token, anyone can take control of your bot and use it to perform malicious actions.

Please consider performing the following steps to assure the security of your bot and server:
* Regenerate your bot's token through the [App Configuration page](https://discordapp.com/developers/applications/me).
* Move token storage to a separate file (even something so simple as `token.txt`) and have your bot read that file when starting.
* Add the file with your token to a file called `.gitignore`, so it isn't committed to GitHub by accident.
* If you're ambitious, rewrite your bot's Git history to remove the token using one of the techniques [here](https://help.github.com/articles/removing-sensitive-data-from-a-repository).

Your token was not used for anything except sending this message. However, the token is public on GitHub, and without steps to protect it, someone with destructive intent may make use of it.

_Code for this message on [GitHub](https://github.com/ErikBoesen/tokenwarn)._
