from django.urls import path
from . import views

app_name = 'cadastro_processo'

urlpatterns = [
    path('', views.cadastro, name='home')
]