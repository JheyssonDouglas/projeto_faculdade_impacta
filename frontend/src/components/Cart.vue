<template>
  <div class="cart">
    <h1>Carrinho de Compras</h1>
    <ul>
      <li v-for="item in cart" :key="item.product.id">
        {{ item.product.name }} - R$ {{ formatPrice(item.product.price) }} x {{ item.quantity }}
      </li>
    </ul>
    <p>Total: R$ {{ formatPrice(total) }}</p>
    <button @click="goToPayment" class="go-to-payment-button">Ir para Pagamento</button>
    <button @click="clearCart" class="clear-cart-button">Limpar Carrinho</button>
    <button @click="goBack">Voltar</button>
  </div>
</template>

<script>
export default {
  name: 'Cart',
  data() {
    return {
      cart: JSON.parse(localStorage.getItem('cart')) || [],
    };
  },
  computed: {
    total() {
      return this.cart.reduce((sum, item) => sum + (Number(item.product.price) * item.quantity || 0), 0);
    }
  },
  methods: {
    formatPrice(price) {
      const numericPrice = Number(price);
      return isNaN(numericPrice) ? '0.00' : numericPrice.toFixed(2);
    },
    goToPayment() {
      localStorage.setItem('cart', JSON.stringify(this.cart));
      localStorage.setItem('total', JSON.stringify(this.total));
      this.$router.push('/payment');
    },
    clearCart() {
      this.cart = []; // Esvazia o array do carrinho
      this.saveCart(); // Salva no localStorage para atualizar
    },
    saveCart() {
      localStorage.setItem('cart', JSON.stringify(this.cart)); // Certifique-se de que saveCart está aqui
    },
    goBack() {
      this.$router.push('/products');
    }
  }
};
</script>

<style scoped>
.cart {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 20px;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  margin-bottom: 20px;
}

button {
  margin-top: 10px;
  padding: 5px 10px;
  cursor: pointer;
}

.go-to-payment-button {
  margin-top: 10px;
  padding: 12px 20px;
  background-color: #007bff; /* Azul padrão */
  color: white;
  font-size: 16px;
  font-weight: bold;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s, transform 0.2s;
  width: 25%;
}

.go-to-payment-button:hover {
  background-color: #0056b3; /* Azul mais escuro no hover */
  transform: scale(1.05); /* Efeito de leve aumento ao passar o mouse */
}

.go-to-payment-button:active {
  background-color: #004494; /* Azul ainda mais escuro ao clicar */
  transform: scale(0.98); /* Pequena redução ao pressionar */
}

.clear-cart-button {
  margin-top: 10px;
  padding: 10px 20px;
  background-color: #ff4d4d; /* Vermelho para indicar remoção */
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s;
  width: 20%;
}

.clear-cart-button:hover {
  background-color: #cc0000; /* Vermelho mais escuro no hover */
}
</style>