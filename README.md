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
* Knowledge about Docker, environment variables and deployments
* OPTIONAL: A GUI tool like Dokémon, Rancher, etc...

# Deployment
* Update variables in the ```docker-compose-default-scheduler.yml```
* Build & run the image ```docker compose -f docker-compose-default-scheduler.yml up```
* Check the logs

# Environment variables
## Basics
* ROLE_ID
    - Defines the role ID to mention with the poll
    - Format: encapsulated string: '<@&154785693>'
* CHANNEL_ID
    - Defines the channel ID to send the poll in
    - Format: basic string: '154785693'
* BOT_OWNER_ID
    - Defines the owner ID to filter over commands
    - Format: basic string: '154785693'
* TOKEN
    - Defines the Discord token ([see docs](https://discord.com/developers))
    - Format: basic string: '154785693'
* NOTIFY
    - Defines the notification settings; with False, the bot will be used with commands only
    - Format: boolean: 'True' or 'False'
## Commands
* PREFIX_CMD
    - Defines the prefix to add for all commands
    - Format: basic string: '_es'
* FORCE_SCHEDULE_CMD
    - Defines comand to force the poll, it will be <PREFIX_CMD><FORCE_SCHEDULE_CMD>
    - Format: basic string: '_force'
* ENABLE_SCHEDULER_CMD
    - Defines the command to enable notifications, it will be <PREFIX_CMD><ENABLE_SCHEDULER_CMD>
    - Format: basic string: '_enable'
* DISABLE_SCHEDULER_CMD
    - Defines the command to disable notifications, it will be <PREFIX_CMD><DISABLE_SCHEDULER_CMD>
    - Format: basic string: '_disable'
## Emojis ([see full list](https://www.prosettings.com/emoji-list/))
* YES_EMOTE
    - Defines the emoji for the yes option
    - Format: encoded string: '\U00002705'
* NO_EMOTE
    - Defines the emoji for the no option
    - Format: encoded string: '\U0000274C'
* WARN_EMOTE
    - Defines the emoji for the warning answer (bot's answer if unknown command sent)
    - Format: encoded string: '\U000026A0'
## Poll settings
* SCHEDULES
    - Defines schedules when the poll is sent
    - Format: <WEEKDAY>-<HOUR>
    - Format: Weekday: 0 (Monday) to 6 (Sunday)
    - Format: Hour: HHMM in 24-hours format
    - Format: basic string: '5-1830'
    - Format: comma-separated if multiple schedules '5-1830,6-1000'
* POLL_DURATION_HOURS
    - Defines the duration of the poll in hours
    - Format: int: '90'
* POLL_ANSWERS: "01-15h00_15h30,03-18h00"
    - Defines available answers for the poll 

# Known bugs
/