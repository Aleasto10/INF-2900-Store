<script setup lang="ts">
import { ref } from 'vue'
import api from '../api'

const name = ref('')
const email = ref('')
const password = ref('')
const msg = ref('')

async function createAccount() {
  msg.value = ''
  try {
    const { data } = await api.post('/signup/', {
      name: name.value,
      email: email.value,
      password: password.value,
    })
    msg.value = `Account created! ID: ${data.id}, Name: ${data.name}`
    name.value = ''
    email.value = ''
    password.value = ''
  } catch (e: any) {
    msg.value = e.message
  }
}
</script>

<template>
  <div style="max-width: 400px; margin: 3rem auto;">
    <h1>Create Account</h1>

    <form @submit.prevent="createAccount">
      <div>
        <label>Name</label>
        <input v-model="name" type="text" placeholder="Name" />
      </div>

      <div>
        <label>Email</label>
        <input v-model="email" type="email" placeholder="Email" />
      </div>

      <div>
        <label>Password</label>
        <input v-model="password" type="password" placeholder="Password" />
      </div>

      <br />
      <button type="submit">Create Account</button>
    </form>
    
    <p v-if="msg">{{ msg }}</p> 
  </div>
</template>