# Nasa Apod Gallery (NAG)
NAG é uma galeria das imagens astronômicas disponibilizadas pela Nasa. Os diferentes serviços de backend deste repositório consomem uma [API da Nasa](https://github.com/nasa/apod-api) para a obtenção das imagens e seus metadados.

O objetivo é criar três serviços de backend (a saber, em Django, em Java e em Go) com as mesmas funcionalidades para colocar em prática e consolidar o conhecimento das linguagens de programação e frameworks já utilizados em outros projetos.

<br>

# Django Backend
Aprenda o que é o Django, como criar seu primeiro projeto e muito mais [nesse tutorial](https://github.com/GustavoMartinx/Nasa-Apod-Gallery-Back/blob/main/Django/DjangoTutorial.md) que eu fiz!

## Como Executar

### 1 - Ative seu Ambiente Virtual:

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

### 2 - Instale as dependências do projeto:
        
- manualmente:

        pip install -r requirements.txt

- ou automaticamente através do makefile:

        make install


### 3 - Conecte com Banco de Dados MySQL e Servidor Local

1. Crie um banco de dados pelo MySql (nomeie-o `nag_db`);

2. Crie um arquivo chamado ``local_settings.py`` dentro do diretório ``Django/NAG/`` e adicione o seguinte código;

- Note que você deve modificar todos os campos abaixo de acordo com as configurações do seu banco de dados, tais como ``USER``, ``PASSWORD`` e ``PORT``.

    ```python
    from nome_do_projeto.settings import *

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'nag_db',
            'USER': 'bd_username',
            'PASSWORD': 'bd_user_password',
            'HOST': '127.0.0.1',
            'PORT': '3306',
        }
    }
    ```

3. **Execute as migrações** (já utilizando as configurações de ``local_settings.py``):

- Crie uma migração a partir do modelo de banco de dados novo ou alterado (através do makefile):
    
        make makemigrations

- E, por fim, aplique a migração criada, também por meio do makefile:
    
        make migrate

### 4 - Execute o Projeto

        make runserver

- Por padrão, o servidor local estará disponível em ``localhost:8000``.
