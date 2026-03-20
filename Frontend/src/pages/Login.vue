<script setup lang="ts">
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import api from '../api'

const router = useRouter()
const email = ref('')
const password = ref('')
const msg = ref('')

//to retrieve info about session, use localStorage.getItem() to retrieve info
async function login() {
  msg.value = ''
  try {
    const { data } = await api.post('/login/', {
      email: email.value,
      password: password.value,
    })
    // Store the session token and account info localy in client browser
    localStorage.setItem('token', data.token)
    localStorage.setItem('account', JSON.stringify(data.account))

    msg.value = `Welcome, ${data.account.name}!`
    router.push('/')
  } catch (e: any) {
    msg.value = e.message
  }
}
</script>

<template>
  <div style="max-width: 400px; margin: 3rem auto;">
    <h1>Log In</h1>

    <form @submit.prevent="login">
      <div>
        <label>Email</label>
        <input v-model="email" type="email" placeholder="you@example.com" />
      </div>

      <div>
        <label>Password</label>
        <input v-model="password" type="password" placeholder="Password" />
      </div>

      <p v-if="msg">{{ msg }}</p>

      <br />
      <button type="submit">Log In</button>
      <router-link to="/createaccount">Create account</router-link>
    </form>
  </div>
</template>