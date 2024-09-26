"""bookstore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.http.response import HttpResponse

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('catalog.urls'))
]






# user = {
#     1: 'Anvar',
#     2: "Sobir",
#     3: 'Qodir'
#
# }
#
#
# def home_view(request):
#     q = request.GET.get('q')
#     return HttpResponse(q[::-1])
#
#
# def catalog_index(request):
#     return HttpResponse('salomlar')
#
#
# def catalog_contact(request):
#     html = ['<ol>']
#     html.extend(map(lambda n: f"<li>Salom: {n}</li>", range(1, 11)))
#     html.append("</ol>")
#
#     a, b = map(int, [request.GET.get(p) for p in ['a', 'b']])
#     return HttpResponse('\n'.join(html) + '<hr/>' + f"{a + b}")
#
#
# # # bu eng oddiy usulda yozilgan kod buni dinamik qilish kere
# # def coll_user_1(request):
# #     return HttpResponse(user[1])
# #
# #
# # def coll_user_2(request):
# #     return HttpResponse(user[2])
#
# ## bu usul orqali dinamik qilish imkonini beradigan funksiya ichida funksiya yozildi
# # def get_users(n):
# #     def coll_user(request):
# #         return HttpResponse(user[n])
# #     return coll_user
# # #bundanda optimal dimanik qilish va path da ham osonroq yozish uchun (pasda)
#
# def coll_user(request, n):
#     if n not in user:
#         raise Http404
#     return HttpResponse(user[n])
#
#
# def catalog_birthday(request, year):
#     return HttpResponse(str(year))
#
#
# class FourDigitYearConverter:
#     regex = '[0-9]{4}[0-9]{2}[0-9]{2}'
#
#     def to_python(self, value):
#         return int(value)
#
#     def to_url(self, value):
#         return f'{value:04d}{value:02d}{value:02d}'
#
#
# register_converter(FourDigitYearConverter, 'yyyy')
#
#
# # path('diff/<date:q>', lambda request, q: HttpResponse(
# #     f"Hozirgi vaqtdan {int((datetime.now() - datetime.strptime(q, 'bd-%Y-%m-%d')).days) // 365} yil {(int((datetime.now() - datetime.strptime(q, 'bd-%Y-%m-%d')).days) % 365) // 30} oy {(int((datetime.now() - datetime.strptime(q, 'bd-%Y-%m-%d')).days) % 365) % 30} kun farqli!"))

#     path('admin/', admin.site.urls),
#     path('salom/', lambda request: HttpResponse(f"{request.GET.get('q')[::-1]}")),
#     path('dunyo/', catalog_contact),
#     path('user/<int:n>/', coll_user),
#     # path('user/1/', get_users(2)), bu usuldan kamroq yozib dinamik qilish usuli (tepada)
#     path('birthday-<yyyy:year>', catalog_birthday),
