# dipoll/config.py

# Base libs
import os
from enum import Enum

# External libs
import discord
from apscheduler.schedulers.asyncio import AsyncIOScheduler

class Globals:
    # os.environ[] is used for critical values because if not found, it will raise a KeyError
    # os.getenv() is used for other values because if not found, it will use the default ones
    
    # Consts
    # Role to mention in Discord
    ROLE_ID = os.environ["ROLE_ID"]
    # Channel to schedule the event
    CHANNEL_ID = os.environ["CHANNEL_ID"]
    # Discord API token
    TOKEN = os.environ["TOKEN"]
    # User ID of the bot's owner
    BOT_OWNER_ID = os.environ["BOT_OWNER_ID"]
    # Prefix of bot's commands
    # default: _es (Event Scheduler)
    PREFIX_CMD = os.getenv("PREFIX_CMD", "_es")
    # All commands available. In Discord you'll have to use <PREFIX_CMD><FORCE_SCHEDULE_CMD> for example.
    # default: _force
    FORCE_SCHEDULE_CMD = os.getenv("FORCE_SCHEDULE_CMD", "_force")
    # default: _enable
    ENABLE_SCHEDULER_CMD = os.getenv("ENABLE_SCHEDULER_CMD", "_enable")
    # default: _disable
    DISABLE_SCHEDULER_CMD = os.getenv("DISABLE_SCHEDULER_CMD", "_disable")
    # Unicode emojis for Discord 
    # default: \U00002705
    YES_EMOTE = os.getenv("YES_EMOTE", '\U00002705')
    # default: \U0000274C
    NO_EMOTE = os.getenv("NO_EMOTE", '\U0000274C')
    # default: \U000026A0
    WARN_EMOTE = os.getenv("WARN_EMOTE", '\U000026A0')
    # This example schedules the mesage for Tuesday at 8PM (24 hours format). Days are mapped from 0 (Monday) to 6 (Sunday). Multiple values are comma separated.
    # default: 0-1200 (Monday at 12h00 or 12PM)
    SCHEDULES = os.getenv("SCHEDULES", "0-1200")
    # Duration of the poll. At the end, it will be closed and no one will be available to choose an option.
    # default: 24 (Can be for example 2.5)
    POLL_DURATION_HOURS = float(os.getenv("POLL_DURATION_HOURS", 24))
    # Available answers for the poll. In this example, it's: between 15h00 (3PM) and 15h20 (3:30PM) for day 1 (Tuesday) and 18h00 (6PM) for day 3 (Thursday)
    # default: 01-15h00_15h30,03-18h00
    POLL_ANSWERS = os.getenv("POLL_ANSWERS", "01-15h00_15h30,03-18h00")
    # Registering all loggers
    LOGGERS = [
        'apscheduler',
        'discord',
        'discord.http',
        'discord.client',
        'discord.gateway',
    ]
        
    # Localization (English by default)
    # Activity shown in Discord 
    # default: DiPoll - Event Scheduler
    ACTIVITY_TEXT = os.getenv("ACTIVITY_TEXT", "DiPoll - Event Scheduler")
    # Title of the poll
    # default: Next Game Session
    POLL_TITLE_TEXT = os.getenv("POLL_TITLE_TEXT", "Next Game Session")
    # Text for the last answer
    # default: Away
    POLL_AWAY_TEXT = os.getenv("POLL_AWAY_TEXT", "Away")
    # Translation for 'between'
    # default: between
    POLL_BETWEEN_TEXT = os.getenv("POLL_BETWEEN_TEXT", "between")
    # Translation for 'and'
    # default: and
    POLL_AND_TEXT = os.getenv("POLL_AND_TEXT", "and")
    # Translation for 'at'
    # default: at
    POLL_AT_TEXT = os.getenv("POLL_AT_TEXT", "at")
    # Translation for 'Monday'
    # default: Monday
    MONDAY_TEXT = os.getenv("MONDAY_TEXT", "Monday")
    # Translation for 'Tuesday'
    # default: Tuesday
    TUESDAY_TEXT = os.getenv("TUESDAY_TEXT", "Tuesday")
    # Translation for 'Wednesday'
    # default: Wednesday
    WEDNESDAY_TEXT = os.getenv("WEDNESDAY_TEXT", "Wednesday")
    # Translation for 'Thursday'
    # default: Thursday
    THURSDAY_TEXT = os.getenv("THURSDAY_TEXT", "Thursday")
    # Translation for 'Friday'
    # default: Friday
    FRIDAY_TEXT = os.getenv("FRIDAY_TEXT", "Friday")
    # Translation for 'Saturday'
    # default: Saturday
    SATURDAY_TEXT = os.getenv("SATURDAY_TEXT", "Saturday")
    # Translation for 'Sunday'
    # default: Sunday
    SUNDAY_TEXT = os.getenv("SUNDAY_TEXT", "Sunday")

    ### Non-consts
    notify = os.getenv("NOTIFY", "true").lower() in ("1", "true", "yes")
    client = discord.Client(intents=discord.Intents.all())
    scheduler = AsyncIOScheduler()

    DAY_MAP_TEXT = {
        0: MONDAY_TEXT,
        1: TUESDAY_TEXT,
        2: WEDNESDAY_TEXT,
        3: THURSDAY_TEXT,
        4: FRIDAY_TEXT,
        5: SATURDAY_TEXT,
        6: SUNDAY_TEXT
    }

class Commands(str, Enum):
    FORCE = Globals.PREFIX_CMD + Globals.FORCE_SCHEDULE_CMD
    ENABLE = Globals.PREFIX_CMD + Globals.ENABLE_SCHEDULER_CMD
    DISABLE = Globals.PREFIX_CMD + Globals.DISABLE_SCHEDULER_CMD