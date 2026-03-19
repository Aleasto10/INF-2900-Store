

<script setup lang ="ts">

import { ref, onMounted} from 'vue'
import api from '@/api'


const account = ref<accountInfo[]>([])

interface accountInfo { 
    id: number, 
    name: string, 
    password: string, 
    email: string, 
    admin_status: boolean, 
    time_created: string //what is the "timedate" equivalent for ts?
}

//Get
const fetchUser = async () => {
  try { 
    const response = await api.get('/getUser/')
    console.log(response.data)
    account.value = response.data
  
  } catch (error){
    console.log('error')
  }
}


//Delete
const deleteAccount = async () => {
  try { 
    const response = await api.delete('/deleteUser/')
    console.log(response.status)
    
  } catch (error){
    console.log('error')
  }  
}

//Put
const editAccount = async () => {
  try { 
    const response = await api.delete('/deleteUser/')
    console.log(response.status)
    
  } catch (error){
    console.log('error')
  }  
}

//Post
const createAccount = async () => {
  try { 
    const response = await api.delete('/deleteUser/')
    console.log(response.status)
    
  } catch (error){
    console.log('error')
  }  
}


//This ensures that fetchUser will always run after opening this page
onMounted(() => {
  fetchUser();
});
    
</script>

<template> 
    <v-container class="text-center"> 
    <v-sheet class="d-flex align-center justify-center text-center">
        <h2>Account admin</h2>
    </v-sheet>
        <v-card>
            <v-text> Admin page for administrating accounts </v-text>

            <v-btn rounded="lg" color="gray" class="ma-2">Remove account</v-btn>
            <v-btn rounded = "lg" color="gray" class="ma-2">Edit account</v-btn>
        </v-card>
        
    </v-container>
</template>

<style scoped>

  

</style>