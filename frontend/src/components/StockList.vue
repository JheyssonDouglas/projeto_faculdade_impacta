<template>
    <div>
      <h1>Estoque</h1>
      <ul>
        <li v-for="stock in stocks" :key="stock.id">{{ stock.item }} - {{ stock.quantity }}</li>
      </ul>
    </div>
  </template>
  
  <script>
  import axios from '../axios';
  
  export default {
    data() {
      return {
        stocks: []
      };
    },
    created() {
      this.fetchStocks();
    },
    methods: {
      fetchStocks() {
        axios.get('/stocks/')
          .then(response => {
            this.stocks = response.data;
          })
          .catch(error => {
            console.error("There was an error fetching the stocks!", error);
          });
      }
    }
  };
  </script>