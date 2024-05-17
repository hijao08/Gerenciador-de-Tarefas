# Django REST Framework CRUD

Este é um projeto básico de CRUD (Create, Read, Update, Delete) utilizando Django e Django Rest Framework.

## Visão Geral

Este projeto demonstra um simples aplicativo de tarefas (Todo) onde você pode:
- Criar novas tarefas
- Ler ou listar todas as tarefas
- Atualizar tarefas existentes
- Deletar tarefas

## Requisitos

- Python 3.8+
- Django 4.2.13
- Django Rest Framework 3.15.1

## Instalação

1. Clone este repositório:

    ```bash
    git clone https://github.com/hijao08/api_todo.git
    cd api_todo
    ```

2. Crie um ambiente virtual:
   
     ```bash
    sudo apt update
    sudo apt install python3.8-venv
    python3.8 -m venv env
    source env/bin/activate  # No Windows use `env\Scripts\activate`
    ```

4. Instale as dependências:

    ```bash
    pip install djangorestframework
    ```

5. Configure o banco de dados:

    ```bash
    python manage.py migrate
    ```

6. Execute o servidor de desenvolvimento:

    ```bash
    python manage.py runserver
    ```

## Endpoints da API

- `GET /todos/` - Lista todas as tarefas
- `POST /todos/` - Cria uma nova tarefa
- `GET /todos/{id}/` - Detalha uma tarefa específica
- `PUT /todos/{id}/` - Atualiza uma tarefa específica
- `DELETE /todos/{id}/` - Deleta uma tarefa específica

