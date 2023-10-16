from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram import Bot, Dispatcher
from data.config import Token

bot = Bot(token=Token)

storage = MemoryStorage()

dp = Dispatcher(bot, storage=storage)


__all__ = ['bot', 'storage', 'dp',]
