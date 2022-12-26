from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages, auth
from receitas.models import Receita



def cadastro(request):
    """ Cadastra uma nova pessoa no sistema """
    if request.method == 'POST':
        name = request.POST['nome']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if User.objects.filter( email=email):
            messages.error(request, 'Email já cadastrado')

        user = User.objects.create_user(username=name, email=email, password=password)
        user.save()
        messages.success(request, 'Usuário cadastrado com sucesso!')
        
        return redirect('login')
    else:
        return render(request, 'usuarios/cadastro.html')


def login(request):
    """ Loga a conta da pessoa do nosso sistema """
    if request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['senha']
        if email == "" or senha == "":
            messages.error(request, 'O email ou senha não podem estar em branco')
            return redirect('login')
        print(email, senha)
        if User.objects.filter(email=email).exists():
            nome = User.objects.filter(email=email).values_list('username', flat=True).get()
            user = auth.authenticate(request, username=nome, password=senha)
            if user is not None:
                auth.login(request, user)
                messages.success(request, 'Login realizado com sucesso')
                print('user' + nome)
                return redirect('dashBoard')
    return render(request, 'usuarios/login.html')


def logout(request):
    """ Desloga a conta da pessoa do nosso sistema """
    auth.logout(request)

    return redirect('index')


def dashBoard(request):
    """ Mostra o dashBoard da pessoa com suas receitas """
    if request.user.is_authenticated:
        id = request.user.id
        receitas = Receita.objects.order_by('-dataReceita').filter(pessoa=id)
        #receitas = receitas.filter(pessoa=id)

        dados = {
            'receitas': receitas
        }

        return render(request, 'usuarios/dashBoard.html', dados)

    return redirect('index')




