from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

Menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Write to the bot")
        ]

    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

Clear = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Clear chat")
        ]

    ],
    resize_keyboard=True,
    one_time_keyboard=True
)