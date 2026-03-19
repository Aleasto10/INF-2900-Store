<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import api from '../api'

interface Product {
  id: number
  name: string
  description: string
  price: string
  stock: number
  origin: string
  image: string
}

const route = useRoute()
const router = useRouter()
const product = ref<Product | null>(null)

async function fetchProduct() {
  try {
    const { data } = await api.get(`/products/${route.params.id}/`)
    product.value = data
  } catch (error) {
    console.error("Product not found", error)
    router.push('/products')
  }
}

onMounted(fetchProduct)
</script>

<template>
  <div v-if="product" class="page-wrapper">
    <div class="card">
      
      <div class="image-container">
        <img v-if="product.image" :src="product.image" alt="Product Image" />
        <div v-else class="empty-image-placeholder">
          <span>📷 No Image Available</span>
        </div>
      </div>

      <div class="info-container">
        <span class="stock-badge">📦 Only {{ product.stock }} left!</span>
        <h1 class="title">{{ product.name }}</h1>
        <p class="price">${{ Number(product.price).toFixed(2) }}</p>
        <p class="description">{{ product.description }}</p>
        <button class="btn">Add to Cart 🛒</button>
      </div>

    </div>
  </div>
</template>

<style scoped>
  .page-wrapper {
    display: flex;
    justify-content: center;
    align-items: center;
    min-height: 80vh;
    background-color: #fafbfc;
    padding: 2rem;
  }
  .card {
    display: flex;
    background: white;
    border-radius: 24px;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.08);
    overflow: hidden;
    max-width: 900px;
    width: 100%;
    gap: 2rem;
  }
  .image-container {
    flex: 1;
    display: flex;
  }
  .image-container img {
    width: 100%;
    height: 100%;
    object-fit: cover;
  }
  .empty-image-placeholder {
    width: 100%;
    height: 100%;
    min-height: 400px; 
    background-color: #f0f2f5;
    border-right: 3px dashed #d1d8e0;
    display: flex;
    justify-content: center;
    align-items: center;
    color: #8d99ae;
    font-size: 1.2rem;
    font-weight: bold;
  }
  .info-container {
    flex: 1;
    padding: 3rem 3rem 3rem 1rem;
    display: flex;
    flex-direction: column;
    justify-content: center;
  }
  .stock-badge {
    align-self: flex-start;
    background-color: #ffe8ec;
    color: #ff4d6d;
    padding: 6px 14px;
    border-radius: 20px;
    font-weight: bold;
    font-size: 0.9rem;
    margin-bottom: 1rem;
  }
  .title {
    font-size: 2.5rem;
    font-weight: 800;
    color: #2b2d42;
    margin: 0 0 0.5rem 0;
  }
  .price {
    font-size: 1.8rem;
    font-weight: 700;
    color: #8d99ae;
    margin: 0 0 1.5rem 0;
  }
  .description {
    font-size: 1.1rem;
    color: #5c677d;
    line-height: 1.6;
    margin-bottom: 2rem;
  }
  .btn {
    background-color: #2b2d42;
    color: white;
    border: none;
    border-radius: 16px;
    padding: 1rem 2rem;
    font-size: 1.2rem;
    font-weight: bold;
    cursor: pointer;
    transition: transform 0.2s, background-color 0.2s;
    box-shadow: 0 4px 15px rgba(43, 45, 66, 0.3);
  }
  .btn:hover {
    background-color: #1a1b28;
    transform: translateY(-2px);
  }
</style>