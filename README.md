# Carros

Um projeto baseado em Django para gerenciar e organizar informações sobre carros e usuários.

## 🚀 Funcionalidades

- **Gerenciamento de Usuários**:
  - Cadastro e autenticação.
  - Perfis de usuário.

- **Gerenciamento de Carros**:
  - Adicionar, editar e listar carros.
  - Detalhes e características de cada veículo.

## 🛠️ Tecnologias Utilizadas

- **Back-end**: Django (Python)
- **Servidor**: uWSGI para implantação.
- **Outras dependências**: (conforme especificado no `requirements.txt`).

## 📦 Instalação

Siga os passos abaixo para configurar o projeto localmente:

1. Clone o repositório:
   ```bash
   git clone https://github.com/BrunoAcioli23/carros.git
   ```
2. Navegue até o diretório do projeto:
   ```bash
   cd carros
   ```
3. Crie e ative um ambiente virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate # No Windows: venv\Scripts\activate
   ```
4. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
5. Realize as migrações do banco de dados:
   ```bash
   python manage.py migrate
   ```
6. Inicie o servidor de desenvolvimento:
   ```bash
   python manage.py runserver
   ```

## 📂 Estrutura do Projeto

- `accounts/`: Módulo de gerenciamento de usuários.
- `cars/`: Módulo de gerenciamento de carros.
- `app/`: Lógica principal do projeto.
- `requirements.txt`: Dependências do projeto.
- `manage.py`: Script para execução e administração do projeto Django.

## 🌐 Deploy

O projeto inclui configurações para deploy utilizando o servidor **uWSGI**. Confira os arquivos `carros_uwsgi.ini` e `uwsgi_params` para ajustes.


Desenvolvido por [Bruno Acioli](https://github.com/BrunoAcioli23)