# login e cadastro usando allauth

# link tutorial:

# https://www.youtube.com/watch?v=ryIFjfbH91I
# https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbFZUUzdHWWhsV3d5aXhvMGNKd0pBNnhEaHFrZ3xBQ3Jtc0trSnRvX19MNEdwRHU1REFZNE9fREFhaFh4ZkJidGREXzBGM3RvOEZhUXY4REk2cFBDMmVtcnRfNW45WmdEY0MzNTRJcTluUHczLVhQbHNVTDlzTThZeHBOLWlUUXB3Y1h2dW1RR2xJMTNFUWd5UDI5WQ&q=https%3A%2F%2Fdjango-allauth.readthedocs.io%2Fen%2Flatest%2Finstallation.html
# https://github.com/fabioruicci/django-cadastro-login-email-senha-allauth-e-custom-user

# etapas iniciais

"""

primeiramente, crie uma variavel ambiente:

    python -m venv venv

dps ative a variavel ambiente entrando na pasta scripts:

    activate

com a variavel ambiente ativa, instale o django com o pip:

    pip install django

"""

# iniciando o projeto

"""

para criar o projeto, use o django admin no terminal:

    django-admin startproject tutorialcadastro
    
sendo 'tutorialcadastro' o nome do projeto

"""

# teste

"""

inicie o projeto para conferir se o projeto esta configurado de forma certa (dentro da pasta 'tutorial cadastro'):

    python manage.py runserver

"""

# django-allauth

"""

instale o allauth:

    pip install django-allauth

no 'settings.py', do nosso projeto, dentro da variavel 'templates', tenha certeza que esteja da seguinte forma:

    'context_processors': [
                    'django.template.context_processors.debug',
                    'django.template.context_processors.request', <---- importante
                    'django.contrib.auth.context_processors.auth',
                    'django.contrib.messages.context_processors.messages',
    ],
    
ainda no 'settings.py', adicione as configurações do django allauth:

    AUTHENTICATION_BACKENDS = [
        "django.contrib.auth.backends.ModelBackend",
        "allauth.account.auth_backends.AuthenticationBackend",
    ]
    
    SITE_ID = 1 
    
e dentro do 'INSTALLED_APPS', adicione:

    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',   <--- confirme
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages', <--- confirme
        'django.contrib.staticfiles',
        'django.contrib.sites', <--- adicione
        
        # 3rd party              <--- adicione
        'allauth',               <---    ''
        'allauth.account',       <---    ''
        'allauth.socialaccount', <---    ''
    ]
    
"""

# em urls.py

"""

importe o include:

    from django.urls import path, include

depois em urlpatterns:

urlpatterns = [
    # django admin
    path('admin/', admin.site.urls),
    
    # user management
    path('account/', include('allauth.urls')), <--- adicione
    
    # local
]
"""

# migrate

""" python manage.py migrate """

"""
agora se vc rodar o codigo, com o 'runserver', vc consegue ver o sintema de registro e de login, do django-allauth

acesse a pagina:

    <ip:porta>/account/login/
    
    
"""

# considerações

"""

após criarmos uma conta, somos redirecionados para 'account/profile/', temos duas opções, ou criamos uma pagina profile,
ou redirecionamos para outra pagina.

"""

# outra pagina

"""

para mudar para onde o usuario vai, após logar na conta, adicionamos no 'settings.py':

    LOGIN_REDIRECT_URL = "/" <--- envia para a primeira pagina
    
"""

# teste o login novamente e veja a alteração, veja que somos redirecionados para a primeira pagina

# configurando os templates

"""

inicie o app:

    python manage.py startapp pages
    
sendo 'pages', o nome do app

em 'settings.py', em 'INSTALLED_APPS':

    INSTALLED_APPS = [    
        (...)
        
        # local apps <---
        'pages.apps.PagesConfig', <--- adicione
    ]

e em 'templates', dentro de 'DIRS':
    
    'DIRS': [BASE_DIR / "templates"],
    
dessa forma, na raiz, podemos criar uma pasta templates, com templates, para ele usar.

"""

# dentro de 'templates'

"""

dentro de tempaltes, crie outra pasta chamada 'account', e dentro de 'account', crie um html 'base.html', e cole o html.
html usado encontrado no github do criador.

faça o mesmo criando um arquivo 'home'.

"""

# configurando as urls

"""

dentro da pasta do app criado ('pages'), crie um arquivo chamado 'urls.py', e dentro dele:

    from django.urls import path
    from . import views
    
    app_name = 'pages'
    
    urlpatterns = [
        path('', views.HomePageView.as_view(), name='home'), <--- ainda temos que criar a classe 'HomePageView', dentro de view
        
    ]

"""

# criando view

"""

dentro do view, adicione:

    from django.views.generic import TemplateView
    
    
    class HomePageView(TemplateView):
        template_name = 'home.html'

"""

# adiconando as urls criadas

"""

dentro de 'urls.py', em 'urlpatterns', da pasta do projeto::

urlpatterns = [
    (...)

    # local
    path('', include(pages.url, namespace = 'pages'))
]
 

"""

# arrumando os inputs, que estao tortos e desalinhados
# django-crispy-forms

"""

instale o django crispy-forms:

    pip install django-crispy-forms
    
adicione 'crispy-forms' no 'INSTALLED_APPS':

    INSTALLED_APPS = [
        (...)
        
        # 3rd party
        'allauth',
        'allauth.account',
        'allauth.socialaccount',
        'crispy_forms', <--- adicione
        
        (...)
    ]

ainda em 'settings.py', adicione:

    # django-crispy-forms <---
    CRISPY_TEMPLATE_PACK = 'bootstrap4' <---
    
"""

# criando os 'html' do crispy-forms

"""

crie uma pasta dentro de 'templates', chamada 'account', e dentro de account:
- crie 3 arquivos html, chamados, 'login.html', 'logout.html' e 'signup.html'
 - use o html do github ja citado.

"""

# considerações finais
# após o tutorial, decidi repitir o processo algumas vezes, e desenvolver meu proprio html e css.
