import { createRouter, createWebHistory } from 'vue-router';
import HomePage from '../components/HomePage.vue';
import ProductList from '../components/ProductList.vue';
import Cart from '../components/Cart.vue';

const routes = [
  { path: '/', component: HomePage },
  { path: '/products', component: ProductList },
  { path: '/cart', component: Cart },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
});

export default router;