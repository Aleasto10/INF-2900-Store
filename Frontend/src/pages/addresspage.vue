<script setup lang="ts">
import { ref } from 'vue'

const fullName = ref('')
const email = ref('')
const phoneNumber = ref('')
const streetAddress = ref('')
const apartment = ref('')
const city = ref('')
const state = ref('')
const zipCode = ref('')
const country = ref('United States')

const submitAddress = () => {
  console.log('Address submitted:')
  console.log({
    fullName: fullName.value,
    email: email.value,
    phoneNumber: phoneNumber.value,
    streetAddress: streetAddress.value,
    apartment: apartment.value,
    city: city.value,
    state: state.value,
    zipCode: zipCode.value,
    country: country.value
  })
}
</script>

<template>
  <div class="address-page">
    <div class="address-card">
      <div class="card-header">
        <div class="icon-box">📦</div>
        <h1>Shipping Address</h1>
      </div>

      <form class="address-form" @submit.prevent="submitAddress">
        <div class="form-row two-columns">
          <div class="form-group">
            <label for="fullName">Full Name *</label>
            <input
              id="fullName"
              type="text"
              placeholder="Mike Hawk"
              v-model="fullName"
            />
          </div>

          <div class="form-group">
            <label for="email">Email Address *</label>
            <input
              id="email"
              type="email"
              placeholder="bob@example.com"
              v-model="email"
            />
          </div>
        </div>

        <div class="form-row">
          <div class="form-group">
            <label for="phoneNumber">Phone Number *</label>
            <input
              id="phoneNumber"
              type="text"
              placeholder="+47 123 45 678"
              v-model="phoneNumber"
            />
          </div>
        </div>

        <div class="form-row">
          <div class="form-group">
            <label for="streetAddress">Street Address *</label>
            <input
              id="streetAddress"
              type="text"
              placeholder="skippergata 123"
              v-model="streetAddress"
            />
          </div>
        </div>

        <div class="form-row">
          <div class="form-group">
            <label for="apartment">Apartment, Suite, etc. (optional)</label>
            <input
              id="apartment"
              type="text"
              placeholder="Apt 4B"
              v-model="apartment"
            />
          </div>
        </div>

        <div class="form-row three-columns">
          <div class="form-group">
            <label for="city">City *</label>
            <input
              id="city"
              type="text"
              placeholder="Tromsø"
              v-model="city"
            />
          </div>

          <div class="form-group">
            <label for="state">State *</label>
            <input
              id="state"
              type="text"
              placeholder="Troms"
              v-model="state"
            />
          </div>

          <div class="form-group">
            <label for="zipCode">ZIP Code *</label>
            <input
              id="zipCode"
              type="text"
              placeholder="1001"
              v-model="zipCode"
            />
          </div>
        </div>

        <div class="form-row">
          <div class="form-group">
            <label for="country">Country *</label>
            <select id="country" v-model="country">
              <option>Norway</option>
              <option>Sweden</option>
              <option>United Kingdom</option>
              <option>Germany</option>
              <option>France</option>
              <option>Spain</option>
            </select>
          </div>
        </div>

        <div class="form-actions">
          <button type="submit">Save Address</button>
        </div>
      </form>
    </div>
  </div>
</template>

<style scoped>
.address-page {
  width: 100%;
  padding: 40px 20px;
  box-sizing: border-box;
  background: #f3f3f3;
}

.address-card {
  max-width: 1050px;
  margin: 0 auto;
  background: #f7f7f7;
  border: 1px solid #d7d7d7;
  border-radius: 16px;
  padding: 28px 30px 30px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.06);
}

.card-header {
  display: flex;
  align-items: center;
  gap: 14px;
  margin-bottom: 28px;
}

.icon-box {
  width: 44px;
  height: 44px;
  border-radius: 12px;
  background: #f7f7f7;
  color: #fff;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 20px;
}

.card-header h1 {
  margin: 0;
  font-size: 22px;
  font-weight: 700;
  color: #111;
}

.address-form {
  display: flex;
  flex-direction: column;
  gap: 22px;
}

.form-row {
  display: grid;
  gap: 20px;
}

.two-columns {
  grid-template-columns: 1fr 1fr;
}

.three-columns {
  grid-template-columns: 1fr 1fr 1fr;
}

.form-group {
  display: flex;
  flex-direction: column;
}

.form-group label {
  font-size: 14px;
  font-weight: 600;
  color: #111;
  margin-bottom: 10px;
}

.form-group input,
.form-group select {
  width: 100%;
  height: 58px;
  padding: 0 18px;
  font-size: 16px;
  color: #333;
  background: #fcfcfc;
  border: 1px solid #cfd4dc;
  border-radius: 14px;
  box-sizing: border-box;
  outline: none;
}

.form-group input::placeholder {
  color: #8d96a3;
}

.form-group input:focus,
.form-group select:focus {
  border-color: #8a8a8a;
}

.form-actions {
  margin-top: 8px;
}

.address-form button {
  padding: 14px 24px;
  font-size: 16px;
  border: none;
  border-radius: 12px;
  background: #000;
  color: #fff;
  cursor: pointer;
  transition: 0.2s;
}

.address-form button:hover {
  background: #222;
}

.address-form button:active {
  background-color: #333;
  transform: translateY(1px);
}

@media (max-width: 900px) {
  .two-columns,
  .three-columns {
    grid-template-columns: 1fr;
  }

  .address-card {
    padding: 22px 18px;
  }
}
</style>