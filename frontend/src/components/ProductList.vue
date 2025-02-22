<template>
  <div class="product-list">
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
    <div class="products-section">
      <h1>Produtos</h1>
      <div class="products-grid">
        <div v-for="product in paginatedProducts" :key="product.id" class="product-item">
          <img :src="getImageUrl(product.image)" alt="product image" v-if="product.image" class="product-image"/>
          <h2>{{ product.name }}</h2>
          <p>{{ product.description }}</p>
          <p>R$ {{ formatPrice(product.price) }}</p>
          <div class="quantity-controls">
            <button @click="decreaseQuantity(product)">-</button>
            <span>{{ getQuantity(product) }}</span>
            <button @click="increaseQuantity(product)">+</button>
          </div>
          <button @click="addToCart(product)">Adicionar</button>
        </div>
      </div>
      <div class="pagination">
        <button @click="prevPage" :disabled="currentPage === 1">Anterior</button>
        <span>Página {{ currentPage }} de {{ totalPages }}</span>
        <button @click="nextPage" :disabled="currentPage === totalPages">Próxima</button>
      </div>
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
      cart: JSON.parse(localStorage.getItem('cart')) || [],
      currentPage: 1,
      itemsPerPage: 20,
    };
  },
  computed: {
    total() {
      return this.cart.reduce((sum, item) => sum + (Number(item.product.price) * item.quantity || 0), 0);
    },
    paginatedProducts() {
      const start = (this.currentPage - 1) * this.itemsPerPage;
      const end = start + this.itemsPerPage;
      return this.products.slice(start, end);
    },
    totalPages() {
      return Math.ceil(this.products.length / this.itemsPerPage);
    }
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
      this.saveCart();
    },
    decreaseQuantity(product) {
      const cartItem = this.cart.find(item => item.product.id === product.id);
      if (cartItem) {
        cartItem.quantity--;
        if (cartItem.quantity <= 0) {
          this.cart = this.cart.filter(item => item.product.id !== product.id);
        }
      }
      this.saveCart();
    },
    increaseQuantity(product) {
      const cartItem = this.cart.find(item => item.product.id === product.id);
      if (cartItem) {
        cartItem.quantity++;
      } else {
        this.cart.push({ product, quantity: 1 });
      }
      this.saveCart();
    },
    getQuantity(product) {
      const cartItem = this.cart.find(item => item.product.id === product.id);
      return cartItem ? cartItem.quantity : 0;
    },
    saveCart() {
      localStorage.setItem('cart', JSON.stringify(this.cart));
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
    },
    prevPage() {
      if (this.currentPage > 1) {
        this.currentPage--;
      }
    },
    nextPage() {
      if (this.currentPage < this.totalPages) {
        this.currentPage++;
      }
    }
  },
  watch: {
    cart: {
      deep: true,
      handler() {
        this.saveCart();
      }
    }
  }
};
</script>

<style scoped>
.product-list {
  display: flex;
  padding: 20px;
}

.cart-summary {
  width: 300px;
  border-right: 1px solid #ccc;
  padding-right: 20px;
  margin-right: 20px;
}

.products-section {
  flex: 1;
}

.products-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
  gap: 20px;
  width: 100%;
}

.product-item {
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  border: 1px solid #ccc;
  padding: 10px;
  border-radius: 5px;
}

.product-image {
  max-width: 100px;
  max-height: 100px;
  margin-bottom: 10px;
}

.quantity-controls {
  display: flex;
  align-items: center;
  margin-bottom: 10px;
}

.quantity-controls button {
  margin: 0 5px;
  padding: 5px 10px;
  cursor: pointer;
}

.pagination {
  display: flex;
  justify-content: center;
  align-items: center;
  margin-top: 20px;
}

.pagination button {
  margin: 0 10px;
  padding: 5px 10px;
  cursor: pointer;
}

.pagination span {
  margin: 0 10px;
}
</style>