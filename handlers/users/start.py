from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.inline.tugma import categoryMenu
from loader import dp


@dp.message_handler(CommandStart(),state='*')
async def bot_start(message: types.Message,state:FSMContext):
    await message.answer(f"Salom, {message.from_user.full_name}!\n"
    "Matnni shifrlash yoki dishifrlash kerakmi?\nQuyidagi buyruqlardan yoki tugmalardan foydalaning\n"
    "/shifrlash  matnni shifrlash buyrug'i\n"
    "/dishifrlash shifrlangan matnni asl holiga qaytarish buyrug'i \n",reply_markup=categoryMenu)
    # agar user stateda turgan bolsa u none ga ozgaradi
    current_state = await state.get_state()
    if current_state:
        await state.finish()

    # CategotyMenu 1.shifrlash 2.dishfrlash bu holatda state=None