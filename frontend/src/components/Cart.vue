<template>
  <div class="cart">
    <h1>Carrinho de Compras</h1>
    <ul>
      <li v-for="item in cart" :key="item.product.id">
        {{ item.product.name }} - R$ {{ formatPrice(item.product.price) }} x {{ item.quantity }}
      </li>
    </ul>
    <p>Total: R$ {{ formatPrice(total) }}</p>
    <button @click="goToCheckout">Ir para Pagamento</button>
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
    goToCheckout() {
      // Lógica para ir para a página de pagamento (checkout)
      console.log('Ir para pagamento');
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
</style>