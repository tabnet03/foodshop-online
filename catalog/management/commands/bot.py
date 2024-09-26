import pathlib
import os
from django.core.management import BaseCommand
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, ContextTypes, CallbackQueryHandler
from django.conf import settings


# from catalog.views import getname


class Command(BaseCommand):
    def start_handler(self, update, context):
        update.message.reply_text('Hi',
              reply_markup=InlineKeyboardMarkup([
                  [InlineKeyboardButton('GoGo', callback_data='save')]
              ])
        )

    def save_handler(self, update: Update, context):
        update.callback_query.answer('Uraa', show_alert=True)

    def handle(self, *args, **options):
        updater = Updater(settings.TELEGRAM_BOT_TOKEN)

        updater.dispatcher.add_handler(CommandHandler('start', self.start_handler))
        updater.dispatcher.add_handler(CallbackQueryHandler(self.save_handler, pattern='^save$'))
        updater.start_polling()
        updater.idle()
