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
      <button @click="goToCart" class="go-to-payment-button">Ir para Pagamento</button>
      <button @click="clearCart" class="clear-cart-button">Limpar Carrinho</button>
      <button @click="logout" class="logout-button">Sair</button>
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
          <button @click="addToCart(product)" class="add-to-cart-button">Adicionar</button>
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
    clearCart() {
      this.cart = []; // Esvazia o array do carrinho
      this.saveCart(); // Salva no localStorage para atualizar
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
    },
    async saveCartToBackend() {
      try {
      await axios.delete('/cart/'); // limpa carrinho antigo
      for (const item of this.cart) {
        await axios.post('/cart/', {
          product: item.product.id,
          quantity: item.quantity,
    });
  }
} catch (error) {
        console.error("Erro ao salvar o carrinho no backend:", error);
      }
    },
    logout() {
      localStorage.removeItem('cart'); // Limpa o carrinho do localStorage
      this.cart = []; // Limpa o carrinho da memória
      this.$router.push('/');
    }
  },
  watch: {
    cart: {
      deep: true,
      handler() {
        this.saveCart();
        this.saveCartToBackend();
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
  border-right: 1px solid #d1d1d1; /* Mudando para um cinza mais escuro */
  padding-right: 20px;
  margin-right: 20px;
  background-color: #f8f9fa; /* Adicionando um fundo mais suave */
  padding: 15px;
  border-radius: 8px; /* Bordas arredondadas */
  position: sticky;
  top: 159px; /* Ajuste a distância do topo */
  height: fit-content;
}

.products-section {
  flex: 1;
}

.products-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
  gap: 20px;
  width: 100%;
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
  width: 100%;
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
  width: 100%;
}

.clear-cart-button:hover {
  background-color: #cc0000; /* Vermelho mais escuro no hover */
}

.product-item {
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  border: 1px solid #ebf1f1;
  padding: 10px;
  border-radius: 5px;
  height: 100%;
}

.product-item p:nth-of-type(2) {
  font-size: 25px; /* Ajuste o tamanho da fonte */
  font-weight: bold; /* Deixe o preço em negrito */
  color: #0976f3; /* Cor personalizada */
  margin: 5px 0;
  margin-top: auto;
}

.product-image {
  max-width: 100px;
  max-height: 100px;
  margin-bottom: 10px;
}

.quantity-controls {
  display: flex;
  align-items: center;
  justify-content: center;
  margin-top: auto; /* Garante que fique no final antes do botão */
  width: 100%;
}

.quantity-controls button {
  margin: 0 5px;
  padding: 5px 10px;
  cursor: pointer;
}

.add-to-cart-button {
  margin-top: auto;
  padding: 10px 20px;
  background-color: #0063f7;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s;
  width: 50%;
}

.add-to-cart-button:hover {
  background-color: #000a61;
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

.logout-button {
  margin-top: 10px;
  padding: 10px 20px;
  background-color: #6c757d; /* Cinza neutro */
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s;
  width: 100%;
}

.logout-button:hover {
  background-color: #5a6268; /* Cinza mais escuro */
}
</style>