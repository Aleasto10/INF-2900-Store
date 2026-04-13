<script setup lang="ts">
import { ref, computed, onMounted } from 'vue'

type StoredAccount = {
  id: number
  name?: string
  email?: string
}

type SavedAddress = {
  id: number
  account_id: number
  line1: string
  line2: string
  city: string
  state: string
  postal_code: string
  country: string
}

const fullName = ref('')
const email = ref('')
const phoneNumber = ref('')
const streetAddress = ref('')
const apartment = ref('')
const city = ref('')
const state = ref('')
const zipCode = ref('')
const country = ref('United States')

const rememberAddress = ref(false)

const savedAccount = ref<StoredAccount | null>(null)
const savedAddress = ref<SavedAddress | null>(null)

const hasAutofillPreview = computed(() => {
  return !!(
    savedAccount.value?.name ||
    savedAccount.value?.email ||
    savedAddress.value
  )
})

onMounted(() => {
  const storedAccount = localStorage.getItem('account')

  if (storedAccount) {
    try {
      savedAccount.value = JSON.parse(storedAccount)
    } catch {
      savedAccount.value = null
    }
  }

  loadSavedAddress()
})

const loadSavedAddress = async () => {
  try {
    const storedAccount = localStorage.getItem('account')
    if (!storedAccount) return

    const account = JSON.parse(storedAccount) as StoredAccount

    const response = await fetch(`http://127.0.0.1:8000/api/accounts/${account.id}/addresses/`)
    const data = await response.json()

    if (response.ok && Array.isArray(data) && data.length > 0) {
      savedAddress.value = data[data.length - 1]
    } else {
      savedAddress.value = null
    }
  } catch (error) {
    console.error('Failed to load saved addresses:', error)
    savedAddress.value = null
  }
}

const applyAutofill = () => {
  if (savedAccount.value) {
    fullName.value = savedAccount.value.name || ''
    email.value = savedAccount.value.email || ''
  }

  if (savedAddress.value) {
    streetAddress.value = savedAddress.value.line1 || ''
    apartment.value = savedAddress.value.line2 || ''
    city.value = savedAddress.value.city || ''
    state.value = savedAddress.value.state || ''
    zipCode.value = savedAddress.value.postal_code || ''
    country.value = savedAddress.value.country || ''
  }
}

const submitAddress = async () => {
  const payload = {
    fullName: fullName.value,
    email: email.value,
    phoneNumber: phoneNumber.value,
    streetAddress: streetAddress.value,
    apartment: apartment.value,
    city: city.value,
    state: state.value,
    zipCode: zipCode.value,
    country: country.value
  }

  console.log('Address form submitted:')
  console.log(payload)

  if (!rememberAddress.value) {
    alert('Address not saved. Check "Remember this address for later" if you want to store it.')
    return
  }

  const storedAccount = localStorage.getItem('account')
  if (!storedAccount) {
    alert('No logged in account found.')
    return
  }

  const account = JSON.parse(storedAccount) as StoredAccount

  try {
    const response = await fetch(`http://127.0.0.1:8000/api/accounts/${account.id}/addresses/`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        line1: streetAddress.value,
        line2: apartment.value,
        city: city.value,
        state: state.value,
        postal_code: zipCode.value,
        country: country.value
      })
    })

    const text = await response.text()
    let data: any

    try {
      data = JSON.parse(text)
    } catch {
      data = { error: text }
    }

    if (!response.ok) {
      console.error('Backend error:', data)
      alert(data.error || 'Failed to save address')
      return
    }

    await loadSavedAddress()
    alert('Address saved successfully')
    console.log('Saved address:', data)
  } catch (error) {
    console.error('Failed to save address:', error)
    alert('Something went wrong while saving the address')
  }
}
</script>

<template>
  <div class="address-page">
    <div class="address-card">
      <div class="card-header">
        <h1>Shipping Address</h1>
      </div>

      <div v-if="hasAutofillPreview" class="autofill-preview" @click="applyAutofill">
        <div class="autofill-preview-text">
          <strong>Saved info</strong>
          <p v-if="savedAccount?.name || savedAccount?.email">
            {{ savedAccount?.name }}<span v-if="savedAccount?.name && savedAccount?.email"> · </span>{{ savedAccount?.email }}
          </p>
          <p v-if="savedAddress">
            {{ savedAddress.line1 }}, {{ savedAddress.city }}, {{ savedAddress.country }}
          </p>
        </div>
        <button type="button" class="autofill-button">Use</button>
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

        <div class="remember-row">
          <label class="remember-label">
            <input type="checkbox" v-model="rememberAddress" />
            Remember this address for later
          </label>
        </div>

        <div class="form-actions">
          <button type="submit">Go to payment</button>
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

.autofill-preview {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 16px;
  margin-bottom: 22px;
  padding: 16px 18px;
  border: 1px solid #d0d0d0;
  border-radius: 14px;
  background: #fcfcfc;
  cursor: pointer;
}

.autofill-preview-text p {
  margin: 6px 0 0;
  color: #666;
  font-size: 14px;
}

.autofill-button {
  padding: 10px 16px;
  border: none;
  border-radius: 10px;
  background: #111;
  color: #fff;
  cursor: pointer;
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

.remember-row {
  margin-top: -6px;
}

.remember-label {
  display: flex;
  align-items: center;
  gap: 10px;
  font-size: 14px;
  color: #111;
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

  .autofill-preview {
    flex-direction: column;
    align-items: flex-start;
  }
}
</style>