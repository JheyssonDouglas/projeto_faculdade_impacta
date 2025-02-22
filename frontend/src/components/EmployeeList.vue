<template>
    <div>
      <h1>Funcionários</h1>
      <ul>
        <li v-for="employee in employees" :key="employee.id">{{ employee.name }} - {{ employee.position }}</li>
      </ul>
    </div>
  </template>
  
  <script>
  import axios from '../axios';
  
  export default {
    data() {
      return {
        employees: []
      };
    },
    created() {
      this.fetchEmployees();
    },
    methods: {
      fetchEmployees() {
        axios.get('/employees/')
          .then(response => {
            this.employees = response.data;
          })
          .catch(error => {
            console.error("There was an error fetching the employees!", error);
          });
      }
    }
  };
  </script>