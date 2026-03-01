import './assets/main.css'

import { createApp } from 'vue'
import App from './App.vue'

import {createRouter, createWebHistory} from 'vue-router'

import admin from '@/views/admin.vue'



const router = createRouter({ 
    history: createWebHistory(),
    routes: [
        {path: '/admin', name: 'admin', component: admin}
    ]
})


createApp(App)  
.use(router)
.mount('#app')

