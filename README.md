# Summary
Hello there,<br>
This small Discord bot written in Python3 allows you to schedule events weekly on Discord using the newest [Poll feature](https://discordpy.readthedocs.io/en/latest/api.html?highlight=poll#poll) based on [discord.py package](https://pypi.org/project/discord.py/).
Below you'll find everything you need to use the bot.

# Results
### <p align="center">Poll rendered in Discord</p>
![Rendered](_samples/ui_rendered.png)<br>
### <p align="center">Logs rendered in [Dokémon](https://github.com/productiveops/dokemon)</p>
![Rendered](_samples/logs_rendered.png)<br>

# Requirements
* [Discord.py (2.5.2)](https://pypi.org/project/discord.py/)
* [APScheduler (3.10.4)](https://pypi.org/project/APScheduler/)
* [Docker (28.0.4)](https://docs.docker.com/)
* Knowledge about Docker, environment variables and deployments.
* OPTIONAL: A GUI tool like Dokémon, Rancher, etc...

# Deployment
* Update variables in the ```docker-compose-default-scheduler.yml```
* Build & run the image ```docker compose -f docker-compose-default-scheduler.yml up```
* Check the logs

# Environment variables

# Known bugs
/