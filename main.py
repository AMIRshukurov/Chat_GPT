
async def on_startup(dp):

    from utils.notify_admin import on_start_notify

    await on_start_notify(dp)


    print('Бот запущен')

    from utils.Commads import set_commands
    await set_commands(dp)


if __name__ == '__main__':
    from aiogram import executor
    from handlers import dp

    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)







