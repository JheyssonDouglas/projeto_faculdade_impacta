<template>
  <div class="home">
    <h1>Bem-vindo à nossa loja</h1>
    <p>Explore nossos produtos clicando no botão abaixo.</p>
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

button {
  margin-top: 20px;
  padding: 10px 20px;
  cursor: pointer;
}
</style>