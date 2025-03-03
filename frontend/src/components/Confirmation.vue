<template>
    <div class="confirmation">
      <h1>Pagamento Concluído</h1>
      <p>Obrigado por sua compra!</p>
      <button @click="goToHome">Voltar para a Página Inicial</button>
    </div>
  </template>
  
  <script>
  export default {
    name: 'ConfirmationPage',
    methods: {
      goToHome() {
        localStorage.removeItem('cart'); // Limpa o carrinho
        this.$router.push('/products'); // Redireciona para a página de produtos
      }
    }
  };
  </script>
  
  <style scoped>
  .confirmation {
    text-align: center;
    padding: 50px;
  }
  
  h1 {
    color: #28a745;
  }
  
  p {
    font-size: 18px;
    margin-bottom: 20px;
  }
  
  button {
    padding: 10px 20px;
    background-color: #007bff;
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    transition: background-color 0.3s;
  }
  
  button:hover {
    background-color: #0056b3;
  }
  </style>
  