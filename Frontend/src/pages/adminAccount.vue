

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

//Post. Does admin need to create accounts? 
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

//Just for testing. If the array is still here, deletes it. 
const items = Array.from({ length: 1000 }, (k, v) => v + 1)
    
</script>

<template> 

<v-main>
    <v-sheet class="d-flex align-center justify-center text-center">
        <h2>Account admin</h2>
    </v-sheet>

    <v-container style="background-color: whitesmoke; border-radius: 10px; border: 2px solid black;"> 
        <v-row> 
            <v-col> 
                <v-card>
                    <v-virtual-scroll :items="items" height="320" item-height="48">
                        
                        <v-list>
                            
                            <v-list-item title="Hello" subtitle="World"> 
                                <template v-slot:prepend> 
                                    <v-icon>mdi-account</v-icon>
                                </template>

                                <template v-slot:append> 
                                    <v-btn icon="mdi-pencil" size="x-small" variant="tonal"></v-btn>
                                </template>
                            </v-list-item>

                            
                        </v-list>
                        
                    </v-virtual-scroll>
                </v-card>
            </v-col>
        
        <v-divider vertical class="border-opacity-100"></v-divider>
        
            <v-col>
                <!-- size should be -->
                <v-card height="320">
                    <v-text> Account details appear here</v-text>
                </v-card>
            </v-col>
        </v-row>
        
        <v-container class="d-flex justify-center">
            <v-btn rounded="lg" style="background-color: whitesmoke; color: black;" class="ma-2">Delete account</v-btn>
            <v-btn rounded = "lg" style="background-color: whitesmoke; color: black;" class="ma-2">Edit account</v-btn>
        </v-container>

        <!-- Adds button for adding account here if required -->

    </v-container>
</v-main>

</template>

<style scoped>


</style>