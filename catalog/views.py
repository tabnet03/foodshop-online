from django.http import HttpResponse, FileResponse
from django.middleware.csrf import get_token
from django.shortcuts import render
from telegram import InlineKeyboardMarkup, InlineKeyboardButton
import pathlib
from .forms import Calcform
from telegram.ext import Updater
from django.conf import settings


def catalog_index(request):
    csrf_token = get_token(request)
    form = Calcform()

    return HttpResponse(f"""
    <form action='hisobla/' method='post' enctype="multipart/form-data">
        <input type="hidden" name="csrfmiddlewaretoken" value="{csrf_token}">
        {form.as_p()}
        <button>hisobla </button> 
    </form>
    """)


def catalog_hisobla(request):
    # form = Calcform(data=request.POST, files=request.FILES)

    img = request.FILES.get('img')

    with open(settings.MEDIA_ROOT / img.name, 'wb') as f:
        for data in img.chunks():
            f.write(data)

    s1 = request.POST.get("son1")
    s2 = request.POST.get("son2")
    op = request.POST.get("op")
    if op == "-":
        natija = int(s1) - int(s2)
    elif op == "+":
        natija = int(s1) + int(s2)
    else:
        natija = 'OP not found'

    return HttpResponse(f"{s1} {op} {s2} = {natija}")

    # s1 = request.POST.get("son1")
    # s2 = request.POST.get("son2")
    # op = request.POST.get("op")
    # if op == "-":
    #     natija = int(s1) - int(s2)
    # elif op == "+":
    #     natija = int(s1) + int(s2)
    # else:
    #     natija = 'OP not found'
    # return HttpResponse(f"{s1} {op} {s2} = {natija}")

# def registration(request):
#     csrf_token = get_token(request)
#     form = Cform()
#     return HttpResponse(f"""
#     <form action='/hisoblash' method="post">
#         <input type="hidden" name='csrfmiddlewaretoken' value={csrf_token}
#         {form.as_p()}
#         <button type='submit'>Jo'natish </button>
#     </form>
#             """)
#
#
# def getname(request):
#     first_name = request.POST.get('first_name')
#     last_name = request.POST.get('last_name')
#     email = request.POST.get('email')
#     phone = request.POST.get('phone')
#     password = request.POST.get('password')
#     updater = Updater(settings.TELEGRAM_BOT_TOKEN)
#     updater.bot.send_message(chat_id=1465475316, text=f'📜 Foydalanuvchi ma\'lumotlari:\n'
#                                                       f'🚶 Ism : {first_name}\n'
#                                                       f'🚶 Familiya : {last_name}\n'
#                                                       f'☎️ Telefon raqam: {phone}\n'
#                                                       f'📧 Email : {email}',
#         reply_markup=InlineKeyboardMarkup([
#             [InlineKeyboardButton('Saqlash✅', callback_data='save')]
#         ])
#     )
#
#     return HttpResponse(f"Ma'lumotlat mucaffaqqiyatli saqlandi! <a href='mla'>Userlarni ko'rish</a>")
#
#
# def show_file(response):
#     files = pathlib.Path(settings.BASE_DIR/'users/').rglob("*txt")
#     a = []
#     for i in files:
#         a.append(i.name)
#     pdf = open(settings.BASE_DIR / 'users/user_1.txt', 'rb')
#     response = FileResponse(pdf)
#     return HttpResponse(f'<a href = "#">{"<br/>".join(map(str, a))}</a>')
