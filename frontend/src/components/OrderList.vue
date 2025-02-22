<template>
    <div>
      <h1>Pedidos</h1>
      <ul>
        <li v-for="order in orders" :key="order.id">{{ order.customerName }} - {{ order.total }}</li>
      </ul>
    </div>
  </template>
  
  <script>
  import axios from '../axios';
  
  export default {
    data() {
      return {
        orders: []
      };
    },
    created() {
      this.fetchOrders();
    },
    methods: {
      fetchOrders() {
        axios.get('/orders/')
          .then(response => {
            this.orders = response.data;
          })
          .catch(error => {
            console.error("There was an error fetching the orders!", error);
          });
      }
    }
  };
  </script>