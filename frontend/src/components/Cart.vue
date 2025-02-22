<template>
  <div class="cart">
    <h1>Carrinho</h1>
    <ul>
      <li v-for="item in cart" :key="item.product.id">
        {{ item.product.name }} - R$ {{ item.product.price.toFixed(2) }} x {{ item.quantity }}
        <p>Subtotal: R$ {{ (item.product.price * item.quantity).toFixed(2) }}</p>
      </li>
    </ul>
    <p>Total: R$ {{ total.toFixed(2) }}</p>
    <button @click="goToPayment">Ir para Pagamento</button>
  </div>
</template>

<script>
export default {
  name: 'Cart',
  data() {
    return {
      cart: [],
    };
  },
  computed: {
    total() {
      return this.cart.reduce((sum, item) => sum + item.product.price * item.quantity, 0);
    },
  },
  created() {
    this.loadCart();
  },
  methods: {
    loadCart() {
      const savedCart = JSON.parse(localStorage.getItem('cart') || '[]');
      this.cart = savedCart;
    },
    goToPayment() {
      alert('Indo para a tela de pagamento...');
    },
  },
};
</script>

<style scoped>
.cart {
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
  margin-top: 20px;
  padding: 10px 20px;
  cursor: pointer;
}
</style>