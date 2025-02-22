import { createRouter, createWebHistory } from 'vue-router';
import HomePage from '../components/HomePage.vue';
import DishsList from '../components/DishsList.vue';
import EmployeeList from '../components/EmployeeList.vue';
import OrderList from '../components/OrderList.vue';
import ReservationList from '../components/ReservationList.vue';
import RestaurantList from '../components/RestaurantList.vue';
import StockList from '../components/StockList.vue';

const routes = [
  { path: '/', component: HomePage },
  { path: '/dishes', component: DishsList },
  { path: '/employees', component: EmployeeList },
  { path: '/orders', component: OrderList },
  { path: '/reservations', component: ReservationList },
  { path: '/restaurants', component: RestaurantList },
  { path: '/stocks', component: StockList },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
});

export default router;