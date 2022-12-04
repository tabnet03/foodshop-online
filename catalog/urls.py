from django.urls import path
from .views import catalog_index, catalog_hisobla

app_name = 'catalog'

urlpatterns = [
    path('', catalog_index, name='index'),
    path('hisobla/', catalog_hisobla, name='hisobla'),

]