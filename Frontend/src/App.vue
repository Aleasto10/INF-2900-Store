<script setup lang="ts">
import Navigationbar from '@/components/Navigationbar.vue';

</script>

<template>
  <header>
    
  </header>
  
  <navigationbar/>
  <router-view/>
  <footer class = "footer">
      <p> © 2026 LootBox Store. All rights reserved.</p>
  </footer>
</template>

<style scoped>
header {
  line-height: 1.5;
}
.logo {
  display: block;
  margin: 0 auto 2rem;
}
@media (min-width: 1024px) {
  header {
    display: flex;
    place-items: center;
    padding-right: calc(var(--section-gap) / 2);
  }
  .logo {
    margin: 0 2rem 0 0;
  }
  header .wrapper {
    display: flex;
    place-items: flex-start;
    flex-wrap: wrap;
  }
}
.footer {
        margin-top: auto;
        width: 100%;
        padding: 1rem;
        text-align: center;
        background-color: #f5f5f5;
        color: #333333;
    }

</style>