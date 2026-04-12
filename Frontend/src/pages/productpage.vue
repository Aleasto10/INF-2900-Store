<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import api from '../api'
import gridSys from '@/components/grid.vue'
import poop from '@/assets/popp.jpeg'


//Removes this and change the variable in template for using the images from the server
const testProducts: Product[] = [
  { id: 1, name: 'Norway', description: '', price: '12.99', stock: 10, origin: 'Norwat', image: 'https://picsum.photos/seed/coffee/200' },
  { id: 2, name: 'Japan',    description: '',    price: '8.99',  stock: 5,  origin: 'Japan',    imageURL: 'https://picsum.photos/seed/tea/200' },
  { id: 3, name: 'Sweden',     description: '',    price: '4.99',  stock: 20, origin: 'Sweden',   imageURL: 'https://picsum.photos/seed/milk/200' },
  { id: 4, name: 'Sweden',     description: '',    price: '4.99',  stock: 20, origin: 'Sweden',   imageURL: 'https://picsum.photos/seed/milk/200' },
  { id: 5, name: 'Sweden',     description: '',    price: '4.99',  stock: 20, origin: 'Sweden',   imageURL: 'https://picsum.photos//milk/200' },
  { id: 6, name: 'shit',     description: 'Barista',    price: '4.99',  stock: 20, origin: 'Sweden',   imageURL: poop },
  { id: 7, name: 'shit',     description: 'Barista',    price: '4.99',  stock: 20, origin: 'Sweden',   imageURL: poop },
  { id: 8, name: 'shit',     description: 'Barista',    price: '4.99',  stock: 20, origin: 'Sweden',   imageURL: poop },
  { id: 9, name: 'shit',     description: 'Barista',    price: '4.99',  stock: 20, origin: 'Sweden',   imageURL: poop },
]

const products = ref<Product[]>(testProducts)
const loading = ref(true)
const error = ref('')

onMounted(fetchProducts)

//Do we need all of these variables? 
interface Product {
  id: number
  name: string
  description: string
  price: string
  stock: number
  origin: string
  image: string
}

//Sending a GET request for getting the data from product table
async function fetchProducts() {
  
  try {
    const { data } = await api.get<Product[]>('/products/')
    products.value = data

  } catch (e: any) {
    error.value = e.message
  } finally {
    loading.value = false
  }
  
  
}

//If the URL fails to load image, replaces it with "poop". If the string is empty, vue will not considered it as fail to load. 
const failToLoadImg = (index : number) =>{ 
  
  if(products.value[index]) { 
    products.value[index].image = poop
  }
  
}
</script>

<template>
  
  <div id = "main">
  <v-container> 

      <!--- Creates a 3x3 grid system -->
      <!-- Change "testProducts" to "products" to use images from server-->
       
      <v-row>
        <v-col v-for="(product, i) in products" :key="product.id" cols="4">
          <v-hover v-slot:default="{ isHovering, props }">
                <v-card  :class="{'on-hover': isHovering}" v-bind="props" :elevation="isHovering ? 12 : 2">
                    
                    <v-img :src="product.image" @error="failToLoadImg(i)"> 
                      <v-card-title style="color: black;"> {{ product.name }}</v-card-title>
                      <v-card-title style="color: black;"> {{ product.price }}€</v-card-title>
                    </v-img> 
                </v-card>
            
          </v-hover>
        </v-col>
      </v-row>
  </v-container>
</div>
    
</template>

<style scoped>

#main{ 
  width: 100%;
  height: 100%;
  position: absolute;
  background-color: whitesmoke;
}

.v-card { 
    transition: opacity 0.4s ease-in-out;
    background-color: transparent; /* just in case */
    border-radius: 10%;
    width:fit-content; 
    aspect-ratio: 1;
}

.v-card:not(.on-hover) {
    opacity: 0.6;
}

.v-img { 
  width: 200px;
}

</style>