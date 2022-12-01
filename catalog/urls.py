from django.urls import path
from .views import registration, getname, show_file

urlpatterns = [
    path('', registration, name='registration'),
    path('hisoblash', getname, name='get'),
    path('mla', show_file, name='ge' )
]