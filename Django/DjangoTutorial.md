# Conhecimentos sobre o Framework Django

Django é um _framework web_ Python que simplifica o desenvolvimento, seguindo o padrão _Model-View-Template_ (MVT), e visa facilitar a criação rápida e eficiente de aplicações web robustas, integrando ORM (_Object-Relational Mapping_), administração automática e facilitando a manipulação de _URLs_.

Seus objetivos incluem promover o desenvolvimento ágil, reduzir a duplicação de código, por meio de seus apps, e fornecer uma estrutura sólida para construção de aplicativos escaláveis e seguros.


## Índice

**1.** [**O Padrão Model View Template (MVT)**](#o-padrão-model-view-template-mvt)<br>
**2.** [**Como iniciar um projeto web em Django**](#como-iniciar-um-projeto-web-em-django)<br>
**3.** [**Como criar um app Django**](#como-criar-um-app-django)<br>
**4.** [**Como criar o usuario administrador do Django**](#como-criar-o-usuário-admin)<br>
**5.** [**Conexão com Banco de Dados MySQL e Servidor Local**](#conexão-com-banco-de-dados-mysql-e-servidor-local)<br>
**6.** [**Como configurar o middleware CORS**](#como-configurar-o-middleware-cors)<br>
**7.** [**Como fazer login de usuários em Django com Google através do AllAuth**](#como-fazer-login-de-usuários-em-django-com-google-através-do-allauth)<br>
**8.** [**Referências e Agradecimentos**](#referências-e-agradecimentos)

<br>


## O Padrão Model View Template (MVT)
**Model**: Representa a camada de acesso a dados. Ele define como os dados são armazenados, acessados e manipulados.

**View**: Lida com a lógica de interação do usuário. Seu papel é gerenciar as requisições, mas não manipula os dados diretamente.

**Template**: Esta camada é responsável pela apresentação da informação. Os templates são usados para criar a interface do usuário com a lógica de apresentação.

<br>


## Como iniciar um projeto web em Django

### 1 - Crie um Ambiente Virtual

    python -m venv ./nome-do-venv
    
Em seguida, **ative-o** (execute este comando sempre antes de executar o projeto Django):

- Linux

    ```
    source ./nome-do-venv/bin/activate
    ```

- Windows (Prompt de Comando)

    ```
    .\nome-do-venv\Scripts\activate
    ```

- Windows (Terminal Integrado do VSCode)

    ```
    source ./nome-do-venv/Scripts/activate
    ```

### 2 - Crie um arquivo para as dependências do projeto:
    pip freeze >> requirements.txt


### 3 - Instale o Django
    python -m pip install Django

### 4 - Crie o projeto Django
    django-admin startproject nome_do_projeto

### 5 - Execute seu mais novo projeto
    cd nome_do_projeto
    python manage.py runserver

- Por padrão, o servidor local estará disponível em ``localhost:8000``.

<br>

### Como criar um app Django
    python manage.py startapp nome_do_app

- Com a app criada, faz-se necessário acoplá-la ao projeto. Para tal, insira a linha ``"nome_do_app.apps.NomeDoAppConfig",`` no fim do array `INSTALLED_APPS` do arquivo `nome_do_projeto/settings.py`, da seguinte forma:

    ```python
    INSTALLED_APPS = [
        "django.contrib.admin",
        "django.contrib.auth",
        ...
        "nome_do_app.apps.NomeDoAppConfig",
    ]
    ```

### Como criar o usuário admin
    python manage.py createsuperuser

<br>

## Conexão com Banco de Dados MySQL e Servidor Local

1. Crie um banco de dados pelo MySql;

2. Crie um arquivo chamado ``local_settings.py`` dentro do diretório ``nome_do_projeto/`` (por exemplo, neste projeto seria ``Django/NAG/NAG``) e adicione o seguinte código;

- Note que você deve modificar todos os campos abaixo de acordo com as configurações do seu banco de dados, tais como ``NAME``, ``USER``, ``PASSWORD`` e ``PORT``. Além disso, acesse o arquivo `nome_do_projeto/settings.py`, remova a `SECRET_KEY` de lá e adicione-a em `local_settings.py` conforme é mostrado a seguir.

    ```python
    from nome_do_projeto.settings import *

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'project_database_name',
            'USER': 'bd_username',
            'PASSWORD': 'bd_user_password',
            'HOST': '127.0.0.1',
            'PORT': '3306',
        }
    }

    SECRET_KEY = "sua_chave_secreta"
    # E demais configurações sigilosas
    ```

- Essa etapa é de extrema importância, pois adiciona uma camada de segurança mínima para a aplicação. Portanto, **lembre-se de adicionar este arquivo (`local_settings.py`) no seu `.gitignore`**.

3. **Execute as migrações** (já utilizando as configurações de ``local_settings.py``):

- Crie uma migração a partir do modelo de banco de dados novo ou alterado:
    
        python manage.py makemigrations --settings=nome_do_projeto.local_settings

- E, por fim, aplique a migração criada:
    
        python manage.py migrate --settings=nome_do_projeto.local_settings

<br>

## Como configurar o middleware CORS
    
Ah, o famoso problema de CORS! Esse erro ocorre quando a sua página da web, hospedada em um domínio (neste caso, ``http://localhost:5173``), tenta fazer uma solicitação XMLHttpRequest para outro domínio (``http://localhost:8000``) que não permite explicitamente tais solicitações.

Para resolver isso, é necessário configurar o seu servidor (``http://localhost:8000``) para incluir os cabeçalhos CORS apropriados em suas respostas. Especificamente, você precisa adicionar um cabeçalho ``Access-Control-Allow-Origin`` com o valor do domínio que está fazendo a solicitação (``http://localhost:5173``).

**1.** No Django, podemos utilizar o pacote ``django-cors-headers``:

        pip install django-cors-headers

**2.** Agora, no arquivo ``settings.py``, adicione o seguinte:

```python
INSTALLED_APPS = [
    # ...
    'corsheaders',
    # ...
]

MIDDLEWARE = [
    # ...
    "corsheaders.middleware.CorsMiddleware", # Adicione a linha do middleware cors
    "django.middleware.common.CommonMiddleware", # Exatamente acima deste middleware
    # ...
]

CORS_ALLOWED_ORIGINS = [
    "http://localhost:5173", # Insira o domínio do seu serviço que consome este backend, neste caso, um local host padrão de React
]
```
<br>


## Como fazer login de usuários em Django com Google através do AllAuth

O pacote AllAuth é um conjunto de pacotes para autenticação de usuários no Django. Atualmente, o pacote AllAuth suporta mais de 115 provedores de autenticação como, por exemplo, Google, GitHub, Facebook e Twitter para você utilizar no seu projeto Django.

Confira sua [documentação oficial](https://django-allauth.readthedocs.io/en/latest/index.html) para mais informações sobre quais são e como utilizar cada um deles. A seguir, você encontra um guia passo-a-passo de configuração do AllAuth em um projeto Django para realizar-se login com Google. Espero que te ajude!

### 1 - Instale o pacote AllAuth

    pip install django-allauth


### 2 - Adicione as seguintes linhas no arquivo `settings.py`:

```python
ALLOWED_HOSTS = ["localhost", "127.0.0.1"]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                # Os contextos já definidos por outros pacotes do Django aqui

                # Adicione o seguinte contexto para o AllAuth:
                'django.template.context_processors.request',
            ],
        },
    },
]

AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
)

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.messages',

    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    
    # Inclua os provedores de autenticação que deseja utilizar no projeto:
    'allauth.socialaccount.providers.google',
    # ...
]

MIDDLEWARE = (
    "django.middleware.common.CommonMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",

    # Adicione o middleware para o AllAuth:
    "allauth.account.middleware.AccountMiddleware",
)

# Realize a configuração específica para cada provedor da sua aplicação, a exemplo:
# OBS.: Talvez você queira inserir este trecho de código em um arquivo de configuração local secreto por motivos de segurança.
SOCIALACCOUNT_PROVIDERS = {
    'google': {
        # Para cada serviço de autenticação, defina uma ``SocialApp``
        # (``socialaccount`` app) contendo as credenciais necessárias da sua aplicação, listando-as aqui:
        # OBS.: Para saber como obter essas informações, consulte o passo 5.
        'APP': {
            'client_id': '123',
            'secret': '456',
            'key': ''
        }
    }
}

# Se você quiser (opcional), pode definir uma URL na qual o usuário será redirecionado assim que o login for concluído. Por padão ele redireciona para a URL da aplicação.
LOGIN_REDIRECT_URL = "http://localhost:5173/"
```

### 3 - Adicione as seguintes linhas no arquivo `urls.py`:

```python
urlpatterns = [
    # ...
    path('accounts/', include('allauth.urls')),
    # ...
]
```

### 4 - Execute a migração do banco de dados:

    python manage.py migrate

### 5 - Obtendo as credenciais do provedor de autenticação do Google:
Novamente, para obter orientação sobre como utilizar outros provedores de autenticação, consulte a [seção de Providers](https://docs.allauth.org/en/latest/socialaccount/providers/index.html) da documentação do AllAuth.

A seguir apresenta-se um exemplo de como obter as credenciais do provedor de autenticação do Google. No entanto, caso seja preferível, acesse a [seção específica do provedor Google aqui](https://docs.allauth.org/en/latest/socialaccount/providers/google.html) para seguir os passos da documentação do AllAuth.

#### **5.1 -** Registre sua aplicação no Google Developer Console
**5.1.1 -** Acesse-o pelo link https://console.developers.google.com/

**5.1.2 -** No canto esquerdo do cabeçalho superior, clique em **"Selecione um projeto"** (ou "Nome-de-outro-projeto", caso você já tenha algum ele esteja selecionado).

**5.1.3 -** Será aberto um menu do tipo modal/pop-up. Nele, crie um **novo projeto** com o botão do canto superior direito. Em seguida, insira o nome da sua aplicação e clique em **"Criar"**.

**5.1.4 -** Agora **selecione o projeto criado** e, no menu da barra lateral esquerda, clique em **"Tela de permissão OAuth"**. Em "User Type", selecione a opção **"Externo"** e clique em **"Criar"**.

**5.1.5 -** Insira as informações da sua aplicação: **Nome**, um **e-mail** para suporte e uma imagem de **logo** (se desejar).

**5.1.6 -** Insira os links do seu **domínio**: 

- Note que se sua aplicação tem um serviço de frontend separado do backend, os links devem corresponder às rotas do frontend.

- Insira a **URL da página inicial** da sua aplicação. Por exemplo: 
    ```bash
    http://localhost:5173/login/
    # ou
    http://example.com/
    ```
- Insira a **URL da Política de Privacidade** (mesmo que ainda não tenha uma). Com o modelo:
    ```bash
    http://localhost:5173/privacy/
    # ou
    http://example.com/privacy/
    ```
- Insira a **URL dos Termos de Serviço** (mesmo que não tenha também). Por exemplo:
    ```bash
    http://localhost:5173/service/
    # ou
    http://example.com/service/
    ```

**5.1.7 -** Adicione um **e-mail** em "Dados de contato do desenvolvedor" e clique em **"Salvar e Continuar"**.

**5.1.8 -** Nos escopos, são descritas as permissões que você solicita que os usuários autorizem para o app. Com elas, o projeto tem acesso a tipos específicos de dados privados do usuário na Conta do Google. Adicione os dados que sua aplicação necessitará. Então clique em **"Salvar e Continuar"**.

**5.1.9 -** Usuários de teste: Enquanto o status de publicação mostrar a opção "Testando", apenas os usuários de teste conseguirão acessar o aplicativo. Então adicione alguns e-mails para testar sua aplicação. Clique em **"Salvar e Continuar"**.

#### 5.2 - Crie as credenciais de autenticação do Google:
**5.2.1 -** No menu da barra lateral esquerda, clique em **"Credenciais"**. Então no canto esquerdo do cabeçalho superior, clique em **"Criar Credenciais"** e escolha a opção **"ID do cliente OAuth"**.

**5.2.2 -** Selecione o **tipo** da sua aplicação, insira novamente o nome da sua aplicação e insira "Origens JavaScript autorizadas", por exemplo:

    http://localhost:5173


**5.2.3 -** Especifique uma **callback URL** (ou também chamada de **"redirect URL"**)
```bash
# Por exemplo:
http://example.com/accounts/google/login/callback

# Ou para desenvolvimento local:
http://localhost:8000/accounts/google/login/callback
```

**5.2.4 -** Ao clicar em **"Criar"**, finalmente obterá as suas credenciais. **As salve!** E adicione-as em ``SOCIALACCOUNT_PROVIDERS`` no arquivo ``settings.py``, conforme o [passo 2](#2---adicione-as-seguintes-linhas-no-arquivo-settingspy).

#### 5.3 - Verifique se as credenciais foram criadas corretamente
Caso todo processo tenha funcionado corretamente, você deverá ver uma página de autenticação vinda dos templates do Django ao acessar as seguintes rotas de login e logup:

    http://127.0.0.1:8000/accounts/login
    http://127.0.0.1:8000/accounts/logup

Além disso, se acessar ``http://127.0.0.1:8000/accounts/``, poderá ver todas as rotas suportadas a serem utilizadas.

Espero que este documento tenha te ajudado de alguma forma!

<br>

## Referências e Agradecimentos:

> "If I have seen further, it is by standing on the shoulders of giants."  — Isaac Newton

Django. **Documentação Oficial**. 3.2. 2021. Disponível em: <https://docs.djangoproject.com/en/3.2/>. Acesso em: 15 jan. 2024.

**Documentação do Django AllAuth**. Disponível em: https://docs.allauth.org/en/latest/introduction/index.html. Acesso em: 09 fev. 2024.

Agradeço ao professor [Dr. Rodrigo Hübner](https://github.com/rodrigohubner), cuja experiência e orientação foram a fonte para a obtenção do conhecimento deste trabalho.

Bem como à instituição UTFPR por todas as experiências, conhecimentos e conexões que proporcionou-me.