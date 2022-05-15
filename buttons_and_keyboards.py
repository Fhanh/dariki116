from telegram import InlineKeyboardButton
from telegram import InlineKeyboardMarkup

# navigation buttons
CALLBACK_BUTTON_GOODS = "callback_button_goods"
CALLBACK_BUTTON_INFO = "callback_button_info"
CALLBACK_BUTTON_MORE = "callback_button_more"
CALLBACK_BUTTON_BACK = "callback_button_back"
CALLBACK_BUTTON_BACK_TO_GOODS = "callback_button_back_to_goods"
CALLBACK_BUTTON_HOME = "callback_button_home"
CALLBACK_BUTTON_SALES = "callback_button_sales"
# goods button
CALLBACK_GOODS_BUTTON1 = "callback_goods_button1"
CALLBACK_GOODS_BUTTON2 = "callback_goods_button2"
CALLBACK_GOODS_BUTTON3 = "callback_goods_button3"
CALLBACK_GOODS_BUTTON4 = "callback_goods_button4"
CALLBACK_GOODS_BUTTON5 = "callback_goods_button5"
CALLBACK_GOODS_BUTTON6 = "callback_goods_button6"
CALLBACK_GOODS_BUTTON7 = "callback_goods_button7"
CALLBACK_GOODS_BUTTON8 = "callback_goods_button8"
CALLBACK_GOODS_BUTTON9 = "callback_goods_button9"
CALLBACK_GOODS_BUTTON10 = "callback_goods_button10"
CALLBACK_GOODS_BUTTON11 = "callback_goods_button11"
CALLBACK_GOODS_BUTTON12 = "callback_goods_button12"
CALLBACK_GOODS_BUTTON13 = "callback_goods_button13"
CALLBACK_GOODS_BUTTON14 = "callback_goods_button14"
CALLBACK_GOODS_BUTTON15 = "callback_goods_button15"
CALLBACK_GOODS_BUTTON16 = "callback_goods_button16"
CALLBACK_GOODS_BUTTON17 = "callback_goods_button17"
CALLBACK_GOODS_BUTTON18 = "callback_goods_button18"
CALLBACK_GOODS_BUTTON19 = "callback_goods_button19"
CALLBACK_GOODS_BUTTON20 = "callback_goods_button20"
CALLBACK_GOODS_BUTTON21 = "callback_goods_button21"
CALLBACK_GOODS_BUTTON22 = "callback_goods_button22"
CALLBACK_GOODS_BUTTON23 = "callback_goods_button23"
CALLBACK_GOODS_BUTTON24 = "callback_goods_button24"
# gender buttons
CALLBACK_GENDER_BUTTON1 = "callback_gender_button1"
CALLBACK_GENDER_BUTTON2 = "callback_gender_button2"
CALLBACK_GENDER_BUTTON3 = "callback_gender_button3"
# admin buttons
CALLBACK_ADMIN_BUTTON1 = "callback_admin_button1"
CALLBACK_ADMIN_BUTTON2 = "callback_admin_button2"

TITLES = {
    # navigation buttons
    CALLBACK_BUTTON_GOODS: "Товары 🎁",
    CALLBACK_BUTTON_INFO: "Информация ℹ️",
    CALLBACK_BUTTON_MORE: "Далее ➡️",
    CALLBACK_BUTTON_BACK: "⬅️ Назад",
    CALLBACK_BUTTON_BACK_TO_GOODS: "⬅️ Категории товаров",
    CALLBACK_BUTTON_HOME: "На главную 🏠",
    CALLBACK_BUTTON_SALES: "Скидки и акции 🛍",
    # goods button
    'CALLBACK_GOODS_BUTTON1': "Футболка",
    'CALLBACK_GOODS_BUTTON2': "Свитшот",
    'CALLBACK_GOODS_BUTTON3': "Кружка",
    'CALLBACK_GOODS_BUTTON4': "Толстовка",
    'CALLBACK_GOODS_BUTTON5': "Брелок в виде гос номера",
    'CALLBACK_GOODS_BUTTON6': "Автодокумент",
    'CALLBACK_GOODS_BUTTON7': "Фотокуб",
    'CALLBACK_GOODS_BUTTON8': "Пазл",
    'CALLBACK_GOODS_BUTTON9': "Бейсболка",
    'CALLBACK_GOODS_BUTTON10': "Акриловый магнит",
    'CALLBACK_GOODS_BUTTON11': "Жетон",
    'CALLBACK_GOODS_BUTTON12': "Подушка",
    'CALLBACK_GOODS_BUTTON13': "Защитная маска",
    'CALLBACK_GOODS_BUTTON14': "Акриловый брелок",
    'CALLBACK_GOODS_BUTTON15': "Метрика",
    'CALLBACK_GOODS_BUTTON16': "Коврик для мышки",
    'CALLBACK_GOODS_BUTTON17': "Фоторамка",
    'CALLBACK_GOODS_BUTTON18': "Водяной сувенир",
    'CALLBACK_GOODS_BUTTON19': "Полотенце",
    'CALLBACK_GOODS_BUTTON20': "Чехол",
    'CALLBACK_GOODS_BUTTON21': "Наклейки",
    'CALLBACK_GOODS_BUTTON22': "Офисные услуги",
    'CALLBACK_GOODS_BUTTON23': "Упаковка подарков",
    'CALLBACK_GOODS_BUTTON24': "Ёлочная игрушка",
    # gender buttons
    CALLBACK_GENDER_BUTTON1: "Мужской 👨🏻",
    CALLBACK_GENDER_BUTTON2: "Женский 👩🏻",
    CALLBACK_GENDER_BUTTON3: "Детский 🧒🏻",
    # admin buttons
    CALLBACK_ADMIN_BUTTON1: "Статус работы бота",
    CALLBACK_ADMIN_BUTTON2: "Управление категорием \"Скидки и акции 🛍\"",
}


