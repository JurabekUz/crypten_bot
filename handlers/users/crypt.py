from aiogram import types
from aiogram.dispatcher import FSMContext
from keyboards.inline.tugma import coursesMenu,Ulashish,categoryMenu
from keyboards.inline.callback import *
from states.states import StateData
from utils import sezer_al, vij_al, A5_1
import re
from loader import dp

matn = "<b>Siz yuborgan matn qaysi usulda shifrlansin</b>\n"
matn += "1️⃣ Sezer usuli - Shifr matn harflardan imorat bo'ladi\n"
matn += "2️⃣ Vijiner usuli - Shifr matn harflarsdan imorat bo'ladi\n"
matn += "3️⃣ A5-1 usuli - Shifr matn 0 va 1 lardan imorat bo'ladi\n"
matn += "❗️<b>ESLATMA</b> Siz yuborgan matndagi harflardan boshqa har qanday belgilar hisobga olinmaydi"

@dp.message_handler(commands="shifrlash",state="*")
async def bot_start(message: types.Message,state: FSMContext):
    await StateData.shifrla.set()
    await message.answer(matn,reply_markup=coursesMenu)


@dp.callback_query_handler(text='encrypt',state='*')
async def bot_start(call: types.CallbackQuery,state: FSMContext):
    await StateData.shifrla.set()
    await call.message.answer(matn,reply_markup=coursesMenu)
    await call.answer(cache_time=60)


# cansel handler
@dp.callback_query_handler(text="cancel",state=StateData.shifrla)
async def cancel_handler(call: types.CallbackQuery,state: FSMContext):
    await call.answer(cache_time=60)
    await call.message.delete()
    await state.finish()

# Usul tanlash
@dp.callback_query_handler(shifr_callback.filter(item_name='sezer'),state=StateData.shifrla)
async def start(call: types.CallbackQuery): 
    await StateData.sezer.set()
    await call.message.answer("✅ Sezer shifrlash usuli\nMatn yuboring")
    await call.message.delete()

@dp.callback_query_handler(shifr_callback.filter(item_name='vijiner'),state=StateData.shifrla)
async def bot_start(call: types.CallbackQuery):
    await StateData.vij.set()
    await call.message.answer("✅ Vijiner shifrlash usuli\nMatn yuboring")
    await call.message.delete()

@dp.callback_query_handler(shifr_callback.filter(item_name='a5_1'),state=StateData.shifrla)
async def bot_start(call: types.CallbackQuery):
    await StateData.Abesh.set()
    await call.message.answer("✅ A5-1 shifrlash usuli\nMatn yuboring")
    await call.message.delete()

# usul boyicha shirfrlash
#sezer usuli
@dp.message_handler(content_types='text',state=StateData.sezer)
async def sezerEncrypt(message: types.Message):
    mes=message.text
    key=11
    res=sezer_al.cipher_encrypt(mes,key)
    await message.reply(f"Shifrlash usuli: Sezer \nMaxfiy kalit(son): 11 ")
    await message.answer(f" Shifr matn: \n{res}")
    await message.answer("<b>Matnlarni shifrlovchi bot</b>\n Bot sizga yoqqan bo'lsa do'stlaringiz bilan baham ko'ring",reply_markup=Ulashish)

# vijiner usuli
@dp.message_handler(content_types='text',state=StateData.vij)
async def vijusul(message: types.Message):
    mes=message.text
    mes = re.sub(r"[^a-zA-Z]", "", mes)
    mes=mes.upper()
    print(mes)
    key1='VIJINER'
    key=vij_al.generateKey(mes,key1)
    res=vij_al.cipherText(mes,key)
    await message.reply(f"Shifrlash usuli: Vijiner \nMaxfiy kalit(so'z): VIJINER ")
    await message.answer(f" Shifr matn: \n{res}")
    await message.answer("<b>Matnlarni shifrlovchi bot</b>\n Bot sizga yoqqan bo'lsa do'stlaringiz bilan baham ko'ring",reply_markup=Ulashish)

# a5-1 usuli
@dp.message_handler(content_types='text',state=StateData.Abesh)
async def abeshbirusul(message: types.Message):
    mes=message.text
    #1-usul
    mes = re.sub(r"[^a-zA-Z]","",mes)
    # 2-usul
    #mes = ''.join([i for i in mes if i.isalnum()]) #harf va sonlarni qoldiradi
    #mes = ''.join([i for i in mes if not i.isdigit()])# sonlarni olib tashlaydi
    mes = mes.upper()
    res=A5_1.encrypt_main(mes)
    await message.reply(f"Shifrlash usuli: A5-1 \nMaxfiy kalit: 1101001000011010110001110001100100101001000000110111111010110111")
    await message.answer(f"<b>Shifr matn:</b> \n{res}")
    await message.answer("<b>Matnlarni shifrlovchi bot</b>\n Bot sizga yoqqan bo'lsa do'stlaringiz bilan baham ko'ring",reply_markup=Ulashish)
    

@dp.callback_query_handler(text="boshiga",state=StateData.vij)
@dp.callback_query_handler(text="boshiga",state=StateData.sezer)
@dp.callback_query_handler(text="boshiga",state=StateData.Abesh)
async def cancel_handler(call: types.CallbackQuery):
    await StateData.shifrla.set()

    await call.message.delete()
    await call.message.answer(matn,reply_markup=categoryMenu)
    await call.answer(cache_time=60)
