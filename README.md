 Desafio Login - Fidelity Pesquisas Cadastrais

📌 Visão Geral
Este projeto é um desafio técnico proposto pela **Fidelity Pesquisas Cadastrais**, que consiste na criação de uma aplicação de login e registro de usuários utilizando **Django** e um banco de dados relacional.

 🎯 Funcionalidades Implementadas

 🖥️ Tela de Login
- Validação do login do usuário.
- Verificação de e-mail e senha, impedindo campos vazios.
- Tratamento de erros:
  - "E-mail inexistente" caso o e-mail não esteja cadastrado no banco.
  - "E-mail inválido" caso o e-mail esteja incorreto.
  - "Senha inexistente" caso a senha não esteja cadastrada no banco.
  - "Senha inválida" caso a senha informada esteja incorreta.
- Redirecionamento para a tela de registro ao clicar em "Registre-se".
- Após login bem-sucedido, o usuário é direcionado para a tela "Menu".

 📝 Tela de Registro
- Formulário com os seguintes campos:
  - **Nome**: aceita apenas letras.
  - **E-mail**: validado para garantir formato correto com "@".
  - **Senha**: requisitos mínimos (8 caracteres, 1 caractere especial, 1 número e 1 letra maiúscula).
  - **Confirmar Senha**: deve ser idêntico ao campo "Senha".
- Opção de visualizar ou ocultar a senha nos campos de "Senha" e "Confirmar Senha".
- Botão **Registrar** para envio do formulário.
- Botão **Cancelar**, que redireciona o usuário de volta para a tela de login.

 🚀 Tecnologias Utilizadas
- **Linguagem**: Python 3.12
- **Framework**: Django 5.1.6
- **Banco de Dados**: SQLite (pode ser alterado para MySQL, MariaDB ou PostgreSQL)
- **Frontend**: HTML

 ⚙️ Como Rodar o Projeto
 1️⃣ Clonar o Repositorio
```sh
    git clone https://github.com/seu-usuario/desafio-login.git
    cd desafio-login
```

 2️⃣ Criar e Ativar o Ambiente Virtual
```sh
    python -m venv venv
    source venv/bin/activate  # Linux/macOS
    venv\Scripts\activate  # Windows
```

 3️⃣ Instalar as Dependência
```sh
    pip install -r requirements.txt
```

 4️⃣ Criar o Banco de Dados e Aplicar Migrações
```sh
    python manage.py migrate
```

 5️⃣ Criar um Superusuário
```sh
    python manage.py createsuperuser
```

 6️⃣ Executar o Servidor Local
```sh
    python manage.py runserver
```
O servidor rodará em `http://127.0.0.1:8000/`

 📌 Endpoints
- `/login/` → Tela de login
- `/registrar/` → Tela de registro
- `/menu/` → Página de menu após login



