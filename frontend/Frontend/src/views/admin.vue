

<script setup lang ="ts">

import { ref, onMounted} from 'vue'
import axios from 'axios'


const users = ref(0)

const fetchUser = async () => {
  try { 
    const response = await axios.get('http://localhost:8000/api/getUser/')
    console.log(response.data)
    users.value = response.data
  
  } catch (error){
    console.log('error')
  }
}



const deleteUser = async () => {
  try { 
    const response = await axios.delete('http://localhost:8000/api/deleteUser/')
    console.log(response.status)
    
  } catch (error){
    console.log('error')
  }  
}


//This ensures that fetchUser will always run after the index.html file is mounted
onMounted(() => {
  fetchUser();
});
    
</script>

<template> 
<header> 
    <title>admin</title>
    <p>account: {{ users.U1 }}</p>
    <p>account {{ users.U2 }}</p> 
</header>


<main>

  <div class ="admin">
    <v-text> Admin page for administrating accounts </v-text>

    <btn class = "adminBtn" type = "button" @click ="deleteUser"> Remove account</btn>
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