<template>
  <div class="home">
    <img alt="logo" src="../assets/logo.png" class="logo"/>
    <h1>Impacta Food</h1>
    <p>Bem-vindo</p>
    <button @click="startOrder">Iniciar Pedido</button>
  </div>
</template>

<script>
export default {
  name: 'HomePage',
  methods: {
    startOrder() {
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
}

.logo {
  width: 150px;
  height: 150px;
}

button {
  margin-top: 20px;
  padding: 10px 20px;
  font-size: 16px;
  cursor: pointer;
}
</style>