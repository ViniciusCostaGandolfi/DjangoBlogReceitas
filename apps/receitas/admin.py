from django.contrib import admin
from .models import Receita


class ListandoReceitas(admin.ModelAdmin):
    list_display = ['id', 'nomeReceita', 'categoria', 'publicada'] # nomes 
    list_display_links  = ['id', 'nomeReceita', 'categoria']# nomes clicaveis
    search_fields  = ['nomeReceita', 'categoria'] # nomes pesquisáveis
    list_filter = ['categoria', 'publicada'] # filtro por categoria
    list_per_page = 15 # Número de objetos por pagina
    list_editable = ['publicada'] # Campo editavel na tabela


admin.site.register(Receita, ListandoReceitas)


# Register your models here.
