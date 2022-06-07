from bson.objectid import ObjectId
from naff import Scale, Permissions
from dataclasses import dataclass

"""
This is for your main DB objects.
"""

@dataclass(slots=True)
class User:
    _id: ObjectId
    id: int


@dataclass(slots=True)
class Guild:
    _id: ObjectId
    id: int


class AdminScale(Scale):
    def __init__(self, bot) -> None:
        self.bot = bot
        self.db = bot.db
        self.database = bot.db.db
        self.add_scale_check(self.is_manager)

    async def is_manager(self, ctx):
        return ctx.author.has_permission(Permissions.MANAGE_GUILD)