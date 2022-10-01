from typing import Any

from nonebot.log import logger
from telethon import TelegramClient

from ..config import config

proxy = None
if config.rss_proxy:
    proxy = (
        "http",
        config.rss_proxy.split(":")[0],
        int(config.rss_proxy.split(":")[1]),
    )

bot = None


async def start_telegram_bot(loop: Any, boot_message: str) -> None:
    if not (
        config.telegram_api_id
        and config.telegram_api_hash
        and config.telegram_bot_token
    ):
        return
    global bot
    bot = TelegramClient(
        "bot",
        config.telegram_api_id,
        config.telegram_api_hash,
        proxy=proxy,
        loop=loop,
    )
    if bot:
        from . import telegram_command
    bot.start(bot_token=config.telegram_bot_token)
    logger.success("Telegram Bot Started")
    if config.telegram_admin_id:
        await bot.send_message(
            config.telegram_admin_id,
            boot_message,
        )