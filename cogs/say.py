import disnake
from disnake.ext import commands
from disnake.ext.commands import slash_command, user_command, message_command


class Say(commands.Cog):
    def __init__(self, bot):
        self.bot: commands.Bot = bot

    @commands.is_owner()
    @slash_command(
    name='say',
    description='🦜',
    )
    async def ping(inter: disnake.ApplicationCommandInteraction, message: str):
        await inter.response.send_message(message)
    

def setup(bot):
    bot.add_cog(Say(bot))
    print(f"COG: Extension {__name__} is ready")