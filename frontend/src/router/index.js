import { createRouter, createWebHistory } from 'vue-router';
import HomePage from '../components/HomePage.vue';
import ProductList from '../components/ProductList.vue';
import Cart from '../components/Cart.vue';
import Payment from '../components/Payment.vue';
import Confirmation from '../components/Confirmation.vue';

const routes = [
  { path: '/', component: HomePage },
  { path: '/products', component: ProductList },
  { path: '/cart', component: Cart },
  { path: '/payment', component: Payment },
  { path: '/confirmation', component: Confirmation },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
});

export default router;