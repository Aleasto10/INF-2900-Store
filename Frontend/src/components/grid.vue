<script setup lang="ts">
import { ref, onMounted } from 'vue'

//Allows to adjust the amount of rows and numbers. Getting from the parent components or parent pages.
defineProps({ 
    rows: Number,
    cols: Number
})

</script>

<template>
  
  <v-container> 

    <!--Need to make the row grow dynamically. Row = column for HTML. Weird AF. -->

    <v-row class ="fill-height align-center justify-center" style="height: 150px" v-for="n in 3" :key="n">
      <v-col v-for="n in 3" :key="n">
        <slot> 

        </slot>
      </v-col>
    </v-row>
  </v-container>
  <!--
  <div class="product-page">
    <h1>Products</h1>
        <div class="product-grid">
            <div v-for="product in products" :key="product.id" class="product-card">
                <h2>{{ product.name }}</h2>
                <p class="picture">Product Picture</p>
                <p>{{ product.description }}</p>
                <p class="price">${{ Number(product.price).toFixed(2) }}</p>
                <p>Stock: {{ product.stock }} &middot; Origin: {{ product.origin }}</p>
            </div>
        </div>
  </div>
  --->
</template>

<style scoped>


/*
.product-page {
  
  width: 100%;
  padding: 40px 20px;
  box-sizing: border-box;
  background: #f3f3f3;
}
.product-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(290px, 1fr));
  gap: 1.5rem;
  margin-top: 1.5rem;
}
.product-card {
  border: 1px solid #ddd;
  border-radius: 8px;
  padding: 1.5rem;
  transition: box-shadow 0.2s;
}
.product-card:hover {
  box-shadow: 0 2px 12px rgba(0, 0, 0, 0.1);
}
.picture {
    border: 1px solid black;
    font-size: 2rem;
    height: 20rem;
    width: 20rem;
}
.price {
  font-size: 1.25rem;
  font-weight: bold;
  color: #263d53;
}
*/
</style>