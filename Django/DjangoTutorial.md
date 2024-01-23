# Conhecimentos sobre o Framework Django

Django é um _framework web_ em Python que simplifica o desenvolvimento, seguindo o padrão _Model-View-Template_ (MVT), e visa facilitar a criação rápida e eficiente de aplicações web robustos, integrando ORM (_Object-Relational Mapping_), administração automática e facilitando a manipulação de _URLs_.

Seus objetivos incluem promover o desenvolvimento ágil, reduzir a duplicação de código, por meio de seus apps, e fornecer uma estrutura sólida para construção de aplicativos escaláveis e seguros.

### Padrão Model View Template (MVT)
**Model**: Representa a camada de acesso a dados. Ele define como os dados são armazenados, acessados e manipulados.

**View**: Representa a camada de apresentação. Ela lida com a lógica de apresentação e interação do usuário, mas não manipula os dados diretamente.

**Template**: Esta camada é responsável pela apresentação da informação e representa a camada de templates do Django. Os templates são usados para criar a interface do usuário com a lógica de apresentação.

<br>


## Como criar uma aplicação web em Django

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

### Como criar o usuário admin
    python manage.py createsuperuser

<br>

## Conexão com Banco de Dados MySQL e Servidor Local

1. Crie um banco de dados pelo MySql;

2. Crie um arquivo chamado ``local_settings.py`` dentro do diretório ``nome_do_projeto/`` (por exemplo, neste projeto seria ``Django/NAG/``) e adicione o seguinte código;

- Note que você deve modificar todos os campos abaixo de acordo com as configurações do seu banco de dados, tais como ``NAME``, ``USER``, ``PASSWORD`` e ``PORT``.

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
    ```

3. **Execute as migrações** (já utilizando as configurações de ``local_settings.py``):

- Crie uma migração a partir do modelo de banco de dados novo ou alterado:
    
        python manage.py makemigrations --settings=nome_do_projeto.local_settings

- E, por fim, aplique a migração criada:
    
        python manage.py migrate --settings=nome_do_projeto.local_settings

<br>

## Referências e Agradecimentos:

> "If I have seen further, it is by standing on the shoulders of giants."  — Isaac Newton

Django. **Documentação Oficial**. 3.2. 2021. Disponível em: <https://docs.djangoproject.com/en/3.2/>. Acesso em: 15 jan. 2024.


Agradeço ao professor [Dr. Rodrigo Hübner](https://github.com/rodrigohubner), cuja experiência e orientação foram a fonte para a obtenção do conhecimento deste trabalho.

Bem como à instituição UTFPR por todas as experiências, conhecimentos e conexões que proporcionou-me.