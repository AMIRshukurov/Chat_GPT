from aiogram.dispatcher.filters.state import StatesGroup, State


class Dialog(StatesGroup):
    start_dialog = State()

