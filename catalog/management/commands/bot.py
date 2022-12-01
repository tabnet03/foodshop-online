import pathlib
import os
from django.core.management import BaseCommand
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, ContextTypes, CallbackQueryHandler
from django.conf import settings
from catalog.views import getname


class Command(BaseCommand):
    def start_handler(self, update, context):
        update.message.reply_text('Hi')

    def save_handler(self, update: Update, context):
        update.callback_query.answer(text='Muvaffaqqiyatli saqlandi!!!✔️', show_alert=True)
        i = 1
        while os.path.exists(settings.BASE_DIR / f"users/user_{i}.txt"):
            i += 1
        with open(settings.BASE_DIR / f"users/user_{i}.txt", 'w') as f:
            f.write(update.callback_query.message.text)
        i += 1

        update.callback_query.delete_message()


    def handle(self, *args, **options):
        updater = Updater(settings.TELEGRAM_BOT_TOKEN)
        updater.dispatcher.add_handler(CommandHandler('start', self.start_handler))
        updater.dispatcher.add_handler(CallbackQueryHandler(self.save_handler, pattern='save'))
        updater.start_polling()
        updater.idle()