from django.shortcuts import render, get_object_or_404, redirect
from receitas.models import Receita
from django.contrib.auth.models import User



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
        if request.FILES:
            receita.fotoReceita = request.FILES['foto_receita']

        receita.save()
        return redirect('dashBoard')

    else:
        return render(request, 'receitas/criaReceita.html')