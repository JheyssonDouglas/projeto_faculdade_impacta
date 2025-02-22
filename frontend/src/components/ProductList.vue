<template>
  <div class="product-list">
    <h1>Produtos</h1>
    <ul>
      <li v-for="product in products" :key="product.id">
        <img :src="getImageUrl(product.image)" alt="product image" v-if="product.image" class="product-image"/>
        <h2>{{ product.name }}</h2>
        <p>{{ product.description }}</p>
        <p>R$ {{ formatPrice(product.price) }}</p>
        <button @click="addToCart(product)">Adicionar</button>
      </li>
    </ul>
    <div class="cart-summary">
      <h2>Carrinho</h2>
      <ul>
        <li v-for="item in cart" :key="item.product.id">
          {{ item.product.name }} - R$ {{ formatPrice(item.product.price) }} x {{ item.quantity }}
        </li>
      </ul>
      <p>Total: R$ {{ formatPrice(total) }}</p>
      <button @click="goToCart">Ir para Pagamento</button>
    </div>
  </div>
</template>

<script>
import axios from '../axios';

export default {
  name: 'ProductList',
  data() {
    return {
      products: [],
      cart: [],
    };
  },
  computed: {
    total() {
      return this.cart.reduce((sum, item) => sum + (Number(item.product.price) * item.quantity || 0), 0);
    },
  },
  created() {
    this.fetchProducts();
  },
  methods: {
    fetchProducts() {
      axios.get('/products/')
        .then(response => {
          this.products = response.data;
        })
        .catch(error => {
          console.error("There was an error fetching the products!", error);
        });
    },
    addToCart(product) {
      const cartItem = this.cart.find(item => item.product.id === product.id);
      if (cartItem) {
        cartItem.quantity++;
      } else {
        this.cart.push({ product, quantity: 1 });
      }
    },
    goToCart() {
      this.$router.push('/cart');
    },
    getImageUrl(imagePath) {
      return imagePath.startsWith('http') ? imagePath : `http://localhost:8000${imagePath}`;
    },
    formatPrice(price) {
      const numericPrice = Number(price);
      return isNaN(numericPrice) ? '0.00' : numericPrice.toFixed(2);
    }
  },
};
</script>

<style scoped>
.product-list {
  display: flex;
  justify-content: space-between;
  padding: 20px;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  margin-bottom: 20px;
}

.product-image {
  max-width: 100px;
  max-height: 100px;
  margin-bottom: 10px;
}

.cart-summary {
  width: 300px;
  border-left: 1px solid #ccc;
  padding-left: 20px;
}

button {
  margin-top: 10px;
  padding: 5px 10px;
  cursor: pointer;
}
</style>