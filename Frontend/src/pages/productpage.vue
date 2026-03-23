<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
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
const products = ref<Product[]>([])
const addingProductId = ref<number | null>(null)
const accountId = 1 
const loading = ref(true)
const error = ref('')
const router = useRouter()

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

async function addToCart(id: number) {
  addingProductId.value = id
  try {
    await api.post('/cart/add/', {
      account_id: accountId,
      product_id: id,
      quantity: 1
    })
  } catch (error) {
    console.error("Error adding to cart", error)
  } finally {
    addingProductId.value = null
  }
}

onMounted(fetchProducts)
</script>

<template>
  <div class="product-page">
    <h1>Products</h1>
        <div class="product-grid">
            <div v-for="product in products" :key="product.id" class="product-card" @click="router.push(`/product/${product.id}`)">
                <h2>{{ product.name }}</h2>
                <img v-if="product.image" :src="product.image" class="picture" alt="Product Image" />
                <p v-else class="picture">Product Picture</p>
                <p>{{ product.description }}</p>
                <p class="price">${{ Number(product.price).toFixed(2) }}</p>
                <p>Stock: {{ product.stock }} &middot; Origin: {{ product.origin }}</p>
                <button class="add-to-cart-button" :disabled="product.stock <= 0 || addingProductId === product.id" @click.stop="addToCart(product.id)">
                  <span v-if="addingProductId === product.id">Adding...</span>
                  <span v-else-if="product.stock <= 0">Out of stock</span>
                  <span v-else>Add to Cart</span>
                </button>
            </div>
        </div>
  </div>
</template>

<style scoped>
.product-page {
  max-width: 100%;
  margin: 0 auto;
  padding: 2rem;
}
.product-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(290px, 1fr));
  gap: 1.5rem;
  margin-top: 1.5rem;
}
.product-card {
  border: 1px solid #ddd;
  border-radius: 8px;
  padding: 1.5rem;
  transition: box-shadow 0.2s;
  cursor: pointer;
}
.product-card:hover {
  box-shadow: 0 2px 12px rgba(0, 0, 0, 0.1);
}
.picture {
    border: 1px solid black;
    font-size: 2rem;
    height: 20rem;
    width: 20rem;
    object-fit: cover;
}
.price {
  font-size: 1.25rem;
  font-weight: bold;
  color: #263d53;
}
.add-to-cart-button {
  margin-top: 1rem;
  padding: 0.9rem 1rem;
  border: none;
  border-radius: 8px;
  background: black;
  color: white;
  font-size: 1rem;
  cursor: pointer;
}
.add-to-cart-button:hover:not(:disabled) {
  background: #222;
}
.add-to-cart-button:disabled {
  background: #999;
  cursor: not-allowed;
}
</style>