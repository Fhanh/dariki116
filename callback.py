from telegram import Update
from telegram import ParseMode
from telegram.ext import CallbackContext

from db import *
from buttons_and_keyboards import *
from photo_main import collages, alerts


def keyboard_callback_handler(update: Update, context: CallbackContext):
    """Обработчик ВСЕХ кнопок со ВСЕХ клавиатур"""
    goods_page = db_select_page(user_id=update.effective_user.id)
    query = update.callback_query
    data = query.data
    chat_id = query.message.chat_id
    message_id = query.message.message_id
    #
    # NAVIGATION BUTTONS
    #
    if data == CALLBACK_BUTTON_GOODS:
        context.bot.delete_message(
            chat_id=chat_id,
            message_id=message_id,
        )
        img = '{0}'.format(collages[goods_page - 1])
        query.bot.send_photo(
            chat_id=chat_id,
            photo=img,
            caption=f"Выберите категорию товаров:\n\n<i>Страница {goods_page}</i>",
            reply_markup=get_goods_inline_keyboard(goods_page),
            parse_mode=ParseMode.HTML,
        )
    elif data == CALLBACK_BUTTON_MORE:
        if goods_page < 6:
            goods_page += 1
        db_change_page(goods_page=goods_page, user_id=update.effective_user.id)
        update.callback_query.data = CALLBACK_BUTTON_GOODS
        keyboard_callback_handler(update, context)
    elif data == CALLBACK_BUTTON_BACK:
        if goods_page > 1:
            goods_page -= 1
        db_change_page(goods_page=goods_page, user_id=update.effective_user.id)
        update.callback_query.data = CALLBACK_BUTTON_GOODS
        keyboard_callback_handler(update, context)
    elif data == CALLBACK_BUTTON_BACK_TO_GOODS:
        update.callback_query.data = CALLBACK_BUTTON_GOODS
        keyboard_callback_handler(update, context)
    elif data == CALLBACK_BUTTON_INFO:
        context.bot.delete_message(
            chat_id=chat_id,
            message_id=message_id,
        )
        query.bot.send_message(
            chat_id=chat_id,
            text='Информация ℹ️\n'
                 '\n📌Срок исполнения:\nв зависимости от вида товара, загрузки и объема заказа срок '
                 'исполнения может занимать от 1-го часа до 3-х дней'
                 '\n📌Наш адрес:\n<code>Республика Татарстан, с.Большая Атня, ул.Карла Маркса, д.26</code>'
                 '\n📌Связь:\nTelegram - <a href="https://t.me/dariki116">Зульфат</a> или <a '
                 'href="https://t.me/AIGUL_BARAK">Айгуль</a>',
            reply_markup=get_home_inline_keyboard(),
            parse_mode=ParseMode.HTML,
            disable_web_page_preview=True,
        )
    elif data == CALLBACK_BUTTON_HOME:
        context.bot.delete_message(
            chat_id=chat_id,
            message_id=message_id,
        )
        img = alerts[0]
        query.bot.send_photo(
            chat_id=chat_id,
            photo=img,
            caption='👋🏻Привет, <u>{0}</u>👋🏻\n\n🎉Рады видеть тебя в студии печати '
                    '<u><b>«Дарики»</b></u>🎉\n\n✨<i>Изделия и товары, которыми мы порадуем тебя:\n</i>Качественная '
                    'печать на футболках, толстовках, свитшотах. Изготовление пазлов, кружок с вашими (или нашими) '
                    'подарки себе любимым, а также своим родным и близким!'.format(update.effective_user.first_name),
            reply_markup=get_base_inline_keyboard(),
            parse_mode=ParseMode.HTML,
        )
    elif data == CALLBACK_BUTTON_SALES:
        context.bot.delete_message(
            chat_id=chat_id,
            message_id=message_id,
        )
        query.bot.send_message(
            chat_id=chat_id,
            text='<i>Раздел "{0}" находится в разработке\n\nПриносим извинения за предоставленные неудобства</i>'.format
            (TITLES[CALLBACK_BUTTON_SALES]),
            reply_markup=get_home_inline_keyboard(),
            parse_mode=ParseMode.HTML,
        )
    #
    # GOODS_HANDLERS
    #
    elif data == 'CALLBACK_GOODS_BUTTON9':
        context.bot.delete_message(
            chat_id=chat_id,
            message_id=message_id,
        )
        img = open('photos/test_t_shirt.jpg', 'rb')
        query.bot.send_photo(
            chat_id=chat_id,
            photo=img,
            caption='👋🏻Привет, <u>{0}</u>👋🏻\n\n🎉Рады видеть тебя в студии печати '
                    '<u><b>«Дарики»</b></u>🎉\n\n✨<i>Изделия и товары, которыми мы порадуем тебя:\n</i>Качественная '
                    'печать на футболках, толстовках, свитшотах. Изготовление пазлов, кружок с вашими (или нашими) '
                    'подарки себе любимым, а также своим родным и близким!'.format(update.effective_user.first_name),
            reply_markup=get_gender_inline_keyboard(),
            parse_mode=ParseMode.HTML,
        )
    #
    # ADMIN MENU
    #
    elif data == CALLBACK_ADMIN_BUTTON1:
        info = context.bot.get_me()
        context.bot.delete_message(
            chat_id=chat_id,
            message_id=message_id,
        )
        query.bot.send_message(
            chat_id=chat_id,
            text=f"*Технические данные\n\n"
            f"*Возможность читать все сообщения группы: {info['can_read_all_group_messages']}\n"
            f"*Название бота: {info['first_name']}\n"
            f"*Возможность зайти в группы: {info['can_join_groups']}\n"
            f"*Поддержка инлайн режима: {info['supports_inline_queries']}\n"
            f"*Имя пользователя: {info['username']}\n"
            f"*ID бота: {info['id']}\n"
            f"*Это бот: {info['is_bot']}\n\n"
            f"*Количество пользователей в базе данных: {len(db_select_users_ids())}\n"
            f"*Количество заказов в базе данных: ?"
        )
