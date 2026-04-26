<template>
  <nav class="navbar">
    <div class="nav-container">
      <div class="logo">
        LootBox Store
      </div>

      <div class="nav-links">
        <router-link to="/">Home</router-link>
        <router-link v-if="!isAdmin && account" to="/cart">&#128722</router-link>
        <router-link v-if="account" to="/account">Account</router-link>
        <router-link v-if="isAdmin" to="/productmanagement">Product management</router-link>
        <router-link v-if="!isAdmin && account" to="/address">Address</router-link>
        <router-link to="/products">Products</router-link>

        <!-- added temporarily -->
        <router-link v-if="isAdmin" to="/adminAccount">Admin</router-link> 
        
        <router-link v-if="!account" to="/login">Log in</router-link>
        <button v-else @click="logout" class="logout-btn">Log out</button>
      </div>
    </div>
  </nav>
</template>

<script setup lang="ts">
//checks on re-render of nav-bar if user's admin status = true, used in v-if checks on router links to
//have access control
import { computed } from 'vue'
import { useRouter } from 'vue-router'
import api from '../api'

const router = useRouter()

const account = computed(() => {
  const raw = localStorage.getItem('account')
  return raw ? JSON.parse(raw) : null
})
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
      alert('Logout failed due to an error with bad request')
    }
  }
  localStorage.removeItem('account')
  localStorage.removeItem('token')
  window.location.href = '/'
}
</script>

<style scoped>
.navbar {
  width: 100%;
  background: #ffffff;
  color: rgb(0, 0, 0);
  box-shadow: 0 2px 5px rgba(0,0,0,0.2);
}

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