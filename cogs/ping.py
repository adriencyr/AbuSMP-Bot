import disnake
from disnake.ext import commands
from disnake.ext.commands import slash_command, user_command, message_command


class Ping(commands.Cog):
    def __init__(self, bot):
        self.bot: commands.Bot = bot

    @slash_command(
    name='ping',
    description='Returns websocket latency in seconds (s).',
    )
    async def ping(self, inter: disnake.ApplicationCommandInteraction):
        await inter.response.send_message(':ping_pong: Pong! `{0}s`'.format(round(self.bot.latency, 1)))
    

def setup(bot):
    bot.add_cog(Ping(bot))
    print(f"COG: Extension {__name__} is ready")