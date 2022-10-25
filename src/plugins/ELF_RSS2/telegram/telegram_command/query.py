import asyncio

from telethon import events
from .permission import handle_permission
from ...telegram import bot
from .start import RssCommands
from .telegram_command import InputButton, wait_btn_callback

QueryCommandFields = [
    # TODO
]


@bot.on(events.CallbackQuery(data=RssCommands.query.command, func=lambda e: handle_permission(e)))  # type: ignore
async def change(event: events.CallbackQuery.Event) -> None:
    await event.delete()

    btns = [
        InputButton(field.description, data=field.key) for field in QueryCommandFields
    ]
    try:
        # 等待用户选择需要修改的字段
        field_key = await wait_btn_callback(
            bot,
            event,
            tips_text="选择需要修改的字段",
            btns=btns,
        )
        if field_key == "query_all":
            # TODO
            pass
        elif field_key == "query_this":
            # TODO
            pass

    except asyncio.TimeoutError:
        pass
    except Exception as e:
        print(e)
