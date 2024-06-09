from aiogram.utils.keyboard import InlineKeyboardBuilder, KeyboardButton, ReplyKeyboardMarkup


def start_keyboard():
    kb = InlineKeyboardBuilder()
    kb.button(text='Geo 🛰', callback_data='geo')
    kb.button(text='Forecast 🌅', callback_data='forecast')
    return kb.as_markup()


def send_geo():
    # Создание кнопки с запросом геопозиции
    kb = ReplyKeyboardMarkup(keyboard=[
        [
            KeyboardButton(text='відправ мені свою геолокацію', request_location=True)]
    ],
        resize_keyboard=True, is_persistent=True
    )
    return kb
