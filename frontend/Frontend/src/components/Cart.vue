<script setup lang="ts">
import { ref, computed, onMounted } from "vue"

interface CartItemType {
  product_id: number
  name: string
  price: number
  quantity: number
  image?: string
  size?: string
  color?: string
}

const cart = ref<CartItemType[]>([])
const accountId = 1 //FOR TESTING

async function fetchCart() {
  //fetch the cart from Django
  try {
    const response = await fetch(`http://localhost:8000/api/cart/${accountId}/`)
    const data = await response.json()
    if (data.items) {
      cart.value = data.items
    } else {
      cart.value = []
    }
  } catch (error) {
    console.error("Make sure Django is running!", error)
  }
}

//run fetchCart automatically when the page loads
onMounted(() => {
  fetchCart()
})

async function addToCart(id: number) {
  //add an item to the cart
  try {
    await fetch('http://localhost:8000/api/cart/add/', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        account_id: accountId,
        product_id: id,
        quantity: 1
      })
    })
    fetchCart() //refresh
  } catch (error) {
    console.error("Error adding to cart", error)
  }
}

async function updateQuantity(id: number, currentQuantity: number, change: number) {
  //increase or decrease quantity
  const newQuantity = currentQuantity + change
  
  if (newQuantity <= 0) {
    removeItem(id)
    return
  }

  const url = change > 0 ? 'http://localhost:8000/api/cart/add/' : 'http://localhost:8000/api/cart/decrease/'
  
  try {
    await fetch(url, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        account_id: accountId,
        product_id: id,
        quantity: 1
      })
    })
    fetchCart() //refresh
  } catch (error) {
    console.error("Error updating quantity", error)
  }
}

async function removeItem(id: number) {
  //remove item entirely
  try {
    await fetch('http://localhost:8000/api/cart/remove/', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        account_id: accountId,
        product_id: id
      })
    })
    fetchCart() //refresh
  } catch (error) {
    console.error("Error removing item", error)
  }
}

const total = computed(() =>
  cart.value.reduce((sum, item) => sum + item.price * item.quantity, 0)
)
</script>

<template>
  <div style="background:#f5f5f5; min-height:100vh; padding:60px 20px;">
    <div style="max-width:1100px; margin:auto;">

      <h1 style="font-size:28px; font-weight:600; margin-bottom:30px;">
        Shopping Cart
      </h1>

      <!-- BUTTON TO TEST FUNCTIONALITIES -->
      <button 
        @click="addToCart(1)" 
        style="margin-bottom: 20px; padding: 12px 20px; background: #007bff; color: white; border: none; border-radius: 8px; font-weight: bold; cursor: pointer;">
        + Test: Add Laptop to Cart
      </button>

      <div
        v-if="cart.length === 0"
        style="text-align:center; padding:60px; color:#666;"
      >
        Your cart is empty.
      </div>

      <div
        v-else
        style="background:white; padding:30px; border-radius:16px; box-shadow:0 10px 25px rgba(0,0,0,0.08);"
      >

        <div
          v-for="item in cart"
          :key="item.product_id"
          style="display:flex; gap:20px; padding:25px 0; border-bottom:1px solid #eee;"
        >
          <img
            src="https://images.unsplash.com/photo-1606220945770-b5b6c2c55bf1"
            style="width:100px; height:100px; object-fit:cover; border-radius:12px;"
          />

          <div style="flex:1;">
            <h2 style="font-size:18px; font-weight:500; margin-bottom:6px;">
              {{ item.name }}
            </h2>

            <div style="margin-top:10px; font-weight:600;">
              €{{ item.price.toFixed(2) }}
            </div>
          </div>

          <div style="display:flex; align-items:center; gap:10px;">
            <button
              @click="updateQuantity(item.product_id, item.quantity, -1)"
              style="padding:6px 12px; border:1px solid #ccc; border-radius:6px; background:white; cursor:pointer;"
            >
              -
            </button>

            <span style="min-width:20px; text-align:center;">
              {{ item.quantity }}
            </span>

            <button
              @click="updateQuantity(item.product_id, item.quantity, 1)"
              style="padding:6px 12px; border:1px solid #ccc; border-radius:6px; background:white; cursor:pointer;"
            >
              +
            </button>
          </div>

          <button
            @click="removeItem(item.product_id)"
            style="color:#d11a2a; font-weight:500; background:none; border:none; cursor:pointer;"
          >
            Remove
          </button>
        </div>

        <div style="margin-top:30px; padding-top:25px; border-top:1px solid #eee;">
          <div style="display:flex; justify-content:space-between; margin-bottom:20px;">
            <span style="font-size:20px; font-weight:600;">Total</span>
            <span style="font-size:22px; font-weight:600;">
              €{{ total.toFixed(2) }}
            </span>
          </div>
        </div>

      </div>
    </div>
  </div>
</template>