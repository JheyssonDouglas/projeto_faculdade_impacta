<template>
    <div>
      <h1>Lista de Restaurantes</h1>
      <ul>
        <li v-for="restaurant in restaurants" :key="restaurant.id">{{ restaurant.name }} - {{ restaurant.location }}</li>
      </ul>
    </div>
  </template>
  
  <script>
  import axios from '../axios';
  
  export default {
    data() {
      return {
        restaurants: []
      };
    },
    created() {
      this.fetchRestaurants();
    },
    methods: {
      fetchRestaurants() {
        axios.get('/restaurants/')
          .then(response => {
            this.restaurants = response.data;
          })
          .catch(error => {
            console.error("There was an error fetching the restaurants!", error);
          });
      }
    }
  };
  </script>