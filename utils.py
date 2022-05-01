from datetime import datetime, timezone
from typing import Optional
from dis_snek import Embed, MISSING

emojis = {
    # Fill with emojis that your bot will use.
}

embed_colors = {
    # Fill with colors that your bot will use in embeds.
}

emoji_name_filter = {
    # extra emoji name translations
}

def emoji(name: str, url: bool = False) -> str:
    if url:
        return f"https://cdn.discordapp.com/emojis/{emoji(name).strip('<>').split(':')[2]}.webp?size=96&quality=lossless"
    else:
        return emojis.get(emoji_name_filter.get(name.lower(), name).lower(), "")

def tryint(s: str) -> int | str:
    try:
        return int(s)
    except ValueError:
        return s

def color(name: str) -> int:
    return embed_colors.get(emoji_name_filter.get(name.lower(), name).lower(), 0x808080)

def time(time: datetime, type: str = 'd') -> str:
    return f"<t:{time.replace(tzinfo=timezone.utc).timestamp():.0f}:{type}>"

def concat(*args) -> str:
    return '\n'.join(args)

def embed(title: Optional[str] = MISSING, description: Optional[str] = MISSING, color: str = MISSING) -> Embed:
    return Embed(
        title=title,
        description=description,
        color=embed_colors.get(color.lower(), 0x2f3136)
    )

def progress(value: int, max: int) -> str:
    return f"{'▰' * value}{'▱' * (max - value)}"