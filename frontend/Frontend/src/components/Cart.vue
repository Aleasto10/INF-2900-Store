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
const accountId = 1 // Hardcoded for Sprint 1 until you build a login system!

// 1. Fetch the cart from Django when the page loads
async function fetchCart() {
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

// Run fetchCart automatically when the component loads
onMounted(() => {
  fetchCart()
})

// 2. Increase or Decrease quantity
async function updateQuantity(id: number, currentQuantity: number, change: number) {
  const newQuantity = currentQuantity + change
  
  if (newQuantity <= 0) {
    removeItem(id)
    return
  }

  // Call Django to decrease or add
  const url = change > 0 ? 'http://localhost:8000/api/cart/add/' : 'http://localhost:8000/api/cart/decrease/'
  
  await fetch(url, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      account_id: accountId,
      product_id: id,
      quantity: 1 // Adding or decreasing by 1
    })
  })
  
  fetchCart() // Refresh UI
}

// 3. Remove item entirely
async function removeItem(id: number) {
  await fetch('http://localhost:8000/api/cart/remove/', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      account_id: accountId,
      product_id: id
    })
  })
  fetchCart() // Refresh UI
}

// 4. Checkout
async function checkout() {
  await fetch('http://localhost:8000/api/cart/checkout/', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ account_id: accountId })
  })
  alert("Checked out successfully!")
  fetchCart() // Refresh UI
}

const total = computed(() =>
  cart.value.reduce((sum, item) => sum + item.price * item.quantity, 0)
)
</script>