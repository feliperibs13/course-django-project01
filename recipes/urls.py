# URLS do app.
from django.urls import path

# Importando as views que serão utilizadas.
from .views import contato, home, sobre

urlpatterns = [
    path('', home),
    path('contato/', contato),
    path('sobre/', sobre)
]
