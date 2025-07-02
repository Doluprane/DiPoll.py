# Summary
Hello there,<br>
This small Discord bot written in Python3 allows you to schedule events weekly on Discord using the newest [Poll feature](https://discordpy.readthedocs.io/en/latest/api.html?highlight=poll#poll) based on [discord.py package](https://pypi.org/project/discord.py/).
Below you'll find everything you need to use the bot.

# Results
### Poll rendered in Discord
![Rendered](_samples/ui_rendered.png)<br>
### Logs rendered in [Dokémon](https://github.com/productiveops/dokemon)
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
    - Format: encapsulated string: ```<@&154785693>```
* CHANNEL_ID
    - Defines the channel ID to send the poll in
    - Format: string: ```154785693```
* BOT_OWNER_ID
    - Defines the owner ID to filter over commands
    - Format: string: ```154785693```
* TOKEN
    - Defines the Discord token ([see docs](https://discord.com/developers))
    - Format: string: ```154785693```
* NOTIFY
    - Defines the notification settings; with False, the bot will be used with commands only
    - Format: boolean: ```True``` or ```False```
## Commands
* PREFIX_CMD
    - Defines the prefix to add for all commands
    - Format: string: ```_es```
* FORCE_SCHEDULE_CMD
    - Defines comand to force the poll, it will be ```<PREFIX_CMD><FORCE_SCHEDULE_CMD>```
    - Format: string: ```_force```
* ENABLE_SCHEDULER_CMD
    - Defines the command to enable notifications, it will be ```<PREFIX_CMD><ENABLE_SCHEDULER_CMD>```
    - Format: string: ```_enable```
* DISABLE_SCHEDULER_CMD
    - Defines the command to disable notifications, it will be ```<PREFIX_CMD><DISABLE_SCHEDULER_CMD>```
    - Format: string: ```_disable```
## Emojis ([see full list](https://www.prosettings.com/emoji-list/))
* YES_EMOTE
    - Defines the emoji for the yes option
    - Format: string: ```\U00002705```
* NO_EMOTE
    - Defines the emoji for the no option
    - Format: string: ```\U0000274C```
* WARN_EMOTE
    - Defines the emoji for the warning answer (bot's answer if unknown command sent)
    - Format: string: ```\U000026A0```
## Poll settings
* SCHEDULES
    - Defines schedules when the poll is sent
    - Format: ```<WEEKDAY>-<HOUR>```
    - Format: weekday: ```0``` (Monday) to ```6``` (Sunday)
    - Format: hour: HHMM in 24-hours format
    - Format: string: ```5-1830```
    - Format: comma-separated if multiple schedules ```5-1830,6-1000```
* POLL_DURATION_HOURS
    - Defines the duration of the poll in hours
    - Format: integer: ```90```
* POLL_ANSWERS: 
    - Defines available answers for the poll 
    - Format: ```<WEEKDAY>-<HOUR>```
    - Format: weekday: ```0``` (Monday) to ```6``` (Sunday)
    - Format: hour: if you use ```15h00_15h30``` it will render as ```between 15h00 and 15h30```
    - Format: hour: if you use ```18h00``` it will render as ```at 18h00```
    - Format: hour: you can use any hour format here, ```8PM_8:30PM``` will be rendered as ```between 8PM and 8:30PM```
    - Format: string: ```01-15h00_15h30```
    - Format: comma-separated if multiple answers ```01-15h00_15h30,03-18h00```
## Localization
* ACTIVITY_TEXT: "Event Scheduler"
    - Defines the bot's activity in Discord
    - Format: string
* POLL_TITLE_TEXT: "Next Game Session"
    - Defines the poll title
    - Format: string
* POLL_AWAY_TEXT: "Away"
    - Defines the last poll option
    - Format: string
* POLL_BETWEEN_TEXT: "between"
    - Defines the replacement for ```between``` in ```POLL_ANSWERS```
    - Format: string
* POLL_AND_TEXT: "and"
    - Defines the replacement for ```and``` in ```POLL_ANSWERS```
    - Format: string
* POLL_AT_TEXT: "at"
    - Defines the replacement for ```at``` in ```POLL_ANSWERS```
    - Format: string
* MONDAY_TEXT: "Monday"
    - Defines the replacement for ```Monday```
    - Format: string
* TUESDAY_TEXT: "Tuesday"
    - Defines the replacement for ```Tuesday```
    - Format: string
* WEDNESDAY_TEXT: "Wednesday"
    - Defines the replacement for ```Wednesday```
    - Format: string
* THURSDAY_TEXT: "Thursday"
    - Defines the replacement for ```Thursday```
    - Format: string
* FRIDAY_TEXT: "Friday"
    - Defines the replacement for ```Friday```
    - Format: string
* SATURDAY_TEXT: "Saturday"
    - Defines the replacement for ```Saturday```
    - Format: string
* SUNDAY_TEXT: "Sunday"
    - Defines the replacement for ```Sunday```
    - Format: string

# Known bugs
/