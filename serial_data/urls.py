from django.urls import path
from . import views

urlpatterns = [
    path('atualizar_variavel/', views.atualizar_variavel, name='atualizar_variavel'),
    
]