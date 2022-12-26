# Django

    python3 -m venv venv
    pip install django


----------------------------------------------------------------

## Help

Mostra os comandos do django
    python3 manage.py help

----------------------------------------------------------------

## Criar Projeto

Criando um projeto, um projeto pode conter muitos apps e configurações.
    django-admin startproject nomeDoProjeto

----------------------------------------------------------------

## Subir servidor

    python3 manage.py runserver

----------------------------------------------------------------

## Criar Aplicativo

Cria um app, app é uma aplicação de um ou mais projetos. Cada app deve ser adicionado a seus respectivos projetos em INSTALLED_APPS de nomeDoProjetp/settings.py

    python3 manage.py startapp nomeDoApp

Criando urls.py no app, para adicionar as urls do aplicativo

----------------------------------------------------------------

## Criar Templates em HTML
Criar uma pasta templates e adicionar as páginas HTML nela, para cada app.


----------------------------------------------------------------

## Arquivos Estáticos
Os arquivos estáticos como HTML, CSS, JS, Imagens, etc. Em nomeDoProjeto/settings.py adicionar na variável TEMPLATES a linha para templates estáticos:

    'DIRS': [os.path.join(BASE_DIR, 'nomeDoApp/templates')],

E adicionar as variáveis para os outros arquivos :

    STATIC_ROOT = os.path.join(BASE_DIR,'static')
    STATTICFILES_DIRS = [
        os.path.join(BASE_DIR, 'nomeDoProjeto/static')
    ]

Para ajudar na otimização dos arquivos estáticos do django execute o comando:

    python manage.py collectstatic


----------------------------------------------------------------


## Carregando Arquivos Estáticos nos Templates

Adicionar nas referencias ods arquivos estáticos dos templates:

    {% load static 'path' %}

Para referenciar outras paginas html dentro de um template: 

    {% load url 'path' %}


----------------------------------------------------------------


## Extends HTML

Semelhante ao conceito 'dont repeatch yourself' do react, o django 
tambem tem uma forma de adicionar partes base do html em todas as páginas, 
geralmente estas partes estão relacionadas a cabeçalho ou rodapé.

Criando o base.html com os componentes padrão das páginas, utilizar:

    {% block content %} {% endblock %}

Para inserir código html dentro desse bloco adicionar:

    {% extends 'base.html' %}
    {% load static %}
    {% block content %}
        SeuCodigoHTML
    {% endblock %}  


----------------------------------------------------------------


## Partials HTML
Resumidamente um método de incluir parte de do html em um arquivo html, 
no template adicionar:

    {% include 'partials/_file.html' %}

*è convencionado que uma partia deve começar com _*
----------------------------------------------------------------

## Usando Variáveis Dinamicas nos Templates

Utilizando {{nomeDaVariavel}} que foi passada na função render, podemos acessar
o dicionário da função render()

    {{nomeDaVariavel}}

Podemos iterar com for ou controlar com if no django com:

*FOR*

    {% for item in lista %}
        HTML
    {% endfor %}


*IF*

    {% if var1 %}
        HTML
    {% elif var2 %}
        HTML
    {% endif %}


----------------------------------------------------------------

## Banco de Dados
O próprio django se encarrega de gerar os bancos de dados baseados 
em seus modelos.

Em settings, altere para seu banco de dados:

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'alura_receita',
            'USER': 'root',
            'PASSWORD': 'mini@mim2',
            'HOST': 'localhost',
            'PORT': '3306',
        }
    }


## Models

O django disponibiliza uma classe onde tudo já esta configurado 
para criarmos nossos bancos de dados, com base na classe Models.
Herdando dela, podemos criar nossos bancos de dados. 


## Views Usando Models

Quando criandos a função que renderiza uma pagina, podemos 
buscar dados do nosso banco de dados, e atribuir como um 
dicionario para nosso template.

    def index(request):

        receitasDB = Receita.objects.all()
        dados = { 'receitas': receitasDB }

        return render(request, 'index.html', dados)

