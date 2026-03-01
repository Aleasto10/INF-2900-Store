<script setup lang ="ts">

import { ref, onMounted} from 'vue'
import axios from 'axios'


const fetching = async () => {
  try { 
    const response = await axios.get('http://localhost:8000/api/user/')
    console.log(response.data)
    return response.data
  } catch (error){
    console.log('error')
  }
  
}
    
</script>

<template> 
<header> 
    <h1> banner goes here</h1>
</header>


<main>
  <v-text> Admin page for administrating accounts </v-text>
  <div id ="banner">
    <btn class = "adminBtn" type = "button" @click ="fetching" > Add account</btn>
    <btn class = "adminBtn" type = "button" > Remove account</btn>
    <btn class = "adminBtn" type = "button" > Edit account</btn>
  </div>
  
</main>

</template>

<style>
  .adminBtn { 
  background-color: black;
  border: 3px solid black;
  color: white;
  padding: 15px 32px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
  margin: 4px 2px;
  cursor: pointer;
  }

</style>