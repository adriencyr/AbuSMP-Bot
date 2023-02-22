import time, disnake, json, os
from urllib.request import urlopen
from disnake.ext import commands, tasks

time.sleep(5.9)


command_sync_flags= commands.CommandSyncFlags.default()
command_sync_flags.sync_commands_debug = True

bot = commands.InteractionBot(
    intents=disnake.Intents.all(),
    command_sync_flags=command_sync_flags,
    test_guilds=[1075115748617355316],
)
    

@bot.event
async def on_ready():
    print(f'BOT: Logged in as {bot.user}')
   
@tasks.loop(minutes=5.0)
async def status_task():
    status = urlopen('https://api.mcsrvstat.us/2/66.70.207.82:25588')
    status_json = json.loads(status.read())
    await bot.change_presence(activity = disnake.Activity(type=disnake.ActivityType.playing, name='AbuSMP | ' + str(status_json["players"]["online"]) + ' online'))


if __name__ in '__main__':
    path = f"cogs"
    folder = f"cogs"
    
    for name in os.listdir(folder):
        if name.endswith('.py') and os.path.isfile(f"cogs/{name}"):
            bot.load_extension(f"{path}.{name[:-3]}")

@commands.is_owner()
@bot.slash_command(
    name='reload',
    description='Reloads specified cog or all cogs if none specified (bot owner only).',
)
async def reloadCogs(inter: disnake.ApplicationCommandInteraction, cog = None):
    try:
        if __name__ in '__main__':
            if cog is None:
                for nam in os.listdir(folder):
                    if nam.endswith('.py') and os.path.isfile(f"cogs/{nam}"):
                        bot.reload_extension(f"{path}.{nam[:-3]}")
                        await inter.response.send_message(f':gear: Reloading all cogs')
            else:
                bot.reload_extension(f"{path}.{cog}")
                await inter.response.send_message(f':gear: Reloading cog `{cog}`')
    except Exception as e:
        print({e})
        await inter.response.send_message(f':x: Exception when running reload task: `{e}`')
        
@commands.is_owner()
@bot.slash_command(
    name='load',
    description='Loads specified cog (bot owner only).'
)
async def loadCog(inter: disnake.ApplicationCommandInteraction, cog: str):
    try:
        bot.load_extension(f'{path}.{cog}')
        await inter.response.send_message(f':gear: Loading cog `{cog}`')
    except Exception as e:
        print({e})
        await inter.response.send_message(f':x: Exception when running load task: `{e}`')     
        
@commands.is_owner()
@bot.slash_command(
    name='unload',
    description='Unloads specified cog (bot owner only).'
)
async def unloadCog(inter: disnake.ApplicationCommandInteraction, cog: str):
    try:
        bot.unload_extension(f'{path}.{cog}')
        await inter.response.send_message(f':gear: Unloading cog `{cog}`')
    except Exception as e:
        print({e})
        await inter.response.send_message(f':x: Exception when running unload task: `{e}`')                   


#status = urlopen('https://api.mcsrvstat.us/2/66.70.207.82:25588')
#status_json = json.loads(status.read())

#activity = disnake.Game(name='AbuSMP | ' + str(status_json["players"]["online"]) + ' online', type=3)    


bot.run('MTA3NTE1MTk3MzY1OTE5MzM2NQ.G7swDd.CErzUab6_5_-J1AeondtvEdrOyyTFXdb33Hub0')