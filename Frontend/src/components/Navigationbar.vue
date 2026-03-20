<template>
  <nav class="navbar">
    <div class="nav-container">
      <div class="logo">
        LootBox Store
      </div>

      <div class="nav-links">
        <router-link to="/">Home</router-link>
        <router-link to="/cart">&#128722</router-link>
        <router-link to="/account">Account</router-link>
        <router-link to="/ProductManagement">Product management</router-link>
        <router-link to="/address">Address</router-link>
        <router-link to="/login">Log-in</router-link>
      </div>
    </div>
  </nav>
</template>

<script>
export default {
  name: "Navigationbar"
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
</style>