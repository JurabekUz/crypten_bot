from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from .callback import shifr_callback
# 1-usul.
categoryMenu = InlineKeyboardMarkup(
    inline_keyboard=[
    [
        InlineKeyboardButton(text="Shifrlash", callback_data="encrypt"),
        
    ],
    [
      InlineKeyboardButton(text="Dishifrlash", callback_data="decrypt"),
    ],
   
])


# Usullar menu si
coursesMenu = InlineKeyboardMarkup(row_width=1)

sezer = InlineKeyboardButton(text=" 1️⃣ Sezer usuli ", callback_data=shifr_callback.new(item_name="sezer"))
coursesMenu.insert(sezer)

vijiner = InlineKeyboardButton(text=" 2️⃣ Vijiner usuli ", callback_data=shifr_callback.new(item_name="vijiner"))
coursesMenu.insert(vijiner)

a5_1 = InlineKeyboardButton(text=" 3️⃣ A5-1 usuli ", callback_data="encrypt:a5_1")
coursesMenu.insert(a5_1)

back_button = InlineKeyboardButton(text="🔙 Ortga", callback_data="cancel")
coursesMenu.insert(back_button)

# Ulashish tugmachalari
Ulashish = InlineKeyboardMarkup(row_width=1)

back_button = InlineKeyboardButton(text="🔙 Boshiga", callback_data="boshiga")
Ulashish.insert(back_button)

ulashish_button = InlineKeyboardButton(text="Ulashish", switch_inline_query="Zo'r bot ekan")
Ulashish.insert(ulashish_button)
