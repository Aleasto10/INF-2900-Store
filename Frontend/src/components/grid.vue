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

    <!--Default grid is 3x3 -->
    <v-row class ="fill-height align-center justify-center" style="height: 150px" v-for="n in rows ? rows:3" :key="n">
      <v-col v-for="n in cols ? cols:3" :key="n">
        <slot> 
            <!-- This allows the parent page/component to add its own tags -->
        </slot>
      </v-col>
    </v-row>
  </v-container>
  
</template>

<style scoped>

</style>