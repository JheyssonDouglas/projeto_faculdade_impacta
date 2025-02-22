<template>
  <div id="app">
    <nav>
      <ul>
        <li><router-link to="/">Home</router-link></li>
        <li><router-link to="/dishes">Pratos</router-link></li>
        <li><router-link to="/employees">Funcionários</router-link></li>
        <li><router-link to="/orders">Pedidos</router-link></li>
        <li><router-link to="/reservations">Reservas</router-link></li>
        <li><router-link to="/restaurants">Restaurantes</router-link></li>
        <li><router-link to="/stocks">Estoque</router-link></li>
      </ul>
    </nav>
    <router-view></router-view>
  </div>
</template>

<script>
export default {
  name: 'App',
};
</script>

<style>
nav ul {
  list-style-type: none;
  padding: 0;
}

nav ul li {
  display: inline;
  margin-right: 10px;
}
</style>
