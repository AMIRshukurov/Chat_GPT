import openai
from aiogram import types
from keyboards.default import Menu, Clear
from utils.states import Dialog
from aiogram.dispatcher import FSMContext
from data.models import session, UserConversation
from loader import dp
import os
from dotenv import load_dotenv
OPENAI_API_KEY=os.getenv("GPT")
load_dotenv()


openai.api_key = OPENAI_API_KEY


@dp.message_handler(text="/start")
async def send_welcome(message: types.Message):
    await message.answer("Choose options", reply_markup=Menu)


@dp.message_handler(text="Write to the bot")
async def start_talk(message: types.Message):
    await message.reply("Hello, I'm a chat bot integrated with ChatGPT 3.5 turbo. How can I help ",reply_markup=Clear)
    await Dialog.start_dialog.set()


@dp.message_handler(state=Dialog.start_dialog)
async def chat_gpt(message: types.Message, state: FSMContext):
    user_message = message.text
    user_id = message.from_user.id

    if user_message == "Clear chat":
        await message.answer("Chat has been cleared", reply_markup=Menu)
        session.query(UserConversation).filter_by(user_id=user_id).update({"message": None})
        session.commit()
        session.close()
        await state.finish()

    else:

        # Получаю историю чата пользователя
        user_conversations = session.query(UserConversation).filter_by(user_id=user_id).all()
        conversation = ""

        for user_conversation in user_conversations:
            conversation += f"You: {user_conversation.message}\nChatGPT {user_conversation.response}\n"

        # Добавляю текущее сообщение пользователя в историю
        conversation += f"You: {user_message}\n"

        # Вызываем модель GPT-3.5-turbo для генерации ответа
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": conversation},
            ]
        )

        bot_response = response['choices'][0]['message']['content']

        # Сохраняем текущий чат в базе данных
        conversation = UserConversation(user_id=user_id, message=user_message, response=bot_response)
        session.add(conversation)
        session.commit()

        await message.answer(bot_response)