def get_base_inline_keyboard():
    keyboard = [
        [
            InlineKeyboardButton(TITLES[CALLBACK_BUTTON_GOODS], callback_data=CALLBACK_BUTTON_GOODS),
        ],
        [
            InlineKeyboardButton(TITLES[CALLBACK_BUTTON_SALES], callback_data=CALLBACK_BUTTON_SALES),
        ],
        [
            InlineKeyboardButton(TITLES[CALLBACK_BUTTON_INFO], callback_data=CALLBACK_BUTTON_INFO),
        ],
    ]
    return InlineKeyboardMarkup(keyboard)


def get_home_inline_keyboard():
    keyboard = [
        [
            InlineKeyboardButton(TITLES[CALLBACK_BUTTON_HOME], callback_data=CALLBACK_BUTTON_HOME),
        ],
    ]
    return InlineKeyboardMarkup(keyboard)


def get_gender_inline_keyboard():
    keyboard = [
        [
            InlineKeyboardButton(TITLES[CALLBACK_GENDER_BUTTON1], callback_data=CALLBACK_GENDER_BUTTON1),
            InlineKeyboardButton(TITLES[CALLBACK_GENDER_BUTTON2], callback_data=CALLBACK_GENDER_BUTTON2),
            InlineKeyboardButton(TITLES[CALLBACK_GENDER_BUTTON3], callback_data=CALLBACK_GENDER_BUTTON3),
        ],
        [
            InlineKeyboardButton(TITLES[CALLBACK_BUTTON_BACK_TO_GOODS], callback_data=CALLBACK_BUTTON_BACK_TO_GOODS),
            InlineKeyboardButton(TITLES[CALLBACK_BUTTON_HOME], callback_data=CALLBACK_BUTTON_HOME),
        ],
    ]
    return InlineKeyboardMarkup(keyboard)


def get_goods_inline_keyboard(goods_page):
    goods_element = (goods_page - 1) * 4
    back = InlineKeyboardButton(TITLES[CALLBACK_BUTTON_BACK], callback_data=CALLBACK_BUTTON_BACK)
    home = InlineKeyboardButton(TITLES[CALLBACK_BUTTON_HOME], callback_data=CALLBACK_BUTTON_HOME)
    more = InlineKeyboardButton(TITLES[CALLBACK_BUTTON_MORE], callback_data=CALLBACK_BUTTON_MORE)
    keyboard = [
        [
            InlineKeyboardButton(TITLES['CALLBACK_GOODS_BUTTON{0}'.format(goods_element + 1)],
                                 callback_data='CALLBACK_GOODS_BUTTON{0}'.format(goods_element + 1)),
            InlineKeyboardButton(TITLES['CALLBACK_GOODS_BUTTON{0}'.format(goods_element + 2)],
                                 callback_data='CALLBACK_GOODS_BUTTON{0}'.format(goods_element + 2)),
        ],
        [
            InlineKeyboardButton(TITLES['CALLBACK_GOODS_BUTTON{0}'.format(goods_element + 3)],
                                 callback_data='CALLBACK_GOODS_BUTTON{0}'.format(goods_element + 3)),
            InlineKeyboardButton(TITLES['CALLBACK_GOODS_BUTTON{0}'.format(goods_element + 4)],
                                 callback_data='CALLBACK_GOODS_BUTTON{0}'.format(goods_element + 4)),
        ]
    ]
    if goods_element == 0:
        keyboard.append([home, more])
    elif 0 < goods_element < 20:
        keyboard.append([back, home, more])
    elif goods_element == 20:
        keyboard.append([back, home])
    return InlineKeyboardMarkup(keyboard)


def get_sales_inline_keyboard():
    keyboard = [
        [
            InlineKeyboardButton(TITLES[CALLBACK_BUTTON_HOME], callback_data=CALLBACK_BUTTON_HOME),
        ],
    ]
    return InlineKeyboardMarkup(keyboard)


def get_admin_inline_keyboard():
    keyboard = [
        [
            InlineKeyboardButton(TITLES[CALLBACK_ADMIN_BUTTON1], callback_data=CALLBACK_ADMIN_BUTTON1),
        ],
        [
            InlineKeyboardButton(TITLES[CALLBACK_ADMIN_BUTTON2], callback_data=CALLBACK_ADMIN_BUTTON2),
        ],
        [
            InlineKeyboardButton(TITLES[CALLBACK_BUTTON_HOME], callback_data=CALLBACK_BUTTON_HOME),
        ],
    ]
    return InlineKeyboardMarkup(keyboard)
