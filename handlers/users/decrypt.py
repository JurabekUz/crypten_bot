from aiogram import types
from aiogram.dispatcher import FSMContext

from keyboards.inline.tugma import coursesMenu, Ulashish, categoryMenu
from states.states import StateData
from keyboards.inline.callback import *
from utils import sezer_al, vij_al, A5_1

from loader import dp

matn = "<b>Yana bir bor Salom</b>\n"
matn += "❗️<b>ESLATMA</b> " \
        "<i>Matn qaysi usulda shifrlangan bo'lsa shu usulda dishifrlash kerak bo'ladi.</i>\n"
matn += "Variantlardan birini tanglang\n"
matn += "1️⃣ Sezer usuli 'Shifr matn harflardan imorat bo'ladi'\n"
matn += "2️⃣ Vijiner usuli 'Shifr matn harflardan imorat bo'ladi'\n"
matn += "3️⃣ A5-1 usuli 'Shifr matn 0 va 1 lardan imorat bo'ladi'\n"

@dp.message_handler(commands='dishifrlash',state='*')
async def bot_start(message: types.Message):
    await StateData.dishifrla.set()
    await message.answer(matn,reply_markup=coursesMenu)

@dp.callback_query_handler(text='decrypt',state='*')
async def bot_start(call: types.CallbackQuery):
    await StateData.dishifrla.set()
    await call.message.answer(matn,reply_markup=coursesMenu)
    await call.answer(cache_time=60)

# cancel handler
@dp.callback_query_handler(text="cancel",state=StateData.dishifrla)
async def cancel_handler(call: types.CallbackQuery,state: FSMContext):
    await  call.message.delete()
    await call.answer(cache_time=60)
    await state.finish()

# Usul tanlash
@dp.callback_query_handler(shifr_callback.filter(item_name='sezer'),state=StateData.dishifrla)
async def start(call: types.CallbackQuery):
    await StateData.disezer.set()
    await call.message.answer("✅ Sezer dishifrlash usuli\nMatn yuboring")
    await call.message.delete()

@dp.callback_query_handler(shifr_callback.filter(item_name='vijiner'),state=StateData.dishifrla)
async def bot_start(call: types.CallbackQuery):
    await StateData.divij.set()
    await call.message.answer("✅ Vijiner dishifrlash usuli\nMatn yuboring")
    await call.message.delete()

@dp.callback_query_handler(shifr_callback.filter(item_name='a5_1'),state=StateData.dishifrla)
async def bot_start(call: types.CallbackQuery):
    await StateData.diAbesh.set()
    await call.message.answer("✅ A5-1 dishifrlash usuli\nMatn yuboring")
    await call.message.delete()


# usul boyicha shirfrlash
# sezer usuli
@dp.message_handler(content_types='text', state=StateData.disezer)
async def sezerEncrypt(message: types.Message):
    mes = message.text
    key = 11
    res = sezer_al.cipher_decrypt(mes, key)
    await message.answer(f"Shifrlash usuli: Sezer \nMaxfiy kalit(son): 11 ")
    await message.reply(f" Dishifr matn(asl matn): \n{res}")
    await message.answer("<b>Matnlarni shifrlovchi bot</b>\n Bot sizga yoqqan bo'lsa do'stlaringiz bilan baham ko'ring",reply_markup=Ulashish)

# vijiner usuli
@dp.message_handler(content_types='text', state=StateData.divij)
async def usul(message: types.Message):
    mes = message.text
    key1 = 'VIJINER'
    key = vij_al.generateKey(mes, key1)
    res = vij_al.originalText(mes, key)
    await message.answer(f"Shifrlash usuli: Vijiner \nMaxfiy kalit(so'z): VIJINER")
    await message.reply(f"Dishifr matn:(asl matn) \n{res}")
    await message.answer("<b>Matnlarni shifrlovchi bot</b>\n Bot sizga yoqqan bo'lsa do'stlaringiz bilan baham ko'ring",reply_markup=Ulashish)

# a5-1 usuli
@dp.message_handler(content_types='text', state=StateData.diAbesh)
async def usul(message: types.Message):
    mes = message.text
    res = A5_1.decrypt_main(mes)
    await message.answer(
        f"Shifrlash usuli: A5-1 \nMaxfiy kalit: 1101001000011010110001110001100100101001000000110111111010110111")
    await message.reply(f"<b>Dishifr matn: (asl matn)</b> \n{res}")
    await message.answer("<b>Matnlarni shifrlovchi bot</b>\n Bot sizga yoqqan bo'lsa do'stlaringiz bilan baham ko'ring",reply_markup=Ulashish)


@dp.callback_query_handler(text="boshiga",state=StateData.divij)
@dp.callback_query_handler(text="boshiga",state=StateData.disezer)
@dp.callback_query_handler(text="boshiga",state=StateData.diAbesh)
async def cancel_buying(call: types.CallbackQuery,state: FSMContext):
    await call.message.answer(matn, reply_markup=categoryMenu)
    await call.answer(cache_time=60)
    await StateData.dishifrla.set()