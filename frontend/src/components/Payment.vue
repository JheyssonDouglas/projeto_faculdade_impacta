<template>
    <div class="payment-page">
      <h1>Pagamento</h1>
      <div v-if="cart.length">
        <h2>Resumo do Pedido</h2>
        <ul>
          <li v-for="item in cart" :key="item.product.id">
            {{ item.product.name }} - R$ {{ formatPrice(item.product.price) }} x {{ item.quantity }}
          </li>
        </ul>
        <p>Total: R$ {{ formatPrice(total) }}</p>
      </div>
      <form @submit.prevent="submitPayment">
        <div class="form-group">
          <label for="cardNumber">Número do Cartão</label>
          <input type="text" id="cardNumber" v-model="paymentDetails.cardNumber" required />
        </div>
        <div class="form-group">
          <label for="cardHolder">Nome do Titular</label>
          <input type="text" id="cardHolder" v-model="paymentDetails.cardHolder" required />
        </div>
        <div class="form-group">
          <label for="expirationDate">Data de Validade</label>
          <input type="text" id="expirationDate" v-model="paymentDetails.expirationDate" placeholder="MM/AA" required />
        </div>
        <div class="form-group">
          <label for="cvv">CVV</label>
          <input type="text" id="cvv" v-model="paymentDetails.cvv" required />
        </div>
        <button type="submit">Pagar</button>
      </form>
    </div>
  </template>
  
  <script>
  export default {
    name: 'PaymentPage',
    data() {
      return {
        paymentDetails: {
          cardNumber: '',
          cardHolder: '',
          expirationDate: '',
          cvv: ''
        },
        cart: [],
        total: 0
      };
    },
    created() {
        const storedCart = localStorage.getItem('cart');
  const storedTotal = localStorage.getItem('total');

  if (storedCart && storedTotal) {
    this.cart = JSON.parse(storedCart);
    this.total = JSON.parse(storedTotal);
  } else {
    this.$router.push('/cart');
  }
    },
    methods: {
      submitPayment() {
        // Aqui você pode adicionar a lógica para enviar os detalhes de pagamento para o backend
        console.log('Detalhes do pagamento:', this.paymentDetails);
        console.log('Carrinho:', this.cart);
        // Redirecionar para a página de confirmação ou mostrar uma mensagem de sucesso
        this.$router.push('/confirmation');
      },
      formatPrice(price) {
        const numericPrice = Number(price);
        return isNaN(numericPrice) ? '0.00' : numericPrice.toFixed(2);
      }
    }
  };
  </script>
  
  <style scoped>
  .payment-page {
    max-width: 500px;
    margin: 0 auto;
    padding: 20px;
    border: 1px solid #ccc;
    border-radius: 5px;
    background-color: #f9f9f9;
  }
  
  h1 {
    text-align: center;
    margin-bottom: 20px;
  }
  
  .form-group {
    margin-bottom: 15px;
  }
  
  label {
    display: block;
    margin-bottom: 5px;
  }
  
  input {
    width: 100%;
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 5px;
  }
  
  button {
    width: 100%;
    padding: 10px;
    background-color: #28a745;
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    transition: background-color 0.3s;
  }
  
  button:hover {
    background-color: #218838;
  }
  </style>