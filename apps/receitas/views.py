from django.shortcuts import render, get_object_or_404, redirect
from .models import Receita
from django.contrib.auth.models import User



#from django.http import HttpResponse
# Create your views here.

# def index(request):
#     return HttpResponse('<h1>Receitas</h1>')


def index(request):
    receitas = Receita.objects.order_by('-dataReceita').filter(publicada=True)

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


def criaReceita(request):
    if request.method == 'POST':
        nomeReceita = request.POST['nome_receita']
        ingredientes = request.POST['ingredientes']
        modoPreparo = request.POST['modo_preparo']
        tempoPreparo = request.POST['tempo_preparo']
        categoria = request.POST['categoria']
        rendimento = request.POST['rendimento']
        fotoReceita = request.FILES['foto_receita']
        publicada = request.POST['publicada'] == 'on'
        user = get_object_or_404(User, pk=request.user.id)


        receita = Receita.objects.create(
            pessoa=user, nomeReceita=nomeReceita,
            ingredientes=ingredientes, modoPreparo=modoPreparo,
            tempoPreparo=tempoPreparo, categoria=categoria,
            fotoReceita=fotoReceita, rendimento=rendimento, 
            publicada=publicada
        )
        receita.save()

        return redirect('dashBoard')

    else:
        return render(request, 'receitas/criaReceita.html')

def deletaReceita(request, receita_id):
    receita = get_object_or_404(Receita, pk=receita_id)
    receita.delete()
    return redirect('dashBoard')

def editaReceita(request, receita_id):
    receita = get_object_or_404(Receita, pk=receita_id)
    receitaEditar = { 'receita': receita }
    return render(request, 'receitas/editaReceita.html', receitaEditar)


def atualizaReceita(request, receita_id):
    if request.method == 'POST':
        receita = Receita.objects.get(pk=receita_id)
        receita.nomeReceita = request.POST['nome_receita']
        receita.ingredientes = request.POST['ingredientes']
        receita.modoPreparo = request.POST['modo_preparo']
        receita.tempoPreparo = request.POST['tempo_preparo']
        receita.categoria = request.POST['categoria']
        receita.rendimento = request.POST['rendimento']
        receita.fotoReceita = request.FILES['foto_receita']

        receita.save()
        return redirect('dashBoard')

    else:
        return render(request, 'receitas/criaReceita.html')