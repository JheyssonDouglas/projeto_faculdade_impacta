<template>
  <div>
    <h1>Lista de Reservas</h1>
    <ul>
      <li v-for="reservation in reservations" :key="reservation.id">{{ reservation.customerName }} - {{ reservation.date }}</li>
    </ul>
  </div>
</template>

<script>
import axios from '../axios';

export default {
  data() {
    return {
      reservations: []
    };
  },
  created() {
    this.fetchReservations();
  },
  methods: {
    fetchReservations() {
      axios.get('/reservations/')
        .then(response => {
          this.reservations = response.data;
        })
        .catch(error => {
          console.error("There was an error fetching the reservations!", error);
        });
    }
  }
};
</script>