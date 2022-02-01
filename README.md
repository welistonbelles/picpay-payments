# README

<p align="center">
    <a href="#sobre">Sobre</a>
    <a href="#tecnologias">Tecnologias</a>
    <a href="#funcionalidades">Funcionalidades</a>
    <a href="#demonstracao">Demonstração</a>
    <a href="#instalacao">Instalação</a>
</p>

# Sobre
<p>Este projeto foi construído com o intuito de praticar o consumo de API's externas e automatizar métodos de pagamentos.<br>
Consiste em 1 página de pagamentos utilizando o PicPay, que pode facilmente ser integrada a projetos onde se faça necessário a utilização de métodos de pagamentos.

# Tecnologias
<p>O projeto foi construído utilizando as seguintes tecnologias:</p>
<ul>
    <li>Python<img align="center" alt="Weliston-Python" height="30" width="40" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg"></li>
    <li>Django<img align="center" alt="Weliston-Django" height="30" width="40" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/django/django-original.svg"></li>
    <li>Django Rest Framework</li>
    <li>HTML5<img align="center" alt="Weliston-HTML" height="30" width="40" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/html5/html5-original.svg"></li>
    <li>CSS<img align="center" alt="Weliston-CSS" height="30" width="40" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/css3/css3-original.svg"></li>
    <li>Postgres SQL (Para o ambiente de produção)</li>
    <li>SQLite (para desenvolvimento local)</li>
</ul>

# Funcionalidades
- ✅ Gerar uma cobrança utilizando a API do PicPay.
- ✅ Apresentar o QRCode para o usuário realizar o pagamento.
- ✅ Apresentar o status das últimas 6 cobranças geradas.
- ✅ Reconhecer quando uma cobrança for paga e atualizar o status dela.
- ✅ Consumo de API de terceiros.


# Demonstracao
Link para a [aplicação](https://picpay-pagamentos-django.herokuapp.com/)
<h1 align="center">
    Tela inicial, contendo a listagem dos últimos pedidos de pagamentos gerados.
    <img alt="Listagem de Tarefas" src="./github/homepage.png"/>
</h1>


# Instalacao
Antes de começar, você vai precisar ter instalado em sua máquina as seguintes ferramentas:
[Git](https://gitscm.com), [Python](https://www.python.org/downloads/).
Além disso é bom ter um editor para trabalhar com o código como o [VSCode](https://code.visualstudio.com/download) ou o [PyCharm](https://www.jetbrains.com/pt-br/pycharm/download/) (Recomendado).

```bash
# Clone este repositório
$ git clone <https://github.com/welistonbelles/picpay-payments>

# Acesse a pasta do projeto no terminal/cmd
$ cd picpay-payments

# Instale as dependências
$ pip install -r requirements.txt
```
### 🔧 Configuracao
```python
# Primeiramente vamos criar as migrations
python manage.py makemigrations

# Agora aplique elas ao seu banco de dados
python manage.py migrate

# Com tudo configurado, basta rodarmos nossa aplicação:
python manage.py runserver
```