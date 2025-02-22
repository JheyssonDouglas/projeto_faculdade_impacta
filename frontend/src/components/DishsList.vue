<template>
  <div>
    <h1>Pratos</h1>
    <ul>
      <li v-for="dish in dishs" :key="dish.id">{{ dish.name }} - {{ dish.price }}</li>
    </ul>
  </div>
</template>

<script>
import axios from '../axios';

export default {
  data() {
    return {
      dishs: []
    };
  },
  created() {
    this.fetchDishs();
  },
  methods: {
    fetchDishs() {
      axios.get('/dishes/')
        .then(response => {
          this.dishs = response.data;
        })
        .catch(error => {
          console.error("There was an error fetching the dishs!", error);
        });
    }
  }
};
</script>