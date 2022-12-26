from django.shortcuts import render, get_object_or_404, redirect
from receitas.models import Receita
from django.core.paginator import Paginator



#from django.http import HttpResponse
# Create your views here.

# def index(request):
#     return HttpResponse('<h1>Receitas</h1>')


def index(request):
    receitas = Receita.objects.order_by('-dataReceita').filter(publicada=True)
    paginator = Paginator(receitas, 9)
    page = request.GET.get('page')
    receitas = paginator.get_page(page)
    dados = {
        'receitas' : receitas
    }
    return render(request,'receitas/index.html', dados)

def receita(request, receita_id):
    receitaDataBase = get_object_or_404(Receita, pk=receita_id)

    receitaObject = {
        'receitaDataBase' : receitaDataBase
    }


    return render(request, 'receitas/receita.html', receitaObject)


def buscar(request):
    receitas = Receita.objects.filter(publicada=True).order_by('-dataReceita')
    nome_a_buscar = request.GET
    if 'buscar' in request.GET:
        nome_a_buscar = request.GET['buscar']
        if nome_a_buscar:
            receitas = receitas.filter(nomeReceita__contains=nome_a_buscar)

    dados = {
        'receitas' : receitas,
        'buscar' : nome_a_buscar
    }
    return render(request,'receitas/buscar.html', dados)