# dipoll/event.py

# Base libs
import os

# External libs
import discord

# DiPoll custom files
from config import Globals, Commands
import poll
import logconf

@Globals.client.event
# Trying to read each message and follow a workflow it the bot can handle it
async def on_message(message):
    try:
        if (message.author.id == int(Globals.BOT_OWNER_ID)):
            if (message.content.startswith(Globals.PREFIX_CMD)):
                match message.content:
                    case Commands.FORCE:
                        logconf.logger.info("* Force schedule asked by %s@%s@%s.", message.author.name, message.author.id, message.id)
                        await poll.schedule_event()
                        await message.delete()
                    case Commands.DISABLE:
                        Globals.notify = False
                        logconf.logger.info("* Disable notify asked by %s@%s@%s.", message.author.name, message.author.id, message.id)
                        await message.delete()
                    case Commands.ENABLE:
                        Globals.notify = True
                        logconf.logger.info("* Enable notify asked by %s@%s@%s.", message.author.name, message.author.id, message.id)
                        await message.delete()
                    case _:
                        logconf.logger.warning("* Unknown command from %s@%s@%s : %s.", message.author.name, message.author.id, message.id, message.content)
                        await message.add_reaction(Globals.WARN_EMOTE)
    except Exception as e:
        logconf.logger.error("* Unable to read the message !")
        logconf.logger.error("* Trace: %s", e)
        raise

@Globals.client.event
# This triggers when the bot is connected to the official Discord API and basically init everything
async def on_ready():
    await Globals.client.change_presence(activity=discord.Game(name=Globals.ACTIVITY_TEXT))
    logconf.logger.info("***** Starting Initialization")
    logconf.logger.info("* Name: %s ", Globals.client.user.name)
    logconf.logger.info("* PID: %s", os.getpid())
    logconf.logger.info("* UID: %s", Globals.client.user.id)
    logconf.logger.info("* CID: %s", Globals.CHANNEL_ID)
    logconf.logger.info("* RID: %s", Globals.ROLE_ID)
    logconf.logger.info("* OID: %s", Globals.BOT_OWNER_ID)
    logconf.logger.info("* Notifications: %s", "Enabled" if Globals.notify else "Disabled")
    logconf.logger.info("***** End of Initialization")
    logconf.logger.info("")
    logconf.logger.info("***** Registering job(s)...")
    poll.register_all_schedules()
    logconf.logger.info("***** Job(s) registered !")
    logconf.logger.info("")
    logconf.logger.info("***** Starting scheduler...")
    Globals.scheduler.start()
    logconf.logger.info("***** Scheduler started !")
    logconf.logger.info("")
    logconf.logger.info("* Entering the -READY- state. Sleeping...")
    logconf.logger.info("")