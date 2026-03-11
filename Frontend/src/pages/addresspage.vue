<script setup lang="ts">
import { ref, } from 'vue';


const country = ref('')
const streetAddress = ref('')
const city = ref('')
const state = ref('')
const zipCode = ref('')

const submitAddress = () => {
  console.log('Address submitted:')
  console.log({
    country: country.value,
    streetAddress: streetAddress.value,
    city: city.value,
    state: state.value,
    zipCode: zipCode.value
  })
}

</script>
<template> 
    <div class="address-page">
        <h1>Address Page</h1>
        <p>Add your address</p>
    </div>

    <form class="address-form" @submit.prevent="submitAddress">
        <input type="text" placeholder="Country" v-model="country">
        <input type="text" placeholder="Street Address" v-model="streetAddress">
        <input type="text" placeholder="City" v-model="city">
        <input type="text" placeholder="State" v-model="state">
        <input type="string" placeholder="Zip Code" v-model="zipCode">
        <button @click="submitAddress">Submit</button>
    </form>
</template>

<style scoped>
.address-page {
    text-align: center;
    margin-top: 20px;
}
.address-form {
    display: flex;
    flex-direction: column;
    align-items: center;
    margin-top: 20px;
}
.address-form input {
    margin: 10px;
    padding: 10px;
    width: 300px;
    font-size: 16px;
}
.address-form button {
    padding: 10px 20px;
    font-size: 16px;
    cursor: pointer;
}
button:active {
  background-color: #E8F7FF;
  transform: translateY(2px); /* Creates a "pressed" effect */
}
</style>