from django.http import HttpResponse, FileResponse
from django.middleware.csrf import get_token
from django.shortcuts import render
from telegram import InlineKeyboardMarkup, InlineKeyboardButton
import pathlib
from .forms import Cform
from telegram.ext import Updater
from django.conf import settings


def registration(request):
    csrf_token = get_token(request)
    form = Cform()
    return HttpResponse(f"""
    <form action='/hisoblash' method="post">
        <input type="hidden" name='csrfmiddlewaretoken' value={csrf_token}
        {form.as_p()}
        <button type='submit'>Jo'natish </button>
    </form>
            """)


def getname(request):
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    email = request.POST.get('email')
    phone = request.POST.get('phone')
    password = request.POST.get('password')
    updater = Updater(settings.TELEGRAM_BOT_TOKEN)
    updater.bot.send_message(chat_id=1465475316, text=f'📜 Foydalanuvchi ma\'lumotlari:\n'
                                                      f'🚶 Ism : {first_name}\n'
                                                      f'🚶 Familiya : {last_name}\n'
                                                      f'☎️ Telefon raqam: {phone}\n'
                                                      f'📧 Email : {email}',
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton('Saqlash✅', callback_data='save')]
        ])
    )

    return HttpResponse(f"Ma'lumotlat mucaffaqqiyatli saqlandi! <a href='mla'>Userlarni ko'rish</a>")


def show_file(response):
    files = pathlib.Path(settings.BASE_DIR/'users/').rglob("*txt")
    a = []
    for i in files:
        a.append(i.name)
    pdf = open(settings.BASE_DIR / 'users/user_1.txt', 'rb')
    response = FileResponse(pdf)
    return HttpResponse(f'<a href = "#">{"<br/>".join(map(str, a))}</a>')