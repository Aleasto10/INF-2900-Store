/**
 * router/index.ts
 *
 * Manual routes for ./src/pages/*.vue
 */

// Composables
import { createRouter, createWebHistory } from 'vue-router'
import Index from '@/pages/index.vue'
import ProductPage from '../pages/productpage.vue'
import Cart from '../components/Cart.vue'
import Account from '../components/ProductManagement.vue'
import ProductManagement from '../components/ProductManagement.vue'
import ProductDetail from '../pages/productdetail.vue'


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    { path: '/',
       component: Index, },
    { path: '/products',
       component: ProductPage },
    { path: '/cart',
       component: Cart },
    { path: '/account',
       component: Account },
    { path: '/productmanagement',
       component: ProductManagement },
    { path: '/product/:id',
       component: ProductDetail }
  ],
})

export default router
