"""Module for the ``ping`` command."""
from nextcord import Embed, Interaction, SlashOption, slash_command
from nextcord.ext.commands.bot import Bot
from nextcord.ext.commands.cog import Cog
from structlog.stdlib import get_logger

from pinger_bot.config import gettext as _
from pinger_bot.helpers import OnCommand

log = get_logger()


class PingCommandCog(Cog):
    """Cog for the ``ping`` command."""

    def __init__(self, bot: Bot) -> None:
        """__init__ method."""
        self.bot = bot

    @slash_command(description=_("Ping the server and give information about it."))
    async def ping(
        self,
        interaction: Interaction,
        ip: str = SlashOption(
            description=_("The IP address of the server."),
            required=True,
        ),
    ) -> None:
        """Ping the server and give information about it."""
        OnCommand(__name__, interaction, ip=ip)
        embed = Embed(title=_("Ping Results"))
        await interaction.response.send_message(embed=embed)


def setup(bot):
    """Default setup function."""
    bot.add_cog(PingCommandCog(bot))
