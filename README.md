# Projeto Impacta Food

Projeto final do curso de ADS da faculdade impacta.

Este projeto é uma loja virtual baseada em uma aplicação web construída com Vue.js no front-end e Django no back-end. A loja permite que os usuários naveguem por produtos, adicionem produtos ao carrinho de compras e façam pagamentos.

## Funcionalidades

- Exibição de produtos cadastrados.
- Adição de produtos ao carrinho.
- Remoção de produtos do carrinho.
- Navegação entre páginas de produtos, carrinho e pagamento.
- Processamento de pagamento.

## Estrutura do Projeto

### Front-end

O front-end foi desenvolvido utilizando Vue.js. A seguir estão as rotas configuradas:

- **`/`** - Página inicial
- **`/products`** - Página de listagem de produtos
- **`/cart`** - Página do carrinho de compras
- **`/payment`** - Página de pagamento

#### Componentes Principais

- **HomePage.vue**: Componente da página inicial.
- **ProductList.vue**: Componente de listagem de produtos.
- **Cart.vue**: Componente do carrinho de compras.
- **Payment.vue**: Componente da página de pagamento.

### Back-end

O back-end foi desenvolvido utilizando Django e Django REST Framework. A seguir estão as rotas configuradas para a API:

- **`/api/products/`** - Endpoint para listar, criar, atualizar e deletar produtos.

### Banco de dados

O banco de dados utilizado foi o MySQL

## Como Rodar o Projeto

### Pré-requisitos

- Node.js e npm
- Python e pip
- Django e Django REST Framework

### Configuração do Front-end

1. Navegue até o diretório do front-end:
   ```sh
   cd frontend
   ```

2. Instale as dependências do projeto:
   ```sh
   npm install
   ```

3. Inicie o servidor de desenvolvimento:
   ```sh
   npm run serve
   ```

### Configuração do Back-end

1. Navegue até o diretório do back-end (gestao_restaurentes):
   ```sh
   cd gestao_restaurentes
   ```

2. Crie e ative um ambiente virtual:
   ```sh
   python -m venv venv
   source venv/bin/activate
   ```

3. Instale as dependências do projeto:
   ```sh
   pip install -r requirements.txt
   ```

4. Aplique as migrações:
   ```sh
   python manage.py migrate
   ```

5. Inicie o servidor de desenvolvimento:
   ```sh
   python manage.py runserver
   ```

### Rodando o Banco de dados

1. Acessando o banco:
   ```sh
   mysql -u root -p
   ```

3. senha:
   ```sh
   banco123
   ```

5. Mostrando os databases:
   ```sh
   show databases;
   ```

7. Escolhendo o database correto:
   ```sh
   use projeto_faculdade_impacta;
   ```

9. Mostrando as tabelas:
   ```sh
    show tables;
   ```

11. Selecionando o projeto;
    ```sh
    select * from restaurente_product;
    ```
