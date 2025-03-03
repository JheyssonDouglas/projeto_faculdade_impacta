<template>
  <div class="home">
    <img src="@/assets/Impacta.png" alt="Impacta Logo" />
    <h1>Bem-vindo à Impacta Food</h1>
    
    <button @click="goToProducts">Ver Produtos</button>
  </div>
</template>

<script>
export default {
  name: 'HomePage',
  methods: {
    goToProducts() {
      this.$router.push('/products');
    }
  }
};
</script>

<style scoped>
.home {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 100vh;
  text-align: center;
}

img {
  margin-top: 20px;
  width: 450px;
}

button {
  margin-top: 20px;
  padding: 10px 20px;
  cursor: pointer;
}
</style>