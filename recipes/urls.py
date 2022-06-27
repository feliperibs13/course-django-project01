# URLS do app.
from django.urls import path

# Importando as views que serão utilizadas.
from .views import home

urlpatterns = [
    path('', home),
]
