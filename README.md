# 🚗 Parking Service

### Um sistema Full Stack para gerenciamento de estacionamentos, desenvolvido em Python/Django no back-end e integrado a um front-end moderno.
### Oferece funcionalidades como cadastro de veículos, controle de entrada/saída, cálculo automático de tarifas e gerenciamento de vagas.

## 📌 Funcionalidades

### Cadastro de clientes e veículos

### Controle de entrada e saída de veículos

### Cálculo automático do valor a pagar

### Relatórios e histórico de uso

### Autenticação e autorização via JWT

### API documentada com drf-spectacular

## 🛠️ Tecnologias Utilizadas

#### Python 3.12+

#### Django 5.2.5

#### Django REST Framework

#### PostgreSQL

#### JWT Authentication (djangorestframework_simplejwt)

#### drf-spectacular (documentação OpenAPI)

#### django-rql (filtros avançados)

### Ferramentas de Desenvolvimento

#### Black, isort, flake8 (formatação e linting)

#### python-decouple (variáveis de ambiente)

#### psycopg2-binary (driver PostgreSQL)

## 📦 Instalação e Execução

### 1️⃣ Clonar o repositório

    git clone https://github.com/seu-usuario/parking-service.git
    cd parking-service

### 2️⃣ Criar e ativar o ambiente virtual

    python -m venv venv
    .\venv\Scripts\activate

### 3️⃣ Instalar as dependências

    pip install -r requirements.txt

### 5️⃣ Rodar as migrações e iniciar o servidor

    python manage.py migrate
    python manage.py runserver

## 📄 Documentação da API

#### Após iniciar o servidor, acesse:

#### Swagger UI: http://localhost:8000/api/schema/swagger-ui/

#### Redoc: http://localhost:8000/api/schema/redoc/

## 📂 Estrutura do Projeto

#### parking-service/
#### │── authentication/       
#### │── config/           
#### │── customer/    
#### │── parking/
#### │── vehicle/
#### └── .flake8
#### └── .gitignore
#### └── docker-compose.yml
#### └── manage.py
#### └── requirements.txt

## 📜 Licença
### Este projeto está licenciado sob a licença MIT - sinta-se livre para usá-lo e modificá-lo.
