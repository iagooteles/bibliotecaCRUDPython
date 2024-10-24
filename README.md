# Projeto de Gerenciamento de Livros

Este é um projeto de gerenciamento de livros desenvolvido com **Flask** e **SQLAlchemy** para o back-end, utilizando **SQLite** como banco de dados. O front-end é estilizado com **Bootstrap**.

## Funcionalidades

- Adicionar e listar livros no banco de dados.
- CRUD dos livros.
- Utilização de seeding para popular a base de dados com livros de exemplo.
- Validação para evitar duplicação de livros com IDs repetidos.

## Tecnologias Utilizadas

- [Flask](https://flask.palletsprojects.com/en/2.3.x/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [SQLite](https://www.sqlite.org/index.html)
- [Bootstrap](https://getbootstrap.com/)
- [Jinja2](https://jinja.palletsprojects.com/en/3.1.x/) (Template engine do Flask)
- [jQuery](https://jquery.com/) para manipulação dinâmica de alguns componentes.

## Como rodar o projeto

### 1. Clonar o repositório

```bash
git clone https://github.com/iagooteles/bibliotecaCRUDPython.git
cd bibliotecaCRUDPython
```

### 2. Criar um ambiente Virtual (Não obrigatório, porém recomendado)

```bash
python -m venv venv
source venv/bin/activate # Linux/Mac
venv\Scripts\activate    # Windows
```

### 3. Instalar as dependências

```bash
pip install -r requirements.txt
```

### 4. Rodar o DB do projeto
Inicie o servidor Flask e execute a criação do banco de dados e o seeding de livros.
Na pasta DB execute o mainDB.py para criar e popular o banco de dados.

```bash
python mainDB.py
```

### 5. Rodar o projeto
Após termos o banco de dados populado, podemos rodar o projeto em main.py

```bash
python main.py
```

## Modelo de dados

O modelo de livro está definido em DB/models/book_model.py com os seguintes campos:

- id (int, chave primária)
- title (string, nome do livro)
- author (string, autor do livro)
- rating (float, avaliação do livro)
