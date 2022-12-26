from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='index'),
    path('<int:receita_id>', receita, name='receita'),
    path('buscar', buscar, name='buscar'),
    path('cria/receita', criaReceita, name='criaReceita'),
    path('deleta/<int:receita_id>', deletaReceita, name='deletaReceita'),
    path('edita/<int:receita_id>', editaReceita, name='editaReceita'),
    path('atualiza/<int:receita_id>', atualizaReceita, name='atualizaReceita'),
    ]