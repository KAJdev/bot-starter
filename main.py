import dotenv
import logging

import naff
from naff import Snake, listen, Activity, Intents, Status, InteractionContext, ActivityType
from naff.client.errors import CommandCheckFailure

import scales
import db

from os import getenv

dotenv.load_dotenv()
logging.basicConfig()
cls_log = logging.getLogger(naff.logger_name)
cls_log.setLevel(logging.INFO)

bot_log = logging.getLogger(getenv("BOT_NAME", 'bot'))
bot_log.setLevel(logging.DEBUG)

class Bot(Snake):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.db = db.Database()
        
        for module in scales.default:
            self.grow_scale(module)

        self.info = lambda *args, **kwargs: bot_log.info(*args, **kwargs)
        self.debug = lambda *args, **kwargs: bot_log.debug(*args, **kwargs)
        self.error = lambda *args, **kwargs: bot_log.error(*args, **kwargs)

        self.info("-----> Bot object created. Connecting to Gateway.")

    @listen()
    async def on_ready(self):
        self.info("Gateway connected. Bot ready.")

        await self.change_presence(
            activity=None,
            status=Status.ONLINE
        )

    async def on_command_error(self, ctx: InteractionContext, error: Exception):
        match error:
            case CommandCheckFailure():
                if error.check.__name__ == 'is_manager':
                    await ctx.send(f'You must have the `Manage Server` permission to use this command.', ephemeral=True)
                    return
        await super().on_command_error(ctx, error)

if __name__ == "__main__":
    bot = Bot(
        intents=Intents.GUILDS | Intents.MESSAGES,
        sync_interactions=True,
        delete_unused_application_cmds=False,
        activity=Activity(
            name="starting...",
            type=ActivityType.WATCHING
        ),
        status=Status.IDLE,
        total_shards=int(getenv("TOTAL_SHARDS", 1)),
        shard_id=int(getenv("SHARD", 0)),
    )
    bot.start(getenv('TOKEN'))