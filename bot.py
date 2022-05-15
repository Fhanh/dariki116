# from telegram.ext import MessageHandler
# from telegram.ext import Filters
from telegram import Bot
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import CallbackQueryHandler
from telegram.utils.request import Request
from callback import *
from photo_main import alerts


def do_start(update: Update, context: CallbackContext):
    db_check_user(update.effective_user.id, update.effective_user.first_name)
    """Оправка сообщения в Инфо Канал context.bot.send_message( chat_id='-1001682916644', text=f"Дата и время: {
    datetime.datetime.now()}\nПрисоединился(-ась): {update.effective_user.first_name}\nID пользователя: {
    update.effective_user.id}", ) """
    img = alerts[0]
    context.bot.send_photo(
        chat_id=update.message.chat_id,
        photo=img,
        caption='👋🏻Привет, <u>{0}</u>👋🏻\n\n🎉Рады видеть тебя в студии печати '
                '<u><b>«Дарики»</b></u>🎉\n\n✨<i>Изделия и товары, которыми мы порадуем тебя:\n</i>Качественная '
                'печать на футболках, толстовках, свитшотах. Изготовление пазлов, кружок с вашими (или нашими) '
                'подарки себе любимым, а также своим родным и близким!'.format(update.effective_user.first_name),
        reply_markup=get_base_inline_keyboard(),
        parse_mode=ParseMode.HTML,
    )


def adminka(update: Update, context: CallbackContext):
    if update.effective_user.id in ADMINS_ID:
        context.bot.send_message(
            chat_id=update.message.chat_id,
            text='Доступ разрешен!\n\n<b><u>АДМИН МЕНЮ:</u></b>',
            reply_markup=get_admin_inline_keyboard(),
            parse_mode=ParseMode.HTML,
        )
    else:
        context.bot.send_message(
            chat_id=update.message.chat_id,
            text='У Вас нет доступа!',
            reply_markup=get_home_inline_keyboard(),
        )


def main():
    print("Запускаем бота...")

    req = Request(
        connect_timeout=0.5,
        read_timeout=1.0,
    )
    req_kwargs = {
        'proxy_url': 'socks5://134.122.87.108:6699/',
        'urllib3_proxy_kwargs': {
            'assert_hostname': 'False',
            'cert_reqs': 'CERT_NONE',
            'username': '1050164391',
            'password': 'FIxzcD87'
        }
    }
    bot = Bot(
        token=TG_TOKEN,
        request=req,
    )
    updater = Updater(
        bot=bot,
        use_context=True,
        request_kwargs=req_kwargs,
    )

    # Проверить что бот корректно подключился к Telegram API

    # Подключение к СУБД
    init_db()

    # Навесить обработчики команд
    udah = updater.dispatcher.add_handler
    udah(CommandHandler("start", do_start))
    udah(CommandHandler("adminka", adminka))
    udah(CallbackQueryHandler(callback=keyboard_callback_handler))

    print("Бот запущен!")

    # Начать бесконечную обработку входящих сообщений
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