## Admin

Em seu projeto, o django ja registra uma url para admin, 
agora só falta registrar o seu modelo em admin.py.

app/admin.py:

    admin.site.register(Receita)

projeto/urls.py:

    urlpatterns = [
        path('', include(receitas_urls)),
    ]

## SuperUser

Criseu um usuário para alterar seu banco de dados pelo admin!

    python manage.py createsuperuser

## Paginas por ID
O django rse encarrega de cria uma url para cada linha do banco de dados, podemos
 ajustar na urls.py
Em seuApp/urls.py:

    urlpatterns = [
        path('', views.index, name='index'),
        path('receita', views.receitas, name='receitas'),
        path('<int:receita_id>', views.receita, name='receita'),
    ]


## Configurações Admin

Em cada app, podemos settar uma configuração de como serão os nomes 
de cada objeto no admin.


    from django.contrib import admin
    from .models import Receita


    class ListandoReceitas(admin.ModelAdmin):
        list_display = ['id', 'nomeReceita', 'categoria'] # nomes 
        list_display_links  = ['id', 'nomeReceita', 'categoria']# nomes clicaveis
        search_fields  = ['nomeReceita', 'categoria'] # nomes pesquisáveis
        list_filter = ['categoria', ] # filtro por categoria
        list_per_page = 15 # Número de objetos por pagina


    admin.site.register(Receita, ListandoReceitas)

## Integrando Modelos

    class Modelo1(models.Model):
        pessoa = models.ForeignKey(Modelo2, on_delete=models.CASCADE)

## Mudando o Nome de Modelos Referenciados

    class Modelo2(models.Model):
        nome = models.CharField(max_length=200)
        email = models.EmailField()
        telefone = models.CharField(max_length=15, validators=[RegexValidator(r'^\(?[1-9]{2}\)? ?(?:[2-8]|9[1-9])[0-9]{3}\-?[0-9]{4}$')])

        def __str__(self) -> str:
            string:str = self.nome
            return string

## Imagens no Banco de Dados

MeuApp/models.py

    class Receita(models.Model):
        ...
        foto = models.ImageField(upload_to='fotos/', blank=True)

MeuProjeto/settings.py

    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
    MEDIA_URL = '/media/'


MeuProjeto/urls.py

    urlpatterns = [
        path('', include(receitas_urls)),
        path('admin/', admin.site.urls),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


## Formularios
É possível validar os 

        from django import forms

        from app.validation import *
        from app.models import MyModel

        class MyModelForms(forms.ModelForm):
            data_pesquisa = forms.DateField(label='Data da pesquisa', disabled=True, initial=datetime.today)

            class Meta:
                model = MyModel
                fields = '__all__'
                labels = {'nomeDoCampo':'Nome do Campo', 'nomeDeOutroCampo':'Nome de Outro Campo', 'informacoes':'Informações',}
                widgets = {
                    'data_um':DatePicker(),
                    'data_dois':DatePicker()
                }
                data_pesquisa = forms.DateField(label='Data da pesquisa', disabled=True, initial=datetime.today)

## Proteção CSRF

O django tem uma proteção padrão para o método POST vindo de nosso 
aplicativo, para cada requisição o django gera um TOKEN para o formualrio 
e vaida este TOKEN antes de efetuar em si o POST.
No HTML de formulaŕios em HTML:
    {% csrf_token %}

## Mensagens

MESSAGE_TAGS = {
    messages.ERROR: 'danger',
    messages.SUCCESS: 'sucess',
}

## Organização

Quando houver mais de 1 app em sua aplicação criar uma pasta chamada apps e 
colocar os apps la, e em settings.py:

    PROJECT_ROOT = os.path.dirname(__file__)
    sys.path.insert(0, os.path.join(PROJECT_ROOT, '../apps'))
  
