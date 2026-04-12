<template>
  
  <v-container class="nav-container">
    <v-sheet class="logo">
      <v-text>LootBox Store</v-text>
    </v-sheet>

    <!-- Search bar-->
    <v-card>
      <v-autocomplete
      v-model:search="searchInput" 
      label="Search for products" 
      :items = "filteredItems"
      :loading = "loading"
      autocomplete="off"
      style = "width: 400px;"
      prepend-inner-icon="mdi-magnify"
      hide-no-data
      hide-details
      >

      </v-autocomplete>
    </v-card> 



    <v-sheet class="nav-links">
      <router-link to="/">Home</router-link>
      <router-link v-if="!isAdmin && account" to="/cart">&#128722</router-link>
      <router-link v-if="account" to="/account">Account</router-link>
      <router-link v-if="isAdmin" to="/productmanagement">Product management</router-link>
      <router-link v-if="!isAdmin && account" to="/address">Address</router-link>
      <router-link to="/products">Products</router-link>

      <!-- added temporarily -->
      <router-link v-if="!account" to="/login">Log in</router-link>
      <button v-else @click="logout" class="logout-btn">Log out</button>
    </v-sheet>
  </v-container>

</template>

<script setup lang="ts">

//checks on re-render of nav-bar if user's admin status = true, used in v-if checks on router links to
//have access control
import { onMounted, computed, ref, watch} from 'vue'
import { useRouter } from 'vue-router'
import api from '../api'
import { de, tr } from 'vuetify/locale'
import { filterItems } from 'vuetify/lib/composables/filter.mjs'

const loading = ref(false)
const products = ref<Product[]>()
const searchInput = ref('')
let debounceTimer: ReturnType<typeof setTimeout> | null = null
const filteredItems = ref<string[]>([])

//const router = useRouter()

const account = computed(() => {
const raw = localStorage.getItem('account')
return raw ? JSON.parse(raw) : null
})

onMounted(fetchProducts)

//Product object. For the records from product table.
interface Product {
  id: number
  name: string
  description: string
  price: string
  stock: number
  origin: string
  image: string
}

//Delays the search for 300 ms after a key is typed in 
watch(searchInput, (val) => {
  clearTimeout(debounceTimer!)
  try {
    if (!val) {
      filteredItems.value = []
      return
    }
    loading.value = true
    debounceTimer = setTimeout(() => {
      filteredItems.value = products.value
        ?.map(p => p.name)
        .filter(name => name.toLowerCase().includes(val.toLowerCase())) ?? []
      loading.value = false
    }, 300) // 300ms delay
  } catch (e: any) { 
    console.log("error with a state change")
  }
})



//Sending a GET request for getting the data from product table
async function fetchProducts() {
  try {
    const { data } = await api.get<Product[]>('/products/')
    products.value = data 

  } catch (e: any) {
    console.log("could not get records from product table")
  } finally {
    loading.value = false
  }
  
}

//to access the product management / account management after admin access control is added
//this line can be changed to allow access under database population - admin_status === true/false
const isAdmin = computed(() => account.value?.admin_status === true)

// logout function to clear local storage and redirect to home page
const logout = async () => {
const token = localStorage.getItem('token')
if (token) {
  try {
    await api.post('/logout/', { token })
  } catch (e) {
    console.error('Logout failed', e)
  }
}
localStorage.removeItem('account')
localStorage.removeItem('token')
window.location.href = '/'
}
</script>

<style scoped>


.nav-container {
max-width: 1200px;
margin: auto;
padding: 15px 30px;
display: flex;
justify-content: space-between;
align-items: center;

}

.logo {
font-size: 20px;
font-weight: bold;
}

.nav-links {
display: flex;
gap: 30px;

}

.nav-links a {
color: rgb(2, 2, 2);
text-decoration: none;
font-size: 16px;
transition: 0.2s;
}

.nav-links a:hover {
color: #616461;
}

.nav-links button {
color: rgb(2, 2, 2);
text-decoration: none;
font-size: 16px;
transition: 0.2s;
background: none;
border: none;
cursor: pointer;
}

.nav-links button:hover {
color: #616461;
}
</style>