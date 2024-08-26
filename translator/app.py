import logging
from aiogram import Bot, Dispatcher, executor, types

from create import create_db
from insert import insert_user
# from insert import select_user
from tarjima import en_uz, uz_en, uz_ru, ru_uz, en_ru, ru_en

bot = Bot(token='7393568188:AAEVSsPg4n7ChSoF6X8LI2paMRZ0m9WqN2c')
logging.basicConfig(level=logging.INFO)
dp = Dispatcher(bot=bot)

d = {'language': 'en_uz'}


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    create_db()
    try:
        insert_user(message.from_user.username, message.from_id)
    except Exception as e:
        print(e)
        pass
    await message.answer(f'Assalomu alekum {message.from_user.full_name}', reply_markup=None)
    if d['language'] == 'en_uz':
        await message.answer('Siz English -> Uzbek bo\'limidasiz!')
    elif d['language'] == 'uz_en':
        await message.answer('Siz Uzbek -> English bo\'limidasiz!')


@dp.message_handler(commands=['uz   _en'])
async def uzen(message: types.Message):
    await message.answer('Siz Uzbek -> English bo\'limidasiz!')
    d.update({'language': 'uz_en'})


@dp.message_handler(commands=['en_uz'])
async def enuz(message: types.Message):
    await message.answer('Siz English -> Uzbek bo\'limidasiz!')
    d.update({'language': 'en_uz'})


@dp.message_handler(commands=['uz_ru'])
async def uzru(message: types.Message):
    await message.answer('Siz Uzbek -> Russian bo\'limidasiz!')
    d.update({'language': 'uz_ru'})


@dp.message_handler(commands=['ru_uz'])
async def ruuz(message: types.Message):
    await message.answer('Siz Russian -> Uzbek bo\'limidasiz!')
    d.update({'language': 'ru_uz'})


@dp.message_handler(commands=['en_ru'])
async def enru(message: types.Message):
    await message.answer('Siz English -> Russian bo\'limidasiz!')
    d.update({'language': 'en_ru'})


@dp.message_handler(commands=['ru_en'])
async def ruen(message: types.Message):
    await message.answer('Siz Russian -> English bo\'limidasiz!')


# @dp.message_handler(text='admin')
# async def admin(message: types.Message):
#     if message.from_id == 1038185913:
#         for i in select_user():
#             await bot.send_message(chat_id=i, text='Qovunlar komandasi')
#     else:
#         await message.answer("Sog'bulas qovun aka yoki opa")


@dp.message_handler()
async def translator(message: types.Message):
    if d.get('language') == 'en_uz':
        await message.answer(en_uz(message.text))
    elif d.get('language') == 'uz_en':
        await message.answer(uz_en(message.text))
    elif d.get('language') == 'uz_ru':
        await message.answer(uz_ru(message.text))
    elif d.get('language') == 'ru_uz':
        await message.answer(ru_uz(message.text))
    elif d.get('language') == 'en_ru':
        await message.answer(en_ru(message.text))
    elif d.get('language') == 'ru_en':
        await message.answer(ru_en(message.text))

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
