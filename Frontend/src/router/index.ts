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
import addresspage from '@/pages/addresspage.vue'
import Login from '@/pages/Login.vue'
import CreateAccount from '@/pages/CreateAccount.vue'


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      component: Index,
    },
    { path: '/products',
       component: ProductPage },
    { path: '/cart',
       component: Cart },
    { path: '/account',
       component: Account },
    { path: '/productmanagement',
       component: ProductManagement },
    { path: '/address',
       component: addresspage },
    { path: '/login', 
       component: Login },
    { path: '/createaccount',
       component: CreateAccount
    }
  ],
})

export default router
