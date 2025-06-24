# dipoll/poll.py

# Base libs
from datetime import datetime, timedelta

# External libs
import discord
from apscheduler.triggers.cron import CronTrigger

# DiPoll custom files
import logconf
from config import Globals

# Allows to use 'between' or 'at' depending of the sentence 
def parse_answer(answer):
    day_str, hour_str = answer.split("-")
    if("_" in hour_str):
        hour_str = Globals.POLL_BETWEEN_TEXT + " " + hour_str.replace("_", " " + Globals.POLL_AND_TEXT + " ")
    else:
        hour_str = Globals.POLL_AT_TEXT + " " + hour_str
    return day_str, hour_str

# Parse the wanted schedule. Example with 1-2000 (for Tuesday (1) 20h00 or 8PM), dd=1;hh=20;mm=00
def parse_schedule(schedule):
    try:
        day_str, hour_str = schedule.strip().split("-")
        if len(hour_str) != 4:
            raise ValueError("* Wrong value detected, hour format should be HHMM !")
        dd = int(day_str)
        hh = int(hour_str[:2])
        mm = int(hour_str[2:])
        return dd, hh, mm 
    except Exception as e:
        logconf.logger.error("* Unable to parse the schedule with %s !", schedule)
        logconf.logger.error("* Trace: %s", e)
        raise

# Basically parse all wanted schedules with parse_schedule() and register them as CronTriggers
def register_all_schedules():
    for i, schedule in enumerate(Globals.SCHEDULES.split(",")):
        try:
            dd, hh, mm = parse_schedule(schedule)
            trigger = CronTrigger(day_of_week=dd, hour=hh, minute=mm)
            Globals.scheduler.add_job(schedule_event, trigger=trigger, id=str(i), replace_existing=True)
            logconf.logger.info("* Job scheduled as %s with schedule %s !", i, schedule)
        except Exception as e:
            logconf.logger.error("* Unable to schedule job %s with %s !", i, schedule)
            logconf.logger.error("* Trace: %s", e)
            raise

# Converts the next weekday to text from int
def get_next_weekday_date(target_day):
    if not 0 <= target_day <= 6:
        raise ValueError("* The target day must be between 0 (Monday) and 6 (Sunday).")

    today = datetime.now()
    today_weekday = today.weekday()

    days_ahead = (target_day - today_weekday + 7) % 7
    if days_ahead == 0:
        days_ahead = 7

    next_date = today + timedelta(days=days_ahead)
    day_name = Globals.DAY_MAP_TEXT[target_day]
    date_str = next_date.strftime("%d/%m/%Y")
    return f"{day_name} {date_str}"

# Returns a Discord Channel based on its ID
async def get_channel(channel_id):
    try:
        channel = await Globals.client.fetch_channel(channel_id)
        return channel
    except Exception as e:
        logconf.logger.error("* Could not fetch channel %s !", channel_id)
        logconf.logger.error("* Trace: %s", e)
        raise

# Schedule the wanted event using discord.Poll, it loops over Globals.POLL_ANSWER to add answer and then add the away answer
async def schedule_event():
    logconf.logger.info("* Trying to schedule an event...")
    channel = await get_channel(Globals.CHANNEL_ID)    
    poll = discord.Poll(question=Globals.POLL_TITLE_TEXT, duration=timedelta(hours=Globals.POLL_DURATION_HOURS))

    try:
        for _, answer in enumerate(Globals.POLL_ANSWERS.split(",")):
            day_str, hour_str = parse_answer(answer)
            text = get_next_weekday_date(int(day_str)) + " " + hour_str
            poll.add_answer(text=text, emoji=Globals.YES_EMOTE)
        
        poll.add_answer(text=Globals.POLL_AWAY_TEXT, emoji=Globals.NO_EMOTE)
        poll.multiple = True

        msg = await channel.send(Globals.ROLE_ID, poll=poll)
        if msg:
            logconf.logger.info("* Event successfully scheduled !")
    except Exception as e:
        logconf.logger.error("* Unable to schedule event !")
        logconf.logger.error("* Trace: %s", e)
        raise