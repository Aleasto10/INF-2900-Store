<script setup lang="ts">
import { ref, onMounted } from 'vue'
import api from '../api'
import gridSys from '@/components/grid.vue'

onMounted(fetchProducts)

interface Product {
  id: number
  name: string
  description: string
  price: string
  stock: number
  origin: string
  image: any
}
const products = ref<Product[]>([])
const loading = ref(true)
const error = ref('')

async function fetchProducts() {
  
  try {
    const { data } = await api.get<Product[]>('/products/')
    products.value = data
    
  } catch (e: any) {
    error.value = e.message
  } finally {
    loading.value = false
  }
}


</script>

<template>
  
  <!--- Passing rows and cols to child component -->
  <gridSys :rows ="3" :cols = "3"> 
    <v-hover v-slot:default="{ isHovering, props }">
            
            <v-card :class ="{'on-hover': isHovering}" v-bind="props" :elevation="isHovering ? 12 : 2">
                 <v-img :width="139", cover src="https://cdn.vuetifyjs.com/images/parallax/material.jpg"> </v-img>
            </v-card>
        
      </v-hover>
  </gridSys>
    
</template>

<style scoped>

.v-card { 
    transition: opacity 0.4s ease-in-out;
}

.v-card:not(.on-hover) {
    opacity: 0.6;
  }

</style>